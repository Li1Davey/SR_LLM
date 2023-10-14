import numpy as np
import time
import argparse
from mcts_model import MCTS
from production_rules import get_production_rules, get_ith_var_rules
from utils import simplify_eq, create_uniform_generations, tree_to_eq
import random
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regress_task import RegressTask
from progam import Program


def run_mcts(
        production_rules, num_iterations, nt_nodes=['A'], mcts_iterations=100,
        max_len=50, eta=0.9999, max_module_init=10, num_aug=50, exp_rate=1 / np.sqrt(2),
):
    """
    Executes the main training loop of Symbolic Physics Learner.
    
    Parameters
    ----------
    task: benchmark task name.
    num_run" number of iterations.
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init : Int object.
        initial maximum length for module transplantation candidates. 
    num_aug : number of trees for module transplantation.
    exp_rate: initial exploration rate.
    norm_threshold: numerical error tolerance for norm calculation, a very small value.
        
    Returns
    -------
    all_eqs: List<Str>. discovered equations.
    success_rate: Float. success rate of all runs performed.
    all_times: List<Float>. runtimes for successful runs.
    """

    # define production rules and non-terminal nodes.
    grammars = production_rules
    all_times = []
    all_eqs = []

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / num_iterations

    best_solution = ('nothing', 0)

    exploration_rate = exp_rate
    max_module = max_module_init
    reward_his = []
    hof = []
    aug_grammars = []

    start_time = time.time()

    mtcs_model = MCTS(base_grammars=grammars,
                      aug_grammars=aug_grammars,
                      nt_nodes=nt_nodes,
                      max_len=max_len,
                      max_module=max_module,
                      aug_grammars_allowed=num_aug,
                      exploration_rate=exploration_rate,
                      eta=eta)

    _, current_solution, population = mtcs_model.MCTS_run(mcts_iterations,
                                                          num_simulations=num_iterations,
                                                          verbose=True)

    end_time = time.time() - start_time

    if not hof:
        hof = population
    else:
        hof = sorted(list(set(hof + population)), key=lambda x: x[1], reverse=True)
    aug_grammars = [x[0] for x in hof[:num_aug]]
    print("aug_grammars:")
    for gi in aug_grammars:
        print(gi)
    print('-' * 20)
    reward_his.append(best_solution[1])

    print('Hall of Fame:')
    for i in range(min(10, len(hof))):
        print(hof[i][-2], hof[i][-1], hof[i][0])

    if current_solution[1] > best_solution[1]:
        best_solution = current_solution
    # print(best_solution)
    max_module += module_grow_step
    exploration_rate *= 5

    print()

    all_eqs.append(simplify_eq(best_solution[0]))
    print('best solution: {}'.format(simplify_eq(best_solution[0])))
    print()

    return all_eqs, all_times


