"""Class for symbolic expression object or program."""
import copy
import sys
import hashlib

import numpy as np
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
np.set_printoptions(precision=4, linewidth=np.inf)

if hasattr(sys, "set_int_max_str_digits"):
    try:
        sys.set_int_max_str_digits(100000)
    except Exception:
        pass

from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify

from scipy.optimize import minimize
from scipy.optimize import basinhopping, shgo, dual_annealing


def _is_pathological_expr_string(expr_str: str) -> bool:
    if not expr_str:
        return True
    if len(expr_str) > 350:
        return True
    if expr_str.count("exp(") > 2:
        return True
    if expr_str.count("**") > 4:
        return True
    if expr_str.count("/") > 4:
        return True
    if any(tok in expr_str for tok in ["zoo", "oo", "nan"]):
        return True
    return False

def _make_eval_safe_expr(expr_str: str) -> str:
    """
    Return a numerically safer copy of expr_str for evaluation only.
    IMPORTANT: never store or print this version as the discovered equation.
    """
    if not expr_str:
        return expr_str

    s = expr_str

    # Guard common removable-singularity denominators only in the
    # temporary evaluation string. Keep the original symbolic form unchanged.
    s = s.replace("(X1-X0)", "((X1-X0)+1e-8)")
    s = s.replace("(X0-X1)", "((X0-X1)+1e-8)")

    return s

def _stable_reward(loss_value: float, tree_size: int, eta: float) -> float:
    if not np.isfinite(loss_value):
        return -np.inf
    loss_value = max(float(loss_value), 0.0)
    return (eta ** tree_size) * (1.0 / (1.0 + loss_value))


def _guard_difference_denominators(expr_str: str) -> str:
    # Cheap textual guard for common removable-singularity denominators.
    expr_str = expr_str.replace("(X1-X0)", "((X1-X0)+1e-8)")
    expr_str = expr_str.replace("(X0-X1)", "((X0-X1)+1e-8)")
    return expr_str


