from gplearn.functions import make_function
import numpy as np

# production rules for each benchmark for SPL
base_rules = ['A->A+A', 'A->A-A', 'A->A*A', 'A->A/A']
inv_rules = ['A->1/A']
sin_cos_rules = ['A->cos(A)', 'A->sin(A)']
exp_rules = ['A->exp(A)']
log_rules = ['A->log(A)']
sqrt_rules = ['A->sqrt(A)']
const_rules = ['A->C']


def get_production_rules(nvars, operators_set):
    """
    nvars: number of input variables.
    operators_set: set of mathematical operators.
    """
    rules = base_rules + get_vars_rules(nvars) + const_rules
    if 'inv' in operators_set:
        rules += inv_rules
    if 'sin' in operators_set or 'cos' in operators_set:
        rules += sin_cos_rules
    if 'sqrt' in operators_set:
        rules += sqrt_rules
    if 'exp' in operators_set:
        rules += exp_rules
    if 'log' in operators_set:
        rules += log_rules
    return rules


def get_vars_rules(nvars: int) -> list:
    return [f'A->X{i}' for i in range(nvars)]


def get_ith_var_rules(xi: int) -> list:
    return [f'A->X{xi}', ]
