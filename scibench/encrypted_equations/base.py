from sympy import Symbol


class KnownEquation(object):
    _eq_name = None
    _function_set = ['exp', 'log', 'sqrt', 'add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self, num_vars, sampling_objs, kwargs_list=None):
        if kwargs_list is None:
            kwargs_list = [{'real': True} for _ in range(num_vars)]

        assert len(kwargs_list) == num_vars
        self.num_vars = num_vars
        self.sampling_objs = sampling_objs
        self.x = [Symbol(f'X_{i}', **kwargs) for i, kwargs in enumerate(kwargs_list)]
        self.sympy_eq = None


class DefaultSampling(object):
    def __init__(self, min_value, max_value, uses_positive=True, uses_negative=True):
        self.min_value = min_value
        self.max_value = max_value
        assert uses_positive or uses_negative
        self.uses_positive = uses_positive
        self.uses_negative = uses_negative


class IntegerSampling(object):
    def __init__(self, min_value, max_value, uses_positive=True, uses_negative=True):
        self.min_value = int(min_value)
        self.max_value = int(max_value)
        assert uses_positive or uses_negative
        self.uses_positive = uses_positive
        self.uses_negative = uses_negative


class SimpleSampling(object):
    def __init__(self, min_value, max_value, uses_positive=True, uses_negative=True):
        self.min_value = min_value
        self.max_value = max_value
        assert uses_positive or uses_negative
        self.uses_positive = uses_positive
        self.uses_negative = uses_negative
