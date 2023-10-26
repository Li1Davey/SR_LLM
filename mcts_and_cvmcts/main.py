import numpy as np
import time
import argparse
from mcts_model import MCTS
from production_rules import get_production_rules, get_ith_var_rules, get_sincos_vars_rules
from utils import pretty_print_expr, create_uniform_generations
import random
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regress_task import RegressTask
from progam import Program


def run_mcts(
        production_rules, non_terminal_nodes=['A'], num_episodes=5000, num_simulations=200,
        max_len=30, eta=0.9999, max_module_init=15, num_aug=10, exp_rate=1 / np.sqrt(2),
        num_transplant=1, norm_threshold=1e-10
):
    """
    Executes the main training loop of Symbolic Physics Learner.
    
    Parameters
    ----------
    production_rules: rules to generate expressions
    num_episodes: number of iterations.
    non_terminal_nodes: used in production rules
    num_simulations
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init:  initial maximum length for module transplantation candidates.
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
    best_solution = ('nothing', 0)

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / num_transplant

    exploration_rate = exp_rate
    max_module = max_module_init
    best_modules = []
    reward_his = []
    aug_grammars = []

    start_time = time.time()
    for i_itr in range(num_transplant):
        print("transplanation step=", i_itr)
        print(aug_grammars)
        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          non_terminal_nodes=non_terminal_nodes,
                          aug_nt_nodes=[],
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta)
        _, current_solution, good_modules = mcts_model.MCTS_run(num_episodes,
                                                                num_simulations=num_simulations,
                                                                verbose=True)

        mcts_model.print_hofs(verbose=True)
        if not best_modules:
            best_modules = good_modules
        else:
            best_modules = sorted(list(set(best_modules + good_modules)), key=lambda x: x[1])

        aug_grammars = [x[0] for x in best_modules[:num_aug]]
        print("AUG Grammars")
        for gi in aug_grammars:
            print(gi)

        if best_modules[0][1] >= 1 - norm_threshold:
            print("find the ground-truth expression, whole program terminates...")
            break

        reward_his.append(best_solution[1])

        if current_solution[1] > best_solution[1]:
            best_solution = current_solution

        max_module += module_grow_step
        exploration_rate *= 1.2
    end_time = time.time() - start_time
    print("MCTS time:", np.round(np.mean(end_time), 3), 'seconds')


def mcts(equation_name, num_episodes, metric_name, noise_type, noise_scale, optimizer):
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

    production_rules = get_production_rules(nvar, operators_set)
    print("The production rules are:", production_rules)
    run_mcts(production_rules=production_rules, num_episodes=num_episodes)


def run_cv_mcts(
        operators_set, opt_num_expr: int, num_iterations: list, nt_nodes=['A'], num_simulations=50,
        max_len=20, eta=0.999, max_module_init=12, num_aug=5, exp_rate=1 / np.sqrt(2),
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

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / np.sum(num_iterations)

    exploration_rate = exp_rate
    max_module = max_module_init
    hof = []
    aug_nt_nodes = []
    aug_grammars = []

    start_time = time.time()
    for round_idx in range(len(num_iterations)):
        print('++++++++++++ ROUND {}  ++++++++++++'.format(round_idx))
        print("update set of free variable and grammars")
        MCTS.program.set_vf(round_idx)
        allowed_inputs = MCTS.program.get_vf()
        MCTS.task.set_allowed_inputs(allowed_inputs)
        if round_idx < len(num_iterations) - 1:
            grammars += get_ith_var_rules(round_idx)
            if 'sin' in operators_set:
                grammars += get_sincos_vars_rules(round_idx, non_terminal_node='A')

        print("grammar:", grammars)
        print("aug grammar:", aug_grammars)
        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          non_terminal_nodes=nt_nodes,
                          aug_nt_nodes=aug_nt_nodes,
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta)

        _, current_solution, population = mcts_model.MCTS_run(num_iterations[round_idx],
                                                                  num_simulations=num_simulations,  # num_iterations[round_idx],
                                                                  verbose=True)


        if not hof:
            hof = sorted(list(set(population)), key=lambda x: x[1], reverse=True)
        else:
            hof = sorted(list(set(population)), key=lambda x: x[1], reverse=True)
        aug_grammars, aug_nt_nodes = mcts_model.freeze_equations(hof[-num_aug:], opt_num_expr)

        grammars = [gi for gi in grammars if str(round_idx) not in gi]

        max_module += int(module_grow_step)
        exploration_rate *= 1.2

        print()

    print('final hof')
    for hi in hof:
        print(hi[-2], hi[-1], hi[0])


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

    num_episodes = 5000
    num_iterations = create_uniform_generations(num_episodes, nvar + 1)
    start = time.time()
    run_cv_mcts(operators_set, opt_num_expr, num_iterations)
    end = time.time() - start
    print('average discovery time is', np.round(end / 60, 3), 'mins')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")
    parser.add_argument('--optimizer',
                        nargs='?',
                        choices=['BFGS', 'Nelder-Mead', 'CG', 'basinhopping', 'dual_annealing', 'shgo', 'direct'],
                        help='list servers, storage, or both (default: %(default)s)')
    parser.add_argument("--metric_name", type=str, default='neg_mse', help="The name of the metric for loss.")
    parser.add_argument("--num_episodes", type=int, default=5000, help="the number of episode for MCTS.")
    parser.add_argument("--noise_type", type=str, default='normal', help="The name of the noises.")
    parser.add_argument("--noise_scale", type=float, default=0.0, help="This parameter adds the standard deviation of the noise")
    parser.add_argument("--cv_mcts", action="store_true",
                        help="whether run normal mcts (cv_mcts=False) or control variable mcts (cv_mcts=True).")

    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)

    seed = int(time.perf_counter() * 10000) % 1000007
    np.random.seed(seed)
    print('np.random seed=', seed)
    print(args)
    if args.cv_mcts:
        cv_mcts(args.equation_name, args.metric_name, args.noise_type, args.noise_scale, args.optimizer)
    else:
        mcts(args.equation_name, args.num_episodes, args.metric_name, args.noise_type, args.noise_scale, args.optimizer)
