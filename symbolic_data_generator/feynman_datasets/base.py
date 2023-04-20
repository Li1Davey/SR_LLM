import warnings

import numpy as np
import sympy
from sympy import Derivative, Matrix, Symbol, simplify, solve, lambdify
from sympy.utilities.misc import func_name

FLOAT32_MAX = np.finfo(np.float32).max
FLOAT32_MIN = np.finfo(np.float32).min
FLOAT32_TINY = np.finfo(np.float32).tiny


class KnownEquation(object):
    _eq_name = None

    def __init__(self, num_vars, sampling_objs, kwargs_list=None):
        super().__init__()
        if kwargs_list is None:
            kwargs_list = [{'real': True} for _ in range(num_vars)]

        assert len(sampling_objs) == num_vars
        assert len(kwargs_list) == num_vars
        self.sampling_objs = sampling_objs
        self.x = [Symbol(f'x{i}', **kwargs) for i, kwargs in enumerate(kwargs_list)]

    def get_eq_name(self, prefix=None, suffix=None):
        if prefix is None:
            prefix = ''
        if suffix is None:
            suffix = ''
        return prefix + self._eq_name + suffix

    def get_var_count(self):
        return len(self.x)

    def get_domain_range(self):
        min_value = None
        max_value = None
        for sampling_objs in self.sampling_objs:
            sub_min_value = sampling_objs.min_value
            sub_max_value = sampling_objs.max_value
            if min_value is None:
                min_value = sub_min_value
                max_value = sub_max_value
            elif sub_min_value < min_value:
                min_value = sub_min_value
            elif sub_max_value > max_value:
                max_value = sub_max_value
        return np.abs(np.log10(np.abs(max_value - min_value)))

    def check_if_valid(self, values):
        return ~np.isnan(values) * ~np.isinf(values) * \
            (FLOAT32_MIN <= values) * (values <= FLOAT32_MAX) * (np.abs(values) >= FLOAT32_TINY)

    def obtain_data_pairs(self, sample_size):
        xs = []
        for i, sampling_func in enumerate(self.sampling_objs):
            one_x = sampling_func(sample_size)
            xs.append(one_x)

        return xs

    def obtain_control_variable_data_pairs(self, sample_size):
        xs = []
        stride = sample_size // len(self.sampling_objs)
        for i, sampling_func in enumerate(self.sampling_objs):
            one_x = sampling_func(sample_size)
            for j in range(i):
                one_x[j * stride:(j + 1) * stride] = one_x[j * stride]
            xs.append(one_x)

        return xs

    def create_dataset(self, sample_size, eq_func, patience=10, use_control_variable=True):
        warnings.filterwarnings('ignore')
        assert len(self.sampling_objs) > 0, f'There should be at least one variable provided'
        if use_control_variable:
            xs = self.obtain_control_variable_data_pairs(sample_size)
        else:
            xs = self.obtain_data_pairs(sample_size)
        y = eq_func(xs)
        # Check if y contains NaN, Infinity, etc
        valid_sample_flags = self.check_if_valid(y)
        valid_sample_size = sum(valid_sample_flags)
        if valid_sample_size == sample_size:
            return np.array([*xs, y]).T

        valid_xs = [x[valid_sample_flags] for x in xs]
        valid_y = y[valid_sample_flags]
        missed_sample_size = sample_size - valid_sample_size
        for i in range(patience):
            xs = self.obtain_data_pairs(missed_sample_size * 3)
            y = eq_func(xs)
            valid_sample_flags = self.check_if_valid(y)
            valid_xs = [np.concatenate([xs[i][valid_sample_flags], valid_xs[i]]) for i in range(len(xs))]
            valid_y = np.concatenate([y[valid_sample_flags], valid_y])
            valid_sample_size = len(valid_y)
            if valid_sample_size >= sample_size:
                xs = [x[:sample_size] for x in valid_xs]
                y = valid_y[:sample_size]
                return np.array([*xs, y]).T
        raise TimeoutError(f'number of valid samples (`{len(valid_y)}`) did not reach to '
                           f'{sample_size} within {patience} trials')

    def create_fixedcolumn_dataset(self, sample_size, eq_func, fixed_columns, patience=10):
        warnings.filterwarnings('ignore')
        assert len(self.sampling_objs) > 0, f'There should be at least one variable provided'
        xs = self.obtain_data_pairs(sample_size)
        for fidx in fixed_columns:
            xs[fidx][:] = xs[fidx][0]
        y = eq_func(xs)
        # Check if y contains NaN, Infinity, etc
        valid_sample_flags = self.check_if_valid(y)
        valid_sample_size = sum(valid_sample_flags)
        if valid_sample_size == sample_size:
            return np.array([*xs, y]).T

        valid_xs = [x[valid_sample_flags] for x in xs]
        valid_y = y[valid_sample_flags]
        missed_sample_size = sample_size - valid_sample_size
        for i in range(patience):
            xs = self.obtain_data_pairs(missed_sample_size * 3)
            for fidx in fixed_columns:
                xs[fidx][:] = xs[fidx][0]
            y = eq_func(xs)
            valid_sample_flags = self.check_if_valid(y)
            valid_xs = [np.concatenate([xs[i][valid_sample_flags], valid_xs[i]]) for i in range(len(xs))]
            valid_y = np.concatenate([y[valid_sample_flags], valid_y])
            valid_sample_size = len(valid_y)
            if valid_sample_size >= sample_size:
                xs = [x[:sample_size] for x in valid_xs]
                y = valid_y[:sample_size]
                return np.array([*xs, y]).T
        raise TimeoutError(f'number of valid samples (`{len(valid_y)}`) did not reach to '
                           f'{sample_size} within {patience} trials')
