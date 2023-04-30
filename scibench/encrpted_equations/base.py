import sympy
from sympy import Symbol


class KnownEquation(object):
    _eq_name = None
    _function_set = ['exp', 'log', 'sqrt', 'add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self, num_vars, kwargs_list=None):
        if kwargs_list is None:
            kwargs_list = [{'real': True} for _ in range(num_vars)]

        assert len(kwargs_list) == num_vars
        self.num_vars = num_vars
        self.x = [Symbol(f'x{i}', **kwargs) for i, kwargs in enumerate(kwargs_list)]
        self.sympy_eq = None

    def get_eq_name(self, prefix=None, suffix=None):
        if prefix is None:
            prefix = ''
        if suffix is None:
            suffix = ''
        return prefix + self._eq_name + suffix
