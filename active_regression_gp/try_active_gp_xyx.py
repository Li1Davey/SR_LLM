from library import Library
import argparse
from program import Program
import regress_task
from const import ScipyMinimize
from symbolic_data_generator import *
from symbolic_equation_evaluator_public import Equation_evaluator
from functions import create_tokens

import gp_xyx

import numpy as np
import random
import time


def run_active_regression_gp(equation_name, metric_name, noise_type, noise_scale):
    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()

    regress_batchsize = 256
    opt_num_expr = 5

    # gp parameters
    cxpb = 0.7
    mutpb = 0.7
    maxdepth = 2
    tour_size = 3
    hof_size = 30

    population_size = 100  # 00
    n_generations = 100

    # get all the functions and variables ready
    all_tokens = create_tokens(nvar, data_query_oracle.function_set, protected=True)
    protected_library = Library(all_tokens)

    protected_library.print_library()

    # get program ready
    Program.library = protected_library
    Program.opt_num_expr = opt_num_expr

    Program.set_execute(True)  # protected = True

    # set const_optimizer
    Program.const_optimizer = ScipyMinimize()
    Program.noise_std = noise_scale

    # set the task
    allowed_input_tokens = np.zeros(nvar, dtype=np.int32)  # set it for now. Will change in gp.run
    Program.task = regress_task.Active_RegressTaskV2(regress_batchsize,
                                                     allowed_input_tokens,
                                                     dataXgen,
                                                     data_query_oracle)

    # set gp helper
    gp_helper = gp_xyx.GPHelper()
    gp_helper.library = protected_library

    # set GP
    gp_xyx.ActiveRegressionGeneticProgram.library = protected_library
    gp_xyx.ActiveRegressionGeneticProgram.gp_helper = gp_helper
    egp = gp_xyx.ActiveRegressionGeneticProgram(cxpb, mutpb, maxdepth, population_size,
                                                tour_size, hof_size, n_generations)

    # run GP
    egp.run()

    # print
    print('final hof=')
    egp.print_hof()
    print('egp.timer_log=', egp.timer_log)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")
    parser.add_argument("--metric_name", type=str, help="The name of the metric for loss.")
    parser.add_argument("--noise_type", type=str, help="The name of the noises.")
    parser.add_argument("--noise_scale", type=float, default=0.0, help="This parameter adds the standard deviation of the noise")

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)

    run_active_regression_gp(args.equation_name, args.metric_name, args.noise_type, args.noise_scale)
