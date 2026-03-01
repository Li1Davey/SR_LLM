from sympy import Symbol, Float, Integer, Rational
import sympy
import os
import numpy as np


def production_rules_to_expr(list_of_production_rules):
    """
    Convert a list of production rules to the exact symbolic equation.
    For example ['f->A', 'A->(A-A)', 'A->X0', 'A->X1'] => X0*X1
    """
    seq = ['f']
    for one_rule in list_of_production_rules:
        for ix, s in enumerate(seq):
            if s == one_rule[0]:
                seq = seq[:ix] + list(one_rule[3:]) + seq[ix + 1:]
                break
    output = ''.join(seq)
    return output


def to_binary_expr_tree(expr):
    if isinstance(expr, Symbol):
        return str(expr)
    elif isinstance(expr, Float) or isinstance(expr, Integer) or isinstance(expr, Rational):
        return expr
    else:
        op = expr.func
        args = expr.args

        if len(args) <= 2:
            return [op.__name__] + [to_binary_expr_tree(arg) for arg in args]
        else:
            left = to_binary_expr_tree(args[0])
            right = to_binary_expr_tree(op(*args[1:]))
            return [op.__name__, left, right]

def _dedupe_preserve_order(rules):
    seen = set()
    out = []
    for rule in rules:
        if rule in seen:
            continue
        seen.add(rule)
        out.append(rule)
    return out


def get_production_rules(nvars, operators_set, non_terminal_node='A'):
    """
    nvars: number of input variables.
    operators_set: set of mathematical operators.
    Return: for example, A->(A+A), A->(A-A), A->A*A, A->(A)/(A)
    """
    if os.getenv("SCIBENCH_SAFE_GRAMMAR", "0") == "1":
        return get_production_rules_safe_singleA(nvars, operators_set, non_terminal_node)
    base_rules = [f'{non_terminal_node}->({non_terminal_node}+{non_terminal_node})',
                  f'{non_terminal_node}->({non_terminal_node}-{non_terminal_node})',
                  f'{non_terminal_node}->{non_terminal_node}*{non_terminal_node}']
    div_rules = [f'{non_terminal_node}->({non_terminal_node})/({non_terminal_node})']
    exp_rules = [f'{non_terminal_node}->exp({non_terminal_node})']
    log_rules = [f'{non_terminal_node}->log({non_terminal_node})']
    sqrt_rules = [f'{non_terminal_node}->sqrt({non_terminal_node})']
    const_rules = [f'{non_terminal_node}->C']
    abs_rules = [f'{non_terminal_node}->abs({non_terminal_node})']

    rules = base_rules + get_vars_rules(nvars, non_terminal_node)
    if 'const' in operators_set:
        rules += const_rules
    if 'inv' in operators_set:
        rules += get_inv_rules(nvars, non_terminal_node)
    if 'div' in operators_set:
        rules += div_rules
    if 'sin' in operators_set or 'cos' in operators_set:
        rules += get_sincos_vars_rules(non_terminal_node)
    if 'sqrt' in operators_set:
        rules += sqrt_rules
    if 'exp' in operators_set:
        rules += exp_rules
    if 'abs' in operators_set:
        rules += abs_rules
    if 'log' in operators_set:
        rules += log_rules
    if 'n2' in operators_set:
        rules += get_n2_rules(nvars, non_terminal_node)
    if 'n3' in operators_set:
        rules += get_n3_rules(nvars, non_terminal_node)
    if 'n4' in operators_set:
        rules += get_n4_rules(nvars, non_terminal_node)
    if 'n5' in operators_set:
        rules += get_n5_rules(nvars, non_terminal_node)
    return _dedupe_preserve_order(rules)

