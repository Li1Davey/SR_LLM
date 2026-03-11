"""Class for symbolic expression object or program."""
import copy
import sys

import numpy as np
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
np.set_printoptions(precision=4, linewidth=np.inf)

# Guard against ValueError: "too many digits in integer" from giant symbolic strings.
if hasattr(sys, "set_int_max_str_digits"):
    try:
        sys.set_int_max_str_digits(100000)
    except Exception:
        pass

from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify

from scipy.optimize import minimize
from scipy.optimize import basinhopping, shgo, dual_annealing

from utils import pretty_print_expr


def _is_pathological_expr_string(expr_str: str) -> bool:
    if not expr_str:
        return True
    # Hard caps to keep symbolic parsing/evaluation bounded.
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


class Program(object):
    # Static variables
    expr_obj_thres = 1e-6  # expression objective threshold
    expr_consts_thres = 1e-3
    evalaute_loss = None

    def __init__(self, n_vars, optimizer="BFGS"):
        """
        opt_num_expr:  # number of experiments done for optimization
        vf: indicator vector for free variables. vf[i]=1 for xi is a free variable
        """
        self.vf = [0, ] * n_vars

        self.n_vars = n_vars
        self.optimizer = optimizer

        self.optimized_constants = []
        self.optimized_obj = []
        self.cache = {}

    def set_vf(self, xi: int):
        """set of free variables"""

        if 0 <= xi < len(self.vf):
            self.vf[xi] = 1
            print('xi is:', xi, ', new vf is:', self.vf)

    def get_vf(self):
        return self.vf

    def optimize(self, eq, tree_size: int, data_X, y_true, input_var_Xs, eta=0.9999, max_opt_iter=1000, verbose=False):
        """
        Calculate reward score for a complete parse tree
        If placeholder C is in the equation, also execute estimation for C
        Reward = 1 / (1 + MSE) * Penalty ** num_term

        Parameters
        ----------
        eq : Str object. the discovered equation (with placeholders for coefficients).
        tree_size: number of production rules in the complete parse tree.
        (data_X, y_true) : 2-d numpy array.

        Returns
        -------
        score: discovered equations.
        eq: discovered equations with estimated numerical values.
        """
        eq = simplify_template(eq)
        if 'A' in eq or 'B' in eq:  # not a valid equation
            return -np.inf, eq, 0, 0
        if _is_pathological_expr_string(eq):
            return -np.inf, eq, 0, np.inf
        # count number of constants in equation
        # C: untied placeholders (each occurrence can take different value)
        # K: tied/shared placeholder (all occurrences share one value)
        has_shared_k = 'K' in eq
        eq = eq.replace('K', 'k_shared')
        num_changing_consts = eq.count('C')
        n_params = num_changing_consts + (1 if has_shared_k else 0)
        t_optimized_constants, t_optimized_obj = 0, np.inf
        if n_params == 0:  # zero constant
            y_pred = execute(eq, data_X.T, input_var_Xs)
            var_ytrue = np.var(y_true)
        elif n_params >= 20:  # discourage over complicated numerical estimations
            return -np.inf, eq, t_optimized_constants, t_optimized_obj
        else:
            c_lst = ['c' + str(i) for i in range(num_changing_consts)]
            for c in c_lst:
                eq = eq.replace('C', c, 1)

            def _constant_bounds(scale=10.0):
                lw = [-scale] * n_params
                up = [scale] * n_params
                return list(zip(lw, up))

            def _initial_guesses():
                """
                Build deterministic multi-start seeds for constant optimization.

                Important: for stiff exponentials we must keep large-magnitude
                starts in the *selected* subset (e.g. -100, -500), otherwise
                local optimizers often collapse to near-constant surrogates.
                """
                n = n_params
                has_exp = 'exp(' in eq

                if has_exp:
                    # Prioritize large negative starts first so caps still include them.
                    prioritized_scales = [-500.0, -300.0, -100.0, -10.0, -1.0, 0.0, 1.0, 10.0]
                else:
                    prioritized_scales = [-10.0, -1.0, 0.0, 1.0, 10.0]

                guesses = [np.full(n, s) for s in prioritized_scales]

                # Add light random perturbations around key scales.
                rng = np.random.default_rng(0)
                random_scales = [1.0, 10.0] + ([100.0] if has_exp else [])
                for s in random_scales:
                    guesses.append(rng.normal(loc=0.0, scale=s, size=n))

                # Keep order, drop duplicates.
                uniq = []
                seen = set()
                for g in guesses:
                    key = tuple(np.round(g, 12).tolist())
                    if key in seen:
                        continue
                    seen.add(key)
                    uniq.append(g)

                # Adaptive cap to reduce runtime overhead while still covering
                # stiff exponential scales.
                if n_params <= 2 and has_exp:
                    max_starts = 6
                elif n_params <= 2:
                    max_starts = 4
                else:
                    max_starts = 3

                return uniq[:max_starts]

            def f(consts: list):
                eq_est = eq
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

                # Reject unstable symbolic forms early.
                if _is_pathological_expr_string(eq_est):
                    return 1e12

                y_pred = execute(eq_est, data_X.T, input_var_Xs)
                var_ytrue = np.var(y_true)
                if not np.all(np.isfinite(y_pred)):
                    return 1e12
                val = -self.evalaute_loss(y_pred, y_true, var_ytrue)
                if not np.isfinite(val):
                    return 1e12
                return val

            try:
                opt_result = None
                def _run_optimizer_once(x0):
                    if self.optimizer == 'Nelder-Mead':
                        return minimize(f, x0, method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': max_opt_iter})

                    if self.optimizer == 'BFGS':
                        return minimize(f, x0, method='BFGS', options={'maxiter': max_opt_iter})
                    if self.optimizer == 'CG':
                        return minimize(f, x0, method='CG', options={'maxiter': max_opt_iter})
                    if self.optimizer == 'L-BFGS-B':
                        return minimize(f, x0, method='L-BFGS-B', options={'maxiter': max_opt_iter})
                    if self.optimizer == "basinhopping":
                        minimizer_kwargs = {"method": "Nelder-Mead",
                                            "options": {'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 100}}
                        # basinhopping is already global/meta; run once.
                        return basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=max_opt_iter)
                    if self.optimizer == 'dual_annealing':
                        minimizer_kwargs = {"method": "Nelder-Mead",
                                            "options": {'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 100}}
                        bound_scale = 1000.0 if 'exp(' in eq else 10.0
                        bounds = _constant_bounds(scale=bound_scale)
                        # dual_annealing ignores x0 in this API path; run once.
                        return dual_annealing(f, bounds, minimizer_kwargs=minimizer_kwargs, maxiter=max_opt_iter)
                    if self.optimizer == 'shgo':
                        minimizer_kwargs = {"method": "Nelder-Mead",
                                            "options": {'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 100}}
                        bound_scale = 1000.0 if 'exp(' in eq else 10.0
                        bounds = _constant_bounds(scale=bound_scale)
                        # shgo is global and does not use x0; run once.
                        return shgo(f, bounds, minimizer_kwargs=minimizer_kwargs, options={'maxiter': max_opt_iter})
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
                    return -np.inf, eq, 0, np.inf
                # elif self.optimizer == "direct":
                #     lw = [-10] * num_changing_consts
                #     up = [10] * num_changing_consts
                #     bounds = list(zip(lw, up))
                #     opt_result = direct(f, bounds, maxiter=max_opt_iter)

                t_optimized_constants = opt_result['x']
                c_lst = t_optimized_constants.tolist()
                t_optimized_obj = opt_result['fun']

                if verbose:
                    print(opt_result)
                eq_est = eq

                idx = 0
                if has_shared_k:
                    est_k = np.mean(c_lst[idx])
                    if abs(est_k) < 1e-5:
                        est_k = 0
                    eq_est = eq_est.replace('k_shared', str(est_k))
                    idx += 1

                for i in range(num_changing_consts):
                    est_c = np.mean(c_lst[idx])
                    if abs(est_c) < 1e-5:
                        est_c = 0
                    eq_est = eq_est.replace('c' + str(i), str(est_c), 1)
                    idx += 1
                eq_est = eq_est.replace('+ -', '-')
                eq_est = eq_est.replace('- -', '+')
                eq_est = eq_est.replace('- +', '-')
                eq_est = eq_est.replace('+ +', '+')

                y_pred = execute(eq_est, data_X.T, input_var_Xs)
                var_ytrue = np.var(y_true)

                # Pretty printing can explode on pathological expressions;
                # fallback to raw expression string in that case.
                try:
                    if _is_pathological_expr_string(eq_est):
                        eq = eq_est
                    else:
                        eq = pretty_print_expr(parse_expr(eq_est))
                except Exception:
                    eq = eq_est

                print('\t reward',
                      eta ** tree_size * float(-np.log10(1e-60 - self.evalaute_loss(y_pred, y_true, var_ytrue))),
                      '\t loss:', -self.evalaute_loss(y_pred, y_true, var_ytrue),
                      'simp:', eq)
            except Exception as e:
                print(e)
                return -np.inf, eq, 0, np.inf

        r = eta ** tree_size * float(-np.log10(1e-60 - self.evalaute_loss(y_pred, y_true, var_ytrue)))

        return r, eq, t_optimized_constants, t_optimized_obj


def execute(expr_str: str, data_X: np.ndarray, input_var_Xs):
    """
    evaluate the output of expression with the given input.
    consts: list of constants.
    """
    # Fast fail for obviously invalid or too-complex symbolic payloads.
    if _is_pathological_expr_string(expr_str):
        return np.ones(data_X.shape[-1]) * np.inf

    used_vars, used_idx = [], []
    for idx, xi in enumerate(input_var_Xs):
        if str(xi) in expr_str:
            used_idx.append(idx)
            used_vars.append(xi)
    try:
        expr = parse_expr(expr_str)
        f = lambdify(used_vars, expr, 'numpy')
        if len(used_idx) != 0:
            y_hat = f(*[data_X[i] for i in used_idx])
        else:
            y_hat = float(expr)
        if y_hat is complex:
            return np.ones(data_X.shape[-1]) * np.inf
    except TypeError as e:
        # print(e, expr, input_var_Xs, data_X.shape)
        y_hat = np.ones(data_X.shape[-1]) * np.inf
    except KeyError as e:
        # print(e, expr)
        y_hat = np.ones(data_X.shape[-1]) * np.inf
    except Exception:
        y_hat = np.ones(data_X.shape[-1]) * np.inf

    # ------------------------------
    # Convert scalar or list-like output to numpy array
    y_hat = np.asarray(y_hat, dtype=float)

    # Convert nan, +inf, -inf to controlled values
    y_hat = np.nan_to_num(y_hat, nan=np.inf, posinf=np.inf, neginf=-np.inf)

    # Limit values to avoid exploding during optimization
    y_hat = np.clip(y_hat, -1e6, 1e6)
    # ------------------------------

    return y_hat


def execute_eval(expr_str: str, data_X: np.ndarray, input_var_Xs, simulated_steps: int, dt: float):
    """
    evaluate the output of expression with the given input.
    consts: list of constants.
    """
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