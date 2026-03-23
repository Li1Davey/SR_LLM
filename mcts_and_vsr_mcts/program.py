"""Class for symbolic expression object or program."""
import copy
import re
import sys
import warnings

import numpy as np
import sympy
from scipy.optimize import basinhopping, dual_annealing, minimize, shgo
from sympy import lambdify
from sympy.parsing.sympy_parser import parse_expr

from utils import pretty_print_expr

warnings.filterwarnings("ignore", category=RuntimeWarning)
np.set_printoptions(precision=4, linewidth=np.inf)

# Guard against ValueError from giant symbolic strings on newer Python versions.
if hasattr(sys, "set_int_max_str_digits"):
    try:
        sys.set_int_max_str_digits(100000)
    except Exception:
        pass


def _is_pathological_expr_string(expr_str: str) -> bool:
    if not expr_str:
        return True
    if len(expr_str) > 2000:
        return True
    if expr_str.count("**") > 12:
        return True
    if expr_str.count("/") > 12:
        return True
    if any(tok in expr_str for tok in ["zoo", "oo", "nan", "ComplexInfinity"]):
        return True
    return False


def _safe_pretty_expr(expr_str: str) -> str:
    """
    Pretty-print only if SymPy produces a sane finite display form.
    Otherwise return the raw expression string.
    """
    try:
        expr = parse_expr(expr_str, evaluate=False)
        eq_pretty = pretty_print_expr(expr)
        bad_display = {"nan", "zoo", "oo", "-oo", "ComplexInfinity"}
        if eq_pretty in bad_display:
            return expr_str
        return eq_pretty
    except Exception:
        return expr_str


