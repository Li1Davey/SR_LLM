import copy
import sys
import numpy as np
from collections import defaultdict
from sympy import Symbol, Pow
from sympy.parsing.sympy_parser import parse_expr
from production_rules import production_rules_to_expr
from program import execute
from utils import pretty_print_expr, expression_to_template, nth_repl
import json
import re
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
                 exploration_rate=1 / np.sqrt(2), eta=0.999, max_opt_iter=500, suggest_log_path="llm_rule_history.log",
                 num_episodes=1000):
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
        # Separate audit log — top expressions seen, length-constrained (DS)
        self.top_expressions = []
        self.exploration_rate = exploration_rate
        # FIXED - size is re-evaluated dynamically every time a new key is created (DS)
        self.UCBs = defaultdict(self._make_ucb_entry)
        self.QN = defaultdict(lambda: np.zeros(2))
        self.scale = 0
        self.eta = eta
        self.max_opt_iter = max_opt_iter
        # LLM timer and audit config (DS)
        self.last_suggest_iter = 0
        self.suggest_interval = max(1, num_episodes // 10)
        self.suggest_log_path = suggest_log_path
        # Consecutive empty LLM call counter — used to skip stale calls (DS)
        self.consecutive_empty_llm_calls = 0

    # (DS)
    def _make_ucb_entry(self):
        """
        Dynamically creates a zero array sized to the CURRENT grammar length.
        Critical because the LLM can expand self.grammars mid-run.
        """
        return np.zeros(len(self.grammars))

    # (DS)
    def _count_new_nonterminals(self, rule):
        """Count how many new A nodes a rule introduces on its RHS."""
        rhs = rule.split('->', 1)[1]
        return rhs.count('A')

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
        One step of Parse Tree traversal.
        Returns: (next_state, ntn, reward, done, eq)
        """
        action = self.grammars[action_idx]
        state = state + ',' + action
        ntn = self.get_non_terminal_nodes(action) + ntn

        if not ntn:
            self.task.rand_draw_data_with_X_fixed()
            y_true = self.task.evaluate()
            expr_template = production_rules_to_expr(state.split(','))

            try:
                # Guard 1: reject oversized template strings (DS)
                if not isinstance(expr_template, str) or len(expr_template) > 200:
                    print(f"         [step] Expression string too long "
                          f"({len(expr_template) if isinstance(expr_template, str) else type(expr_template)} chars) — skipping")
                    return state, ntn, -999.0, True, expr_template

                # Guard 2: reject chained power towers (DS)
                if re.search(r'\*\*\d+\*\*\d+', expr_template):
                    print(f"         [step] Chained power tower detected — skipping: {expr_template[:80]}")
                    return state, ntn, -999.0, True, expr_template

                # Guard 3: reject states with too many production rules (DS)
                num_rules = len(state.split(','))
                if num_rules > 20:
                    print(f"         [step] Too many production rules ({num_rules}) — skipping: {expr_template[:80]}")
                    return state, ntn, -999.0, True, expr_template

                test_expr = parse_expr(expr_template.replace('C', '1'))

                # Guard 4: reject astronomically large integer exponents (DS)
                max_exp = max(
                    (abs(int(a.exp)) for a in test_expr.atoms(Pow) if a.exp.is_Integer),
                    default=0
                )
                if max_exp > 20:
                    print(f"         [step] Exponent too large ({max_exp}) — skipping: {expr_template[:80]}")
                    return state, ntn, -999.0, True, expr_template

                # Guard 5: reject expressions with no free variables (DS)
                if not test_expr.free_symbols:
                    print(f"         [step] Expression has no free variables — skipping: {expr_template[:80]}")
                    return state, ntn, -999.0, True, expr_template

            except Exception as e:
                print(f"         [step] Guard check failed ({type(e).__name__}: {e}) — skipping: "
                      f"{str(expr_template)[:80]}")
                return state, ntn, -999.0, True, expr_template

            reward, eq, _, _ = self.program.optimize(expr_template,
                                                      len(state.split(',')),
                                                      self.task.X,
                                                      y_true,
                                                      self.input_var_Xs,
                                                      eta=self.eta,
                                                      max_opt_iter=self.max_opt_iter)

            if not np.isfinite(reward):
                print(f"         [step] Non-finite reward ({reward}) replaced with -999.0 for: {eq}")
                reward = -999.0

            return state, ntn, reward, True, eq
        else:
            return state, ntn, 0, False, None

    def rollout(self, num_play, state_initial, ntn_initial):
        """Perform num_play simulations, return maximum reward."""
        # Note: reward, next_state, and eq are intentionally not initialized here.
        # as they were already assigned inside the loop (DS)
        best_eq = ''
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
        """Creates a policy based on UCB scores."""
        # Pre-compute which grammar indices are terminal (RHS contains no 'A')
        # so we don't recompute this inside the hot loop. (DS)
        terminal_indices = frozenset(
            i for i, rule in enumerate(self.grammars)
            if 'A' not in rule.split('->', 1)[1]
        )
        TERMINAL_PENALTY = 0.5

        def policy_fn(state, node):
            valid_action = self.valid_production_rules(node)

            ucb_scores = []
            for a in valid_action:
                score = np.exp(self.UCBs[state][a])
                if a in terminal_indices:
                    # discount terminal rules (DS)
                    score *= TERMINAL_PENALTY
                ucb_scores.append(score)

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
            best_action  = valid_action[np.argmax(policy_valid)]
            A[best_action] += 0.8
            A[valid_action] += float(0.2 / len(valid_action))
            return A

        return policy_fn

    def update_hall_of_fame(self, state, reward, eq):
        """
        Update HOF and top_expressions audit log.
        Both lists enforce the module length constraint so the LLM
        only ever sees compact, structurally meaningful expressions.
        """
        # Reject trivially zero or constant-only expressions — these have
        # reward 0.0 by coincidence (optimizer found best fit is zero) but
        # contribute nothing useful to the HOF or LLM context. (DS)
        if eq is None:
            return
        try:
            if parse_expr(str(eq)).is_number:
                return
        except Exception:
            pass

        module = state
        if state.count(',') <= self.max_module:
            if not self.hall_of_fame:
                self.hall_of_fame = [(module, reward, eq)]
            elif eq not in [x[2] for x in self.hall_of_fame]:
                if len(self.hall_of_fame) < self.max_aug:
                    self.hall_of_fame = sorted(
                        self.hall_of_fame + [(module, reward, eq)],
                        key=lambda x: x[1]
                    )
                else:
                    if reward > self.hall_of_fame[0][1]:
                        self.hall_of_fame = sorted(
                            self.hall_of_fame[1:] + [(module, reward, eq)],
                            key=lambda x: x[1]
                        )

            # --- Update top_expressions audit log ---
            # Same module length constraint as HOF — guarantees compact expressions
            # so the audit log and LLM context stay clean (DS)
            if eq not in [x[2] for x in self.top_expressions]:
                if len(self.top_expressions) < 20:
                    self.top_expressions = sorted(
                        self.top_expressions + [(module, reward, eq)],
                        key=lambda x: x[1]
                    )
                else:
                    if reward > self.top_expressions[0][1]:
                        self.top_expressions = sorted(
                            self.top_expressions[1:] + [(module, reward, eq)],
                            key=lambda x: x[1]
                        )

    def MCTS_run_orig(self, num_episodes, num_rollouts=50, verbose=False, print_freq=5,
                      is_first_round=False, reward_threhold=10):
        """Monte Carlo Tree Search algorithm."""
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

            # Scenario 1: fully expanded node — follow UCB policy
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
                    self.back_propagate(state, action, reward)
                    reward_his.append(best_solution[1])
                    break

            # Scenario 2: not fully expanded — follow uniform random policy
            if len(unvisited_children) != 0:
                print("uniform_random_policy... ", unvisited_children)
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
            # Single trigger: fire every suggest_interval episodes if the HOF
            # has at least one expression to show the LLM.
            # min_reward_for_llm — all redundant once we use a simple periodic trigger.
            iterations_since_last = t - self.last_suggest_iter
            has_context = len(self.hall_of_fame) > 0
            interval_elapsed = (iterations_since_last >= self.suggest_interval)

            if interval_elapsed and has_context:
                best_current_reward = max(x[1] for x in self.hall_of_fame)

                if best_current_reward >= reward_threhold:
                    print(f">>> [MCTS-LLM] Skipping LLM call — reward threshold already met "
                          f"({best_current_reward:.4f} >= {reward_threhold}).")
                    self.last_suggest_iter = t
                    continue

                # Skip if the last N calls all returned nothing — grammar is saturated
                # for the current expression landscape. Reset after one skip to retry. (DS)
                if self.consecutive_empty_llm_calls >= 2:
                    print(f">>> [MCTS-LLM] Skipping LLM call — "
                          f"{self.consecutive_empty_llm_calls} consecutive empty responses, "
                          f"grammar may be saturated. Will retry next interval.")
                    self.last_suggest_iter = t
                    self.consecutive_empty_llm_calls = 0
                    continue

                print(f"\n>>> [MCTS-LLM] Querying LLM at iteration {t} "
                      f"(best reward so far: {best_current_reward:.4f})...")

                # 1. Top 20 best expressions as LLM context — sorted descending by reward
                #    so the best are first. HOF enforces max_module so all are compact. (DS)
                best_expr_examples = [
                    item[2] for item in sorted(
                        self.top_expressions, key=lambda x: x[1], reverse=True
                    )
                ]

                # 2. Operator set
                allowed_ops = {'+', '-', '*', '/', 'sin', 'cos', 'exp', 'log', '**'}
                if hasattr(self.task, 'get_allowed_operators'):
                    allowed_ops = set(self.task.get_allowed_operators())

                # 3. Variable ranges
                vars_range = None
                if hasattr(self.task, 'data_query_oracle'):
                    try:
                        raw = self.task.data_query_oracle.get_vars_range_and_types()
                        if isinstance(raw, str):
                            vars_range = json.loads(raw)
                        elif isinstance(raw, list) and raw and not isinstance(raw[0], dict):
                            vars_range = json.loads(''.join(str(c) for c in raw))
                        else:
                            vars_range = raw
                    except Exception:
                        vars_range = None

                print(f">>> [DEBUG] vars_range retrieved: {vars_range}")

                # 4. Call the suggestion pipeline
                new_rules, rejected = suggest_rules(
                    equation_name=getattr(self.task, 'name', 'SymbolicDiscovery'),
                    current_rules=self.grammars,
                    best_expressions=best_expr_examples,
                    nvars=self.nvars,
                    operators_set=allowed_ops,
                    vars_range=vars_range,
                    base_rules=self.base_grammars,
                    log_path=self.suggest_log_path
                )

                # Update consecutive empty call counter (DS)
                if not new_rules:
                    self.consecutive_empty_llm_calls += 1
                else:
                    self.consecutive_empty_llm_calls = 0

                # 5. Hard whitelist — strip rules using undeclared operators
                task_function_set = set(getattr(self.task, 'function_set', []))
                all_possible_ops  = {'sin', 'cos', 'exp', 'log', 'sqrt', 'tan'}

                if task_function_set:
                    forbidden_ops = all_possible_ops - task_function_set
                    if forbidden_ops and new_rules:
                        safe_rules = []
                        for rule in new_rules:
                            blocked_by = [
                                op for op in forbidden_ops
                                if re.search(rf'\b{op}\b', rule)
                            ]
                            if blocked_by:
                                print(f">>> [MCTS-LLM] Rejected rule {rule!r} "
                                      f"— uses forbidden op(s): {blocked_by}")
                                rejected.append(rule)
                            else:
                                safe_rules.append(rule)
                        new_rules = safe_rules

                # 6. Integrate new rules — final duplicate guard here as safety net (DS)
                if new_rules:
                    added_count = 0
                    for rule in new_rules:
                        if rule not in self.grammars:
                            new_nts = self._count_new_nonterminals(rule)
                            if new_nts > 3:
                                print(f">>> [MCTS-LLM] Rejected rule {rule!r} "
                                      f"— introduces {new_nts} non-terminals (max 3)")
                                continue
                            self.grammars.append(rule)
                            added_count += 1
                        else:
                            print(f">>> [MCTS-LLM] Rule already in grammar, skipping: {rule!r}")

                    if added_count > 0:
                        print(f">>> [MCTS-LLM] Expanded grammar with {added_count} new rules.")
                        nA = len(self.grammars)
                        for state_key in self.UCBs:
                            old = self.UCBs[state_key]
                            if len(old) < nA:
                                self.UCBs[state_key] = np.pad(old, (0, nA - len(old)))
                        ucb_policy = self.get_ucb_policy(nA)

                # 7. Reset timer
                self.last_suggest_iter = t

        return reward_his, self.hall_of_fame

    # Simplified (DS)
    def print_hofs(self, reset_vf=False, verbose=False):
        self.task.rand_draw_data_with_X_fixed()
        print(f"PRINT HOF (free variables={self.task.fixed_column})")
        print("=" * 20)
        for pr in self.hall_of_fame:
            print('        ' + str(get_state(pr)), end="\n")
        print("=" * 20)

# Simplified (DS)
def get_state(pr):
    return {
        'reward':    pr[1],
        'pretty-eq': pretty_print_expr(pr[2]),
        'rules':     pr[0],
    }
