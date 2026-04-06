import copy
import sys
import numpy as np
from collections import defaultdict
from sympy import Symbol, Pow
from sympy.parsing.sympy_parser import parse_expr
from production_rules import production_rules_to_expr
from program import execute
from utils import pretty_print_expr, expression_to_template, nth_repl
# Imports (DS)
import json
import re
# Import the suggestion pipeline functions we defined earlier
from suggester import suggest_rules 


class MCTS(object):
    """
    hall_of_fame: ranked good expressions.
    """
    task = None  # Task
    program = None
    # constants
    opt_num_expr = 1  # number of experiments done for optimization
    expr_obj_thres = 1e-6
    expr_consts_thres = 1e-3

    noise_std = 0.0

    def __init__(self, base_grammars, aug_grammars, non_terminal_nodes, aug_nt_nodes, max_len, max_module, aug_grammars_allowed,
                 exploration_rate=1 / np.sqrt(2), eta=0.999, max_opt_iter=500, suggest_log_path="llm_rule_history.log"):
        # number of input variables
        self.nvars = self.task.data_query_oracle.get_nvars()
        self.input_var_Xs = [Symbol('X' + str(i)) for i in range(self.nvars)]
        self.base_grammars = base_grammars
        self.aug_grammars = aug_grammars
        self.grammars = base_grammars + [x for x in aug_grammars if x not in base_grammars]
        self.aug_nt_nodes = aug_nt_nodes
        self.non_terminal_nodes = non_terminal_nodes
        self.max_len = max_len
        self.max_module = max_module
        self.max_aug = aug_grammars_allowed
        self.hall_of_fame = []
        self.exploration_rate = exploration_rate
        # FIXED - size is re-evaluated dynamically every time a new key is created (DS)
        self.UCBs = defaultdict(self._make_ucb_entry)
        self.QN = defaultdict(lambda: np.zeros(2))
        self.scale = 0
        self.eta = eta
        self.max_opt_iter = max_opt_iter
        # --- LLM guide and timer configurations (DS)
        self.last_best_reward_at_suggest = np.inf 
        # Tracks the last time we successfully queried the LLM
        self.last_suggest_iter = 0
        # How many MCTS episodes to wait before asking the LLM for new rules again
        self.suggest_interval = 20
        # Never call LLM more often than every # iters
        self.min_gap = 10
        # Only call LLM if we have something useful
        self.min_reward_for_llm = -8.0
        # Require meaningful improvement before resetting the stuck clock
        self.stuck_improvement_threshold = 0.3
        # A flag that turns True whenever a high-quality expression enters the Hall of Fame
        self.hof_improved = False       
        # File path for auditing LLM prompts and responses
        self.suggest_log_path = suggest_log_path

    # (DS)
    def _make_ucb_entry(self):
        """
        Dynamically creates a zero array sized to the CURRENT grammar length.
        This is critical because the LLM can expand self.grammars mid-run,
        and the defaultdict must reflect the new size for any new states it creates.
        """
        return np.zeros(len(self.grammars))

    def valid_production_rules(self, Node):
        # Get index of all possible production rules starting with a given node
        return [self.grammars.index(x) for x in self.grammars if x.startswith(Node)]
    
    def get_non_terminal_nodes(self, prod) -> list:
        # Get all the non-terminal nodes from right-hand side of a production rule grammar
        return [i for i in prod[3:] if i in self.non_terminal_nodes]

    def get_unvisited_children(self, state, node) -> list:
        #  Pick an action to to visit the index of all unvisited child.
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
        ntn = self.get_non_terminal_nodes(action) + ntn

        if not ntn:
            self.task.rand_draw_data_with_X_fixed()
            y_true = self.task.evaluate()
            expr_template = production_rules_to_expr(state.split(','))
            
            # Guard against astronomically large exponents produced by chained
            # power rules (e.g. A**3**3**3). (DS)
            try:
                test_expr = parse_expr(expr_template.replace('C', '1'))
                max_exp = max(
                    (abs(int(a.exp)) for a in test_expr.atoms(Pow) if a.exp.is_Integer),
                    default=0
                )
                if max_exp > 100:
                    print(f"         [step] Exponent too large ({max_exp}) — skipping: {expr_template}")
                    return state, ntn, -10.0, True, expr_template
            except Exception:
                # If parsing itself fails, treat as invalid
                return state, ntn, -10.0, True, expr_template
            
            reward, eq, _, _ = self.program.optimize(expr_template,
                                                     len(state.split(',')),
                                                     self.task.X,
                                                     y_true,
                                                     self.input_var_Xs,
                                                     eta=self.eta,
                                                     max_opt_iter=self.max_opt_iter)
            
            # Penalise any non-finite result (nan, inf, -inf) instead of
            # propagating it into UCB scores and corrupting the search tree. (DS)
            if not np.isfinite(reward):
                print(f"         [step] Non-finite reward ({reward}) replaced with -10.0 for: {eq}")
                reward = -10.0

            return state, ntn, reward, True, eq
        else:
            return state, ntn, 0, False, None

    def rollout(self, num_play, state_initial, ntn_initial):
        """
        Perform `num_play` simulation, get the maximum reward
        """
        best_eq = ''
        reward = -100
        next_state = None
        eq = ''
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
                state = next_state
                ntn = ntn_next

                if state.count(',') >= self.max_len:  # tree depth shall be less than max_len
                    break

            if done:
                idx += 1
                # Check if finite (DS)
                if np.isfinite(reward) and reward > best_r:
                    self.update_hall_of_fame(next_state, reward, eq)
                    best_eq = eq
                    best_r = reward

        return best_r, best_eq

    def update_ucb_mcts(self, state, action):
        """
        Get the ucb score for a given child of current node
        Q and N values are stored in QN matrix.
        """
        next_state = state + ',' + action
        Q_child = self.QN[next_state][0]
        N_parent = self.QN[state][1]
        N_child = self.QN[next_state][1]
        return Q_child / N_child + self.exploration_rate * np.sqrt(np.log(N_parent) / N_child)

    def update_QN_scale(self, new_scale):
        # Update the Q and the N values self.scaled by the new best reward.
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
            # print("the state is", state)
            if self.scale != 0:
                self.QN[state][0] += reward / self.scale
            else:
                self.QN[state][0] += 0
            self.QN[state][1] += 1
            self.UCBs[state][self.grammars.index(action)] = self.update_ucb_mcts(state, action)
            if state in self.grammars:
                state = ''
            elif ',' in state:
                state, action = state.rsplit(',', 1)
            else:
                state = ''

    def get_ucb_policy(self, nA):
        """
        Creates an policy based on ucb score.
        """

        def policy_fn(state, node):
            valid_action = self.valid_production_rules(node)

            # Compute all UCB scores first so the uniform fallback check
            # has actual values to compare — the original code checked an
            # empty list, so the fallback was never reachable. (DS)
            ucb_scores = [np.exp(self.UCBs[state][a]) for a in valid_action]
            sum_ucb = sum(ucb_scores)

            A = np.zeros(nA, dtype=float)

            # If sum is zero or all scores are identical, fall back to uniform.
            # This guards against ZeroDivisionError and NaN propagation into
            # the UCB tree when a new rule has never been visited. (DS)
            if sum_ucb == 0 or len(set(ucb_scores)) == 1:
                A[valid_action] = float(1 / len(valid_action))
                return A

            # Normalise each score — no need to track the action index here
            # since ucb_scores is already ordered to match valid_action (DS)
            policy_valid = [score / sum_ucb for score in ucb_scores]

            best_action = valid_action[np.argmax(policy_valid)]
            A[best_action] += 0.8
            A[valid_action] += float(0.2 / len(valid_action))
            return A

        return policy_fn
    
    def update_hall_of_fame(self, state, reward, eq):
        """
        If we pass by a concise solution with high score, we store it as an
        single action for future use.
        """
        module = state
        if state.count(',') <= self.max_module:
            if not self.hall_of_fame:
                self.hall_of_fame = [(module, reward, eq)]
                # Trigger LLM because the first valid lead was found (DS)
                self.hof_improved = True 
            elif eq not in [x[2] for x in self.hall_of_fame]:
                # set hof_improved if the expression actually
                # enters the hall of fame, not just because it is unique. (DS)
                if len(self.hall_of_fame) < self.max_aug:
                    # HOF has room — expression always enters
                    self.hall_of_fame = sorted(
                        self.hall_of_fame + [(module, reward, eq)],
                        key=lambda x: x[1]
                    )
                    # Mark improvement only after confirmed entry
                    self.hof_improved = True
                else:
                    if reward > self.hall_of_fame[0][1]:
                        # Expression is better than the current worst — it enters
                        self.hall_of_fame = sorted(
                            self.hall_of_fame[1:] + [(module, reward, eq)],
                            key=lambda x: x[1]
                        )
                        # Mark improvement only after confirmed entry
                        self.hof_improved = True

    def MCTS_run_orig(self, num_episodes, num_rollouts=50, verbose=False, print_freq=5, is_first_round=False, reward_threhold=10):
        """
        Monte Carlo Tree Search algorithm
        """
        #  Must complete at least 10% of episodes (DS)
        min_episodes = max(1, num_episodes // 10)
        nA = len(self.grammars)
        states = []

        # The policy we're following:
        # ucb_policy for fully expanded node and uniform_random_policy for not fully expanded node
        ucb_policy = self.get_ucb_policy(nA)
        reward_his = []
        best_solution = ('C', -100)

        for t in range(1, num_episodes + 1):
            print("\tITER {}/{}...".format(t, num_episodes))
            if t % print_freq == 0 and verbose and len(self.hall_of_fame) >= 1:
                print("\tIteration {}/{}...".format(t, num_episodes))
                print("#QN:", len(self.QN.keys()))
                self.print_hofs()
                sys.stdout.flush()
                print([x[1] for x in self.hall_of_fame], reward_threhold)

            if not is_first_round:
                state = 'f->B'
                ntn = ['B']
            else:
                state = 'f->A'
                ntn = ['A']
            unvisited_children = self.get_unvisited_children(state, ntn[0])

            # scenario 1: if current parent node fully expanded, follow ucb_policy
            while not unvisited_children:
                prob = ucb_policy(state, ntn[0])
                print("UCB_policy... prob=", prob)
                # derive the range directly from the length of prob itself 
                # so the sample space always matches the array that was actually returned (DS)
                action = np.random.choice(len(prob), p=prob / np.sum(prob))
                print('state:', state, '\t action:', self.grammars[action])
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn[1:])
                if state not in states:
                    states.append(state)

                if not done:
                    state = next_state
                    ntn = ntn_next
                    unvisited_children = self.get_unvisited_children(state, ntn[0])

                    if state.count(',') >= self.max_len:
                        unvisited_children = []
                        self.back_propagate(state, action, 0)
                        reward_his.append(best_solution[1])
                        break
                else:
                    unvisited_children = []
                    if np.isfinite(reward) and reward > best_solution[1]:
                        self.update_hall_of_fame(next_state, reward, eq)
                        if reward > 0:
                            self.update_QN_scale(reward)
                        best_solution = (eq, reward)
                    # print("BACK-PROPAGATION STEP")
                    self.back_propagate(state, action, reward)
                    reward_his.append(best_solution[1])
                    break

            # scenario 2: if current parent node not fully expanded, follow uniform_random_policy
            if len(unvisited_children) != 0:
                print("uniform_random_policy... ", unvisited_children)
                # prob = uniform_random_policy(unvisited_children)
                action = np.random.choice(unvisited_children)
                next_state, ntn_next, reward, done, eq = self.step(state, action, ntn[1:])
                print('state:', state, '\t action:', self.grammars[action])
                if not done:
                    reward, eq = self.rollout(num_rollouts, next_state, ntn_next)
                    if state not in states:
                        states.append(state)
                if np.isfinite(reward) and reward > best_solution[1]:
                    self.update_hall_of_fame(next_state, reward, eq)
                    if reward > 0:
                        self.update_QN_scale(reward)
                    best_solution = (eq, reward)
                # 4. BACK-PROPAGATION STEP in MCTS.
                self.back_propagate(state, action, reward)
                reward_his.append(best_solution[1])
                unvisited_children.remove(action)
                # Inner exit: only allow early exit after min_episodes is reached (DS)
                if (len(self.hall_of_fame) > 1
                        and max([x[1] for x in self.hall_of_fame]) > reward_threhold
                        and t >= min_episodes):
                    print(f">>> Early exit (inner) at iteration {t} — reward threshold met.")
                    break

            # Outer exit: same guard, prevents exit on iteration 1 (DS)
            if (len(self.hall_of_fame) > 1
                    and max([x[1] for x in self.hall_of_fame]) > reward_threhold
                    and t >= min_episodes):
                print(f">>> Early exit (outer) at iteration {t} — reward threshold met.")
                break
            
            # LLM rule suggestion logic (DS)
            # Trigger if the model reached the interval OR if it found a new HOF entry 
            # and we have at least one example to show the LLM.
            best_current_reward = max([x[1] for x in self.hall_of_fame]) if self.hall_of_fame else -100
            iterations_since_last = t - self.last_suggest_iter

            # Only consider stuck if improvement is less than threshold — avoids noise triggering a call
            is_stuck = (best_current_reward <= self.last_best_reward_at_suggest + self.stuck_improvement_threshold)
            interval_elapsed = (iterations_since_last >= self.suggest_interval)
            
            has_min_gap = (iterations_since_last >= self.min_gap)
            has_good_context = (best_current_reward > self.min_reward_for_llm)

            # Stuck relative to last call — same as before
            should_suggest = interval_elapsed and is_stuck

            # HOF improved but we haven't called recently — same as before  
            should_suggest_early = self.hof_improved and has_min_gap and is_stuck

            # NEW: interval elapsed regardless of stuck status — catches post-improvement plateaus
            should_suggest_periodic = interval_elapsed

            if (should_suggest or should_suggest_early or should_suggest_periodic) and has_good_context:
                print(f"\n>>> [MCTS-LLM] MCTS is stuck at reward {best_current_reward:.4f}. Querying LLM at iteration {t}...")

                # 1. Extract the top 5 most successful expressions found so far as context
                best_expr_examples = [item[2] for item in self.hall_of_fame[-5:]]

                # 2. Define the operator set (fallback to standard ops if task doesn't specify)
                # This ensures the LLM doesn't suggest 'tan' if the solver only supports 'sin'
                allowed_ops = {'+', '-', '*', '/', 'sin', 'cos', 'exp', 'log', '**'}
                if hasattr(self.task, 'get_allowed_operators'):
                    allowed_ops = set(self.task.get_allowed_operators())

                # 3. Retrieve vars_range so suggest_rules can filter domain-unsafe rules
                # e.g. reject log(A) if any variable range includes negative numbers
                vars_range = None
                if hasattr(self.task, 'data_query_oracle'):
                    try:
                        raw = self.task.data_query_oracle.get_vars_range_and_types()
                        if isinstance(raw, str):
                            vars_range = json.loads(raw)
                        elif isinstance(raw, list) and raw and not isinstance(raw[0], dict):
                            # Handles char-by-char split — rejoin and parse
                            vars_range = json.loads(''.join(str(c) for c in raw))
                        else:
                            vars_range = raw
                    except Exception:
                        vars_range = None
                
                # Debug print temporarily just before the suggest_rules call:
                print(f">>> [DEBUG] vars_range retrieved: {vars_range}")

                # 4. Call the external suggestion pipeline
                # This handles prompt building, API call, safety validation and domain filtering
                new_rules, rejected = suggest_rules(
                    equation_name=getattr(self.task, 'name', 'SymbolicDiscovery'),
                    current_rules=self.grammars,
                    best_expressions=best_expr_examples,
                    nvars=self.nvars,
                    operators_set=allowed_ops,
                    vars_range=vars_range,
                    log_path=self.suggest_log_path
                )

                # Hard whitelist filter — reject any rule using an operator the task
                # did not declare in its function_set, regardless of what the LLM suggeste
                task_function_set = set(getattr(self.task, 'function_set', []))
                all_possible_ops  = {'sin', 'cos', 'exp', 'log', 'sqrt', 'tan'}
                
                # Only apply the filter if the task declared a non-empty function_set.
                # An empty set is ambiguous — it could mean "not configured" rather than
                # "everything is forbidden". Skipping the filter in that case prevents
                # silently rejecting every transcendental rule the LLM suggests.
                if task_function_set:
                    forbidden_ops = all_possible_ops - task_function_set  # ops NOT in function_set

                    if forbidden_ops and new_rules:
                        safe_rules = []
                        for rule in new_rules:
                            # word-boundary regex so 'exp' only matches the actual
                            # function call 'exp(' and not substrings inside other tokens.
                            blocked_by = [
                                op for op in forbidden_ops
                                if re.search(rf'\b{op}\b', rule)
                            ]
                            if blocked_by:
                                print(f">>> [MCTS-LLM] Rejected rule {rule!r} — uses forbidden op(s): {blocked_by}")
                                rejected.append(rule)
                            else:
                                safe_rules.append(rule)
                        new_rules = safe_rules

                # 5. Integrate the new rules into the MCTS search space
                if new_rules:
                    added_count = 0
                    for rule in new_rules:
                        if rule not in self.grammars:
                            self.grammars.append(rule)
                            added_count += 1

                    if added_count > 0:
                        print(f">>> [MCTS-LLM] Successfully expanded grammar with {added_count} new rules.")
                        # IMPORTANT: Since self.grammars grew, we must refresh the policy
                        # so it can choose from the new indices in future iterations.
                        nA = len(self.grammars)
                        for state_key in self.UCBs:
                            old = self.UCBs[state_key]
                            if len(old) < nA:
                                # Pad with zeros for the new rule indices
                                self.UCBs[state_key] = np.pad(old, (0, nA - len(old)))

                        # Refresh the policy so it knows about the new indices
                        ucb_policy = self.get_ucb_policy(nA)

                # 6. Reset triggers to prevent redundant API calls
                self.last_suggest_iter = t
                self.last_best_reward_at_suggest = best_current_reward
                self.hof_improved = False

        return reward_his, self.hall_of_fame

    # Simplified (DS)
    def print_hofs(self, reset_vf=False, verbose=False):
        self.task.rand_draw_data_with_X_fixed()
        print(f"PRINT HOF (free variables={self.task.fixed_column})")
        print("=" * 20)
        for pr in self.hall_of_fame:
            print('        ' + str(get_state(pr)), end="\n")
        print("=" * 20)

def get_state(pr):
    state_dict = {
        'reward': pr[1],
        'pretty-eq': pretty_print_expr(pr[2]),
        'rules': pr[0],
    }
    return state_dict