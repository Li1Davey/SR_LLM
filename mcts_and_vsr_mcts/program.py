"""Class for symbolic expression object or program."""
import copy
import re

import numpy as np
import sympy
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
np.set_printoptions(precision=4, linewidth=np.inf)

from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify

from scipy.optimize import minimize
from scipy.optimize import basinhopping, shgo, dual_annealing

from utils import pretty_print_expr


def _safe_pretty_expr(expr_str: str):
    try:
        expr = parse_expr(expr_str, evaluate=False)
        eq_pretty = pretty_print_expr(expr)
        bad_display = {"nan", "zoo", "oo", "-oo", "ComplexInfinity"}

        if eq_pretty in bad_display:
            return expr_str

        raw_has_structure = any(
            tok in expr_str
            for tok in ["X0", "X1", "+", "-", "*", "/", "exp(", "sin(", "cos(", "sqrt("]
        )
        if str(eq_pretty).strip() == "0" and raw_has_structure:
            return expr_str

        return eq_pretty
    except Exception:
        return expr_str


def _is_pathological_expr_string(expr_str: str):
    if not expr_str:
        return True
    if len(expr_str) > 2000:
        return True
    if expr_str.count("**") > 12:
        return True
    if expr_str.count("/") > 12:
        return True
    if any(tok in expr_str for tok in ("zoo", "oo", "nan", "ComplexInfinity")):
        return True
    return False


def _has_bad_denominator(expr_str: str, data_X: np.ndarray, input_var_Xs, eps: float = 1e-8):
    if "/" not in expr_str:
        return False
    try:
        expr = parse_expr(expr_str, evaluate=False)
        _, den = sympy.fraction(sympy.together(expr))
        if den == 1:
            return False
        den_str = str(den)
        used_vars, used_idx = [], []
        for idx, xi in enumerate(input_var_Xs):
            if str(xi) in den_str:
                used_idx.append(idx)
                used_vars.append(xi)
        f_den = lambdify(used_vars, den, "numpy")
        if len(used_idx) != 0:
            den_vals = f_den(*[data_X[i] for i in used_idx])
        else:
            den_vals = float(den)
        den_vals = np.asarray(den_vals, dtype=float)
        den_vals = np.nan_to_num(den_vals, nan=0.0, posinf=0.0, neginf=0.0)
        return np.any(np.abs(den_vals) < eps)
    except Exception:
        return True


DEFAULT_CONST_BOUND = 10.0
EXP_CONST_BOUND = 4.0
DENOM_CONST_BOUND = 5.0
DENOM_MIN_ABS = 1e-2
DEFAULT_MULTI_STARTS = 6
NEAR_CONSTANT_VAR_RATIO = 1e-4
NEAR_CONSTANT_RANGE_RATIO = 1e-3


def _cleanup_expression_text(expr_str: str) -> str:
    expr_str = expr_str.replace('+ -', '-')
    expr_str = expr_str.replace('- -', '+')
    expr_str = expr_str.replace('- +', '-')
    expr_str = expr_str.replace('+ +', '+')
    return expr_str


def _extract_constant_contexts(eq_with_consts: str, num_consts: int):
    contexts = [dict(in_exp=False, in_denominator=False) for _ in range(num_consts)]
    if num_consts == 0:
        return contexts

    try:
        expr = parse_expr(eq_with_consts, evaluate=False)
        _, den = sympy.fraction(sympy.together(expr))
        den_str = str(den)
    except Exception:
        den_str = ''

    compact_eq = eq_with_consts.replace(' ', '')
    for idx in range(num_consts):
        token = f'c{idx}'
        contexts[idx]['in_denominator'] = token in den_str
        for match in re.finditer(re.escape(token), compact_eq):
            before = compact_eq[max(0, match.start() - 48):match.start()]
            last_exp = before.rfind('exp(')
            if last_exp != -1:
                suffix = before[last_exp:]
                if suffix.count('(') >= suffix.count(')'):
                    contexts[idx]['in_exp'] = True
                    break
    return contexts


def _raw_bounds_for_context(context):
    if context.get('in_exp'):
        return (-6.0, 6.0)
    if context.get('in_denominator'):
        return (-6.0, 6.0)
    return (-DEFAULT_CONST_BOUND, DEFAULT_CONST_BOUND)


def _transform_single_constant(raw_value: float, context):
    value = float(raw_value)
    if context.get('in_exp'):
        value = EXP_CONST_BOUND * np.tanh(value / max(EXP_CONST_BOUND, 1e-12))
    else:
        value = float(np.clip(value, -DEFAULT_CONST_BOUND, DEFAULT_CONST_BOUND))

    if context.get('in_denominator'):
        value = DENOM_CONST_BOUND * np.tanh(value / max(DENOM_CONST_BOUND, 1e-12))
        if abs(value) < DENOM_MIN_ABS:
            sign = 1.0 if value == 0 else np.sign(value)
            value = float(sign * DENOM_MIN_ABS)
    return value