def run_cv_mcts(
        operators_set, opt_num_expr: int, num_iterations: list, nt_nodes=['A'], mcts_iterations=100,
        max_len=50, eta=0.9999, max_module_init=10, num_aug=10, exp_rate=1 / np.sqrt(2),
):
    """
    Executes the main training loop of Symbolic Physics Learner.
    num_run: number of iterations.
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init : Int object.
        initial maximum length for module transplantation candidates.
    num_aug : number of trees for module transplantation.
    exp_rate: initial exploration rate.

    all_eqs: List<Str>. discovered equations.
    success_rate: Float. success rate of all runs performed.
    all_times: List<Float>. runtimes for successful runs.
    """

    # define production rules and non-terminal nodes.
    production_rules = get_production_rules(0, operators_set)
    print("The production rules are:", production_rules)
    grammars = production_rules
    all_times = []
    all_eqs = []

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / np.sum(num_iterations)

    exploration_rate = exp_rate
    max_module = max_module_init
    hof = []
    aug_nt_nodes = []
    aug_grammars = []

    start_time = time.time()
    for round_idx in range(len(num_iterations)):
        print("update set of free variable and grammars")
        MCTS.program.set_vf(round_idx)
        # MCTS.program.set_vf(round_idx + 1)
        allowed_inputs = MCTS.program.get_vf()
        MCTS.task.set_allowed_inputs(allowed_inputs)
        if round_idx < len(num_iterations) - 1:
            grammars += get_ith_var_rules(round_idx)
        print('++++++++++++ ROUND {}  ++++++++++++'.format(round_idx))
        # debug begin
        # nt_nodes.append('B')
        # grammars.extend(get_production_rules(0, operators_set, non_terminal_node='B'))
        # grammars.extend(get_ith_var_rules(round_idx + 1, non_terminal_node='B'))
        # aug_grammars.append('A->A+A;A->A+A;A->A*A;A->B;A->X0;A->A/A;A->B;A->X0;A->C')
        # print(tree_to_eq('f->A,A->A+A,A->A+A,A->A*A,A->C,A->X0,A->A/A,A->C,A->X0,A->C'.split(',')))

        # debug ends
        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          nt_nodes=nt_nodes,
                          aug_nt_nodes=aug_nt_nodes,
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta)

        _, current_solution, population = mcts_model.MCTS_run(mcts_iterations,
                                                              num_simulations=50,  # num_iterations[round_idx],
                                                              verbose=True)
        #
        # end_time = time.time() - start_time
        #
        if not hof:
            hof = sorted(list(set(population)), key=lambda x: x[1], reverse=True)
        else:
            hof = sorted(list(set(population)), key=lambda x: x[1], reverse=True)
        # aug_grammars = list(set([x[0] for x in hof[:num_aug]]))
        # aug_grams_debug = [
        #     ('A->A+A,A->A+A,A->A*A,A->B,A->X0,A->A/A,A->B,A->X0,A->C,B->C,B->B/B,B->C,B->X1', 0.9920393649645961, '-0.12545874191252*X0+0.4378999964344581/X1/X0+14.740017243123066')]
        freezed, aug_grammars, aug_nt_nodes = mcts_model.freeze_equations(hof,
                                                                          opt_num_expr)  # mcts_model.freeze_equations(hof[:num_aug], opt_num_expr)
        print('++++++++++++ ROUND {} AUG Grammar ++++++++++++'.format(round_idx, ))
        for gi in aug_grammars:
            print(gi)
        print('-' * 20)
        if freezed == True:
            nt_nodes.append('B')
            nt_nodes = list(set(nt_nodes)).sort()
            grammars.extend(get_production_rules(0, operators_set, non_terminal_node='B'))
            grammars.extend(get_ith_var_rules(round_idx + 1, non_terminal_node='B'))
            grammars = list(set(grammars)).sort()
            print("new grammars:", grammars)

        print('Hall of Fame:')
        for i in range(min(10, len(hof))):
            print(hof[i][-2], hof[i][-1], hof[i][0])

        # print(best_solution)
        max_module += module_grow_step
        exploration_rate *= 5

        print()

    print('final hof')
    for hi in hof:
        print(hi[-2], hi[-1], hi[0])

    return all_eqs, all_times


def mcts(equation_name, metric_name, noise_type, noise_scale, optimizer):
    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()
    operators_set = data_query_oracle.get_operators_set()

    regress_batchsize = 256
    allowed_input_tokens = np.ones(nvar, dtype=np.int32)
    MCTS.task = RegressTask(regress_batchsize,
                            allowed_input_tokens,
                            dataXgen,
                            data_query_oracle)
    MCTS.program = Program(nvar, optimizer)

    num_iterations = 100

    production_rules = get_production_rules(nvar, operators_set)
    print("The production rules are:", production_rules)
    all_eqs, all_times = run_mcts(production_rules, num_iterations)

    print('average discovery time is', np.round(np.mean(all_times), 3), 'seconds')


def cv_mcts(equation_name, metric_name, noise_type, noise_scale, optimizer):
    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()
    operators_set = data_query_oracle.get_operators_set()

    regress_batchsize = 256
    opt_num_expr = 5
    allowed_input_tokens = np.ones(nvar, dtype=np.int32)
    MCTS.task = RegressTask(regress_batchsize,
                            allowed_input_tokens,
                            dataXgen,
                            data_query_oracle)
    MCTS.program = Program(nvar, optimizer)

    num_iterations = 10000
    num_iterations = create_uniform_generations(num_iterations, nvar + 1)

    all_eqs, all_times = run_cv_mcts(operators_set, opt_num_expr, num_iterations)

    print('average discovery time is', np.round(np.mean(all_times), 3), 'seconds')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")
    parser.add_argument('--optimizer',
                        nargs='?',
                        choices=['BFGS', 'Nelder-Mead', 'CG', 'basinhopping', 'dual_annealing', 'shgo', 'direct'],
                        help='list servers, storage, or both (default: %(default)s)')
    parser.add_argument("--metric_name", type=str, default='neg_mse', help="The name of the metric for loss.")
    parser.add_argument("--noise_type", type=str, default='normal', help="The name of the noises.")
    parser.add_argument("--noise_scale", type=float, default=0.0, help="This parameter adds the standard deviation of the noise")
    parser.add_argument("--cv_mcts", action="store_true", help="whether run normal mcts (cv_mcts=False) or control_variable_mcts.")

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)
    if args.cv_mcts:
        cv_mcts(args.equation_name, args.metric_name, args.noise_type, args.noise_scale, args.optimizer)
    else:
        mcts(args.equation_name, args.metric_name, args.noise_type, args.noise_scale, args.optimizer)
