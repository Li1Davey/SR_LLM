import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import WhiteKernel, RBF
from modAL.models import ActiveLearner

X = np.random.uniform(low=1, high=10, size=(200, 4))
y = np.sum(np.sin(X) + np.random.normal(scale=0.1, size=X.shape), axis=-1)


def GP_regression_std(regressor, X, batch_size):
    _, std = regressor.predict(X, return_std=True)

    dist = np.exp(std)
    dist /= np.sum(dist)
    query_idics = np.random.choice(range(len(dist)), batch_size, p=dist)
    return query_idics


n_initial = 128
initial_idx = np.random.choice(range(X.shape[0]), size=n_initial, replace=True)
X_training, y_training = X[initial_idx], y[initial_idx]
kernel = RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(noise_level=1, noise_level_bounds=(1e-10, 1e+1))

print(X_training.shape, y_training.shape)
regressor = ActiveLearner(
    estimator=GaussianProcessRegressor(kernel=kernel),
    query_strategy=GP_regression_std,
    X_training=X_training, y_training=y_training
)

# In[7]:


X_grid = np.linspace((1, 1, 1, 1), (10, 10, 10, 10), 4000)
y_pred, y_std = regressor.predict(X_grid, return_std=True)
y_pred, y_std = y_pred.ravel(), y_std.ravel()

# In[9]:


len(y_std)

n_queries = 10
batch_size = 11
query_idics, _ = regressor.query(X_grid, batch_size)
print(query_idics, X[query_idics].shape, y[query_idics].shape)
regressor.teach(X[query_idics].reshape(batch_size, -1), y[query_idics])

y_pred_final, y_std_final = regressor.predict(X_grid, return_std=True)
y_pred_final, y_std_final = y_pred_final.ravel(), y_std_final.ravel()
