import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import WhiteKernel, RBF, Exponentiation
from modAL.models import ActiveLearner
import warnings

warnings.filterwarnings("ignore")
import os, sys


class Active_RegressTaskV2(object):
    """
    input parameters:

    batchsize:
    allowed_input: 1 if the input can be in the approximated expr. 0 cannot.
    n_input: num of vars in X
    true_program: the program to map from X to Y

    reward_function(self, p) # in reward function need to decide on 
                             # non-varying parameters

    evaluate(self, p)        # this is the inference task 
                               (evaluate the program on the test set).

    NOTE: nexpr should be left to program.optimize() (nexpr: number of experiments)
    """

    def __init__(self, batchsize, allowed_input, dataX, data_query_oracle, kernel_type='rbf'):
        self.batchsize = batchsize
        self.allowed_input = allowed_input
        self.n_input = allowed_input.size
        self.dataX = dataX
        self.data_query_oracle = data_query_oracle

        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]

        self.init = True
        self.X_grid = self.dataX.get_X_grids()
        if kernel_type == 'rbf':
            self.kernel = RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(noise_level=1,
                                                                                               noise_level_bounds=(1e-10, 1e+1))
        elif kernel_type == 'exp':
            raise NotImplementedError("kernel not found")

    def set_allowed_inputs(self, allowed_inputs):
        self.allowed_input = np.copy(allowed_inputs)

    def set_allowed_input(self, i, flag):
        self.allowed_input[i] = flag

    def rand_draw_data(self):
        self.X = self.dataX.randn(sample_size=self.batchsize)
        # self.y_true = self.data_query_oracle.evaluate(self.X)

    def rand_draw_X_nonfixed(self):
        self.X = self.dataX.randn(sample_size=self.batchsize)
        # self.y_true = self.data_query_oracle.evaluate(self.X)

    def reward_function_fixed_data(self, p):

        # X = self.dataX.randn(sample_size=self.batchsize)
        y_hat = p.execute(self.X)
        if self.init:
            self.init = False
            y_true = self.data_query_oracle.evaluate(self.X)
            self.regressor = ActiveLearner(
                estimator=GaussianProcessRegressor(kernel=self.kernel),
                query_strategy=GP_regression_std,
                X_training=self.X, y_training=y_true
            )
            self.call_idx = 1
        if np.random.randn() > 0.5:
            query_idxes, _ = self.regressor.query(self.X_grid, self.batchsize)
            self.X = self.X_grid[query_idxes]
            self.call_idx += 1

        if self.call_idx % 50 == 0:
            y_true = self.data_query_oracle.evaluate(self.X)
            self.regressor.teach(self.X, y_true)

        print(self.call_idx, end=" ")
        sys.stdout.flush()

        return self.data_query_oracle._evaluate_loss(self.X, y_hat)

    def reward_function(self, p):

        y_hat = p.execute(self.X)
        return self.data_query_oracle._evaluate_loss(self.X, y_hat)

    def reward_function_fixed_data_all_metrics(self, p):
        y_hat = p.execute(self.X)
        dict_of_result = self.data_query_oracle._evaluate_all_losses(self.X, y_hat)
        print('%' * 30)
        for mertic_name in dict_of_result:
            print(f"{mertic_name} {dict_of_result[mertic_name]}")
        print('%' * 30)


def GP_regression_std(regressor, X, batch_size):
    _, std = regressor.predict(X, return_std=True)

    dist = np.exp(std)
    dist /= np.sum(dist)
    query_idics = np.random.choice(range(len(dist)), batch_size, p=dist)
    return query_idics  # , X[query_idx]
