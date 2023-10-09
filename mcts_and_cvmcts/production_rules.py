from gplearn.functions import make_function
import numpy as np


# production rules for each benchmark for SPL


def get_production_rules(nvars, operators_set, non_terminal_node='A'):
    """
    nvars: number of input variables.
    operators_set: set of mathematical operators.
    """
    base_rules = [f'{non_terminal_node}->{non_terminal_node}+{non_terminal_node}',
                  # f'{non_terminal_node}->{non_terminal_node}-{non_terminal_node}',
                  f'{non_terminal_node}->{non_terminal_node}*{non_terminal_node}']
    inv_rules = [f'{non_terminal_node}->{non_terminal_node}/{non_terminal_node}']
    sin_cos_rules = [f'{non_terminal_node}->cos({non_terminal_node})', f'{non_terminal_node}->sin({non_terminal_node})']
    exp_rules = [f'{non_terminal_node}->exp({non_terminal_node})']
    log_rules = [f'{non_terminal_node}->log({non_terminal_node})']
    sqrt_rules = [f'{non_terminal_node}->sqrt({non_terminal_node})']
    const_rules = [f'{non_terminal_node}->C']

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


def remove_consts_rules_in_eq(k, non_terminal_node='A'):
    # remove k-th A->C rules in the expression
    return None


def get_vars_rules(nvars: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{i}' for i in range(nvars)]


def get_ith_var_rules(xi: int, non_terminal_node='A') -> list:
    return [f'{non_terminal_node}->X{xi}', ]
