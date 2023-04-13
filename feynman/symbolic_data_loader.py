import time

import numpy as np
import scipy
from feynman_datasets import sampling, physic_equations
from feynman_datasets.registry import get_eq_obj
from feynman_datasets.sampling import build_sampling_objs
import json


# call a million batch of dataset. compute the time.
# a class takes the input of a file, that a file is an equation.
# the class will return a batch of data, everytime it was queried.
# don't do the tcp version.
# create a offline version to bitbucket.org
#
# future competition.
# offline evaluation: that are not open.
# type of noise, rate of noise.


def _recv_config_send_Xy():
    import zmq
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    idx = 0
    while True:
        #  Wait for next request from client
        message = socket.recv_json()
        # print("Received request: {}".format(message))
        dataset = generate_batch_Xy(message['eq_name'], message['batch_size'])

        #  Do some 'work'
        # time.sleep(1)
        # print('Sending data pairs: {}'.format(dataset.shape))
        #  Send reply back to client
        socket.send(dataset)
        idx += 1
        if idx % 100 == 0:
            print("sending", idx)


def generate_batch_Xy(dataset_name, sample_size):
    print(f'Generating dataset `{dataset_name}` ...')
    print()
    dataset_kwargs = dict()

    # Instantiate equation object
    sampling_objs = build_sampling_objs(dataset_kwargs.pop('sampling_objs')) if 'sampling_objs' in dataset_kwargs else None
    eq_instance = get_eq_obj(dataset_name, sampling_objs=sampling_objs, **dataset_kwargs)
    # Generate tabular dataset
    dataset = eq_instance.create_dataset(sample_size)
    return dataset


def generate_cvgp_format_dataset(dataset_name, sample_file_size, singlefile_sample_size=256):
    print(f'Generating dataset `{dataset_name}` ...')
    dataset_kwargs = dict()
    # Instantiate equation object
    sampling_objs = build_sampling_objs(dataset_kwargs.pop('sampling_objs')) if 'sampling_objs' in dataset_kwargs else None
    eq_instance = get_eq_obj(dataset_name, sampling_objs=sampling_objs, **dataset_kwargs)

    # Write out each split
    fixed_column = [i for i in range(len(eq_instance.x))]
    dataset = eq_instance.create_fixedcolumn_dataset(singlefile_sample_size, fixed_column)
    return dataset


class Dataloader(object):
    def __init__(self, dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name):
        '''
        true_program: the program to map from X to Y
        batch_size: number of data points.
        noise_type, noise_scale: the type and scale of noise.
        metric_name: evaluation metric name for `y_true` and `y_pred`
        '''
        self.dataset_family = dataset_family
        self.true_program = true_program
        self.batch_size = batch_size

        # metric
        self.metric_name = metric_name
        self.metric = make_regression_metric(metric_name)

        # noise
        self.noise_type = noise_type
        self.noise_scale = noise_scale
        self.noises = construct_noise(self.noise_type)

    def gen_X_randomly(self, input_dim, fixed_dims, scale=9.5, bias=0.5, **extra_params):
        '''
        generate a batch of data randomly.
        '''

        X = np.random.rand(self.batch_size, input_dim) * scale + bias
        if len(fixed_dims) != 0:
            X[:, fixed_dims] = X[0, fixed_dims]
        return X

    def compute_ytrue_from_given_X(self, X):
        """
        evaluate the y_true from given input X
        """
        y_true = self.true_program.execute(X) + self.noises(self.noise_scale, self.batch_size)
        return y_true

    def compute_metric_loss(self, y_true, y_pred):
        """
        evaluate the metric value between y_true and y_pred
        """
        if self.metric_name in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse']:
            loss = self.metric(y_true, y_pred, np.var(y_true))
        elif self.metric_name in ['neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']
            loss = self.metric(y_true, y_pred)
        return loss


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


