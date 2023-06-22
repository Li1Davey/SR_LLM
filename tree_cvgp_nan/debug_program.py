from sympy.parsing.sympy_parser import parse_expr
import functions
from library import Library, Token, PlaceholderConstant
import argparse
from program import Program
import regress_task
from const import ScipyMinimize

import gp_xyx
import gen_true_program

import numpy as np
import random
import time
from pythonds.basic import Stack

averaged_var_y = 10

config = {
    'neg_mse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': 0.01},
    'neg_nmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': 0.01 / averaged_var_y},
    'neg_nrmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': np.sqrt(0.01 / averaged_var_y)},
    'neg_rmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': 0.1},
    'inv_mse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': -1 / (1 + 0.01)},
    'inv_nmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': -1 / (1 + 0.01 / averaged_var_y)},
    'inv_nrmse': {'expr_consts_thres': 1e-3, 'expr_obj_thres': -1 / (1 + np.sqrt(0.01 / averaged_var_y))},
}


def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True


def load_prog35_gp_pred_program():
    raw_string = "sub, -10.371738225318362, mul, sub, 10.700713035599259, mul, sub, 2.750852184125945, mul, -0.11765431709952094, sub, X_0, mul, mul, -0.02338608845578278, sub, add, X_4, X_4, 13.497428633585345, X_1, sub, 4.442858305031236, mul, sub, 17.63128612393629, sub, add, X_1, X_0, mul, 3.196221124530321, sub, add, X_4, X_4, 6.8572322721690915, sub, 0.020470160645142177, mul, -0.001036378157606791, sub, X_3, X_2, sub, add, X_1, X_0, mul, 0.9962385842993893, sub, X_0, X_2"
    preorder_exp_expr = [it.strip() for it in raw_string.split(',')]
    preorder = []
    const_loc = []
    const = []
    for i in range(len(preorder_exp_expr)):
        if isfloat(preorder_exp_expr[i]):
            preorder.append('const')
            const_loc.append(i)
            const.append(float(preorder_exp_expr[i]))
        else:
            preorder.append(preorder_exp_expr[i])
    return {'preorder': preorder, 'const_loc': const_loc, 'consts': const}


def load_prog_egp_pred_program(raw_string):
    # program 21
    # from sympy import preorder_traversal, symbols
    preorder_exp_expr = [it.strip() for it in raw_string.split(',')]
    preorder = []
    const_loc = []
    const = []
    for i in range(len(preorder_exp_expr)):
        if isfloat(preorder_exp_expr[i]):
            preorder.append('const')
            const_loc.append(i)
            const.append(float(preorder_exp_expr[i]))
        else:
            preorder.append(preorder_exp_expr[i])
    return {'preorder': preorder, 'const_loc': const_loc, 'consts': const}


def compute_egp_diff(nvar, true_program_file, raw_expr_str, metric_name):
    #############################
    # step 1: load true program #
    #############################
    # nvar = 5
    regress_batchsize = 256
    opt_num_expr = 5

    expr_obj_thres = config[metric_name]['expr_obj_thres']
    expr_consts_thres = config[metric_name]['expr_consts_thres']

    # gp parameters
    cxpb = 0.5
    mutpb = 0.5
    maxdepth = 2
    tour_size = 3
    hof_size = 2

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
        functions.protected_ops[0],  # 'div'
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

    # read the program
    prog = gen_true_program.read_true_program(true_program_file)
    true_pr = gen_true_program.build_program(prog, protected_library, 0)

    # set the task
    allowed_input_tokens = np.ones(nvar, dtype=np.int32)  # set it for now. Will change in gp.run
    Program.task = regress_task.RegressTaskV1(regress_batchsize,
                                              allowed_input_tokens,
                                              true_pr,
                                              metric=metric_name)

    # set gp helper
    gp_helper = gp_xyx.GPHelper()
    gp_helper.library = protected_library

    # set GP
    gp_xyx.ExpandingGeneticProgram.library = protected_library
    gp_xyx.ExpandingGeneticProgram.gp_helper = gp_helper
    gp = gp_xyx.ExpandingGeneticProgram(cxpb, mutpb, maxdepth, population_size,
                                        tour_size, hof_size, n_generations, nvar)

    #####################################
    # step 2: load predicted expression
    # and generate the test result
    #####################################
    pred_prog = load_prog_egp_pred_program(raw_expr_str)
    pred_pr = gen_true_program.build_program(pred_prog, protected_library, 0)
    gp.population[0] = pred_pr
    gp.population[0].task.fixed_column = []
    pr = gp.population[0]
    print(pr.__getstate__())
    print(pr.print_expression())
    list_of_random_test = []
    for it in range(10):
        pr.task.rand_draw_data()
        print('iter:{}, validate r={}'.format(it, pr.task.reward_function_fixed_data(pr)))
        # result_dict = pr.task.reward_function_fixed_data_all_metrics(pr)
        # list_of_random_test.append(result_dict)

    gp.population[0].allow_change_tokens = np.ones_like(gp.population[0].allow_change_tokens)
    #####################################
    # step 3: optimize the predicted
    # expression
    #####################################
    print(gp.population[0].r)

    pr = gp.population[0]
    print(pr.__getstate__())
    print(pr.print_expression())
    list_of_random_test2 = []
    list_of_valid_r = []
    for it in range(20):
        pr.task.rand_draw_data()
        list_of_valid_r.append(pr.task.reward_function_fixed_data(pr))
        print('iter:{}, validate r={}'.format(it, list_of_valid_r[-1]))
        # result_dict = pr.task.reward_function_fixed_data_all_metrics(pr)
        # list_of_random_test2.append(result_dict)
    print(list_of_valid_r)
    print(np.min(np.abs(list_of_valid_r)), np.max(np.abs(list_of_valid_r)))
    return