def _transform_constants(raw_consts, contexts):
    return np.asarray([
        _transform_single_constant(raw_consts[i], contexts[i]) for i in range(len(contexts))
    ], dtype=float)


def _substitute_constants(eq_template: str, consts) -> str:
    eq_est = eq_template
    for idx, const in enumerate(consts):
        est_c = float(const)
        if abs(est_c) < 1e-5:
            est_c = 0.0
        eq_est = eq_est.replace(f'c{idx}', str(est_c), 1)
    return _cleanup_expression_text(eq_est)


def _prediction_collapse_penalty(y_pred, y_true, var_ytrue: float) -> float:
    if not np.isfinite(var_ytrue) or var_ytrue <= 1e-12:
        return 0.0

    y_pred = np.asarray(y_pred, dtype=float)
    if y_pred.size == 0 or not np.all(np.isfinite(y_pred)):
        return 10.0

    pred_var = float(np.var(y_pred))
    pred_range = float(np.max(y_pred) - np.min(y_pred))
    y_scale = float(np.sqrt(max(var_ytrue, 1e-12)))

    var_ratio = pred_var / max(var_ytrue, 1e-12)
    range_ratio = pred_range / max(y_scale, 1e-12)

    penalty = 0.0
    if range_ratio < NEAR_CONSTANT_RANGE_RATIO:
        penalty += 2.0
    if var_ratio < NEAR_CONSTANT_VAR_RATIO:
        severity = np.log10(NEAR_CONSTANT_VAR_RATIO / max(var_ratio, 1e-12)) + 1.0
        penalty += float(np.clip(severity, 0.0, 4.0))
    return penalty


def _effective_metric(raw_metric: float, y_pred, y_true, var_ytrue: float):
    penalty = _prediction_collapse_penalty(y_pred, y_true, var_ytrue)
    return float(raw_metric) - penalty, penalty


def _metric_to_reward(metric_value: float, tree_size: int, eta: float) -> float:
    if not np.isfinite(metric_value):
        return -np.inf
    stable_arg = max(1e-300, 1e-60 - float(metric_value))
    return eta ** tree_size * float(-np.log10(stable_arg))


def _build_initial_guesses(num_consts: int, num_starts: int):
    rng = np.random.default_rng()
    seeds = [
        np.zeros(num_consts, dtype=float),
        np.ones(num_consts, dtype=float),
        -np.ones(num_consts, dtype=float),
        rng.uniform(-0.5, 0.5, size=num_consts),
    ]
    while len(seeds) < num_starts:
        seeds.append(rng.uniform(-2.0, 2.0, size=num_consts))

    deduped = []
    seen = set()
    for seed in seeds:
        key = tuple(np.round(seed, 8))
        if key not in seen:
            seen.add(key)
            deduped.append(seed)
    return deduped


