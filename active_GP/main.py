import StackGP as sgp
import numpy as np
from plots import plot_models
import argparse
import time
import random
from pympler import classtracker, asizeof
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regression_task import RegressTask
from function import construct_ops


# Define demo function to generate data


def run_stack_GP(
        equation_name, num_generations, metric_name, noise_type, noise_scale
):
    """
    """
    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()
    operators_set = data_query_oracle.get_operators_set()
    ops = construct_ops(operators_set)
    regress_batchsize = 256
    allowed_input_tokens = np.ones(nvar, dtype=np.int32)
    task = RegressTask(regress_batchsize,
                       allowed_input_tokens,
                       dataXgen,
                       data_query_oracle)

    inputData = np.array([range(10), np.random.randint(1, 10, 10)])

    def demoFunc(x, y):
        return x ** 2 / y

    response = demoFunc(inputData[0], inputData[1])

    # Generate models
    start = time.time()
    models = sgp.evolve(inputData, response, num_generations, ops=ops)
    end_time = time.time() - start
    # View best model
    print(sgp.print_gp_model(models[0]))

    print("actGP time is {} mins".format(np.round(end_time / 60, 3)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")

    parser.add_argument("--metric_name", type=str, default='neg_mse', help="The name of the metric for loss.")
    parser.add_argument("--num_generations", type=int, default=1000, help="the number of generations for GP.")
    parser.add_argument("--noise_type", type=str, default='normal', help="The name of the noises.")
    parser.add_argument("--noise_scale", type=float, default=0.0, help="This parameter adds the standard deviation of the noise")

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)
    print(args)
    run_stack_GP(args.equation_name, args.num_generations, args.metric_name, args.noise_type, args.noise_scale)
