import re

import sympy
from sympy.core.numbers import Float, Rational, NegativeOne, Integer
from sympy import simplify, Symbol
from sympy.parsing.sympy_parser import parse_expr


def _max_parentheses_depth(expr: str) -> int:
    depth = 0
    max_depth = 0
    for ch in expr:
        if ch == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ')':
            depth = max(0, depth - 1)
    return max_depth


def _looks_pathological_for_simplify(expr: str) -> bool:
    """Cheap textual checks to avoid SymPy simplify stalls."""
    if not expr:
        return True
    if len(expr) > 220:
        return True
    if expr.count('exp(') > 2:
        return True
    if expr.count('**') > 3:
        return True
    if expr.count('/') > 5:
        return True
    if _max_parentheses_depth(expr) > 18:
        return True
    if any(tok in expr for tok in ('zoo', 'oo', 'nan', 'Infinity', 'ComplexInfinity')):
        return True
    # Reject giant numeric literals that can trigger expensive parsing paths.
    if re.search(r"\d{40,}", expr):
        return True
    return False


def pretty_print_expr(eq) -> str:
    '''
    Ask sympy to return a compact/canonical expression string.

    NOTE:
    We intentionally avoid `expand(...)` here. Expanding can transform a
    compact, interpretable identity into long partial-fraction style forms,
    which hurts exact-equation readability for recovered solutions.
    '''
    if isinstance(eq, str):
        if _looks_pathological_for_simplify(eq):
            return eq
        eq = parse_expr(eq, evaluate=False)

    eq_str = str(eq)
    if _looks_pathological_for_simplify(eq_str):
        return eq_str

    try:
        expr = simplify(eq)
        # Prefer compact rational/exponential structure over expanded sums.
        expr = sympy.together(expr)
        expr = sympy.cancel(expr)
        expr = sympy.factor(expr)
        expr = simplify(expr)
        return str(expr)
    except Exception:
        return eq_str


def create_geometric_generations(n_generations, nvar, ratio=1.2):
    gens = [0] * nvar
    round = 0
    total_ratios = sum([ratio ** it for it in range(nvar)])
    for it in range(nvar):
        gens[it] += int(n_generations * ratio ** it / total_ratios)

    # gens[0] = n_generations
    for it in range(0, nvar):
        if gens[it] < 20:
            gens[it] = 20
    gens = gens
    print('generation #:', gens, 'sum=', sum(gens))
    return gens


def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find + len(sub):]
    return s


def create_reward_threshold(highest_threhold, nvar, ratio=0.95):
    return [highest_threhold * ratio ** i for i in range(nvar)]


def create_uniform_generations(n_generations, nvar):
    gens = [0] * nvar
    for it in range(nvar):
        gens[it] = n_generations
    print('generation #:', gens, 'sum=', sum(gens))
    return gens


def expression_to_template(expr, stand_alone_constants) -> str:
    C = Symbol('C')
    all_floats = list(expr.atoms(Float))
    for fi in all_floats:
        if len(stand_alone_constants) >= 1 and min([abs(fi - ci) for ci in stand_alone_constants]) < 1e-5:
            continue
        expr = expr.replace(fi, C)
    return str(expr)