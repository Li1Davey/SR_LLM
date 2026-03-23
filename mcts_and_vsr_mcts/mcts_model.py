import copy
import sys
import os
import json
import time
import numpy as np
from collections import defaultdict
from sympy import Symbol

from llm_supexp_feedback import maybe_generate_supexpressions
from production_rules import production_rules_to_expr
from program import execute
from utils import pretty_print_expr
import re

def _qn_to_serializable(qn_dict, topk=None):
    items = []
    for k, v in qn_dict.items():
        try:
            q = float(v[0])
            n = int(v[1])
        except Exception:
            continue
        items.append((str(k), q, n))

    items.sort(key=lambda x: x[2], reverse=True)
    if topk is not None:
        items = items[: int(topk)]

    out = {k: {"Q": q, "N": n, "Q_per_N": (q / n if n else None)} for (k, q, n) in items}
    return out, len(items)


def _save_qn_snapshot(qn_dict, step=None, reason="periodic"):
    if os.environ.get("SCIBENCH_SAVE_QN", "0") != "1":
        return

    qn_dir = os.environ.get("SCIBENCH_QN_DIR", "").strip()
    if not qn_dir:
        return

    os.makedirs(qn_dir, exist_ok=True)

    eq_file = os.environ.get("SCIBENCH_EQ_FILE", "unknown_eq")
    eq_stem = os.path.splitext(os.path.basename(eq_file))[0]
    run_tag = os.environ.get("SCIBENCH_RUN_TAG", "run")
    pid = os.getpid()
    ts = time.strftime("%Y%m%d_%H%M%S")

    topk_env = os.environ.get("SCIBENCH_SAVE_QN_TOPK", "").strip()
    topk = int(topk_env) if topk_env else None

    qn_out, saved_count = _qn_to_serializable(qn_dict, topk=topk)

    payload = {
        "timestamp": ts,
        "pid": pid,
        "eq_file": eq_file,
        "run_tag": run_tag,
        "step": step,
        "reason": reason,
        "topk": topk,
        "num_entries_saved": saved_count,
        "QN": qn_out,
    }

    step_str = f"_step{step}" if step is not None else ""
    path = os.path.join(
        qn_dir,
        f"{ts}_{eq_stem}_pid{pid}_{run_tag}{step_str}_QN_{reason}.json"
    )

    with open(path, "w") as f:
        json.dump(payload, f)

    print(f"[QN] saved: {path}", flush=True)

def _canonicalize_eq_structure(eq: str) -> str:
    """
    Normalize an equation string so HoF dedup compares structure rather than
    exact fitted constants.
    """
    if eq is None:
        return ""
    s = str(eq)

    # Normalize whitespace.
    s = re.sub(r"\s+", "", s)

    # Replace numeric literals with buckets so close fits count as one template.
    # Keep X0/X1 names intact because they do not match this regex.
    number_pat = r'(?<![A-Za-z_])[-+]?(?:\d+\.\d*|\d*\.\d+|\d+)(?:e[-+]?\d+)?'

    def repl(m):
        token = m.group(0)
        try:
            val = float(token)
        except Exception:
            return token

        # Keep exact zeros / ones stable because they often reflect structure.
        if abs(val) < 1e-12:
            return "0"
        if abs(val - 1.0) < 1e-12:
            return "1"
        if abs(val + 1.0) < 1e-12:
            return "-1"

        # Collapse all other fitted constants to a generic marker.
        return "CNUM"

    s = re.sub(number_pat, repl, s)
    return s

