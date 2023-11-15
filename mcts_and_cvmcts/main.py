from pympler import classtracker, asizeof
import time
import argparse
from mcts_model import MCTS
from production_rules import *
from utils import create_uniform_generations, create_geometric_generations, create_reward_threshold
import random
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regress_task import RegressTask
from progam import Program


def run_mcts(
        production_rules, non_terminal_nodes=['A'], num_episodes=500, num_rollouts=10,
        max_len=30, eta=0.9999, max_module_init=15, num_aug=10, exp_rate=1 / np.sqrt(2),
        num_transplant=5, norm_threshold=1e-10
):
    """
    production_rules: rules to generate expressions
    num_episodes: number of iterations.
    non_terminal_nodes: used in production rules
    num_rollouts
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init:  initial maximum length for module transplantation candidates.
    num_aug : number of trees for module transplantation.
    exp_rate: initial exploration rate.
    norm_threshold: numerical error tolerance for norm calculation, a very small value.
    """

    # define production rules and non-terminal nodes.
    grammars = production_rules

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / num_transplant

    exploration_rate = exp_rate
    max_module = max_module_init
    best_modules = []
    aug_grammars = []

    start_time = time.time()
    for i_itr in range(num_transplant):
        print("transplanation step=", i_itr)
        print(aug_grammars)
        max_opt_iter = 200
        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          non_terminal_nodes=non_terminal_nodes,
                          aug_nt_nodes=[],
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          max_opt_iter=max_opt_iter,
                          eta=eta)

        _, good_modules = mcts_model.MCTS_run_orig(num_episodes,
                                                   num_rollouts=num_rollouts,
                                                   verbose=True,
                                                   is_first_round=True,
                                                   print_freq=5)

        mcts_model.print_hofs(-1, verbose=True)

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
    MCTS.program.evalaute_loss = data_query_oracle.compute_metric
    operators_set.remove('const')
    production_rules = get_production_rules(nvar, operators_set)
    print("The production rules are:", production_rules)
    run_mcts(production_rules=production_rules, num_episodes=num_episodes)


def run_cv_mcts(
        operators_set, opt_num_expr: int, num_iterations: list, nt_nodes=['A'], num_rollouts=40,
        max_len=30, eta=0.999, max_module_init=12, num_aug=5, exp_rate=1 / np.sqrt(2),
):
    """
    num_run: number of iterations.
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init: initial maximum length for module transplantation candidates.
    num_aug : number of trees for module transplantation.
    exp_rate: initial exploration rate.
    """

    # define production rules and non-terminal nodes.
    production_rules = get_production_rules(0, operators_set)
    print("The production rules are:", production_rules)
    grammars = production_rules

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / np.sum(num_iterations)

    exploration_rate = exp_rate
    max_module = max_module_init
    stand_alone_constants = []

    aug_nt_nodes = []
    aug_grammars = []

    reward_thresh = create_reward_threshold(10, len(num_iterations))
    for round_idx in range(len(num_iterations)):
        print('++++++++++++ ROUND {}  ++++++++++++'.format(round_idx))
        MCTS.program.set_vf(round_idx)
        MCTS.task.set_allowed_inputs(MCTS.program.get_vf())
        if round_idx < len(num_iterations):
            grammars += get_ith_var_rules(round_idx)
            if 'sin' in operators_set:
                grammars += get_ith_sincos_rules(round_idx, non_terminal_node='A')
            if 'inv' in operators_set:
                grammars += get_ith_inv_rules(round_idx, non_terminal_node='A')
            if 'n2' in operators_set:
                grammars += get_ith_n2_rules(round_idx)
            if 'n3' in operators_set:
                grammars += get_ith_n3_rules(round_idx)
            if 'n4' in operators_set:
                grammars += get_ith_n4_rules(round_idx)
            if 'n5' in operators_set:
                grammars += get_ith_n5_rules(round_idx)

        print("grammars:", grammars)
        print("aug grammars:", aug_grammars)
        print("aug ntn nodes:", aug_nt_nodes)
        print("num_rollouts:", num_rollouts)
        tracker = classtracker.ClassTracker()

        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          non_terminal_nodes=nt_nodes,
                          aug_nt_nodes=aug_nt_nodes,
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta,
                          max_opt_iter=200)
        iter_time = time.time()
        tracker.track_object(mcts_model)
        print_freq = 1
        _, population = mcts_model.MCTS_run(num_iterations[round_idx],
                                            num_rollouts=num_rollouts,
                                            reward_threhold=reward_thresh[round_idx],
                                            verbose=True,
                                            is_first_round=(round_idx == 0),
                                            print_freq=print_freq)
        print("Time usage of round {} is {} mins".format(round_idx, np.round((time.time() - iter_time) / 60, 3)))
        tracker.create_snapshot()
        tracker.stats.print_summary()
        mcts_model.UCBs = {}
        mcts_model.QN = {}
        print(population)
        if round_idx < len(num_iterations) - 1:
            # the last round does not need freeze
            aug_grammars, aug_nt_nodes, stand_alone_constants = mcts_model.freeze_equations(population, opt_num_expr, stand_alone_constants)
            print("AUG grammars")
            print(aug_grammars)

            grammars = [gi for gi in grammars if str(round_idx) not in gi]

        max_module += int(module_grow_step)
        exploration_rate *= 1.2
        num_rollouts = max(5, int(num_rollouts * 0.5))
    for round_idx in range(len(num_iterations)):
        MCTS.program.set_vf(round_idx)
        MCTS.task.set_allowed_inputs(MCTS.program.get_vf())
    print("final hof")
    mcts_model.print_hofs(-1, verbose=True)


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
    MCTS.program.evalaute_loss = data_query_oracle.compute_metric
    num_per_episodes = 20
    num_iterations = create_uniform_generations(num_per_episodes, nvar)
    start = time.time()
    run_cv_mcts(operators_set, opt_num_expr, num_iterations)
    end = time.time() - start
    print('average discovery time is', np.round(end / 60, 3), 'mins')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")
    parser.add_argument('--optimizer',
                        nargs='?',
                        choices=['BFGS', 'L-BFGS-B', 'Nelder-Mead', 'CG', 'basinhopping', 'dual_annealing', 'shgo', 'direct'],
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
        # run control variable experiment based Monte Carlo Tree Search
        cv_mcts(args.equation_name, args.metric_name, args.noise_type, args.noise_scale, args.optimizer)
    else:
        # run Monte Carlo Tree Search
        mcts(args.equation_name, args.num_episodes, args.metric_name, args.noise_type, args.noise_scale, args.optimizer)
