import math
import random as _stdlib_random
from typing import Sequence
from collections.abc import Iterable

inf = float('inf')
infty = inf
pi = math.pi
nan = float('nan')


def _safe_div(a, b):
    if b == 0:
        return nan if a == 0 else math.copysign(inf, a)
    try:
        return a / b
    except ZeroDivisionError:
        return nan if a == 0 else math.copysign(inf, a)


def set_printoptions(*_, **__):
    return None


def _to_list(value):
    if isinstance(value, SimpleArray):
        return value.data
    if isinstance(value, (list, tuple)):
        return list(value)
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
        return list(value)
    return [value]


class SimpleArray:
    def __init__(self, data: Sequence):
        self.data = list(data)

    @property
    def shape(self):
        if len(self.data) and isinstance(self.data[0], (list, tuple, SimpleArray)):
            inner = self.data[0]
            if isinstance(inner, SimpleArray):
                return (len(self.data),) + inner.shape
            return (len(self.data), len(inner))
        return (len(self.data),)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    @property
    def size(self):
        return len(self.data)

    def __getitem__(self, item):
        if isinstance(item, list):
            return SimpleArray([self.data[i] for i in item])
        if isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], list):
            # basic column selection
            rows = self.data if isinstance(self.data, list) else []
            selected = []
            for row in rows:
                if isinstance(row, SimpleArray):
                    selected.append([row.data[i] for i in item[1]])
                elif isinstance(row, list):
                    selected.append([row[i] for i in item[1]])
            return SimpleArray(selected)
        return self.data[item]

    def __setitem__(self, key, value):
        if isinstance(key, list):
            vals = _to_list(value)
            for idx, target in enumerate(key):
                self.data[target] = vals[idx if idx < len(vals) else -1]
            return
        if isinstance(key, tuple) and len(key) == 2 and isinstance(key[1], list):
            cols = key[1]
            vals = _to_list(value)
            for r_idx, row in enumerate(self.data):
                for c_i, c in enumerate(cols):
                    v = vals[c_i if c_i < len(vals) else -1]
                    if isinstance(row, SimpleArray):
                        row.data[c] = v
                    elif isinstance(row, list):
                        row[c] = v
            return
        self.data[key] = value

    def _binary_op(self, other, op):
        if isinstance(other, SimpleArray):
            other = other.data
        if isinstance(other, (list, tuple)):
            return SimpleArray([op(a, b) for a, b in zip(self.data, other)])
        return SimpleArray([op(a, other) for a in self.data])

    def __add__(self, other):
        return self._binary_op(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._binary_op(other, lambda a, b: a - b)

    def __mul__(self, other):
        return self._binary_op(other, lambda a, b: a * b)

    def __truediv__(self, other):
        return self._binary_op(other, _safe_div)

    def __rtruediv__(self, other):
        return SimpleArray([_safe_div(other, a) for a in self.data])

    def __pow__(self, power, modulo=None):
        return self._binary_op(power, lambda a, b: a ** b)

    def __rpow__(self, other):
        return SimpleArray([other ** v for v in self.data])

    def __neg__(self):
        return SimpleArray([-v for v in self.data])

    def __gt__(self, other):
        return self._binary_op(other, lambda a, b: a > b)

    def __lt__(self, other):
        return self._binary_op(other, lambda a, b: a < b)

    def __ge__(self, other):
        return self._binary_op(other, lambda a, b: a >= b)

    def __le__(self, other):
        return self._binary_op(other, lambda a, b: a <= b)

    def __eq__(self, other):  # type: ignore[override]
        return self._binary_op(other, lambda a, b: a == b)

    def __ne__(self, other):  # type: ignore[override]
        return self._binary_op(other, lambda a, b: a != b)

    def tolist(self):
        out = []
        for v in self.data:
            if isinstance(v, SimpleArray):
                out.append(v.tolist())
            else:
                out.append(v)
        return out

    def tostring(self):
        return str(self.data).encode()

    def squeeze(self):
        return squeeze(self)

    @property
    def T(self):
        return self


ndarray = SimpleArray


class RandomModule:
    @staticmethod
    def rand(*shape):
        total = 1
        for dim in shape:
            total *= dim
        flat = [_stdlib_random.random() for _ in range(total)]
        return reshape(SimpleArray(flat), shape)

    @staticmethod
    def uniform(low, high, size=None):
        if size is None:
            return _stdlib_random.uniform(low, high)
        total = 1
        for dim in _shape_tuple(size):
            total *= dim
        flat = [_stdlib_random.uniform(low, high) for _ in range(total)]
        return reshape(SimpleArray(flat), _shape_tuple(size))

    @staticmethod
    def randint(low, high=None, size=None):
        if high is None:
            high = low
            low = 0
        if size is None:
            return _stdlib_random.randint(low, high)
        total = 1
        for dim in _shape_tuple(size):
            total *= dim
        flat = [_stdlib_random.randint(low, high) for _ in range(total)]
        return reshape(SimpleArray(flat), _shape_tuple(size))

    @staticmethod
    def normal(loc=0.0, scale=1.0, size=None):
        def sample():
            return _stdlib_random.gauss(loc, scale)
        if size is None:
            return sample()
        total = 1
        for dim in _shape_tuple(size):
            total *= dim
        flat = [sample() for _ in range(total)]
        return reshape(SimpleArray(flat), _shape_tuple(size))

    @staticmethod
    def laplace(loc=0.0, scale=1.0, size=None):
        def sample():
            u = _stdlib_random.random() - 0.5
            return loc - scale * math.copysign(1.0, u) * math.log(1 - 2 * abs(u))
        if size is None:
            return sample()
        total = 1
        for dim in _shape_tuple(size):
            total *= dim
        flat = [sample() for _ in range(total)]
        return reshape(SimpleArray(flat), _shape_tuple(size))

    @staticmethod
    def exponential(scale=1.0, size=None):
        def sample():
            u = _stdlib_random.random()
            return -scale * math.log(1 - u)
        if size is None:
            return sample()
        total = 1
        for dim in _shape_tuple(size):
            total *= dim
        flat = [sample() for _ in range(total)]
        return reshape(SimpleArray(flat), _shape_tuple(size))

    @staticmethod
    def logistic(loc=0.0, scale=1.0, size=None):
        def sample():
            u = _stdlib_random.random()
            return loc + scale * math.log(u / (1 - u))
        if size is None:
            return sample()
        total = 1
        for dim in _shape_tuple(size):
            total *= dim
        flat = [sample() for _ in range(total)]
        return reshape(SimpleArray(flat), _shape_tuple(size))

    @staticmethod
    def shuffle(arr):
        lst = _to_list(arr)
        _stdlib_random.shuffle(lst)
        if isinstance(arr, SimpleArray):
            arr.data = lst
        else:
            return lst

    @staticmethod
    def seed(val=None):
        _stdlib_random.seed(val)

    @staticmethod
    def choice(seq):
        return _stdlib_random.choice(list(seq))


random = RandomModule()


def _shape_tuple(size):
    if isinstance(size, (list, tuple)):
        return tuple(size)
    return (size,)


def reshape(arr: SimpleArray, shape):
    shape = tuple(shape)
    flat = _to_list(arr)

    def _reshape(data, dims):
        if not dims:
            return data.pop(0)
        dim = dims[0]
        if len(dims) == 1:
            slice_vals = [data.pop(0) for _ in range(dim)]
            return SimpleArray(slice_vals)
        return SimpleArray([_reshape(data, dims[1:]) for _ in range(dim)])

    data_copy = list(flat)
    reshaped = _reshape(data_copy, list(shape))
    return reshaped


def array(seq, dtype=float):
    return asarray(seq, dtype=dtype)


def asarray(seq, dtype=float):
    if isinstance(seq, SimpleArray):
        return seq
    if isinstance(seq, (list, tuple)):
        converted = []
        for x in seq:
            if isinstance(x, SimpleArray):
                converted.append(x)
            elif isinstance(x, (list, tuple)):
                converted.append(asarray(x, dtype=dtype))
            else:
                converted.append(dtype(x))
        return SimpleArray(converted)
    return SimpleArray([dtype(seq)])


def zeros(length, dtype=float):
    if isinstance(length, (list, tuple)) and len(length) == 2:
        return SimpleArray([[dtype(0.0) for _ in range(length[1])] for _ in range(length[0])])
    return SimpleArray([dtype(0.0) for _ in range(length)])


def ones(length, dtype=float):
    if isinstance(length, (list, tuple)) and len(length) == 2:
        return SimpleArray([[dtype(1.0) for _ in range(length[1])] for _ in range(length[0])])
    return SimpleArray([dtype(1.0) for _ in range(length)])


def copy(arr):
    return asarray(_to_list(arr))


def squeeze(arr):
    if isinstance(arr, SimpleArray):
        data = arr.data
    else:
        data = arr
    while isinstance(data, list) and len(data) == 1:
        data = data[0]
    return asarray(data)


def stack(list_of_arrays, axis=0):
    converted = [asarray(a) for a in list_of_arrays]
    if axis == 0:
        return SimpleArray([a.data for a in converted])
    raise NotImplementedError


def concatenate(arrays, axis=0):
    combined = []
    for arr in arrays:
        combined.extend(_to_list(arr))
    return SimpleArray(combined)


def nan_to_num(arr, nan=0.0, posinf=None, neginf=None):
    posinf = inf if posinf is None else posinf
    neginf = -inf if neginf is None else neginf

    def _fix(v):
        if isinstance(v, float) and math.isnan(v):
            return nan
        if v == inf:
            return posinf
        if v == -inf:
            return neginf
        return v

    return SimpleArray([_fix(v) for v in _to_list(arr)])


def clip(arr, low, high):
    def _as_number(v):
        if isinstance(v, SimpleArray):
            return _as_number(v.data[0] if v.data else 0)
        if isinstance(v, list):
            return _as_number(v[0] if v else 0)
        return v

    return SimpleArray([builtins_max(low, builtins_min(high, _as_number(v))) for v in _to_list(arr)])


def mean(arr):
    vals = _to_list(arr)
    return sum(vals) / len(vals) if vals else 0.0


def var(arr):
    vals = _to_list(arr)
    m = mean(vals)
    return sum((v - m) ** 2 for v in vals) / len(vals) if vals else 0.0


def std(arr):
    return math.sqrt(var(arr))


def max(arr):
    vals = _to_list(arr)
    return builtins_max(vals) if vals else 0.0


def sum(arr):
    vals = list(_to_list(arr))
    return builtins_sum(vals)


def _map_unary(x, func):
    if isinstance(x, SimpleArray):
        return SimpleArray([func(v) for v in x])
    return func(x)


def _map_binary(a, b, func):
    if isinstance(a, SimpleArray):
        a_vals = a.data
    else:
        a_vals = _to_list(a)
    if isinstance(b, SimpleArray):
        b_vals = b.data
    else:
        b_vals = _to_list(b)
    max_len = max(len(a_vals), len(b_vals))
    a_vals = (a_vals * max_len)[:max_len]
    b_vals = (b_vals * max_len)[:max_len]
    return SimpleArray([func(x, y) for x, y in zip(a_vals, b_vals)])


def add(a, b):
    return _map_binary(a, b, lambda x, y: x + y)


def subtract(a, b):
    return _map_binary(a, b, lambda x, y: x - y)


def multiply(a, b):
    return _map_binary(a, b, lambda x, y: x * y)


def divide(a, b):
    return _map_binary(a, b, lambda x, y: x / y if y != 0 else inf)


def power(a, b):
    return _map_binary(a, b, lambda x, y: x ** y)


def sin(x):
    return _map_unary(x, math.sin)


def cos(x):
    return _map_unary(x, math.cos)


def tan(x):
    return _map_unary(x, math.tan)


def exp(x):
    return _map_unary(x, math.exp)


def log(x):
    return _map_unary(x, lambda v: math.log(v) if v != 0 else -inf)


def sqrt(x):
    return _map_unary(x, math.sqrt)


def log10(x):
    return _map_unary(x, math.log10)


def negative(x):
    return _map_unary(x, lambda v: -v)


def maximum(x, y):
    return _map_binary(x, y, builtins_max)


def minimum(x, y):
    return _map_binary(x, y, builtins_min)


def tanh(x):
    return _map_unary(x, math.tanh)


def reciprocal(x):
    return _map_unary(x, lambda v: 1.0 / v if v != 0 else inf)


def square(x):
    return power(x, 2)


def where(cond, x1, x2):
    cond_list = _to_list(cond)
    x1_list = _to_list(x1)
    x2_list = _to_list(x2)
    max_len = max(len(cond_list), len(x1_list), len(x2_list))
    cond_list = (cond_list * max_len)[:max_len]
    x1_list = (x1_list * max_len)[:max_len]
    x2_list = (x2_list * max_len)[:max_len]
    return SimpleArray([x1_list[i] if cond_list[i] else x2_list[i] for i in range(max_len)])


def linspace(start, stop, num):
    step = (stop - start) / (num - 1)
    return SimpleArray([start + i * step for i in range(num)])


def arange(start, stop=None):
    if stop is None:
        start, stop = 0, start
    return SimpleArray(list(range(int(start), int(stop))))


class _ErrState:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


def errstate(**kwargs):
    return _ErrState()


def atleast_1d(val):
    if isinstance(val, SimpleArray):
        return val
    if isinstance(val, (list, tuple)):
        return SimpleArray(val)
    return SimpleArray([val])


float32 = float
int32 = int
integer = int


def abs(val):
    if isinstance(val, SimpleArray):
        return SimpleArray([builtins_abs(v) for v in val])
    return builtins_abs(val)


def seterrcall(*args, **kwargs):
    return None


def seterr(**kwargs):
    return None


def round(x, decimals=0):
    factor = 10 ** decimals
    return _map_unary(x, lambda v: builtins_round(v * factor) / factor)


from builtins import max as builtins_max, min as builtins_min, sum as builtins_sum, abs as builtins_abs, round as builtins_round
