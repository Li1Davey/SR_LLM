import StackGP as sgp
import numpy as np
from plots import plot_models

# Define demo function to generate data
def demoFunc(x, y):
    return x ** 2 / y


inputData = np.array([range(10), np.random.randint(1, 10, 10)])
response = demoFunc(inputData[0], inputData[1])

# Generate models
models = sgp.evolve(inputData, response)
# View model population quality
plot_models(models)
# View best model
sgp.print_gp_model(models[0])
