import numpy as np


class RegressTask(object):
    """
    Minimal task with per-episode cached train/validation batches.

    The important change is that MCTS can evaluate all candidates in an episode
    on the same data instead of redrawing on every terminal expansion.
    """

    def __init__(self, batchsize, dataX, data_query_oracle):
        self.batchsize = batchsize
        self.dataX = dataX
        self.data_query_oracle = data_query_oracle
        self.X = None
        self.y = None

        self.train_X = None
        self.train_y = None
        self.val_X = None
        self.val_y = None

    def _ensure_2d_X(self, X):
        X = np.asarray(X)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        # DataX.randn() returns [num_vars, sample_size] for scalar variables.
        # Equation_evaluator.evaluate() expects [sample_size, num_vars].
        expected_nvars = self.data_query_oracle.get_nvars()
        if X.ndim == 2 and X.shape[0] == expected_nvars and X.shape[1] != expected_nvars:
            X = X.T

        return X

    def rand_draw_data(self):
        self.X = self._ensure_2d_X(self.dataX.randn(sample_size=self.batchsize))
        self.y = self.data_query_oracle.evaluate(self.X)

    def draw_episode_batches(self):
        self.train_X = self._ensure_2d_X(self.dataX.randn(sample_size=self.batchsize))
        self.train_y = self.data_query_oracle.evaluate(self.train_X)

        self.val_X = self._ensure_2d_X(self.dataX.randn(sample_size=self.batchsize))
        self.val_y = self.data_query_oracle.evaluate(self.val_X)

        # Keep current batch aligned with train by default for backward compatibility.
        self.X = self.train_X
        self.y = self.train_y

    def get_train_batch(self):
        if self.train_X is None or self.train_y is None:
            self.draw_episode_batches()
        return self.train_X, self.train_y

    def get_val_batch(self):
        if self.val_X is None or self.val_y is None:
            self.draw_episode_batches()
        return self.val_X, self.val_y

    def evaluate(self):
        if self.y is None:
            self.rand_draw_data()
        return self.y

    def reward_function(self, p):
        y_hat = p.execute(self.X)

        if isinstance(y_hat, np.ndarray) and (not np.all(np.isfinite(y_hat))):
            return -1e9

        if getattr(p, "invalid", False):
            return -1e9

        return self.data_query_oracle._evaluate_loss(self.X, y_hat)