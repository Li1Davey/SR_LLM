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


def load_prog21_gp_pred_program():
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


def load_prog21_egp_pred_program():
    # program 21
    # from sympy import preorder_traversal, symbols
    pred_expr_str = "X0 * ( 0.8082306774611323 * X2 + 0.05211913323160484 * X4 * X4 ) - 0.12287456124170289 * X2 + 1.0 * X3 * X4 + X3 + ( 0.49313700032845215 * X0 + 0.49313700032845215 ) * ( X1 - 1.0 * X4 * X4 ) + 2 / X4"
    expr = parse_expr(pred_expr_str)
    # print(preorder_traversal(expr))
    # 0.49313700032845215*X0*X1 + 0.8082306774611323*X0*X2 - 0.44101786709684731*X0*X4**2
    # + 0.49313700032845215*X1 - 0.12287456124170289*X2 + X3*X4
    # + X3 - 0.49313700032845215*X4**2 + 2/X4
    preorder_exp_expr = ['add', 'add', 'add',
                         'add',
                         'X_3',
                         'mul', '2', 'inv', 'X_4',
                         'add',
                         'mul', '0.49313700032845215', 'X_1',
                         'mul', '-0.49313700032845215',
                         'mul', 'X_4', 'X_4',
                         'add',
                         'mul', '-0.12287456124170289', 'X_2',
                         'mul', 'X_3', 'X_4',
                         'add',
                         'mul', '0.8082306774611323',
                         'mul', 'X_0', 'X_2',
                         'add',
                         'mul', '0.49313700032845215',
                         'mul',
                         'X_0',
                         'X_1',
                         'mul', '-0.44101786709684731',
                         'mul', 'X_0',
                         'mul', 'X_4',
                         'X_4'
                         ]
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


def compute_egp_diff(nvar, true_program_file, metric_name):
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
    pred_prog = load_prog21_egp_pred_program()
    pred_pr = gen_true_program.build_program(pred_prog, protected_library, 0)
    gp.population[0] = pred_pr
    gp.population[0].task.fixed_column=[]
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
    for it in range(10):
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
                        default="/home/jiangnan/PycharmProjects/xyx_dso/src/data/synthetic_nv5_nt55/prog_21.data")
    parser.add_argument("metric_name", type=str, help="The name of the metric.",
                        default='neg_mse')

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)
    compute_egp_diff(args.nvar, args.true_program_file, args.metric_name)
    # compute_gp_diff(args.nvar, args.true_program_file, args.metric_name)