def construct_noise(noise_type):
    _all_samplers = {
        'normal': lambda scale, batch_size: np.random.normal(loc=0.0, scale=scale, size=batch_size),
        'exponential': lambda scale, batch_size: np.random.exponential(scale=scale, size=batch_size),
        'uniform': lambda scale, batch_size: np.random.uniform(low=-np.abs(scale), high=np.abs(scale), size=batch_size),
        'laplace': lambda scale, batch_size: np.random.laplace(loc=0.0, scale=scale, size=batch_size),
        'logistic': lambda scale, batch_size: np.random.logistic(loc=0.0, scale=scale, size=batch_size)
    }
    assert noise_type in _all_samplers, "Unrecognized noise_type" + noise_type

    return _all_samplers[noise_type]


def make_regression_metric(metric_name):
    """
    Factory function for a regression metric. This includes a closures for metric parameters and the variance of the training data.
    metric_name: Regression metric mapping true and estimated values to a scalar.
    """
    all_metrics = {
        # Negative mean squared error
        # Range: [-inf, 0]
        # Value = -var(y) when y_hat == mean(y)
        "neg_mse": lambda y, y_hat: -np.mean((y - y_hat) ** 2),

        # Negative root mean squared error
        # Range: [-inf, 0]
        # Value = -sqrt(var(y)) when y_hat == mean(y)
        "neg_rmse": lambda y, y_hat: -np.sqrt(np.mean((y - y_hat) ** 2)),

        # Negative normalized mean squared error
        # Range: [-inf, 0]
        # Value = -1 when y_hat == mean(y)
        "neg_nmse": lambda y, y_hat, var_y: -np.mean((y - y_hat) ** 2) / var_y,

        # Negative normalized root mean squared error
        # Range: [-inf, 0]
        # Value = -1 when y_hat == mean(y)
        "neg_nrmse": lambda y, y_hat, var_y: -np.sqrt(np.mean((y - y_hat) ** 2) / var_y),

        # (Protected) negative log mean squared error
        # Range: [-inf, 0]
        # Value = -log(1 + var(y)) when y_hat == mean(y)
        "neglog_mse": lambda y, y_hat: -np.log(1 + np.mean((y - y_hat) ** 2)),

        # (Protected) inverse mean squared error
        # Range: [0, 1]
        # Value = 1/(1 + args[0]*var(y)) when y_hat == mean(y)
        "inv_mse": lambda y, y_hat: 1 / (1 + np.mean((y - y_hat) ** 2)),

        # (Protected) inverse normalized mean squared error
        # Range: [0, 1]
        # Value = 1/(1 + args[0]) when y_hat == mean(y)
        "inv_nmse": lambda y, y_hat, var_y: 1 / (1 + np.mean((y - y_hat) ** 2) / var_y),

        # (Protected) inverse normalized root mean squared error
        # Range: [0, 1]
        # Value = 1/(1 + args[0]) when y_hat == mean(y)
        "inv_nrmse": lambda y, y_hat, var_y: 1 / (1 + np.sqrt(np.mean((y - y_hat) ** 2) / var_y)),

        # Pearson correlation coefficient
        # Range: [0, 1]
        "pearson": lambda y, y_hat: scipy.stats.pearsonr(y, y_hat)[0],

        # Spearman correlation coefficient
        # Range: [0, 1]
        "spearman": lambda y, y_hat: scipy.stats.spearmanr(y, y_hat)[0]
    }

    assert metric_name in all_metrics, "Unrecognized reward function name."

    return all_metrics[metric_name]


class Feynman_dataloader(Dataloader):
    def __int__(self, dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name):
        """
        dataset_family: feynman-easy, feynman-medium, feynman-hard
        """
        super().__int__(dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name)
        pass

    def gen_X_randomly(self, input_dim, fixed_dims, scale=9.5, bias=0.5, **extra_params):
        pass


class SinCosInv_dataloader(Dataloader):
    def __int__(self, dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name):
        """
        dataset_family: Inv, SinCos, SinCosInv
        """
        super().__int__(dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name)
        pass

    def gen_X_randomly(self, input_dim, fixed_dims, scale=9.5, bias=0.5, **extra_params):
        pass
