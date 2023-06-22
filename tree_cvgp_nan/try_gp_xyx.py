import functions
from library import Library, Token, PlaceholderConstant
import execute
import argparse
from program import Program
import regress_task
from const import ScipyMinimize

import gp_xyx
import gen_true_program

import numpy as np
# np.random.seed(42)
import random
# random.seed(42)
import time

averaged_var_y = 10  # 569

config = {'neg_mse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': 0.01},
          'neg_nmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': 0.01 / averaged_var_y},
          'neg_nrmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': np.sqrt(0.01 / averaged_var_y)},
          'neg_rmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': 0.1},
          'inv_mse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': -1 / (1 + 0.01)},
          'inv_nmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': -1 / (1 + 0.01 / averaged_var_y)},
          'inv_nrmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': -1 / (1 + np.sqrt(0.01 / averaged_var_y))},
          }


def run_expanding_gp(nvar, true_program_file, metric_name, noise_std):
    # nvar = 5
    regress_batchsize = 10
    opt_num_expr = 5

    expr_obj_thres = config[metric_name]['expr_obj_thres']
    expr_consts_thres = config[metric_name]['expr_consts_thres']

    # gp parameters
    cxpb = 0.5
    mutpb = 0.5
    maxdepth = 2
    tour_size = 3
    hof_size = 10

    population_size = 25  # 00
    n_generations = 100

    # get all the functions and variables ready
    var_x = []
    for i in range(nvar):
        xi = Token(None, 'X_' + str(i), 0, 0., i)
        var_x.append(xi)

    ops = [
        # Binary operators
        Token(np.add, "add", arity=2, complexity=1),
        Token(np.subtract, "sub", arity=2, complexity=1),
        Token(np.multiply, "mul", arity=2, complexity=1),
        Token(np.sin, "sin", arity=1, complexity=3),
        Token(np.cos, "cos", arity=1, complexity=3),
        # functions.protected_ops[0],  # 'div'
        functions.protected_ops[5]  # 'inv' '1/x'
    ]
    named_const = [PlaceholderConstant(1.0)]
    protected_library = Library(ops + var_x + named_const)

    protected_library.print_library()

    # get program ready
    Program.library = protected_library
    Program.opt_num_expr = opt_num_expr
    Program.expr_obj_thres = expr_obj_thres
    Program.expr_consts_thres = expr_consts_thres

    Program.set_execute(True)  # protected = True

    # set const_optimizer
    Program.const_optimizer = ScipyMinimize()
    Program.noise_std = noise_std

    # create the true program
    # XYX: no more creating program. read program
    # x_0 + 3 x_2 + 5 x_4 - 6 x_2 x_4 + 9 x_0 x_2
    # preorder = ['add', \
    #                  'add', 'add', 'X_0', 'mul', 'const', 'X_2', \
    #                         'mul', 'const', 'X_4', \
    #                  'sub', 'mul', 'const', 'mul', 'X_0', 'X_2', \
    #                         'mul', 'const', 'mul', 'X_2', 'X_4']
    # x_0 + 3 1/x_2 + 5 x_4 - 6 1/x_0 x_4 + 9 x_0 x_2
    # preorder = ['add', \
    #                   'add', 'add', 'X_0', 'mul', 'const', 'inv', 'X_2', \
    #                          'mul', 'const', 'X_4', \
    #                   'sub', 'mul', 'const', 'mul', 'X_0', 'X_2', \
    #                          'mul', 'const', 'mul', 'inv', 'X_0', 'X_4']

    # preorder_actions = protected_library.actionize(preorder)
    # true_pr_allow_change = np.zeros(len(preorder), dtype=np.int32)
    # true_pr = Program(preorder_actions, true_pr_allow_change)

    # true_pr.traversal[5] = PlaceholderConstant(3.0) 
    # true_pr.traversal[9] = PlaceholderConstant(5.0) 
    # true_pr.traversal[13] = PlaceholderConstant(9.0) 
    # true_pr.traversal[18] = PlaceholderConstant(6.0)
    # true_pr.traversal[5] = PlaceholderConstant(3.0)
    # true_pr.traversal[8] = PlaceholderConstant(5.0)
    # true_pr.traversal[12] = PlaceholderConstant(9.0)
    # true_pr.traversal[17] = PlaceholderConstant(6.0)

    # # x_0 + 3 x_2
    # preorder = ['add', 'X_0', 'mul', 'const', 'X_2']
    # preorder_actions = protected_library.actionize(preorder)
    # true_pr_allow_change = np.zeros(len(preorder), dtype=np.int32)
    # true_pr = Program(preorder_actions, true_pr_allow_change)

    # true_pr.traversal[3] = PlaceholderConstant(3.0) 

    # x_0 + 3
    # preorder = ['add', 'X_0', 'const']
    # preorder_actions = protected_library.actionize(preorder)
    # true_pr_allow_change = np.zeros(len(preorder), dtype=np.int32)
    # true_pr = Program(preorder_actions, true_pr_allow_change)

    # true_pr.traversal[2] = PlaceholderConstant(3.0) 

    # read the program
    prog = gen_true_program.read_true_program(true_program_file)
    true_pr = gen_true_program.build_program(prog, protected_library, 0)

    # set the task
    allowed_input_tokens = np.zeros(nvar, dtype=np.int32)  # set it for now. Will change in gp.run
    Program.task = regress_task.RegressTaskV1(regress_batchsize,
                                              allowed_input_tokens,
                                              true_pr,
                                              noise_std,
                                              metric=metric_name)

    # set gp helper
    gp_helper = gp_xyx.GPHelper()
    gp_helper.library = protected_library

    # set GP
    gp_xyx.ExpandingGeneticProgram.library = protected_library
    gp_xyx.ExpandingGeneticProgram.gp_helper = gp_helper
    gp = gp_xyx.ExpandingGeneticProgram(cxpb, mutpb, maxdepth, population_size,
                                        tour_size, hof_size, n_generations, nvar)

    # run GP
    # gp.run()
    gp.run_with_tree_based_randomized_vatriable_ordering()

    # print
    print('final hof=')
    gp.print_hof()
    print('gp.timer_log=', gp.timer_log)