def get_production_rules_safe_singleA(nvars, operators_set, non_terminal_node="A"):
    """
    Safer but more versatile grammar for Feynman-like equations.

    Design goals:
    - preserve numeric stability (bounded denominator forms)
    - increase cross-variable coverage (sum/diff/product interactions)
    - improve functional expressiveness with affine-in-variable unary forms
    """
    rules = [
        f"{non_terminal_node}->({non_terminal_node}+{non_terminal_node})",
        f"{non_terminal_node}->({non_terminal_node}-{non_terminal_node})",
        f"{non_terminal_node}->{non_terminal_node}*{non_terminal_node}",
    ]

    # variables
    rules += get_vars_rules(nvars, non_terminal_node)

    # affine variable atoms for broader fit classes (linear offsets/scales)
    if "const" in operators_set:
        rules += [f"{non_terminal_node}->C"]
        for i in range(nvars):
            rules += [
                f"{non_terminal_node}->C*X{i}",
                f"{non_terminal_node}->(C*X{i}+C)",
            ]

    # explicit pairwise interactions across all variable pairs
    for i in range(nvars):
        for j in range(i + 1, nvars):
            rules += [
                f"{non_terminal_node}->(X{i}+X{j})",
                f"{non_terminal_node}->(X{i}-X{j})",
                f"{non_terminal_node}->(X{j}-X{i})",
                f"{non_terminal_node}->X{i}*X{j}",
            ]

    # inv (safe-ish): ONLY 1/Xi and C/(Xi+C), not 1/(A)
    if "inv" in operators_set:
        for i in range(nvars):
            rules += [f"{non_terminal_node}->1/X{i}"]
            if "const" in operators_set:
                rules += [f"{non_terminal_node}->C/(X{i}+C)"]

    # div: constrain denominators to avoid monsters
    if "div" in operators_set:
        for i in range(nvars):
            # normalized / saturating forms
            rules += [
                f"{non_terminal_node}->X{i}/(X{i}+C)",
                f"{non_terminal_node}->C/(X{i}+C)",
            ]

            for j in range(nvars):
                if i == j:
                    continue
                rules += [
                    f"{non_terminal_node}->X{i}/(X{j}+C)",
                    f"{non_terminal_node}->(X{i}+C)/(X{j}+C)",
                ]

            # allow A in numerator, but stabilize denominator
            rules += [f"{non_terminal_node}->({non_terminal_node})/(X{i}+C)"]

        # robust pairwise-difference denominator for any pair (not just X1-X0)
        if "abs" in operators_set:
            for i in range(nvars):
                for j in range(i + 1, nvars):
                    rules += [f"{non_terminal_node}->({non_terminal_node})/(abs(X{i}-X{j})+C)"]

    # exp: variables + affine-in-variable forms (avoid exp(A) blow-up)
    if "exp" in operators_set:
        for i in range(nvars):
            rules += [f"{non_terminal_node}->exp(X{i})"]
            if "const" in operators_set:
                rules += [
                    f"{non_terminal_node}->exp(C*X{i})",
                    f"{non_terminal_node}->exp(C*X{i}+C)",
                ]

    # sin/cos: variable and affine-variable forms only (not sin(A))
    if ("sin" in operators_set) or ("cos" in operators_set):
        for i in range(nvars):
            if "sin" in operators_set:
                rules += [f"{non_terminal_node}->sin(X{i})"]
                if "const" in operators_set:
                    rules += [f"{non_terminal_node}->sin(C*X{i})"]
            if "cos" in operators_set:
                rules += [f"{non_terminal_node}->cos(X{i})"]
                if "const" in operators_set:
                    rules += [f"{non_terminal_node}->cos(C*X{i})"]

    # sqrt/log/abs: stability-aware variable forms
    if "sqrt" in operators_set:
        for i in range(nvars):
            if "abs" in operators_set:
                rules += [f"{non_terminal_node}->sqrt(abs(X{i}))"]
                if "const" in operators_set:
                    rules += [f"{non_terminal_node}->sqrt(abs(X{i})+C)"]
            else:
                rules += [f"{non_terminal_node}->sqrt(X{i})"]

    if "log" in operators_set:
        for i in range(nvars):
            if ("abs" in operators_set) and ("const" in operators_set):
                rules += [
                    f"{non_terminal_node}->log(abs(X{i})+C)",
                    f"{non_terminal_node}->log(abs(C*X{i})+C)",
                ]
            else:
                rules += [f"{non_terminal_node}->log(X{i})"]

    if "abs" in operators_set:
        for i in range(nvars):
            rules += [f"{non_terminal_node}->abs(X{i})"]
            if "const" in operators_set:
                rules += [f"{non_terminal_node}->abs(C*X{i}+C)"]

    # powers: keep direct Xi**k plus one safe affine-square family
    if "n2" in operators_set:
        rules += get_n2_rules(nvars, non_terminal_node)
        if "const" in operators_set:
            for i in range(nvars):
                rules += [f"{non_terminal_node}->(C*X{i}+C)**2"]
    if "n3" in operators_set:
        rules += get_n3_rules(nvars, non_terminal_node)
    if "n4" in operators_set:
        rules += get_n4_rules(nvars, non_terminal_node)
    if "n5" in operators_set:
        rules += get_n5_rules(nvars, non_terminal_node)

    return _dedupe_preserve_order(rules)


def get_inv_rules(nvars: int, non_terminal_node='A') -> list:
    rules = []
    for i in range(nvars):
        rules += get_ith_inv_rules(i, non_terminal_node)
    return rules


def get_vars_rules(nvars: int, non_terminal_node='A') -> list:
    rules = []
    for i in range(nvars):
        rules += get_ith_var_rules(i, non_terminal_node)
    return rules


def get_n2_rules(nvars: int, non_terminal_node='A') -> list:
    rules = []
    for i in range(nvars):
        rules += get_ith_n2_rules(i, non_terminal_node)
    return rules


def get_n3_rules(nvars: int, non_terminal_node='A') -> list:
    rules = []
    for i in range(nvars):
        rules += get_ith_n3_rules(i, non_terminal_node)
    return rules


def get_n4_rules(nvars: int, non_terminal_node='A') -> list:
    rules = []
    for i in range(nvars):
        rules += get_ith_n4_rules(i, non_terminal_node)
    return rules


def get_n5_rules(nvars: int, non_terminal_node='A') -> list:
    rules = []
    for i in range(nvars):
        rules += get_ith_n5_rules(i, non_terminal_node)
    return rules


def get_sincos_vars_rules(non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->sin({non_terminal_node})', f'{non_terminal_node}->cos({non_terminal_node})']


def get_var_i_production_rules(round_idx, operators_set):
    grammars = get_ith_var_rules(round_idx)
    if 'inv' in operators_set:
        grammars += get_ith_inv_rules(round_idx, non_terminal_node='A')
    if 'n2' in operators_set:
        grammars += get_ith_n2_rules(round_idx)
    if 'n3' in operators_set:
        grammars += get_ith_n3_rules(round_idx)
    if 'n4' in operators_set:
        grammars += get_ith_n4_rules(round_idx)
    if 'n5' in operators_set:
        grammars += get_ith_n5_rules(round_idx)
    return grammars


def get_ith_var_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}', ]


def get_ith_n2_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}**2', ]


def get_ith_n3_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}**3', ]


def get_ith_n4_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}**4', ]


def get_ith_n5_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}**5', ]


def get_ith_inv_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->1/X{xi}']


if __name__ == '__main__':
    seq = "f->A,A->A*A,A->sqrt(A),A->sqrt(A),A->C,A->(A+A),A->sqrt(A),A->X0,A->C"
    seq = seq.split(',')
    production_rules_to_expr(seq)
