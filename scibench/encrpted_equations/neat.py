from collections import OrderedDict
import numpy as np
import sympy
from sympy import Symbol
from base import KnownEquation

NEAT_EQUATION_CLASS_DICT = OrderedDict()


def register_neat_eq_class(cls):
    NEAT_EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls


@register_neat_eq_class
class Neat_1(KnownEquation):
    _eq_name = 'Neat-1'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0] ** 4 + x[0] ** 3 + x[0] ** 2 + x[0]


@register_neat_eq_class
class Neat_2(KnownEquation):
    _eq_name = 'Neat-2'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0] ** 5 + x[0] ** 4 + x[0] ** 3 + x[0] ** 2 + x[0]


@register_neat_eq_class
class Neat_3(KnownEquation):
    _eq_name = 'Neat-3'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(x[0] ** 2) * sympy.cos(x[0]) - 1


@register_neat_eq_class
class Neat_4(KnownEquation):
    _eq_name = 'Neat-4'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq =  sympy.log(x[0] + 1) + sympy.log(x[0] ** 2 + 1)


@register_neat_eq_class
class Neat_5(KnownEquation):
    _eq_name = 'Neat-5'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 2 * sympy.sin(x[0]) * sympy.cos(x[1])


@register_neat_eq_class
class Neat_6(KnownEquation):
    _eq_name = 'Neat-6'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = []


@register_neat_eq_class
class Neat_7(KnownEquation):
    _eq_name = 'Neat-7'

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2-2.1*sympy.cos(9.8*x[0])*sympy.sin(1.3*x[1])


@register_neat_eq_class
class Neat_8(KnownEquation):
    _eq_name = 'Neat-8'

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.exp(-(x[0]-1)**2))/(1.2+(x[1]-2.5)**2)


@register_neat_eq_class
class Neat_9(KnownEquation):
    _eq_name = 'Neat-9'

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 1/(1+x[0]**(-4))+1/(1+x[1]**(-4))

