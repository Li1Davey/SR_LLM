from pympler import classtracker
import time
import argparse
import os

from mcts_model import MCTS

import random
import numpy as np
from scibench.symbolic_data_generator import DataX
from scibench.symbolic_equation_evaluator_public import Equation_evaluator
from regress_task import RegressTask
from program import Program

import datetime


def run_mcts(
        production_rules, non_terminal_nodes=None, num_episodes=1000, num_rollouts=40,
        max_len=30, eta=0.9999, max_module_init=15, num_aug=10, exp_rate=1 / np.sqrt(2),
        num_transplant=1,
        max_opt_iter=200,
        suggest_log_path='llm_rule_history.log',
        use_llm=False
):
    if non_terminal_nodes is None:
        non_terminal_nodes = ['A']

    grammars = production_rules
    module_grow_step = (max_len - max_module_init) / num_transplant
    exploration_rate = exp_rate
    max_module = max_module_init
    best_modules = []
    aug_grammars = []

    # Write the log header once before the transplant loop.
    # FIXED: removed the misplaced inner try block that referenced i_itr and
    # mcts_model before they existed — both are only defined inside the loop (DS)
    if use_llm:
        try:
            dir_name = os.path.dirname(suggest_log_path)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(suggest_log_path, 'a') as f:
                f.write(f"=== LLM Rule History Log — started {datetime.datetime.now().isoformat()} ===\n\n")
        except Exception as e:
            print(f">>> [MCTS-LLM] Warning: could not create log file: {type(e).__name__}: {e}")

    for i_itr in range(num_transplant):
        print("transplanation step=", i_itr)
        print("aug_grammars:", aug_grammars)
        tracker = classtracker.ClassTracker()

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
                          suggest_log_path=suggest_log_path,
                          use_llm=use_llm,
                          num_episodes=num_episodes)

        # Log config for this transplant step.
        # FIXED: removed references to min_reward_for_llm and min_gap which no
        # longer exist on MCTS after the LLM trigger was simplified (DS)
        if use_llm:
            try:
                with open(suggest_log_path, 'a') as f:
                    f.write(f"=== Transplant step {i_itr} — "
                            f"suggest_interval={mcts_model.suggest_interval} ===\n\n")
            except Exception as e:
                print(f">>> [MCTS-LLM] Warning: could not write transplant header: {type(e).__name__}: {e}")

        tracker.track_object(mcts_model)
        start = time.time()
        _, good_modules = mcts_model.MCTS_run_orig(num_episodes,
                                                   num_rollouts=num_rollouts,
                                                   verbose=True,
                                                   is_first_round=True,
                                                   print_freq=5)
        tracker.create_snapshot()
        tracker.stats.print_summary()
        mcts_model.print_hofs()

        if not best_modules:
            best_modules = good_modules
        else:
            best_modules = sorted(list(set(best_modules + good_modules)), key=lambda x: x[1])

        aug_grammars = [x[0] for x in best_modules[:num_aug]]
        print("AUG Grammars")
        for gi in aug_grammars:
            print(gi)

        max_module += module_grow_step
        exploration_rate *= 1.2

    # Guard against num_transplant=0 where mcts_model would never be defined
    if 'mcts_model' in locals():
        print("final hof")
        mcts_model.print_hofs()


