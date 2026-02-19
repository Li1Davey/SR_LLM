import numpy as np


class RegressTask(object):
    """
    Minimal task: always sample full X and evaluate y.
    No controlled/fixed variables (CTV) logic.
    """

    def __init__(self, batchsize, dataX, data_query_oracle):
        self.batchsize = batchsize
        self.dataX = dataX
        self.data_query_oracle = data_query_oracle
        self.X = None

    @staticmethod
    def _ensure_2d_X(X):
        X = np.asarray(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return X

    def rand_draw_data(self):
        self.X = self._ensure_2d_X(self.dataX.randn(sample_size=self.batchsize))

    def evaluate(self):
        return self.data_query_oracle.evaluate(self.X)

    def reward_function(self, p):
        y_hat = p.execute(self.X)

        # hard reject invalid outputs
        if isinstance(y_hat, np.ndarray) and (not np.all(np.isfinite(y_hat))):
            return -1e9

        # if Program tracks invalids, reject those too
        if getattr(p, "invalid", False):
            return -1e9

        return self.data_query_oracle._evaluate_loss(self.X, y_hat)
    