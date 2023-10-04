import sys
import numpy as np
from collections import defaultdict
from utils import tree_to_eq
from sympy import Symbol


class MCTS(object):
    """
    hall_of_fame: ranked good expressions.
    """
    # task = None  # Task
    program = None
    # constants
    const_optimizer = None  # Function to optimize constants
    opt_num_expr = 1  # number of experiments done for optimization
    expr_obj_thres = 1e-2
    expr_consts_thres = 1e-3

    noise_std = 0.0

    def __init__(self, task, base_grammars, aug_grammars, nt_nodes, max_len, max_module, aug_grammars_allowed,
                 exploration_rate=1 / np.sqrt(2), eta=0.999):
        # for generating input data and evaluate the output.
        self.task = task
        # number of input variables
        self.nvars = self.task.data_query_oracle.get_nvars()
        self.input_var_Xs = [Symbol('X' + str(i)) for i in range(self.nvars)]
        self.base_grammars = base_grammars
        self.grammars = base_grammars + [x for x in aug_grammars if x not in base_grammars]
        self.nt_nodes = nt_nodes
        self.max_len = max_len
        self.max_module = max_module
        self.max_aug = aug_grammars_allowed
        self.hall_of_fame = []
        self.exploration_rate = exploration_rate
        self.UCBs = defaultdict(lambda: np.zeros(len(self.grammars)))
        self.QN = defaultdict(lambda: np.zeros(2))
        self.scale = 0
        self.eta = eta

    def valid_production_rules(self, Node):
        """
        Get index of all possible production rules starting with a given node
        """
        return [self.grammars.index(x) for x in self.grammars if x.startswith(Node)]

    def get_non_terminal_nodes(self, prod, prod_idx) -> list:
        """
        Get all the non-terminal nodes from right-hand side of a production rule grammar
        """
        if prod_idx >= len(self.base_grammars):
            return []
        else:
            return [i for i in prod[3:] if i in self.nt_nodes]

    def get_unvisited_children(self, state, node) -> list:
        """
        Pick an action to to visit the index of all unvisited child.
        """
        valid_actions = self.valid_production_rules(node)
        return [act for act in valid_actions if self.QN[state + ',' + self.grammars[act]][1] == 0]

    def step(self, state, action_idx, ntn):
        """
        state:      all production rules
        action_idx: index of grammar starts from the current Non-terminal Node
        tree:       the current tree
        ntn:        all remaining non-terminal nodes
        
        
        This defines one step of Parse Tree traversal
        return tree (next state), remaining non-terminal nodes, reward, and if it is done
        """
        action = self.grammars[action_idx]
        state = state + ',' + action
        ntn = self.get_non_terminal_nodes(action, action_idx) + ntn[1:]

        if not ntn:
            self.task.rand_draw_X_non_fixed()
            y_true = self.task.evaluate()
            reward, eq = self.program.optimize(tree_to_eq(state.split(',')),
                                               len(state.split(',')),
                                               self.task.X,
                                               y_true,
                                               self.input_var_Xs,
                                               eta=self.eta)
            return state, ntn, reward, True, eq
        else:
            return state, ntn, 0, False, None

    def rollout(self, num_play, state_initial, ntn_initial):
        """
        Perform a n-play rollout simulation, get the maximum reward
        """
        best_eq = ''
        best_r = 0
        for n in range(num_play):
            done = False
            state = state_initial
            ntn = ntn_initial

            while not done:
                valid_index = self.valid_production_rules(ntn[0])
                action = np.random.choice(valid_index)
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn)
                state = next_state
                ntn = ntn_next

                if state.count(',') >= self.max_len:
                    break

            if done:
                if reward > best_r:
                    # save the current expression into hall-of-fame
                    self.update_hall_of_fame(next_state, reward, eq)
                    best_eq = eq
                    best_r = reward

        return best_r, best_eq

    def update_ucb_mcts(self, state, action):
        """
        Get the ucb score for a given child of current node
        """
        next_state = state + ',' + action
        Q_child = self.QN[next_state][0]
        N_parent = self.QN[state][1]
        N_child = self.QN[next_state][1]
        return Q_child / N_child + self.exploration_rate * np.sqrt(np.log(N_parent) / N_child)

    def update_QN_scale(self, new_scale):
        """
        Update the Q values self.scaled by the new best reward.
        """
        if self.scale != 0:
            for s in self.QN:
                self.QN[s][0] *= (self.scale / new_scale)

        self.scale = new_scale

    def back_propagate(self, state, action_index, reward):
        """
        Update the Q, N and ucb for all corresponding decedent after a complete rollout
        """

        action = self.grammars[action_index]
        if self.scale != 0:
            self.QN[state + ',' + action][0] += reward / self.scale
        else:
            self.QN[state + ',' + action][0] += 0
        self.QN[state + ',' + action][1] += 1

        while state:
            if self.scale != 0:
                self.QN[state][0] += reward / self.scale
            else:
                self.QN[state][0] += 0
            self.QN[state][1] += 1
            self.UCBs[state][self.grammars.index(action)] = self.update_ucb_mcts(state, action)
            if ',' in state:
                state, action = state.rsplit(',', 1)
            else:
                state = ''

    def get_ucb_policy(self, nA):
        """
        Creates an policy based on ucb score. 
        """

        def policy_fn(state, node):
            valid_action = self.valid_production_rules(node)

            # collect ucb scores for all valid actions
            policy_valid = []

            sum_ucb = sum(self.UCBs[state][valid_action])

            for a in valid_action:
                policy_mcts = self.UCBs[state][a] / sum_ucb
                policy_valid.append(policy_mcts)

            # if all ucb scores identical, return uniform policy
            if len(set(policy_valid)) == 1:
                A = np.zeros(nA)
                A[valid_action] = float(1 / len(valid_action))
                return A

            # return action with largest ucb score
            A = np.zeros(nA, dtype=float)
            best_action = valid_action[np.argmax(policy_valid)]
            A[best_action] += 0.8
            A[valid_action] += float(0.2 / len(valid_action))
            return A

        return policy_fn

    def get_uniform_random_policy(self, nA):
        """
        Creates an random policy to select an unvisited child. 
        """

        def policy_fn(UC):
            if len(UC) != len(set(UC)):
                print(UC)
                print(self.grammars)
            action_probs = np.ones(nA, dtype=float) * float(1 / len(UC))
            return action_probs

        return policy_fn

    def update_hall_of_fame(self, state, reward, eq):
        """
        If we pass by a concise solution with high score, we store it as an 
        single action for future use. 
        """
        module = state[5:]
        if state.count(',') <= self.max_module:
            if not self.hall_of_fame:
                self.hall_of_fame = [(module, reward, eq)]
            elif eq not in [x[2] for x in self.hall_of_fame]:
                if len(self.hall_of_fame) < self.max_aug:
                    self.hall_of_fame = sorted(self.hall_of_fame + [(module, reward, eq)], key=lambda x: x[1])
                else:
                    if reward > self.hall_of_fame[0][1]:
                        self.hall_of_fame = sorted(self.hall_of_fame[1:] + [(module, reward, eq)], key=lambda x: x[1])

    def MCTS_run(self, num_iterations, num_simulations=50, verbose=False, print_freq=100):
        """
        Monte Carlo Tree Search algorithm
        """

        nA = len(self.grammars)
        # search history
        states = []

        # The policy we're following: 
        # ucb_policy for fully expanded node and uniform_random_policy for not fully expanded node
        ucb_policy = self.get_ucb_policy(nA)
        uniform_random_policy = self.get_uniform_random_policy(nA)

        reward_his = []
        best_solution = ('nothing', 0)

        for iter in range(1, num_iterations + 1):
            if iter % print_freq == 0 and verbose:
                print("\rIteration {}/{}...".format(iter, num_iterations))
                for i in range(min(len(self.hall_of_fame), 10)):
                    print(self.hall_of_fame[i])
                # print("current reward {:.4f}. expr {}")
                sys.stdout.flush()

            state = 'f->A'
            ntn = ['A']
            unvisited_children = self.get_unvisited_children(state, ntn[0])

            ########################################################
            # check scenario: if parent node fully expanded or not #
            ########################################################

            # scenario 1: if current parent node fully expanded, follow ucb_policy
            while not unvisited_children:
                print("following UCB_policy...")
                prob = ucb_policy(state, ntn[0])
                action = np.random.choice(np.arange(nA), p=prob / np.sum(prob))
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn)
                if state not in states:
                    states.append(state)

                if not done:
                    state = next_state
                    ntn = ntn_next
                    unvisited_children = self.get_unvisited_children(state, ntn[0])

                    if state.count(',') >= self.max_len:
                        unvisited_children = []
                        print("BACK-PROPAGATION STEP")
                        self.back_propagate(state, action, 0)
                        reward_his.append(best_solution[1])
                        break
                else:
                    unvisited_children = []
                    if reward > best_solution[1]:
                        self.update_hall_of_fame(next_state, reward, eq)
                        self.update_QN_scale(reward)
                        best_solution = (eq, reward)
                    print("BACK-PROPAGATION STEP")
                    self.back_propagate(state, action, reward)
                    reward_his.append(best_solution[1])
                    break

            # scenario 2: if current parent node not fully expanded, follow uniform_random_policy
            if unvisited_children:
                print("follow uniform_random_policy:", unvisited_children)
                prob = uniform_random_policy(unvisited_children)
                action = np.random.choice(np.arange(nA), p=prob / np.sum(prob))
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn)
                if not done:
                    # 3. SIMULATION STEP in MCTS.
                    print("simulation step")
                    reward, eq = self.rollout(num_simulations, next_state, ntn_next)
                    if state not in states:
                        states.append(state)

                if reward > best_solution[1]:
                    self.update_QN_scale(reward)
                    best_solution = (eq, reward)
                # 4. BACK-PROPAGATION STEP in MCTS.
                print("BACK-PROPAGATION STEP")
                self.back_propagate(state, action, reward)
                reward_his.append(best_solution[1])
                print("the Q table:")
                for key in self.QN:
                    print(key, self.QN[key])
                print('-' * 40)

        return reward_his, best_solution, self.hall_of_fame