def _run_optimizer(objective_fn, x0, optimizer_name: str, max_opt_iter: int, bounds=None):
    if optimizer_name == 'Nelder-Mead':
        return minimize(objective_fn, x0, method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': max_opt_iter})
    if optimizer_name == 'BFGS':
        return minimize(objective_fn, x0, method='BFGS', options={'maxiter': max_opt_iter})
    if optimizer_name == 'CG':
        return minimize(objective_fn, x0, method='CG', options={'maxiter': max_opt_iter})
    if optimizer_name == 'L-BFGS-B':
        return minimize(objective_fn, x0, method='L-BFGS-B', bounds=bounds, options={'maxiter': max_opt_iter})
    if optimizer_name == 'basinhopping':
        minimizer_kwargs = {
            'method': 'L-BFGS-B',
            'bounds': bounds,
            'options': {'maxiter': min(max_opt_iter, 100)},
        }
        return basinhopping(objective_fn, x0, minimizer_kwargs=minimizer_kwargs, niter=max_opt_iter)
    if optimizer_name == 'dual_annealing':
        return dual_annealing(objective_fn, bounds, maxiter=max_opt_iter)
    if optimizer_name == 'shgo':
        return shgo(objective_fn, bounds, options={'maxiter': max_opt_iter})
    raise ValueError(f'Unsupported optimizer: {optimizer_name}')


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

    def optimize(self, eq, tree_size: int, data_X, y_true, input_var_Xs, eta=0.9999, max_opt_iter=250, verbose=False):
        """
        Calculate reward score for a complete parse tree.
        Multi-start constant fitting is used to reduce collapse into a single bad basin,
        sensitive constants are bounded/reparameterized, and near-constant predictions are penalized.
        """
        eq = simplify_template(eq)
        if 'A' in eq or 'B' in eq:
            return -np.inf, eq, 0, 0
        if _is_pathological_expr_string(eq):
            return -np.inf, eq, 0, np.inf

        num_changing_consts = eq.count('C')
        t_optimized_constants, t_optimized_obj = 0, np.inf
        var_ytrue = np.var(y_true)

        if num_changing_consts == 0:
            y_pred = execute(eq, data_X.T, input_var_Xs)
            raw_metric = self.evalaute_loss(y_pred, y_true, var_ytrue)
            effective_metric, collapse_penalty = _effective_metric(raw_metric, y_pred, y_true, var_ytrue)
            eq = _safe_pretty_expr(eq)
            if verbose:
                print('	 metric', raw_metric, '	 collapse_penalty:', collapse_penalty, '	 simp:', eq)
        elif num_changing_consts >= 20:
            return -np.inf, eq, t_optimized_constants, t_optimized_obj
        else:
            raw_template = eq
            for idx in range(num_changing_consts):
                raw_template = raw_template.replace('C', f'c{idx}', 1)

            const_contexts = _extract_constant_contexts(raw_template, num_changing_consts)
            bounds = [_raw_bounds_for_context(ctx) for ctx in const_contexts]
            num_starts = min(DEFAULT_MULTI_STARTS, max(3, num_changing_consts + 1))
            init_points = _build_initial_guesses(num_changing_consts, num_starts)

            def objective(raw_consts):
                transformed_consts = _transform_constants(raw_consts, const_contexts)
                eq_est = _substitute_constants(raw_template, transformed_consts)
                if _is_pathological_expr_string(eq_est):
                    return 1e12
                y_pred = execute(eq_est, data_X.T, input_var_Xs)
                raw_metric = self.evalaute_loss(y_pred, y_true, var_ytrue)
                effective_metric, _ = _effective_metric(raw_metric, y_pred, y_true, var_ytrue)
                loss_val = -effective_metric
                if not np.isfinite(loss_val):
                    return 1e12
                return float(loss_val)

            best_result = None
            best_fun = np.inf
            best_raw_consts = None
            for x0 in init_points:
                try:
                    opt_result = _run_optimizer(objective, x0, self.optimizer, max_opt_iter, bounds=bounds)
                    cand_fun = float(opt_result['fun'])
                    cand_x = np.asarray(opt_result['x'], dtype=float)
                    if np.isfinite(cand_fun) and np.all(np.isfinite(cand_x)) and cand_fun < best_fun:
                        best_result = opt_result
                        best_fun = cand_fun
                        best_raw_consts = cand_x
                except Exception:
                    continue

            if best_result is None or best_raw_consts is None:
                return -np.inf, eq, 0, np.inf

            t_optimized_constants = _transform_constants(best_raw_consts, const_contexts)
            t_optimized_obj = best_fun
            eq_est = _substitute_constants(raw_template, t_optimized_constants)
            y_pred = execute(eq_est, data_X.T, input_var_Xs)
            raw_metric = self.evalaute_loss(y_pred, y_true, var_ytrue)
            effective_metric, collapse_penalty = _effective_metric(raw_metric, y_pred, y_true, var_ytrue)
            eq = _safe_pretty_expr(eq_est)

            if verbose:
                print(best_result)
            print(
                '	 reward', _metric_to_reward(effective_metric, tree_size, eta),
                '	 loss:', -raw_metric,
                '	 collapse_penalty:', collapse_penalty,
                '	 effective_loss:', -effective_metric,
                'simp:', eq,
            )

        r = _metric_to_reward(effective_metric, tree_size, eta)
        return r, eq, t_optimized_constants, t_optimized_obj


def execute(expr_str: str, data_X: np.ndarray, input_var_Xs):
    """
    evaluate the output of expression with the given input.
    consts: list of constants.
    """
    n_samples = data_X.shape[-1]

    if _is_pathological_expr_string(expr_str):
        return np.ones(n_samples) * np.inf
    if _has_bad_denominator(expr_str, data_X, input_var_Xs):
        return np.ones(n_samples) * np.inf

    used_vars, used_idx = [], []
    for idx, xi in enumerate(input_var_Xs):
        if str(xi) in expr_str:
            used_idx.append(idx)
            used_vars.append(xi)
    try:
        expr = parse_expr(expr_str, evaluate=False)
        f = lambdify(used_vars, expr, 'numpy')
        if len(used_idx) != 0:
            y_hat = f(*[data_X[i] for i in used_idx])
        else:
            y_hat = np.full(n_samples, float(expr), dtype=float)
        y_hat = np.asarray(y_hat, dtype=float)
        if y_hat.ndim == 0:
            y_hat = np.full(n_samples, float(y_hat), dtype=float)
    except TypeError:
        y_hat = np.ones(n_samples) * np.inf
    except KeyError:
        y_hat = np.ones(n_samples) * np.inf
    except ValueError:
        y_hat = np.ones(n_samples) * np.inf
    except OverflowError:
        y_hat = np.ones(n_samples) * np.inf
    except Exception:
        y_hat = np.ones(n_samples) * np.inf

    y_hat = np.nan_to_num(y_hat, nan=np.inf, posinf=np.inf, neginf=-np.inf)
    y_hat = np.clip(y_hat, -1e6, 1e6)
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