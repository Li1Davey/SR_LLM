import numpy as np


class RegressTask(object):
    """
    Used to handle input data 'X' for querying the data oracle.
    Also used to set controlled variables in input data `X`.
    """

    def __init__(self, batchsize, allowed_input, dataX, data_query_oracle):
        """
        batchsize: batch size
        allowed_input: 1 if the input variable is free, 0 if controlled
        dataX: input data generator
        """
        self.batchsize = batchsize
        self.allowed_input = allowed_input
        self.n_input = allowed_input.size
        self.dataX = dataX
        self.data_query_oracle = data_query_oracle

        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]

        # Always keep X_fixed as a 1D vector of length n_input
        self.X_fixed = np.atleast_1d(self.dataX.randn(sample_size=1))
        if self.X_fixed.size != self.n_input:
            self.X_fixed = np.resize(self.X_fixed, self.n_input)

    def set_allowed_inputs(self, allowed_inputs):
        self.allowed_input = np.copy(allowed_inputs)
        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]

    def set_allowed_input(self, i, flag):
        self.allowed_input[i] = flag
        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]

    def _ensure_2d_X(self, X):
        """
        Ensure X has shape (batchsize, num_vars).
        """
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return X

    def rand_draw_X_non_fixed(self):
        self.X = self.dataX.randn(sample_size=self.batchsize)
        self.X = self._ensure_2d_X(self.X)

    def rand_draw_X_fixed(self):
        X_fixed = self.dataX.randn(sample_size=1)
        X_fixed = np.atleast_1d(X_fixed)

        if X_fixed.size != self.n_input:
            X_fixed = np.resize(X_fixed, self.n_input)

        self.X_fixed = X_fixed

    def rand_draw_X_fixed_with_index(self, xi):
        X_fixed = self.dataX.randn(sample_size=1)
        X_fixed = np.atleast_1d(X_fixed)

        if X_fixed.size != self.n_input:
            X_fixed = np.resize(X_fixed, self.n_input)

        self.X_fixed[xi] = X_fixed[xi]

        if hasattr(self, "X") and len(self.fixed_column):
            self.X[:, self.fixed_column] = self.X_fixed[self.fixed_column]

    def rand_draw_data_with_X_fixed(self):
        self.X = self.dataX.randn(sample_size=self.batchsize)
        self.X = self._ensure_2d_X(self.X)

        if len(self.fixed_column):
            self.X[:, self.fixed_column] = self.X_fixed[self.fixed_column]

    def evaluate(self):
        return self.data_query_oracle.evaluate(self.X)

    def reward_function(self, p):
        y_hat = p.execute(self.X)
        return self.data_query_oracle._evaluate_loss(self.X, y_hat)
