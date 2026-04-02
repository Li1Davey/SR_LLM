try:
    from pympler import classtracker
except ImportError:
    classtracker = None
import time
import argparse
import os

from mcts_model import MCTS
from llm_production_rule_feedback import create_run_rule_bank, maybe_generate_production_rules

from utils import create_uniform_generations, create_reward_threshold
import random
import numpy as np
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regress_task import RegressTask
from program import Program


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_float(name: str, default: float) -> float:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _dedupe_preserve_order(items):
    seen = set()
    out = []
    for item in items:
        if item is None:
            continue
        key = str(item).strip()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def run_mcts(
        production_rules, non_terminal_nodes=['A'], num_episodes=1000, num_rollouts=40,
        max_len=30, eta=0.9999, max_module_init=15, num_aug=10, exp_rate=1 / np.sqrt(2),
        num_transplant=1, norm_threshold=1e-10, rule_bank=None, max_opt_iter=100, print_freq=5
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

    module_grow_step = (max_len - max_module_init) / num_transplant

    exploration_rate = exp_rate
    max_module = max_module_init
    best_modules = []
    aug_grammars = []

    for i_itr in range(num_transplant):
        tracker = classtracker.ClassTracker() if classtracker is not None and os.getenv("SCIBENCH_TRACK_MEM", "0") == "1" else None
        grammars = _dedupe_preserve_order(rule_bank.current_rules if rule_bank is not None else production_rules)

        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          non_terminal_nodes=non_terminal_nodes,
                          aug_nt_nodes=[],
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          max_opt_iter=max_opt_iter,
                          eta=eta,
                          rule_bank=rule_bank)
        if tracker is not None:
            tracker.track_object(mcts_model)
        start = time.time()
        _, good_modules = mcts_model.MCTS_run_orig(num_episodes,
                                                   num_rollouts=num_rollouts,
                                                   verbose=True,
                                                   is_first_round=True,
                                                   print_freq=print_freq)

        if tracker is not None:
            tracker.create_snapshot()
            tracker.stats.print_summary()
        mcts_model.print_hofs(-2, verbose=False)

        if not best_modules:
            best_modules = good_modules
        else:
            best_modules = sorted(list(set(best_modules + good_modules)), key=lambda x: x[1], reverse=True)

        aug_grammars = _dedupe_preserve_order([x[0] for x in best_modules[:num_aug]])

        max_module += module_grow_step
        exploration_rate *= 1.2
    print("final hof")
    mcts_model.print_hofs(-2, verbose=False)


