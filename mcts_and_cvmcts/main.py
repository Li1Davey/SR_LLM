import numpy as np
import time
import argparse
from mcts_model import MCTS
from production_rules import get_production_rules
from utils import simplify_eq
import random
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regress_task import RegressTask


def run_mcts(task, production_rules, num_iterations, nt_nodes=['A'], max_len=50, eta=0.9999,
             max_module_init=10, num_aug=50, exp_rate=1 / np.sqrt(2),
             optimizer='BFGS'):
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
    aug_grammars = ['A->A-A,A->C,A->C', 'A->sqrt(A),A->C', 'A->sqrt(A),A->A+A,A->X0,A->A/A, A->X0,A->X0']

    start_time = time.time()

    for i_itr in range(num_iterations):
        print(f"i_itr={i_itr},")
        mtcs_model = MCTS(task=task,
                          base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          nt_nodes=nt_nodes,
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta)

        _, current_solution, population = mtcs_model.MCTS_run(num_iterations,
                                                              num_simulations=10,
                                                              verbose=True)

        end_time = time.time() - start_time

        if not hof:
            hof = population
        else:
            hof = sorted(list(set(hof + population)), key=lambda x: x[1])
        aug_grammars = [x[0] for x in hof[-num_aug:]]
        print("aug_grammars:", aug_grammars)
        reward_his.append(best_solution[1])

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


def mcts(equation_name, metric_name, noise_type, noise_scale, optimizer):
    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()
    operators_set = data_query_oracle.get_operators_set()

    regress_batchsize = 256
    opt_num_expr = 1
    allowed_input_tokens = np.ones(nvar, dtype=np.int32)
    task = RegressTask(regress_batchsize,
                       allowed_input_tokens,
                       dataXgen,
                       data_query_oracle)

    num_iterations = 100
    production_rules = get_production_rules(nvar, operators_set)
    print("The production rules are:", production_rules)
    all_eqs, all_times = run_mcts(task, production_rules, num_iterations, optimizer=optimizer)

    print('average discovery time is', np.round(np.mean(all_times), 3), 'seconds')


def cv_mcts(equation_name, metric_name, noise_type, noise_scale, optimizer):
    pass


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
