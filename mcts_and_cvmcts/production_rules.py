from sympy import Symbol, Float, Integer, Rational
import sympy
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




def get_production_rules(nvars, operators_set, non_terminal_node='A'):
    """
    nvars: number of input variables.
    operators_set: set of mathematical operators.
    Return: for example, A->(A+A), A->(A-A), A->A*A, A->(A)/(A)
    """
    base_rules = [f'{non_terminal_node}->({non_terminal_node}+{non_terminal_node})',
                  f'{non_terminal_node}->({non_terminal_node}-{non_terminal_node})',
                  f'{non_terminal_node}->{non_terminal_node}*{non_terminal_node}']
    div_rules = [f'{non_terminal_node}->({non_terminal_node})/({non_terminal_node})']
    # inv_rules = [f'{non_terminal_node}->1/({non_terminal_node})']
    exp_rules = [f'{non_terminal_node}->exp({non_terminal_node})']
    log_rules = [f'{non_terminal_node}->log({non_terminal_node})']
    sqrt_rules = [f'{non_terminal_node}->sqrt({non_terminal_node})']
    const_rules = [f'{non_terminal_node}->C']

    rules = base_rules + get_vars_rules(nvars) + const_rules
    if 'inv' in operators_set:
        rules += get_inv_rules(nvars)
    if 'div' in operators_set:
        rules += div_rules
    if 'sin' in operators_set or 'cos' in operators_set:
        rules += get_sincos_vars_rules(nvars)
    if 'sqrt' in operators_set:
        rules += sqrt_rules
    if 'exp' in operators_set:
        rules += exp_rules
    if 'log' in operators_set:
        rules += log_rules
    return rules


def get_inv_rules(nvars: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->1/X{xi}' for xi in range(nvars) ]

def get_vars_rules(nvars: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{i}' for i in range(nvars)]


def get_sincos_vars_rules(nvars: int, non_terminal_node='A') -> list:
    """
    return [A->sin(Xi), A->cos(Xi)]
    """
    return [f'{non_terminal_node}->sin(X{i})' for i in range(nvars)] + [f'{non_terminal_node}->cos(X{i})' for i in range(nvars)]

def get_ith_sincos_rules(i: int, non_terminal_node='A') -> list:
    """
    return [A->sin(Xi), A->cos(Xi)]
    """
    return [f'{non_terminal_node}->sin(X{i})', f'{non_terminal_node}->cos(X{i})']
def get_ith_var_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}', ]


def get_ith_inv_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->1/X{xi}', ]

if __name__ == '__main__':
    X0=Symbol('X0')
    expr=2.1/X0 #3.5*X0+4.0+
    preorder_traversal_expr = to_binary_expr_tree(expr)