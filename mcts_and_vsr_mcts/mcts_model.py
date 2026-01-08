import copy
import sys
import numpy as np
from collections import defaultdict
from sympy import Symbol

from production_rules import production_rules_to_expr
from program import execute
from utils import pretty_print_expr


class MCTS(object):
    task = None
    program = None

    def __init__(
        self, base_grammars, aug_grammars, non_terminal_nodes, aug_nt_nodes,
        max_len, max_module, aug_grammars_allowed,
        exploration_rate=1 / np.sqrt(2), eta=0.999, max_opt_iter=500
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
        self.scale = 0
        self.eta = eta
        self.max_opt_iter = max_opt_iter

    def valid_production_rules(self, node):
        return [self.grammars.index(x) for x in self.grammars if x.startswith(node)]

    def get_non_terminal_nodes(self, prod) -> list:
        return [i for i in prod[3:] if i in self.non_terminal_nodes]

    def get_unvisited_children(self, state, node) -> list:
        valid_actions = self.valid_production_rules(node)
        return [act for act in valid_actions if self.QN[state + "," + self.grammars[act]][1] == 0]

    def step(self, state, action_idx, ntn):
        action = self.grammars[action_idx]
        state = state + "," + action
        ntn = self.get_non_terminal_nodes(action) + ntn

        if not ntn:
            # CTV removed: always sample full data
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
                max_opt_iter=self.max_opt_iter
            )
            return state, ntn, reward, True, eq

        return state, ntn, 0, False, None

    def update_ucb_mcts(self, state, action):
        next_state = state + "," + action
        Q_child = self.QN[next_state][0]
        N_parent = self.QN[state][1]
        N_child = self.QN[next_state][1]
        return Q_child / N_child + self.exploration_rate * np.sqrt(np.log(N_parent) / N_child)

    def back_propagate(self, state, action_index, reward):
        action = self.grammars[action_index]
        if self.scale != 0:
            self.QN[state + "," + action][0] += reward / self.scale
        self.QN[state + "," + action][1] += 1

        while state:
            if self.scale != 0:
                self.QN[state][0] += reward / self.scale
            self.QN[state][1] += 1
            self.UCBs[state][self.grammars.index(action)] = self.update_ucb_mcts(state, action)

            if "," in state:
                state, action = state.rsplit(",", 1)
            else:
                state = ""

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
        best_eq = ""
        best_r = -100
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

                if state.count(",") >= self.max_len:
                    break

            if done:
                idx += 1
                if reward > best_r:
                    self.update_hall_of_fame(next_state, reward, eq)
                    best_eq = eq
                    best_r = reward

        return best_r, best_eq

    def MCTS_run_orig(self, num_episodes, num_rollouts=50, verbose=False, print_freq=5):
        nA = len(self.grammars)
        best_solution = ("C", -100)

        for t in range(1, num_episodes + 1):
            print("\tITER {}/{}...".format(t, num_episodes))

            # Always start at A (CTV removed)
            state = "f->A"
            ntn = ["A"]

            unvisited_children = self.get_unvisited_children(state, ntn[0])

            if len(unvisited_children) != 0:
                action = np.random.choice(unvisited_children)
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn[1:])
                if not done:
                    reward, eq = self.rollout(num_rollouts, next_state, ntn_next)

                if reward > best_solution[1]:
                    best_solution = (eq, reward)

                self.back_propagate(state, action, reward)

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
