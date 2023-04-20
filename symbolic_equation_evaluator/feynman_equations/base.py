import warnings

import numpy as np
import sympy
from sympy import Derivative, Matrix, Symbol, simplify, solve, lambdify
from sympy.utilities.misc import func_name

FLOAT32_MAX = np.finfo(np.float32).max
FLOAT32_MIN = np.finfo(np.float32).min
FLOAT32_TINY = np.finfo(np.float32).tiny


class FeynmanEquation(object):
    _eq_name = None

    def __init__(self, num_vars, kwargs_list=None):
        super().__init__()
        if kwargs_list is None:
            kwargs_list = [{'real': True} for _ in range(num_vars)]

        assert len(kwargs_list) == num_vars
        self.x = [Symbol(f'x{i}', **kwargs) for i, kwargs in enumerate(kwargs_list)]
        self.sympy_eq = None

    def get_eq_name(self, prefix=None, suffix=None):
        if prefix is None:
            prefix = ''
        if suffix is None:
            suffix = ''
        return prefix + self._eq_name + suffix

    def get_var_count(self):
        return len(self.x)

    def get_op_count(self):
        return self.sympy_eq.count_ops()

    def check_num_vars_consistency(self, debug=False):
        num_vars = self.get_var_count()
        num_vars_used = len(self.sympy_eq.atoms(Symbol))
        consistent = num_vars == num_vars_used
        if debug and not consistent:
            print(f'\tnumber of variables (`{num_vars}`) is not consistent with '
                  f'number of those used in sympy_eq (`{num_vars_used}`)')
        return consistent

    def eq_func(self, x):
        """This expression function must be implemented"""
        raise NotImplementedError()

    def check_if_valid(self, values):
        return ~np.isnan(values) * ~np.isinf(values) * \
            (FLOAT32_MIN <= values) * (values <= FLOAT32_MAX) * (np.abs(values) >= FLOAT32_TINY)

    def visualize_tree(self, output_file_path=None, ext=None):
        import graphviz

        eq_name = self.get_eq_name()
        dot = graphviz.Digraph(comment=eq_name, format=ext)
        # Need to convert PI symbol to numerical value
        sympy_eq = self.sympy_eq.evalf()
        num_vars = self.get_var_count()
        num_ops = sympy_eq.count_ops()
        dot.attr(label=f'\n\n{eq_name}:\t{sympy_eq}\nNumber of variables:\t{num_vars}\n'
                       f'Number of operations:\t{num_ops}\n')
        traverse_tree(sympy_eq, dot)
        dot.render(filename=output_file_path, cleanup=True, view=False)

    def find_stationary_points(self, excludes_saddle_points=False):
        if self.sympy_eq is None:
            raise ValueError('`sympy_eq` is None and should be initialized with sympy object')

        # 1st-order partial derivative
        f_primes = [Derivative(self.sympy_eq, var).doit() for var in self.x]

        # Find stationary points
        try:
            stationary_points = solve(f_primes, self.x)
            stationary_points = [sp for sp in map(lambda sp: simplify(sp), stationary_points)
                                 if isinstance(sp, sympy.core.containers.Tuple) and all([s.is_real for s in sp])]
            if len(stationary_points) == 0 or not excludes_saddle_points:
                return stationary_points
        except Exception as e:
            print(f'====={e}=====')
            return []

        # 2nd-order partial derivative
        f_prime_mat = [[Derivative(f_prime, var).doit() for var in self.x] for f_prime in f_primes]

        # Hesse matrix
        hesse_mat = Matrix(f_prime_mat)
        det_hessian = hesse_mat.det()

        # Find saddle points
        saddle_point_list = list()
        diff_stationary_point_list = list()
        for sp in stationary_points:
            pairs = [(var, sp_value) for var, sp_value in zip(self.x, sp)]
            sign_det_hessian = det_hessian.subs(pairs).evalf()
            if sign_det_hessian < 0:
                saddle_point_list.append(sp)
            else:
                diff_stationary_point_list.append(sp)
        return diff_stationary_point_list




def traverse_tree(node, dot, from_idx=None, node_list=None, num_digits=4):
    if node_list is None:
        node_list = list()

    if node.is_number:
        dot.attr('node', shape='box')
        node_label = str(node.evalf(num_digits))
    elif isinstance(node, sympy.Symbol):
        dot.attr('node', shape='doublecircle')
        node_label = str(node)
    else:
        dot.attr('node', shape='ellipse')
        node_label = func_name(node)

    current_idx = len(node_list)
    dot.node(str(current_idx), label=node_label)
    node_list.append(current_idx)
    if from_idx is not None:
        dot.edge(str(from_idx), str(current_idx))

    for child_node in node.args:
        traverse_tree(child_node, dot, current_idx, node_list, num_digits)
