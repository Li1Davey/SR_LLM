import pandas as pd
import numpy as np
import warnings

from scibench.symbolic_equation_evaluator import Equation_evaluator

FLOAT32_MAX = np.finfo(np.float32).max
FLOAT32_MIN = np.finfo(np.float32).min
FLOAT32_TINY = np.finfo(np.float32).tiny


def load_dataset_df(eq_name='prog_0', batch_size=256):
    return dataX_generator.random_uniform_dataset(eq_name, batch_size)


# class DataLoader(object):
#     def __init__(self, dataset_family_name, eq_name, noise_type='normal', noise_scale=0):
#         self.dataset_family_name = dataset_family_name
#         self.eq_name = eq_name
#         self.noise_type = noise_type
#         self.noise_scale = noise_scale
def check_if_valid(values):
    return ~np.isnan(values) * ~np.isinf(values) * \
        (FLOAT32_MIN <= values) * (values <= FLOAT32_MAX) * (np.abs(values) >= FLOAT32_TINY)


class DataLoader(object):
    def __int__(self, eq_name_public, noise_type, noise_scale):
        """
        dataset_family: symbolic_equation_evaluator-easy, symbolic_equation_evaluator-medium, symbolic_equation_evaluator-hard
        """
        self.dataX_generator = get_eq_obj(self.eq_name)
        self.eq_evaulator = Equation_evaluator(eq_name_public)

    def random_uniform_data(self, sample_size, patience=30):
        warnings.filterwarnings('ignore')
        assert len(self.dataX_generator.sampling_objs) > 0, f'There should be at least one variable provided'

        xs = self.dataX_generator.obtain_dataX(sample_size)
        y = self.eq_evaulator.evaluate(xs)

        # Check if y contains NaN, Infinity, etc
        valid_sample_flags = check_if_valid(y)
        valid_sample_size = sum(valid_sample_flags)
        if valid_sample_size == sample_size:
            return np.array([*xs, y]).T

        valid_xs = [x[valid_sample_flags] for x in xs]
        valid_y = y[valid_sample_flags]
        missed_sample_size = sample_size - valid_sample_size
        for _ in range(patience):
            xs = self.dataX_generator.obtain_dataX(missed_sample_size * 3)
            y = self.eq_evaulator.evaluate(xs)
            valid_sample_flags = check_if_valid(y)
            valid_xs = [np.concatenate([xs[i][valid_sample_flags], valid_xs[i]]) for i in range(len(xs))]
            valid_y = np.concatenate([y[valid_sample_flags], valid_y])
            valid_sample_size = len(valid_y)
            if valid_sample_size >= sample_size:
                xs = [x[:sample_size] for x in valid_xs]
                y = valid_y[:sample_size]
                return pd.DataFrame(np.array([*xs, y]).T)
        raise TimeoutError(f'number of valid samples (`{len(valid_y)}`) did not reach to '
                           f'{sample_size} within {patience} trials')

    def Control_variable_dataset(self, batch_size):
        pass

    def Active_learning_dataset(self):
        pass


def make_data_sample_distribution(dataX_sampling_type):
    _all_samplers = {
        'normal': lambda scale, batch_size: np.random.normal(loc=0.0, scale=scale, size=batch_size),
        'exponential': lambda scale, batch_size: np.random.exponential(scale=scale, size=batch_size),
        'uniform': lambda scale, batch_size: np.random.uniform(low=-np.abs(scale), high=np.abs(scale), size=batch_size),
        'laplace': lambda scale, batch_size: np.random.laplace(loc=0.0, scale=scale, size=batch_size),
        'logistic': lambda scale, batch_size: np.random.logistic(loc=0.0, scale=scale, size=batch_size)
    }
    assert dataX_sampling_type in _all_samplers, "Unrecognized noise_type" + dataX_sampling_type

    return _all_samplers[dataX_sampling_type]
