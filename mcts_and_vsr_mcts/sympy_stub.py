import math
import re
from dataclasses import dataclass
from typing import Any, Iterable
import numpy_stub as np

class Symbol(str):
    def __new__(cls, name, *args, **kwargs):
        return super().__new__(cls, name)

class Float(float):
    pass

class Rational(float):
    pass

class Integer(int):
    pass

NegativeOne = -1


def parse_expr(expr: str):
    return Expression(expr)


def simplify(expr):
    return expr


def expand(expr):
    return expr


def lambdify(used_vars, expr, modules=None):
    expr_str = _sanitize(str(expr))
    var_names = [str(v) for v in used_vars]

    def _evaluate(*args):
        local_ns = {name: args[i] for i, name in enumerate(var_names)}
        safe_math = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
        safe_math.update({
            'sin': math.sin,
            'cos': math.cos,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
        })
        safe_math.update({
            'np': np,
            'numpy': np,
        })
        local_ns.update(safe_math)
        return eval(expr_str, {**safe_math, 'np': np, 'numpy': np}, local_ns)

    return _evaluate


def _extract_floats(expr_str: str):
    matches = re.findall(r"[-+]?[0-9]*\.?[0-9]+", expr_str)
    return {Float(m) for m in matches}


def _sanitize(expr: str) -> str:
    expr = re.sub(r'(\)|[A-Za-z_][A-Za-z0-9_]*)(?=-?\d)', r'\1*', expr)
    expr = re.sub(r'(?<![\d\.])0(\d+)', r'0.\1', expr)
    expr = re.sub(r'\bX\b', 'X0', expr)
    return expr


@dataclass
class Expression:
    raw: Any

    def __str__(self):
        return str(self.raw)

    def atoms(self, cls):
        if cls in (Float, int, float):
            return _extract_floats(str(self.raw))
        return set()

    def replace(self, target, repl):
        new_raw = str(self.raw).replace(str(target), str(repl))
        return Expression(new_raw)

    @property
    def func(self):
        return lambda *args, **kwargs: None

    @property
    def args(self):
        return []
