import copy
import sys
import os
import json
import time
import numpy as np
from collections import defaultdict
from sympy import Symbol

from production_rules import production_rules_to_expr
from program import execute
from utils import pretty_print_expr


def _qn_to_serializable(qn_dict, topk=None):
    """
    Convert QN defaultdict into JSON-serializable dict:
      state -> {"Q": float, "N": int, "Q_per_N": float|None}

    If topk is set, keep only top-k entries by N (visit count).
    """
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
    """
    Save QN snapshot if SCIBENCH_SAVE_QN=1.

    Env vars:
      SCIBENCH_SAVE_QN=1
      SCIBENCH_QN_DIR=<dir to write json>
      SCIBENCH_EQ_FILE=<equation file path>     (optional)
      SCIBENCH_RUN_TAG=<case_run label>         (optional)
      SCIBENCH_SAVE_QN_TOPK=<int>               (optional)
    """
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


class MCTS(object):
    """
    MCTS for symbolic regression.

    Notes:
    - CTV removed: always samples full X via task.rand_draw_data().
    - QN now accumulates raw reward, and deeper states are recorded so JSON snapshots are meaningful.
    """
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
        self.QN = defaultdict(lambda: np.zeros(2))  # [Q, N]

        self.eta = eta
        self.max_opt_iter = max_opt_iter

    def valid_production_rules(self, node):
        return [i for i, x in enumerate(self.grammars) if x.startswith(node)]

    def get_non_terminal_nodes(self, prod) -> list:
        return [i for i in prod[3:] if i in self.non_terminal_nodes]

    def get_unvisited_children(self, state, node) -> list:
        valid_actions = self.valid_production_rules(node)
        return [act for act in valid_actions if self.QN[state + "," + self.grammars[act]][1] == 0]

    def step(self, state, action_idx, ntn):
        """
        Apply one grammar rule to expand the parse tree.
        If no non-terminals remain, evaluate and return reward.
        """
        action = self.grammars[action_idx]
        state = state + "," + action
        ntn = self.get_non_terminal_nodes(action) + ntn

        if not ntn:
            self.task.rand_draw_data()
            y_true = self.task.evaluate()

            expr_template = production_rules_to_expr(state.split(","))
            reward, eq, _, _ = self.program.optimize(
                expr_template,
                len(state.split(",")),
                self.task.X,
                y_true,
                self.input_var_Xs,
                eta=self.eta,
                max_opt_iter=self.max_opt_iter,
            )
            return state, ntn, reward, True, eq

        return state, ntn, 0, False, None

    def update_ucb_mcts(self, state, action):
        """
        UCB score for choosing `action` from `state`.
        Uses Q/N + exploration term.
        """
        next_state = state + "," + action
        Q_child = self.QN[next_state][0]
        N_parent = self.QN[state][1]
        N_child = self.QN[next_state][1]

        # avoid div-by-zero
        if N_child <= 0:
            return float("inf")
        if N_parent <= 0:
            N_parent = 1

        return (Q_child / N_child) + self.exploration_rate * np.sqrt(np.log(N_parent) / N_child)

    def back_propagate(self, state, action_index, reward):
        """
        Backpropagate raw reward into QN and update UCBs along the ancestry of `state`.
        This makes Q nonzero even early (no scale gating).
        """
        action = self.grammars[action_index]

        # update (state, action) edge
        edge_key = state + "," + action
        self.QN[edge_key][0] += reward
        self.QN[edge_key][1] += 1

        # update state chain
        cur_state = state
        cur_action = action

        while cur_state:
            self.QN[cur_state][0] += reward
            self.QN[cur_state][1] += 1

            # update UCB for the action taken at this state
            try:
                aidx = self.grammars.index(cur_action)
                self.UCBs[cur_state][aidx] = self.update_ucb_mcts(cur_state, cur_action)
            except ValueError:
                pass

            if "," in cur_state:
                cur_state, cur_action = cur_state.rsplit(",", 1)
            else:
                cur_state = ""

    def update_hall_of_fame(self, state, reward, eq):
        module = state
        if state.count(",") <= self.max_module:
            if not self.hall_of_fame:
                self.hall_of_fame = [(module, reward, eq)]
            elif eq not in [x[2] for x in self.hall_of_fame]:
                if len(self.hall_of_fame) < self.max_aug:
                    self.hall_of_fame = sorted(self.hall_of_fame + [(module, reward, eq)], key=lambda x: x[1])
                else:
                    if reward > self.hall_of_fame[0][1]:
                        self.hall_of_fame = sorted(self.hall_of_fame[1:] + [(module, reward, eq)], key=lambda x: x[1])

    def rollout(self, num_play, state_initial, ntn_initial):
        """
        Perform `num_play` random rollouts from (state_initial, ntn_initial).
        Returns (best_reward, best_eq, best_state).
        """
        best_eq = ""
        best_r = -100
        best_state = None
        idx = 0

        while idx < num_play:
            done = False
            state = state_initial
            ntn = ntn_initial

            while not done:
                valid_index = self.valid_production_rules(ntn[0])
                action = np.random.choice(valid_index)
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn[1:])
                state, ntn = next_state, ntn_next
                self.QN[state][1] += 1

                if state.count(",") >= self.max_len:
                    break

            if done:
                idx += 1
                if reward > best_r:
                    self.update_hall_of_fame(next_state, reward, eq)
                    best_eq = eq
                    best_r = reward
                    best_state = next_state

        return best_r, best_eq, best_state

    def MCTS_run_orig(self, num_episodes, num_rollouts=50, verbose=False, print_freq=5):
        """
        Simple MCTS loop:
        - selects one unvisited child from root each episode
        - uses rollout to estimate reward
        - backpropagates reward for root-edge
        - ALSO records best deep rollout state into QN (so exported QN is informative)
        """
        best_solution = ("C", -100)
        save_every = int(os.environ.get("SCIBENCH_SAVE_QN_EVERY", "0") or 0)

        for t in range(1, num_episodes + 1):
            print("\tITER {}/{}...".format(t, num_episodes))

            state = "f->A"
            ntn = ["A"]

            unvisited_children = self.get_unvisited_children(state, ntn[0])

            if len(unvisited_children) != 0:
                action_idx = np.random.choice(unvisited_children)
                next_state, ntn_next, reward, done, eq = self.step(state, action_idx, ntn[1:])

                best_state = None

                if not done:
                    reward, eq, best_state = self.rollout(num_rollouts, next_state, ntn_next)
                else:
                    best_state = next_state

                # record deep best state so QN includes deeper keys
                if best_state is not None:
                    self.QN[best_state][0] += reward
                    self.QN[best_state][1] += 1

                if reward > best_solution[1]:
                    best_solution = (eq, reward)

                # backprop from root choice (still improves root policy)
                self.back_propagate(state, action_idx, reward)

            if save_every and (t % save_every == 0):
                _save_qn_snapshot(self.QN, step=t, reason="periodic")

            if t % print_freq == 0 and verbose:
                print("#QN:", len(self.QN.keys()))
                self.print_hofs()

        _save_qn_snapshot(self.QN, step=num_episodes, reason="final")
        self.print_hofs()
        return [], self.hall_of_fame

    def print_hofs(self):
        self.task.rand_draw_data()
        print("PRINT HOF")
        print("=" * 20)
        for pr in self.hall_of_fame:
            print("        " + str(get_state(pr)))
        print("=" * 20)


def get_state(pr):
    return {
        "reward": pr[1],
        "pretty-eq": pretty_print_expr(pr[2]),
        "rules": pr[0],
    }