def compute_gp_diff(nvar, true_program_file, metric_name):
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
        functions.protected_ops[0],  # 'div'
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

    # read the program
    prog = gen_true_program.read_true_program(true_program_file)
    true_pr = gen_true_program.build_program(prog, protected_library, 0)

    # set the task
    Program.task = regress_task.RegressTaskV1(regress_batchsize,
                                              allowed_input_tokens,
                                              true_pr,
                                              metric=metric_name)

    # set gp helper
    gp_helper = gp_xyx.GPHelper()
    gp_helper.library = protected_library

    # set GP
    gp_xyx.GeneticProgram.library = protected_library
    gp_xyx.GeneticProgram.gp_helper = gp_helper
    gp = gp_xyx.GeneticProgram(cxpb, mutpb, maxdepth, population_size, tour_size, \
                               hof_size, n_generations)

    #####################################
    # step 2: load predicted expression
    # and generate the test result
    #####################################
    pred_prog = load_prog21_gp_pred_program()
    pred_pr = gen_true_program.build_program(pred_prog, protected_library, 0)
    gp.population[0] = pred_pr
    pr = gp.population[0]
    print(pr.__getstate__())
    print(pr.print_expression())
    list_of_random_test = []
    for it in range(100):
        pr.task.rand_draw_data()
        print('iter:{}, validate r={}'.format(it, pr.task.reward_function_fixed_data(pr)))
        # result_dict = pr.task.reward_function_fixed_data_all_metrics(pr)
        # list_of_random_test.append(result_dict)

    # gp.population[0].allow_change_tokens = np.ones_like(gp.population[0].allow_change_tokens)
    #
    # # print
    print('final hof=')
    # gp.print_hof()
    # print('gp.timer_log=', gp.timer_log)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("nvar", type=int, help="number of variables.",
                        default=5)
    parser.add_argument("true_program_file", help="the filename of the true program (pickle dump).",
                        default="/home/jiangnan/PycharmProjects/xyx_dso/src/data/synthetic_nv5_nt55/prog_35.data")
    parser.add_argument("metric_name", type=str, help="The name of the metric.",
                        default='neg_mse')

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)
    # raw_string = "sub, mul, div, sub, X_2, mul, sub, mul, X_4, sub, 10.285499313959354, div, -29.997564102363928, X_1, X_0, 1.0, mul, 1.0, 1.0, X_0, sub, mul, 1.0, sub, 1.0, sub, add, sub, inv, 1.0, X_3, mul, div, 1.0, 1.0, sub, X_2, add, sub, mul, 27.20078181898557, add, sub, mul, 28.293248903445637, sub, 0.885011319050715, sub, add, sub, inv, 0.9502889993302134, X_3, mul, div, 4.030121686665944, 0.768164458093994, sub, X_2, add, sub, mul, X_4, add, sub, mul, sub, 1.1955066786499609, sub, mul, sub, 1.5525808389420057, X_3, mul, div, -0.07975712742784412, 3.9927575894400786, sub, X_4, mul, sub, sub, mul, X_4, sub, 7.904671112802548, div, 6.952528774959578, X_1, X_0, X_0, 1.0, X_0, sub, 11.354309399023428, div, 1.0, 14.681289034845618, div, X_3, div, 1.0, -54.025679293639854, 1.0, div, X_3, X_3, 1.0, X_0, div, X_3, div, 1.0, 0.02980904495194394, 1.0, div, X_3, X_3, 1.0, X_0, X_0"
    # raw_string ="mul, add, div, mul, 0.9207653201033978, X_0, 1.0, add, sub, add, mul, X_1, sub, X_4, add, div, div, add, 1.0, X_4, mul, X_2, add, 1.0, 1.0, 1.0, 1.0, add, 1.0, 1.0, sub, add, mul, X_1, sub, 1.0, add, div, mul, X_2, add, 1.0, 1.0, 1.0, div, 1.0, 1.0, add, div, 1.0, add, X_4, 462.9187999825935, 1.0, div, X_3, 1.0, div, add, mul, mul, 365.97562793530443, X_1, add, div, mul, X_3, add, X_4, 1.0, 1.0, 1.0, div, add, mul, 371.191147934296, 1.0, 1.0, div, X_3, 1.0, 115.16799061595574, 19.52466050768651"
    raw_string="sub, add, add, div, X_0, add, div, add, sub, add, add, div, X_0, add, div, add, 907.1778844240454, X_1, add, 443.337783863357, add, X_4, X_4, -1.9587830988607482, add, X_4, X_4, mul, -2.1035818482172406, add, X_2, add, X_1, X_3, X_4, X_1, add, 367.2631656866165, add,       X_4, X_4, 0.12089085074356119, 19.855908151199763, mul, -4.707038914186502, add, X_2, add, X_1, X_3, X_4"
    compute_egp_diff(args.nvar, args.true_program_file, raw_string, args.metric_name)

    # compute_gp_diff(args.nvar, args.true_program_file, args.metric_name)