class MCTS(object):
    task = None
    program = None

    def __init__(
        self,
        base_grammars,
        aug_grammars,
        non_terminal_nodes,
        aug_nt_nodes,
        max_len,
        max_module,
        aug_grammars_allowed,
        exploration_rate=1 / np.sqrt(2),
        eta=0.999,
        max_opt_iter=500,
    ):
        self.nvars = self.task.data_query_oracle.get_nvars()
        self.input_var_Xs = [Symbol("X" + str(i)) for i in range(self.nvars)]

        self.base_grammars = base_grammars
        self.aug_grammars = aug_grammars
        self.grammars = base_grammars + [x for x in aug_grammars if x not in base_grammars]

        self.non_terminal_nodes = non_terminal_nodes
        self.max_len = max_len
        self.max_module = max_module
        self.max_aug = aug_grammars_allowed

        self.hall_of_fame = []
        self.exploration_rate = exploration_rate
        self.UCBs = defaultdict(lambda: np.zeros(len(self.grammars)))
        self.QN = defaultdict(lambda: np.zeros(2))

        self.eta = eta
        self.max_opt_iter = max_opt_iter

    def valid_production_rules(self, node):
        return [i for i, x in enumerate(self.grammars) if x.startswith(node)]

    def get_non_terminal_nodes(self, prod) -> list:
        return [i for i in prod[3:] if i in self.non_terminal_nodes]

    def get_unvisited_children(self, state, node) -> list:
        valid_actions = self.valid_production_rules(node)
        return [act for act in valid_actions if self.QN[state + "," + self.grammars[act]][1] == 0]

    def score_expression_on_validation(self, eq, state_len):
        val_X, val_y = self.task.get_val_batch()
        reward, _, _, _ = self.program.optimize(
            eq,
            state_len,
            val_X,
            val_y,
            self.input_var_Xs,
            eta=self.eta,
            max_opt_iter=self.max_opt_iter,
        )
        return reward

    def step(self, state, action_idx, ntn):
        action = self.grammars[action_idx]
        state = state + "," + action
        ntn = self.get_non_terminal_nodes(action) + ntn

        if not ntn:
            train_X, train_y = self.task.get_train_batch()

            expr_template = production_rules_to_expr(state.split(","))
            reward_train, eq, _, _ = self.program.optimize(
                expr_template,
                len(state.split(",")),
                train_X,
                train_y,
                self.input_var_Xs,
                eta=self.eta,
                max_opt_iter=self.max_opt_iter,
            )

            if not np.isfinite(reward_train):
                return state, ntn, reward_train, True, eq

            reward_val = self.score_expression_on_validation(eq, len(state.split(",")))
            reward = reward_val if np.isfinite(reward_val) else reward_train
            return state, ntn, reward, True, eq

        return state, ntn, 0, False, None

    def update_ucb_mcts(self, state, action):
        next_state = state + "," + action
        Q_child = self.QN[next_state][0]
        N_parent = self.QN[state][1]
        N_child = self.QN[next_state][1]

        if N_child <= 0:
            return float("inf")
        if N_parent <= 0:
            N_parent = 1

        return (Q_child / N_child) + self.exploration_rate * np.sqrt(np.log(N_parent) / N_child)

    def back_propagate(self, path, reward):
        if not path:
            return

        ordered_states = [path[0][0]] + [child_state for _, _, child_state in path]
        seen = set()
        deduped_states = []
        for s in ordered_states:
            if s not in seen:
                deduped_states.append(s)
                seen.add(s)

        for s in deduped_states:
            self.QN[s][0] += reward
            self.QN[s][1] += 1

        for parent_state, action_index, _ in reversed(path):
            self.UCBs[parent_state][action_index] = self.update_ucb_mcts(
                parent_state, self.grammars[action_index]
            )

    def update_hall_of_fame(self, state, reward, eq):
        reward = float(reward)
        module = state
        if state.count(",") <= self.max_module:
            hof_changed = False
            eq_key = _canonicalize_eq_structure(eq)
            existing_keys = {_canonicalize_eq_structure(x[2]) for x in self.hall_of_fame}

            if not self.hall_of_fame:
                self.hall_of_fame = [(module, reward, eq)]
                hof_changed = True
            elif eq_key not in existing_keys:
                if len(self.hall_of_fame) < self.max_aug:
                    self.hall_of_fame = sorted(self.hall_of_fame + [(module, reward, eq)], key=lambda x: x[1])
                    hof_changed = True
                else:
                    if reward > self.hall_of_fame[0][1]:
                        self.hall_of_fame = sorted(self.hall_of_fame[1:] + [(module, reward, eq)], key=lambda x: x[1])
                        hof_changed = True
            else:
                # If the structure already exists, keep the better-scoring fit.
                improved = False
                new_hof = []
                for item in self.hall_of_fame:
                    if _canonicalize_eq_structure(item[2]) == eq_key:
                        if reward > item[1]:
                            new_hof.append((module, reward, eq))
                            improved = True
                        else:
                            new_hof.append(item)
                    else:
                        new_hof.append(item)
                if improved:
                    self.hall_of_fame = sorted(new_hof, key=lambda x: x[1])
                    hof_changed = True

            if hof_changed:
                try:
                    maybe_generate_supexpressions(self.hall_of_fame, self.nvars)
                except Exception as e:
                    print(f"[SUPEXP] generation skipped: {e}", flush=True)

    def rollout(self, num_play, state_initial, ntn_initial):
        best_eq = ""
        best_r = -100
        best_state = None
        idx = 0

        while idx < num_play:
            done = False
            state = state_initial
            ntn = list(ntn_initial)

            while not done and ntn:
                valid_index = self.valid_production_rules(ntn[0])
                action = np.random.choice(valid_index)
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn[1:])
                state, ntn = next_state, ntn_next

                if not done and state.count(",") >= self.max_len:
                    break

            idx += 1

            if done and reward > best_r:
                self.update_hall_of_fame(state, reward, eq)
                best_eq = eq
                best_r = reward
                best_state = state

        return best_r, best_eq, best_state

    def tree_num_nodes(self):
        return len(self.QN)

    def tree_height(self):
        if not self.QN:
            return 0
        return max(s.count(",") for s in self.QN.keys())

    def select_action(self, state, node):
        unvisited_children = self.get_unvisited_children(state, node)
        valid_actions = self.valid_production_rules(node)

        if len(unvisited_children) != 0:
            return int(np.random.choice(unvisited_children)), True

        ucb_vals = self.UCBs[state][valid_actions]
        if np.allclose(ucb_vals, 0):
            return int(np.random.choice(valid_actions)), False

        ucb_vals = ucb_vals - np.max(ucb_vals)
        p = np.exp(ucb_vals)
        p = p / np.sum(p)
        return int(np.random.choice(valid_actions, p=p)), False

    def MCTS_run_orig(self, num_episodes, num_rollouts=50, verbose=False, print_freq=5):
        best_solution = ("C", -100)
        save_every = int(os.environ.get("SCIBENCH_SAVE_QN_EVERY", "0") or 0)

        for t in range(1, num_episodes + 1):
            self.task.draw_episode_batches()
            self.program.clear_cache()

            if t == 1 or (print_freq and t % print_freq == 0):
                print(
                    f"\tITER {t}/{num_episodes} | "
                    f"Tree nodes={self.tree_num_nodes()} | "
                    f"Tree height={self.tree_height()}"
                )

            state = "f->A"
            ntn = ["A"]
            path = []
            reward = -100
            eq = ""
            done = False

            while not done and ntn:
                action_idx, expanded_new_child = self.select_action(state, ntn[0])
                next_state, ntn_next, reward, done, eq = self.step(state, action_idx, ntn[1:])
                path.append((state, action_idx, next_state))
                state, ntn = next_state, ntn_next

                if done:
                    self.update_hall_of_fame(state, reward, eq)
                    break

                if state.count(",") >= self.max_len:
                    reward = -100
                    eq = ""
                    break

                if expanded_new_child:
                    reward, eq, _ = self.rollout(num_rollouts, state, ntn)
                    break

            if reward > best_solution[1]:
                best_solution = (eq, reward)

            self.back_propagate(path, reward)

            if save_every and (t % save_every == 0):
                _save_qn_snapshot(self.QN, step=t, reason="periodic")

            if verbose and (t == 1 or (print_freq and t % print_freq == 0)):
                print("#QN:", len(self.QN.keys()))
                self.print_hofs()

        _save_qn_snapshot(self.QN, step=num_episodes, reason="final")
        self.print_hofs()
        return [], self.hall_of_fame

    def print_hofs(self):
        print("PRINT HOF")
        print("=" * 20)
        for pr in self.hall_of_fame:
            print("        " + str(get_state(pr)))
        print("=" * 20)


def get_state(pr):
    eq = pr[2]
    if not isinstance(eq, str):
        eq = str(eq)
    if len(eq) > 300:
        pretty = eq
    else:
        try:
            pretty = pretty_print_expr(eq)
        except Exception:
            pretty = eq
    return {
        "reward": float(pr[1]),
        "pretty-eq": pretty,
        "rules": pr[0],
    }
