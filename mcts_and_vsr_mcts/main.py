try:
    from pympler import classtracker
except ImportError:
    classtracker = None
import time
import argparse
import os
import random
import numpy as np

from mcts_model import MCTS
from regress_task import RegressTask
from program import Program


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"Environment variable {name} must be an integer, got: {raw!r}") from exc


def run_mcts(production_rules, non_terminal_nodes=["A"], num_episodes=1000, num_rollouts=40,
            max_len=20, eta=0.99, max_module_init=15, num_aug=10, exp_rate=1 / np.sqrt(2),
            num_transplant=1, max_opt_iter=50):
    grammars = production_rules
    exploration_rate = exp_rate

    use_tracker = os.getenv("SCIBENCH_TRACK_MEM", "0") == "1"
    tracker = classtracker.ClassTracker() if (use_tracker and classtracker is not None) else None

    mcts_model = MCTS(
        base_grammars=grammars,
        aug_grammars=[],
        non_terminal_nodes=non_terminal_nodes,
        aug_nt_nodes=[],
        max_len=max_len,
        max_module=max_module_init,
        aug_grammars_allowed=num_aug,
        exploration_rate=exploration_rate,
        eta=eta,
        max_opt_iter=max_opt_iter,
    )

    if tracker:
        tracker.track_object(mcts_model)

    start = time.time()
    mcts_model.MCTS_run_orig(
        num_episodes,
        num_rollouts=num_rollouts,
        verbose=True,
        print_freq=5
    )

    if tracker:
        tracker.create_snapshot()
        tracker.stats.print_summary()

    print("MCTS {} mins".format(np.round((time.time() - start) / 60, 3)))


def mcts(equation_name, num_episodes, metric_name, noise_type, noise_scale, optimizer,
         production_rules_mode, num_rollouts, max_len, eta, batch_size, max_opt_iter):
    from scibench.program import sciProgram
    from scibench.symbolic_data_generator import DataX
    from scibench.symbolic_equation_evaluator_public import Equation_evaluator

    data_query_oracle = Equation_evaluator(equation_name, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()
    operators_set = data_query_oracle.get_operators_set()

    protected = True
    sciProgram.set_execute(protected=protected, simulated_exec=False)
    print(f"[exec] protected={protected}")

    if batch_size <= 0:
        raise ValueError(f"batch_size must be positive, got {batch_size}")
    if max_opt_iter <= 0:
        raise ValueError(f"max_opt_iter must be positive, got {max_opt_iter}")

    MCTS.task = RegressTask(batch_size, dataXgen, data_query_oracle)
    MCTS.program = Program(nvar, optimizer)
    MCTS.program.evalaute_loss = data_query_oracle.compute_metric

    resolved_config = {
        "equation_name": equation_name,
        "optimizer": optimizer,
        "metric_name": metric_name,
        "num_episodes": num_episodes,
        "num_rollouts": num_rollouts,
        "max_len": max_len,
        "eta": eta,
        "noise_type": noise_type,
        "noise_scale": noise_scale,
        "production_rule_mode": production_rules_mode,
        "batch_size": batch_size,
        "max_opt_iter": max_opt_iter,
    }
    print("[config]", resolved_config)

    os.environ["SCIBENCH_PRODUCTION_RULE_MODE"] = production_rules_mode

    if production_rules_mode == "trigometric":
        try:
            from production_rules_trigometric import get_production_rules
        except ImportError:
            print('[warn] production_rules_trigometric not found; falling back to feynman grammar')
            from production_rules_feynman import get_production_rules
    elif production_rules_mode == "livermore2":
        try:
            from production_rules import get_production_rules
        except ImportError:
            print('[warn] production_rules not found; falling back to feynman grammar')
            from production_rules_feynman import get_production_rules
    elif production_rules_mode == "feynman":
        from production_rules_feynman import get_production_rules
    else:
        raise ValueError(f"Unknown production_rules_mode: {production_rules_mode}")

    production_rules = get_production_rules(nvar, operators_set)
    print("The production rules are:", production_rules)

    run_mcts(
        production_rules=production_rules,
        num_episodes=num_episodes,
        num_rollouts=num_rollouts,
        max_len=max_len,
        eta=eta,
        max_opt_iter=max_opt_iter,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--equation_name", required=True, help="Path to .in file.")
    parser.add_argument("--optimizer", default="L-BFGS-B",
                        choices=["BFGS", "L-BFGS-B", "Nelder-Mead", "CG", "basinhopping", "dual_annealing", "shgo"])
    parser.add_argument("--metric_name", type=str, default="neg_nmse")
    parser.add_argument("--num_episodes", type=int, default=1000)
    parser.add_argument("--num_rollouts", type=int, default=40)
    parser.add_argument("--max_len", type=int, default=20, help="Max grammar expansion length (tree depth limit).")
    parser.add_argument(
        "--eta",
        type=float,
        default=0.99,
        help="Reward decay factor for expression length (closer to 1.0 = weaker penalty)"
    )
    parser.add_argument("--noise_type", type=str, default="normal")
    parser.add_argument("--noise_scale", type=float, default=0.0)
    parser.add_argument("--production_rule_mode", type=str, default="feynman")
    parser.add_argument(
        "--batch_size",
        type=int,
        default=_env_int("SCIBENCH_BATCHSIZE", 256),
        help="Regression batch size per episode for both train and validation batches. Can also be set with SCIBENCH_BATCHSIZE.",
    )
    parser.add_argument(
        "--max_opt_iter",
        type=int,
        default=_env_int("SCIBENCH_MAX_OPT_ITER", 50),
        help="Maximum optimizer iterations for constant fitting. Can also be set with SCIBENCH_MAX_OPT_ITER.",
    )
    args = parser.parse_args()

    seed = int(time.perf_counter() * 10000) % 1000007
    random.seed(seed)
    np.random.seed(seed)

    print("random seed=", seed)
    print(args)

    mcts(args.equation_name, args.num_episodes, args.metric_name, args.noise_type, args.noise_scale,
         args.optimizer, args.production_rule_mode, args.num_rollouts, args.max_len, args.eta,
         args.batch_size, args.max_opt_iter)