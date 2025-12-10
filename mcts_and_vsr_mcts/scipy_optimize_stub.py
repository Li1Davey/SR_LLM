from dataclasses import dataclass
from typing import Callable, List, Any


@dataclass
class OptimizeResult:
    x: Any
    fun: float

    def __getitem__(self, item):
        if item == 'x':
            return self.x
        if item == 'fun':
            return self.fun
        raise KeyError(item)


def _evaluate(fun: Callable, x0):
    try:
        return float(fun(x0))
    except Exception:
        return float('inf')


def minimize(fun: Callable, x0, method=None, options=None):
    val = _evaluate(fun, x0)
    return OptimizeResult(x0, val)


def basinhopping(fun: Callable, x0, minimizer_kwargs=None, niter=10):
    val = _evaluate(fun, x0)
    return OptimizeResult(x0, val)


def dual_annealing(fun: Callable, bounds, minimizer_kwargs=None, maxiter=None):
    # pick mid-point of bounds
    x0 = [(low + high) / 2 for low, high in bounds]
    val = _evaluate(fun, x0)
    return OptimizeResult(x0, val)


def shgo(fun: Callable, bounds, minimizer_kwargs=None, options=None):
    x0 = [(low + high) / 2 for low, high in bounds]
    val = _evaluate(fun, x0)
    return OptimizeResult(x0, val)