def run_gp(nvar, true_program_file, metric_name, noise_std):
    # nvar = 5
    regress_batchsize = 256
    opt_num_expr = 1  # currently do not need to re-run the experiments multiple times.

    # gp parameters
    cxpb = 0.5
    mutpb = 0.5
    maxdepth = 2
    population_size = 25  # 00 #00
    tour_size = 3
    hof_size = 10
    n_generations = 100  # 00

    # get all the functions and variables ready
    var_x = []
    for i in range(nvar):
        xi = Token(None, 'X_' + str(i), 0, 0., i)
        var_x.append(xi)

    ops = [
        # Binary operators
        Token(np.add, "add", arity=2, complexity=1),
        Token(np.subtract, "sub", arity=2, complexity=1),
        Token(np.multiply, "mul", arity=2, complexity=1),
        Token(np.sin, "sin", arity=1, complexity=3),
        Token(np.cos, "cos", arity=1, complexity=3),
        # functions.protected_ops[0],  # 'div'
        functions.protected_ops[5]  # 'inv' '1/x'
    ]
    named_const = [PlaceholderConstant(1.0)]
    protected_library = Library(ops + var_x + named_const)

    protected_library.print_library()

    # everything is allowed.
    allowed_input_tokens = np.ones(nvar, dtype=np.int32)
    protected_library.set_allowed_input_tokens(allowed_input_tokens)

    # get program ready
    Program.library = protected_library
    Program.opt_num_expr = opt_num_expr
    Program.set_execute(True)  # protected = True

    # set const_optimizer
    Program.const_optimizer = ScipyMinimize()
    Program.noise_std = noise_std

    # create the true program
    # XYX: no more creating program. read program
    # x_0 + 3 1/x_2 + 5 x_4 - 6 1/x_2 x_4 + 9 x_0 x_2
    # preorder = ['add', \
    #                   'add', 'add', 'X_0', 'mul', 'const', 'inv', 'X_2', \
    #                          'mul', 'const', 'X_4', \
    #                   'sub', 'mul', 'const', 'mul', 'X_0', 'X_2', \
    #                          'mul', 'const', 'mul', 'inv', 'X_2', 'X_4']
    # preorder_actions = protected_library.actionize(preorder)
    # true_pr_allow_change = np.zeros(len(preorder), dtype=np.int32)
    # true_pr = Program(preorder_actions, true_pr_allow_change)

    # true_pr.traversal[5] = PlaceholderConstant(3.0) 
    # true_pr.traversal[9] = PlaceholderConstant(5.0) 
    # true_pr.traversal[13] = PlaceholderConstant(9.0) 
    # true_pr.traversal[18] = PlaceholderConstant(6.0)

    # # x_0 + 3 x_2
    # preorder = ['add', 'X_0', 'mul', 'const', 'X_2']
    # preorder_actions = protected_library.actionize(preorder)
    # true_pr_allow_change = np.zeros(len(preorder), dtype=np.int32)
    # true_pr = Program(preorder_actions, true_pr_allow_change)

    # true_pr.traversal[3] = PlaceholderConstant(3.0) 

    # x_0 + 3
    # preorder = ['add', 'X_0', 'const']
    # preorder_actions = protected_library.actionize(preorder)
    # true_pr_allow_change = np.zeros(len(preorder), dtype=np.int32)
    # true_pr = Program(preorder_actions, true_pr_allow_change)

    # true_pr.traversal[2] = PlaceholderConstant(3.0)

    # read the program
    prog = gen_true_program.read_true_program(true_program_file)
    true_pr = gen_true_program.build_program(prog, protected_library, 0)

    # set the task
    Program.task = regress_task.RegressTaskV1(regress_batchsize,
                                              allowed_input_tokens,
                                              true_pr,
                                              noise_std,
                                              metric=metric_name)

    # set gp helper
    gp_helper = gp_xyx.GPHelper()
    gp_helper.library = protected_library

    # set GP
    gp_xyx.GeneticProgram.library = protected_library
    gp_xyx.GeneticProgram.gp_helper = gp_helper
    gp = gp_xyx.GeneticProgram(cxpb, mutpb, maxdepth, population_size, tour_size, \
                               hof_size, n_generations)

    # run GP
    gp.run()

    # print
    print('final hof=')
    gp.print_hof()
    print('gp.timer_log=', gp.timer_log)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("nvar", type=int, help="number of variables.")
    parser.add_argument("true_program_file", help="the filename of the true program (pickle dump).")
    parser.add_argument("metric_name", type=str, help="The name of the metric.")
    parser.add_argument("--expand_gp", action="store_true", help="whether run normal gp (expand_gp=False) or expand_gp.")
    parser.add_argument("--noise_std", type=float,  default=0.0, help="running with Gaussian noise added. This parameter adds the standard deviation of the Gaussian. Default=0 (no noise)")

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)

    if args.expand_gp:
        run_expanding_gp(args.nvar, args.true_program_file, args.metric_name, args.noise_std)
    else:
        run_gp(args.nvar, args.true_program_file, args.metric_name, args.noise_std)