def _output_behavior_penalty(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    """
    Penalize candidates whose predictions are nearly flat / constant.

    This is intentionally generic:
    - no operator checks
    - no expression-type checks
    - only uses prediction behavior on the current batch
    """
    if not np.all(np.isfinite(y_pred)):
        return 1e12

    true_std = float(np.std(y_true))
    if true_std < 1e-12:
        return 0.0

    pred_std = float(np.std(y_pred))
    std_ratio = pred_std / (true_std + 1e-12)

    penalty = 0.0

    # Strong penalty for almost-constant outputs.
    if std_ratio < 1e-4:
        penalty += 1e6
    elif std_ratio < 1e-3:
        penalty += 1e3 * (1e-3 - std_ratio)

    # Extra penalty if the prediction takes only a tiny number of distinct values.
    y_rounded = np.round(np.asarray(y_pred, dtype=float), 8)
    n_unique = np.unique(y_rounded).size
    if n_unique <= max(3, int(0.01 * y_rounded.size)):
        penalty += 1e3

    return penalty


def _has_bad_denominator(expr_str: str, data_X: np.ndarray, input_var_Xs, eps: float = 1e-8) -> bool:
    """
    Return True if the symbolic denominator becomes too close to zero
    anywhere on the current batch.
    """
    if "/" not in expr_str:
        return False

    try:
        expr = parse_expr(expr_str, evaluate=False)
        _, den = sympy.fraction(sympy.together(expr))

        # No real denominator.
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
        # If denominator analysis itself breaks, treat as unsafe.
        return True


def _has_input_variable(expr_str: str) -> bool:
    """
    Return True if the raw expression mentions any Xi variable.
    """
    if not expr_str:
        return False
    return re.search(r"X\d+", expr_str) is not None


def _is_constant_only_raw_template(expr_str: str) -> bool:
    """
    True if the raw expression contains no Xi variables at all.
    These all belong to the same functional family: constants.
    """
    if not expr_str:
        return True
    return not _has_input_variable(expr_str)


class Program(object):
    # Static variables
    expr_obj_thres = 1e-6
    expr_consts_thres = 1e-3
    evalaute_loss = None

    def __init__(self, n_vars, optimizer="BFGS", max_restarts=8):
        """
        vf: indicator vector for free variables. vf[i]=1 for xi is a free variable
        """
        self.vf = [0] * n_vars
        self.n_vars = n_vars
        self.optimizer = optimizer
        self.max_restarts = max_restarts

        self.optimized_constants = []
        self.optimized_obj = []
        self.cache = {}
        self.raw_expr_cache = {}
        self.constant_family_cache = None

    def set_vf(self, xi: int):
        """set of free variables"""
        if 0 <= xi < len(self.vf):
            self.vf[xi] = 1
            print("xi is:", xi, ", new vf is:", self.vf)

    def get_vf(self):
        return self.vf

    def clear_cache(self):
        self.cache = {}
        self.raw_expr_cache = {}
        self.constant_family_cache = None

    def _constant_bounds(self, n_params: int):
        # Generic bounds, not expression-specific.
        lw = [-10.0] * n_params
        up = [10.0] * n_params
        return list(zip(lw, up))

    def _initial_guesses(self, n_params: int):
        """
        Neutral restart policy:
        - symmetric seeds around zero
        - no exp/div-specific branching
        - fixed restart budget controlled by self.max_restarts
        """
        if n_params <= 0:
            return [np.array([])]

        guesses = []

        # Simple uniform starts
        base_scales = [-1.0, -0.1, 0.0, 0.1, 1.0]
        for s in base_scales:
            guesses.append(np.full(n_params, s, dtype=float))

        # Coordinate starts
        for i in range(n_params):
            for v in (-1.0, 1.0):
                g = np.zeros(n_params, dtype=float)
                g[i] = v
                guesses.append(g)

        # A few random starts
        rng = np.random.default_rng(0)
        for scale in (0.1, 1.0, 3.0):
            guesses.append(rng.normal(loc=0.0, scale=scale, size=n_params))

        # Deduplicate
        uniq = []
        seen = set()
        for g in guesses:
            key = tuple(np.round(g, 12).tolist())
            if key in seen:
                continue
            seen.add(key)
            uniq.append(g)

        return uniq[:self.max_restarts]

    def _reward_from_loss(self, loss_value: float, tree_size: int, eta: float) -> float:
        score_term = float(1.0 / (1.0 + loss_value))
        return (eta ** tree_size) * score_term

    def optimize(
        self,
        eq,
        tree_size: int,
        data_X,
        y_true,
        input_var_Xs,
        eta=0.9999,
        max_opt_iter=1000,
        verbose=False,
    ):
        """
        Calculate reward score for a complete parse tree.

        If placeholder C is in the equation, also estimate constants.
        Reward = score_from_loss * eta ** tree_size
        """
        eq_raw_input = eq

        # Exact duplicate raw-expression cache.
        if eq_raw_input in self.raw_expr_cache:
            cached = self.raw_expr_cache[eq_raw_input]
            r = self._reward_from_loss(cached["loss_value"], tree_size, eta)
            return (
                r,
                cached["eq_pretty"],
                copy.deepcopy(cached["optimized_constants"]),
                cached["optimized_obj"],
            )

        # Reuse a shared baseline for all constant-only raw templates.
        if _is_constant_only_raw_template(eq_raw_input) and self.constant_family_cache is not None:
            cached = self.constant_family_cache
            r = self._reward_from_loss(cached["loss_value"], tree_size, eta)

            self.raw_expr_cache[eq_raw_input] = {
                "loss_value": cached["loss_value"],
                "eq_pretty": cached["eq_pretty"],
                "optimized_constants": copy.deepcopy(cached["optimized_constants"]),
                "optimized_obj": cached["optimized_obj"],
            }
            return (
                r,
                cached["eq_pretty"],
                copy.deepcopy(cached["optimized_constants"]),
                cached["optimized_obj"],
            )

        eq = simplify_template(eq)

        if "A" in eq or "B" in eq:
            return -np.inf, eq, 0, 0

        if _is_pathological_expr_string(eq):
            return -np.inf, eq, 0, np.inf

        num_changing_consts = eq.count("C")
        t_optimized_constants, t_optimized_obj = 0, np.inf

        # Zero-constant case
        if num_changing_consts == 0:
            y_pred = execute(eq, data_X.T, input_var_Xs)
            var_ytrue = np.var(y_true)
            loss_value = -self.evalaute_loss(y_pred, y_true, var_ytrue)

            if not np.isfinite(loss_value):
                return -np.inf, eq, 0, np.inf

            loss_value = float(loss_value) + _output_behavior_penalty(y_pred, y_true)

            eq_pretty = _safe_pretty_expr(eq)
            r = self._reward_from_loss(loss_value, tree_size, eta)

            print(
                "\t reward", r,
                "\t loss:", loss_value,
                "raw:", eq_raw_input,
                "simp:", eq_pretty,
            )

            self.raw_expr_cache[eq_raw_input] = {
                "loss_value": loss_value,
                "eq_pretty": eq_pretty,
                "optimized_constants": 0,
                "optimized_obj": loss_value,
            }

            if _is_constant_only_raw_template(eq_raw_input):
                self.constant_family_cache = {
                    "loss_value": loss_value,
                    "eq_pretty": eq_pretty,
                    "optimized_constants": 0,
                    "optimized_obj": loss_value,
                }

            return r, eq_pretty, 0, loss_value

        # Too many constants -> skip
        if num_changing_consts >= 20:
            return -np.inf, eq, t_optimized_constants, t_optimized_obj

        eq_template = eq
        c_names = ["c" + str(i) for i in range(num_changing_consts)]
        for c in c_names:
            eq_template = eq_template.replace("C", c, 1)

        def f(consts: list):
            eq_est = eq_template
            for i in range(len(consts)):
                eq_est = eq_est.replace("c" + str(i), str(consts[i]), 1)

            eq_est = eq_est.replace("+ -", "-")
            eq_est = eq_est.replace("- -", "+")
            eq_est = eq_est.replace("- +", "-")
            eq_est = eq_est.replace("+ +", "+")

            if _is_pathological_expr_string(eq_est):
                return 1e12

            y_pred = execute(eq_est, data_X.T, input_var_Xs)
            var_ytrue = np.var(y_true)
            val = -self.evalaute_loss(y_pred, y_true, var_ytrue)

            if not np.isfinite(val):
                return 1e12

            val = float(val) + _output_behavior_penalty(y_pred, y_true)
            return val

        try:
            starts = self._initial_guesses(num_changing_consts)
            opt_result = None

            def _run_optimizer_once(x0):
                if self.optimizer == "Nelder-Mead":
                    return minimize(
                        f,
                        x0,
                        method="Nelder-Mead",
                        options={"xatol": 1e-10, "fatol": 1e-10, "maxiter": max_opt_iter},
                    )
                elif self.optimizer == "BFGS":
                    return minimize(f, x0, method="BFGS", options={"maxiter": max_opt_iter})
                elif self.optimizer == "CG":
                    return minimize(f, x0, method="CG", options={"maxiter": max_opt_iter})
                elif self.optimizer == "L-BFGS-B":
                    return minimize(f, x0, method="L-BFGS-B", options={"maxiter": max_opt_iter})
                elif self.optimizer == "basinhopping":
                    minimizer_kwargs = {
                        "method": "Nelder-Mead",
                        "options": {"xatol": 1e-10, "fatol": 1e-10, "maxiter": 100},
                    }
                    return basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=max_opt_iter)
                elif self.optimizer == "dual_annealing":
                    minimizer_kwargs = {
                        "method": "Nelder-Mead",
                        "options": {"xatol": 1e-10, "fatol": 1e-10, "maxiter": 100},
                    }
                    bounds = self._constant_bounds(num_changing_consts)
                    return dual_annealing(
                        f, bounds, minimizer_kwargs=minimizer_kwargs, maxiter=max_opt_iter
                    )
                elif self.optimizer == "shgo":
                    minimizer_kwargs = {
                        "method": "Nelder-Mead",
                        "options": {"xatol": 1e-10, "fatol": 1e-10, "maxiter": 100},
                    }
                    bounds = self._constant_bounds(num_changing_consts)
                    return shgo(
                        f, bounds, minimizer_kwargs=minimizer_kwargs, options={"maxiter": max_opt_iter}
                    )
                else:
                    return None

            # Global optimizers already explore broadly, so one start is enough.
            global_optimizers = {"basinhopping", "dual_annealing", "shgo"}
            if self.optimizer in global_optimizers:
                starts = starts[:1]

            for x0 in starts:
                cur = _run_optimizer_once(x0)
                if cur is None:
                    continue
                if not np.isfinite(cur["fun"]):
                    continue
                if opt_result is None or cur["fun"] < opt_result["fun"]:
                    opt_result = cur

            if opt_result is None:
                return -np.inf, eq, 0, np.inf

            t_optimized_constants = opt_result["x"]
            c_vals = t_optimized_constants.tolist()
            t_optimized_obj = float(opt_result["fun"])

            if verbose:
                print(opt_result)

            eq_fit = eq_template
            for i in range(len(c_vals)):
                est_c = float(c_vals[i])
                if abs(est_c) < 1e-5:
                    est_c = 0.0
                eq_fit = eq_fit.replace("c" + str(i), str(est_c), 1)

            eq_fit = eq_fit.replace("+ -", "-")
            eq_fit = eq_fit.replace("- -", "+")
            eq_fit = eq_fit.replace("- +", "-")
            eq_fit = eq_fit.replace("+ +", "+")

            y_pred = execute(eq_fit, data_X.T, input_var_Xs)
            var_ytrue = np.var(y_true)
            loss_value = -self.evalaute_loss(y_pred, y_true, var_ytrue)

            if not np.isfinite(loss_value):
                return -np.inf, eq, 0, np.inf

            loss_value = float(loss_value) + _output_behavior_penalty(y_pred, y_true)

            eq_pretty = _safe_pretty_expr(eq_fit)
            r = self._reward_from_loss(loss_value, tree_size, eta)

            print(
                "\t reward", r,
                "\t loss:", loss_value,
                "raw:", eq_raw_input,
                "simp:", eq_pretty,
            )

            self.raw_expr_cache[eq_raw_input] = {
                "loss_value": loss_value,
                "eq_pretty": eq_pretty,
                "optimized_constants": np.array(t_optimized_constants, copy=True),
                "optimized_obj": t_optimized_obj,
            }

            if _is_constant_only_raw_template(eq_raw_input):
                self.constant_family_cache = {
                    "loss_value": loss_value,
                    "eq_pretty": eq_pretty,
                    "optimized_constants": np.array(t_optimized_constants, copy=True),
                    "optimized_obj": t_optimized_obj,
                }

            return r, eq_pretty, t_optimized_constants, t_optimized_obj

        except Exception as e:
            print(e)
            return -np.inf, eq, 0, np.inf