def mcts(equation_name, num_episodes, metric_name, noise_type, noise_scale, optimizer,
         production_rules_mode, memray_output_bin, track_memory=False):
    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()
    operators_set = data_query_oracle.get_operators_set()

    regress_batchsize = _env_int("SCIBENCH_BATCH_SIZE", 256)
    max_len = _env_int("SCIBENCH_MAX_LEN", 30)
    eta = _env_float("SCIBENCH_ETA", 0.9999)
    max_opt_iter = _env_int("SCIBENCH_MAX_OPT_ITER", 100)
    print_freq = _env_int("SCIBENCH_PRINT_FREQ", 5)

    try:
        from scibench.program import sciProgram
        protected = True
        sciProgram.set_execute(protected=protected, simulated_exec=False)
        print(f"[exec] protected={protected}")
    except Exception:
        print("[exec] protected=True")

    allowed_input_tokens = np.ones(nvar, dtype=np.int32)
    MCTS.task = RegressTask(regress_batchsize,
                            allowed_input_tokens,
                            dataXgen,
                            data_query_oracle)
    MCTS.program = Program(nvar, optimizer)
    MCTS.program.evalaute_loss = data_query_oracle.compute_metric
    resolved_config = {
        "equation_name": equation_name,
        "optimizer": optimizer,
        "metric_name": metric_name,
        "num_episodes": num_episodes,
        "num_rollouts": _env_int("SCIBENCH_NUM_ROLLOUTS", 40),
        "max_len": max_len,
        "eta": eta,
        "noise_type": noise_type,
        "noise_scale": noise_scale,
        "production_rule_mode": production_rules_mode,
        "batch_size": regress_batchsize,
        "max_opt_iter": max_opt_iter,
    }
    print("[config]", resolved_config)
    if production_rules_mode == 'trigometric':
        from production_rules_trigometric import get_production_rules
    elif production_rules_mode == 'livermore2':
        from production_rules import get_production_rules
    elif production_rules_mode == 'feynman':
        from production_rules_feynman import get_production_rules
    production_rules = get_production_rules(nvar, operators_set)
    rule_bank = create_run_rule_bank(
        production_rules,
        tag=f"{equation_name}-mcts",
        extra_metadata={
            "equation_name": equation_name,
            "mode": "mcts",
            "production_rules_mode": production_rules_mode,
        },
    )
    print("The production rules are:", production_rules)
    if track_memory:
        import memray
        if os.path.isfile(memray_output_bin):
            os.remove(memray_output_bin)
        with memray.Tracker(memray_output_bin):
            start = time.time()
            run_mcts(
                production_rules=production_rules,
                num_episodes=num_episodes,
                num_rollouts=_env_int("SCIBENCH_NUM_ROLLOUTS", 40),
                max_len=max_len,
                eta=eta,
                rule_bank=rule_bank,
                max_opt_iter=max_opt_iter,
                print_freq=print_freq,
            )
            end_time = time.time() - start
    else:
        start = time.time()
        run_mcts(
            production_rules=production_rules,
            num_episodes=num_episodes,
            num_rollouts=_env_int("SCIBENCH_NUM_ROLLOUTS", 40),
            max_len=max_len,
            eta=eta,
            rule_bank=rule_bank,
            max_opt_iter=max_opt_iter,
            print_freq=print_freq,
        )
        end_time = time.time() - start
    print("MCTS {} mins".format(np.round(end_time / 60, 3)))


def run_vsr_mcts(
        operators_set, opt_num_expr: int, num_iterations: list, nt_nodes=['A'], num_rollouts=40,
        max_len=30, eta=0.999, max_module_init=12, num_aug=5, exp_rate=1 / np.sqrt(2),
        production_rules_mode='trigometric', rule_bank=None
):
    """
    num_run: number of iterations.
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init: initial maximum length for module transplantation candidates.
    num_aug : number of trees for module transplantation.
    exp_rate: initial exploration rate.
    """

    if production_rules_mode == 'trigometric':
        from production_rules_trigometric import get_var_i_production_rules, get_production_rules
    elif production_rules_mode == 'livermore2':
        from production_rules import get_var_i_production_rules, get_production_rules
    elif production_rules_mode == 'feynman':
        from production_rules_feynman import get_var_i_production_rules, get_production_rules
    production_rules = get_production_rules(0, operators_set)
    print("The production rules are:", production_rules)
    if rule_bank is None:
        rule_bank = create_run_rule_bank(production_rules, tag="vsr")

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
        grammars = list(rule_bank.current_rules)
        if round_idx < len(num_iterations):
            grammars += get_var_i_production_rules(round_idx, operators_set)
        grammars = _dedupe_preserve_order(grammars)
        print("grammars:", grammars)
        print("aug grammars:", aug_grammars)
        print("aug ntn nodes:", aug_nt_nodes)
        print("num_rollouts:", num_rollouts)

        mcts_model = MCTS(base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          non_terminal_nodes=nt_nodes,
                          aug_nt_nodes=aug_nt_nodes,
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta,
                          max_opt_iter=100,
                          rule_bank=rule_bank)
        iter_time = time.time()
        print_freq = 1
        _, population = mcts_model.MCTS_run(num_iterations[round_idx],
                                            num_rollouts=num_rollouts,
                                            reward_threhold=reward_thresh[round_idx],
                                            verbose=True,
                                            is_first_round=(round_idx == 0),
                                            print_freq=print_freq)

        added = maybe_generate_production_rules(
            hall_of_fame=mcts_model.hall_of_fame,
            rule_bank=rule_bank,
            nvars=MCTS.task.data_query_oracle.get_nvars(),
            operators_set=operators_set,
        )
        if added:
            print(f"[PR_FEEDBACK] using {len(rule_bank.current_rules)} active rules in later VSR rounds")

        print("Time usage of round {} is {} mins".format(round_idx, np.round((time.time() - iter_time) / 60, 4)))

        mcts_model.UCBs = {}
        mcts_model.QN = {}
        print(population)
        if round_idx < len(num_iterations) - 1:
            aug_grammars, aug_nt_nodes, stand_alone_constants = mcts_model.freeze_equations(population,
                                                                                            opt_num_expr,
                                                                                            stand_alone_constants,
                                                                                            round_idx + 1)
            aug_grammars = _dedupe_preserve_order(aug_grammars)
            print("AUG grammars")
            print(aug_grammars)

        max_module += int(module_grow_step)
        exploration_rate *= 1.2
        num_rollouts = max(15, int(num_rollouts * 0.8))
    print("final hof")
    mcts_model.print_hofs(-1, verbose=False)