def mcts(equation_name, num_episodes, num_rollouts, metric_name, noise_type, noise_scale,
         optimizer, production_rules_mode, memray_output_bin,
         max_opt_iter=200,
         suggest_log_path='llm_rule_history.log',
         track_memory=False,
         use_llm=False):
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

    # Fix: added else branch to raise a clear error for unrecognised modes
    # instead of silently leaving production_rules undefined (NameError)
    if production_rules_mode == 'trigometric':
        from production_rules_trigometric import get_production_rules
    elif production_rules_mode == 'livermore2':
        from production_rules import get_production_rules
    elif production_rules_mode == 'feynman':
        from production_rules_feynman import get_production_rules
    else:
        raise ValueError(
            f"Unknown production_rule_mode: '{production_rules_mode}'. "
            f"Choose from: trigometric, livermore2, feynman"
        )

    production_rules = get_production_rules(nvar, operators_set)
    print("The production rules are:", production_rules)

    if track_memory:
        import memray
        # Remove stale memray output file before starting a fresh trace
        if os.path.isfile(memray_output_bin):
            os.remove(memray_output_bin)
        with memray.Tracker(memray_output_bin):
            start = time.time()
            run_mcts(
                production_rules=production_rules,
                num_episodes=num_episodes,
                num_rollouts=num_rollouts,
                max_opt_iter=max_opt_iter,
                suggest_log_path=suggest_log_path,
                use_llm=use_llm
            )
            elapsed = time.time() - start
    else:
        start = time.time()
        run_mcts(
            production_rules=production_rules,
            num_episodes=num_episodes,
            num_rollouts=num_rollouts,
            max_opt_iter=max_opt_iter,
            suggest_log_path=suggest_log_path,
            use_llm=use_llm
        )
        # Fix: renamed end_time → elapsed since this is a duration, not a timestamp
        elapsed = time.time() - start

    print("MCTS {} mins".format(np.round(elapsed / 60, 3)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", help="the filename of the true program.")
    parser.add_argument('--optimizer',
                        nargs='?',
                        choices=['BFGS', 'L-BFGS-B', 'Nelder-Mead', 'CG', 'basinhopping', 'dual_annealing', 'shgo', 'direct'],
                        help='list servers, storage, or both (default: %(default)s)')
    parser.add_argument("--metric_name", type=str, default='neg_mse', help="The name of the metric for loss.")
    parser.add_argument("--num_episodes", type=int, default=1000, help="the number of episode for MCTS.")
    # Fix: removed dead --num_per_episodes arg that was parsed but never forwarded anywhere
    parser.add_argument("--num_rollouts", type=int, default=40,
                        help="Number of rollouts per episode.")
    parser.add_argument("--max_opt_iter", type=int, default=200,
                        help="Max optimizer iterations per rollout.")
    parser.add_argument("--noise_type", type=str, default='normal', help="The name of the noises.")
    parser.add_argument("--noise_scale", type=float, default=0.0,
                        help="Standard deviation of noise added to observations.")
    parser.add_argument("--memray_output_bin", type=str, default="memray_output.bin",
                        help="Output file for memray memory profiling.")
    parser.add_argument("--production_rule_mode", type=str, default='trigometric',
                        help="Production rule set to use: trigometric, livermore2, or feynman.")
    parser.add_argument('--suggest_log_path', type=str,
                        default='llm_rule_history.log',
                        help='Path to save LLM prompt/response audit log.')
    parser.add_argument("--track_memory", action="store_true",
                        help="Whether to enable memory tracking via memray.")
    # Agrument for when to use LLM suggester
    parser.add_argument(
    "--use_llm",
    type=lambda x: x.lower() == "true",
    default=False,
    help="Whether to enable LLM rule suggestions during MCTS (default: false).")
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed for reproducibility. If not set, uses time-based seed.")


    args = parser.parse_args()

    # Fix: use seed+1 for numpy to guarantee the two seeds are always different,
    # even if both calls to perf_counter() land on the same timer tick
    seed = args.seed if args.seed is not None else int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    print('random seed=', seed)
    np.random.seed(seed + 1)
    print('np.random seed=', seed + 1)
    print(args)

    mcts(args.equation_name, args.num_episodes, args.num_rollouts,
        args.metric_name, args.noise_type, args.noise_scale,
        args.optimizer, args.production_rule_mode,
        args.memray_output_bin,
        max_opt_iter=args.max_opt_iter,
        suggest_log_path=args.suggest_log_path,
        track_memory=args.track_memory,
        use_llm=args.use_llm)