def execute(expr_str: str, data_X: np.ndarray, input_var_Xs):
    """
    Evaluate the output of expression with the given input.
    Reject expressions with near-zero denominators on the current batch.
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
        f = lambdify(used_vars, expr, "numpy")

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
    except Exception:
        y_hat = np.ones(n_samples) * np.inf

    y_hat = np.nan_to_num(y_hat, nan=np.inf, posinf=np.inf, neginf=-np.inf)
    y_hat = np.clip(y_hat, -1e6, 1e6)
    return y_hat


def execute_eval(expr_str: str, data_X: np.ndarray, input_var_Xs, simulated_steps: int, dt: float):
    """
    Evaluate the output of expression with the given input.
    """
    try:
        y_hat = eval(expr_str)
    except TypeError as e:
        print(e)
        y_hat = None

    return y_hat


def simplify_template(eq):
    for _ in range(10):
        eq = eq.replace("(C+C)", "C")
        eq = eq.replace("sqrt(C)", "C")
        eq = eq.replace("sin(C)", "C")
        eq = eq.replace("cos(C)", "C")
        eq = eq.replace("(1/C)", "C")
        eq = eq.replace("(C-C)", "C")
        eq = eq.replace("C*C", "C")
        eq = eq.replace("(C/C)", "C")
    return eq


if __name__ == "__main__":
    expr_temp = "sqrt(sqrt(C))*(sqrt(X0)+C)"
    simplify_template(expr_temp)
