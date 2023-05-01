import os
import random
from typing import List, Set
import numpy as np
import scipy
from file_util import decrypt_equation
import time

# call a million batch of dataset. compute the time.
# a class takes the input of a file, that a file is an equation.
# the class will return a batch of data, everytime it was queried.
# create a offline version to bitbucket.org
#
# future competition.
# offline evaluation: that are not open.
# type of noise, rate of noise.


# init
# 1nd way: the `eq_filename` that contains the equation
# 2nd way is for compeition:
# kill the program for more than 1 hour,
# they need output the best equation vis STDOUT. save to a paticular filename in format '.out' in 1 hours.
# as a participant, we give  them some eq_name_string, output_file_name, _time_limits.
# when you get a better

EQUATION_EXTENSION = ".encrypt"


class Equation_evaluator(object):
    def __init__(self, noise_type='normal', noise_scale=0.1, metric_name="neg_nmse"):
        '''
        true_equation: the program to map from X to Y
        noise_type, noise_scale: the type and scale of noise.
        metric_name: evaluation metric name for `y_true` and `y_pred`
        '''
        self._time_limits = 3600  # 1 hours
        self.true_equation, self.num_vars, self.function_set = self._load_random_equation()

        # metric
        self.metric_name = metric_name
        self.metric = make_regression_metric(metric_name)

        # noise
        self.noise_type = noise_type
        self.noise_scale = noise_scale
        self.noises = construct_noise(self.noise_type)
        self.start = time.time()

    def _load_random_equation(self, equation_folder="encrypted_equtions"):
        program_files = dict()
        for root, dirs, files in os.walk(equation_folder, topdown=False):
            for name in files:
                if name.endswith(EQUATION_EXTENSION):
                    program_files[name] = os.path.join(root, name)
        self.eq_name = random.choice(list(program_files.keys()))

        one_equation = decrypt_equation(program_files[self.eq_name], key_filename="ecrypted_equation/public.key")
        return one_equation['eq_expression'], int(one_equation['num_vars']), one_equation['function_set']

    def evaluate(self, X):
        self.check_timeout()

        # evaluate the y_true from given input X
        nvar, batch_size = X.shape
        if self.true_equation is None:
            self._load_random_equation()
        y_true = self.true_equation.execute(X) + self.noises(self.noise_scale, batch_size)

        return y_true

    def evaluate_loss(self, X, y_hat):
        """
        Compute the y_true based on the input X. And then evaluate the metric value between y_true and y_pred
        """
        self.check_timeout()
        y_true = self.evaluate(X)
        if self.metric_name in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse']:
            loss_val = self.metric(y_true, y_hat, np.var(y_true))
        elif self.metric_name in ['neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
            loss_val = self.metric(y_true, y_hat)
        return loss_val

    def set_best_predicted_equations(self, best_pred_eqs):
        """the client set the best predicted equations"""
        self.best_pred_eqs = best_pred_eqs

    # def final_test_performance(self):
    #     for one_eq in self.best_pred_eqs:
    #

    def evaluate_all_losses(self, X, y_hat):
        """
        Compute the y_true based on the input X. And then evaluate the metric value between y_true and y_hat.
        Return a dictionary of all the loss values.
        """
        self.check_timeout()
        y_true = self.evaluate(X)
        loss_val_dict = {}
        metric_params = (1.0,)
        for metric_name in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse']:
            metric = make_regression_metric(metric_name, *metric_params)
            loss_val = metric(y_true, y_hat, np.var(y_true))
            loss_val_dict[metric_name] = loss_val
        for metric_name in ['neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
            metric = make_regression_metric(metric_name, *metric_params)
            loss_val = metric(y_true, y_hat)
            loss_val_dict[metric_name] = loss_val
        return loss_val_dict

    def check_timeout(self):
        if time.time() - self.start > self._time_limits:
            self.true_equation, self.num_vars, self.function_set = None, None, None
            raise TimeoutError(f"cannot call this protocol for more than {self._time_limits} seconds")

    def get_eq_name(self):
        return self.eq_name

    def get_nvars(self):
        return self.num_vars

    def get_function_set(self):
        return self.function_set


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
    all_metrics = {
        # Negative mean squared error
        "neg_mse": lambda y, y_hat: -np.mean((y - y_hat) ** 2),
        # Negative root mean squared error
        "neg_rmse": lambda y, y_hat: -np.sqrt(np.mean((y - y_hat) ** 2)),
        # Negative normalized mean squared error
        "neg_nmse": lambda y, y_hat, var_y: -np.mean((y - y_hat) ** 2) / var_y,
        # Negative normalized root mean squared error
        "neg_nrmse": lambda y, y_hat, var_y: -np.sqrt(np.mean((y - y_hat) ** 2) / var_y),
        # (Protected) negative log mean squared error
        "neglog_mse": lambda y, y_hat: -np.log(1 + np.mean((y - y_hat) ** 2)),
        # (Protected) inverse mean squared error
        "inv_mse": lambda y, y_hat: 1 / (1 + np.mean((y - y_hat) ** 2)),
        # (Protected) inverse normalized mean squared error
        "inv_nmse": lambda y, y_hat, var_y: 1 / (1 + np.mean((y - y_hat) ** 2) / var_y),
        # (Protected) inverse normalized root mean squared error
        "inv_nrmse": lambda y, y_hat, var_y: 1 / (1 + np.sqrt(np.mean((y - y_hat) ** 2) / var_y)),
        # Pearson correlation coefficient       # Range: [0, 1]
        "pearson": lambda y, y_hat: scipy.stats.pearsonr(y, y_hat)[0],
        # Spearman correlation coefficient      # Range: [0, 1]
        "spearman": lambda y, y_hat: scipy.stats.spearmanr(y, y_hat)[0],
        "accuracy(r2)": lambda y, y_hat: evaluate_accuracy_r2(y, y_hat)}
    assert metric_name in all_metrics, "Unrecognized reward function name."
    return all_metrics[metric_name]


def evaluate_accuracy_r2(y, y_hat, tau=0.95):
    from sklearn.metrics import r2_score
    score = r2_score(y, y_hat)
    return score