def vsr_mcts(equation_name, num_per_episodes, metric_name, noise_type, noise_scale, optimizer,
             production_rules_mode,
             memray_output_bin, track_memory=False):
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
    num_iterations = create_uniform_generations(num_per_episodes, nvar)
    if production_rules_mode == 'trigometric':
        from production_rules_trigometric import get_production_rules
    elif production_rules_mode == 'livermore2':
        from production_rules import get_production_rules
    elif production_rules_mode == 'feynman':
        from production_rules_feynman import get_production_rules
    base_rules = get_production_rules(0, operators_set)
    rule_bank = create_run_rule_bank(
        base_rules,
        tag=f"{equation_name}-vsr",
        extra_metadata={
            "equation_name": equation_name,
            "mode": "vsr",
            "production_rules_mode": production_rules_mode,
        },
    )
    if track_memory:
        import memray
        if os.path.isfile(memray_output_bin):
            os.remove(memray_output_bin)
        with memray.Tracker(memray_output_bin):
            start = time.time()
            run_vsr_mcts(operators_set, opt_num_expr, num_iterations, production_rules_mode=production_rules_mode, rule_bank=rule_bank)
            end_time = time.time() - start
    else:
        start = time.time()
        run_vsr_mcts(operators_set, opt_num_expr, num_iterations, production_rules_mode=production_rules_mode, rule_bank=rule_bank)
        end_time = time.time() - start

    print("VSR-MCTS {} mins".format(np.round(end_time / 60, 3)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")
    parser.add_argument('--optimizer',
                        nargs='?',
                        choices=['BFGS', 'L-BFGS-B', 'Nelder-Mead', 'CG', 'basinhopping', 'dual_annealing', 'shgo'],
                        help='list servers, storage, or both (default: %(default)s)')
    parser.add_argument("--metric_name", type=str, default='neg_mse', help="The name of the metric for loss.")
    parser.add_argument("--num_episodes", type=int, default=1000, help="the number of episode for MCTS.")
    parser.add_argument("--num_per_episodes", type=int, default=30, help="the number of episode for MCTS.")
    parser.add_argument("--noise_type", type=str, default='normal', help="The name of the noises.")
    parser.add_argument("--noise_scale", type=float, default=0.0, help="This parameter adds the standard deviation of the noise")
    parser.add_argument("--memray_output_bin", type=str, help="memory profile")
    parser.add_argument("--production_rule_mode", type=str, default='livermore2', help="production rules")
    parser.add_argument("--track_memory", action="store_true",
                        help="whether run memery track evaluation.")
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
    os.environ["SCIBENCH_NUM_ROLLOUTS"] = str(args.num_per_episodes)

    if args.cv_mcts:
        vsr_mcts(args.equation_name, args.num_per_episodes, args.metric_name, args.noise_type, args.noise_scale, args.optimizer,
                 args.production_rule_mode,
                 args.memray_output_bin,
                 args.track_memory)
    else:
        mcts(args.equation_name, args.num_episodes, args.metric_name, args.noise_type, args.noise_scale, args.optimizer,
             args.production_rule_mode,
             args.memray_output_bin, args.track_memory)