class Program(object):
    expr_obj_thres = 1e-6
    expr_consts_thres = 1e-3
    evalaute_loss = None

    def __init__(self, n_vars, optimizer="BFGS"):
        self.vf = [0, ] * n_vars
        self.n_vars = n_vars
        self.optimizer = optimizer
        self.optimized_constants = []
        self.optimized_obj = []
        self.cache = {}

    def set_vf(self, xi: int):
        if 0 <= xi < len(self.vf):
            self.vf[xi] = 1
            print('xi is:', xi, ', new vf is:', self.vf)

    def get_vf(self):
        return self.vf

    def clear_cache(self):
        self.cache = {}

    def optimize(self, eq, tree_size: int, data_X, y_true, input_var_Xs, eta=0.9999, max_opt_iter=1000, verbose=False):
        eq = simplify_template(eq)
        if 'A' in eq or 'B' in eq:  # not a valid equation
            return -np.inf, eq, 0, 0
        if _is_pathological_expr_string(eq):
            return -np.inf, eq, 0, np.inf

        # Keep a clean symbolic template for storage / display.
        eq_clean = eq

        has_shared_k = 'K' in eq_clean
        eq_work = eq_clean.replace('K', 'k_shared')
        num_changing_consts = eq_work.count('C')
        n_params = num_changing_consts + (1 if has_shared_k else 0)
        t_optimized_constants, t_optimized_obj = 0, np.inf

        if n_params == 0:  # zero constant
            y_pred = execute(eq_clean, data_X.T, input_var_Xs)
            var_ytrue = np.var(y_true)
            loss_value = -self.evalaute_loss(y_pred, y_true, var_ytrue)
        elif n_params >= 20:  # discourage over complicated numerical estimations
            return -np.inf, eq_clean, t_optimized_constants, t_optimized_obj
        else:
            c_lst = ['c' + str(i) for i in range(num_changing_consts)]
            for c in c_lst:
                eq_work = eq_work.replace('C', c, 1)

            def f(consts: list):
                eq_est = eq_work
                idx = 0
                if has_shared_k:
                    eq_est = eq_est.replace('k_shared', str(consts[idx]))
                    idx += 1
                for i in range(num_changing_consts):
                    eq_est = eq_est.replace('c' + str(i), str(consts[idx]), 1)
                    idx += 1

                eq_est = eq_est.replace('+ -', '-')
                eq_est = eq_est.replace('- -', '+')
                eq_est = eq_est.replace('- +', '-')
                eq_est = eq_est.replace('+ +', '+')

                if _is_pathological_expr_string(eq_est):
                    return 1e12

                y_pred = execute(eq_est, data_X.T, input_var_Xs)
                var_ytrue = np.var(y_true)
                if not np.all(np.isfinite(y_pred)):
                    return 1e12

                pred_std = np.std(y_pred)
                true_std = np.std(y_true)
                if pred_std < 1e-10:
                    return 1e9
                if pred_std / (true_std + 1e-12) < 1e-4:
                    return 1e7

                val = -self.evalaute_loss(y_pred, y_true, var_ytrue)
                if not np.isfinite(val):
                    return 1e12
                return val

            try:
                opt_result = None
                has_exp = 'exp(' in eq_work
                has_div = '/' in eq_work

                local_max_opt_iter = max_opt_iter
                if has_exp and has_div:
                    local_max_opt_iter = min(local_max_opt_iter, 20)

                def _constant_bounds(scale=10.0):
                    lw = [-scale] * n_params
                    up = [scale] * n_params
                    return list(zip(lw, up))

                def _initial_guesses():
                    n = n_params

                    if has_exp:
                        prioritized_scales = [-500.0, -300.0, -100.0, -10.0, -1.0, 0.0, 1.0, 10.0]
                    else:
                        prioritized_scales = [-10.0, -1.0, 0.0, 1.0, 10.0]

                    guesses = [np.full(n, s) for s in prioritized_scales]

                    rng = np.random.default_rng(0)
                    random_scales = [1.0, 10.0] + ([100.0] if has_exp else [])
                    for s in random_scales:
                        guesses.append(rng.normal(loc=0.0, scale=s, size=n))

                    uniq = []
                    seen = set()
                    for g in guesses:
                        key = tuple(np.round(g, 12).tolist())
                        if key in seen:
                            continue
                        seen.add(key)
                        uniq.append(g)

                    if n_params <= 2 and has_exp and has_div:
                        max_starts = 3
                    elif n_params <= 2 and has_exp:
                        max_starts = 6
                    elif n_params <= 2:
                        max_starts = 4
                    else:
                        max_starts = 3

                    return uniq[:max_starts]

                def _run_optimizer_once(x0):
                    if self.optimizer == 'Nelder-Mead':
                        return minimize(f, x0, method='Nelder-Mead',
                                        options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': local_max_opt_iter})
                    if self.optimizer == 'BFGS':
                        return minimize(f, x0, method='BFGS', options={'maxiter': local_max_opt_iter})
                    if self.optimizer == 'CG':
                        return minimize(f, x0, method='CG', options={'maxiter': local_max_opt_iter})
                    if self.optimizer == 'L-BFGS-B':
                        return minimize(f, x0, method='L-BFGS-B', options={'maxiter': local_max_opt_iter})
                    if self.optimizer == "basinhopping":
                        minimizer_kwargs = {"method": "Nelder-Mead",
                                            "options": {'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 100}}
                        return basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=local_max_opt_iter)
                    if self.optimizer == 'dual_annealing':
                        minimizer_kwargs = {"method": "Nelder-Mead",
                                            "options": {'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 100}}
                        bound_scale = 1000.0 if has_exp else 10.0
                        bounds = _constant_bounds(scale=bound_scale)
                        return dual_annealing(f, bounds, minimizer_kwargs=minimizer_kwargs, maxiter=local_max_opt_iter)
                    if self.optimizer == 'shgo':
                        minimizer_kwargs = {"method": "Nelder-Mead",
                                            "options": {'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 100}}
                        bound_scale = 1000.0 if has_exp else 10.0
                        bounds = _constant_bounds(scale=bound_scale)
                        return shgo(f, bounds, minimizer_kwargs=minimizer_kwargs, options={'maxiter': local_max_opt_iter})
                    return None

                global_optimizers = {'basinhopping', 'dual_annealing', 'shgo'}
                starts = _initial_guesses()
                if self.optimizer in global_optimizers:
                    starts = starts[:1]

                for x0 in starts:
                    cur = _run_optimizer_once(x0)
                    if cur is None:
                        continue
                    if not np.isfinite(cur['fun']):
                        continue
                    if opt_result is None or cur['fun'] < opt_result['fun']:
                        opt_result = cur

                if opt_result is None:
                    return -np.inf, eq_clean, 0, np.inf

                t_optimized_constants = opt_result['x']
                c_vals = t_optimized_constants.tolist()
                t_optimized_obj = opt_result['fun']

                if verbose:
                    print(opt_result)

                eq_est = eq_work
                idx = 0
                if has_shared_k:
                    est_k = float(c_vals[idx])
                    if abs(est_k) < 1e-5:
                        est_k = 0.0
                    eq_est = eq_est.replace('k_shared', str(est_k))
                    idx += 1

                for i in range(num_changing_consts):
                    est_c = float(c_vals[idx])
                    if abs(est_c) < 1e-5:
                        est_c = 0.0
                    eq_est = eq_est.replace('c' + str(i), str(est_c), 1)
                    idx += 1

                eq_est = eq_est.replace('+ -', '-')
                eq_est = eq_est.replace('- -', '+')
                eq_est = eq_est.replace('- +', '-')
                eq_est = eq_est.replace('+ +', '+')

                # Keep this clean version as the discovered expression.
                eq_clean = eq_est

                y_pred = execute(eq_clean, data_X.T, input_var_Xs)
                var_ytrue = np.var(y_true)
                loss_value = -self.evalaute_loss(y_pred, y_true, var_ytrue)
                
                loss_value = float(loss_value)
                t_optimized_obj = float(t_optimized_obj) if np.isfinite(t_optimized_obj) else t_optimized_obj
                eq = eq_clean

                print('\t reward', 1 / (1 + loss_value) * eta ** tree_size, '\t loss:', loss_value, 'simp:', eq)
            except Exception as e:
                print(e)
                return -np.inf, eq_clean, 0, np.inf

        r = float(1 / (1 + loss_value) * eta ** tree_size)
        return r, eq, t_optimized_constants, t_optimized_obj


def execute(expr_str: str, data_X: np.ndarray, input_var_Xs):
    if _is_pathological_expr_string(expr_str):
        return np.ones(data_X.shape[-1]) * np.inf

    # Use a guarded copy only for numeric evaluation.
    expr_eval = _make_eval_safe_expr(expr_str)

    used_vars, used_idx = [], []
    for idx, xi in enumerate(input_var_Xs):
        if str(xi) in expr_eval:
            used_idx.append(idx)
            used_vars.append(xi)

    try:
        expr = parse_expr(expr_eval)
        f = lambdify(used_vars, expr, 'numpy')
        if len(used_idx) != 0:
            y_hat = f(*[data_X[i] for i in used_idx])
        else:
            y_hat = float(expr)
        if y_hat is complex:
            return np.ones(data_X.shape[-1]) * np.inf
    except TypeError:
        y_hat = np.ones(data_X.shape[-1]) * np.inf
    except KeyError:
        y_hat = np.ones(data_X.shape[-1]) * np.inf
    except Exception:
        y_hat = np.ones(data_X.shape[-1]) * np.inf

    y_hat = np.asarray(y_hat, dtype=float)
    y_hat = np.nan_to_num(y_hat, nan=np.inf, posinf=np.inf, neginf=-np.inf)
    y_hat = np.clip(y_hat, -1e6, 1e6)
    return y_hat


def execute_eval(expr_str: str, data_X: np.ndarray, input_var_Xs, simulated_steps: int, dt: float):
    try:
        y_hat = eval(expr_str)
    except TypeError as e:
        print(e)
    return y_hat


def simplify_template(eq):
    orig = eq
    for i in range(10):
        eq = eq.replace('(C+C)', 'C')
        eq = eq.replace('sqrt(C)', 'C')
        eq = eq.replace('sin(C)', 'C')
        eq = eq.replace('cos(C)', 'C')
        eq = eq.replace('(1/C)', 'C')
        eq = eq.replace('(C-C)', 'C')
        eq = eq.replace('C*C', 'C')
        eq = eq.replace('(C/C)', 'C')
    return eq


if __name__ == '__main__':
    expr_temp = 'sqrt(sqrt(C))*(sqrt(X0)+C)'
    simplify_template(expr_temp)