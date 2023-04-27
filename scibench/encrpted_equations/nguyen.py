from collections import OrderedDict
import numpy as np
import sympy
from sympy import Symbol
from base import KnownEquation

NGUYEN_EQUATION_CLASS_DICT = OrderedDict()


def register_nguyen_eq_class(cls):
    NGUYEN_EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls


@register_nguyen_eq_class
class Nguyen_1(KnownEquation):
    _eq_name = 'Nguyen-1'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0] ** 3 + x[0] ** 2 + x[0]


@register_nguyen_eq_class
class Nguyen_2(KnownEquation):
    _eq_name = 'Nguyen-2'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0] ** 4 + x[0] ** 3 + x[0] ** 2 + x[0]


@register_nguyen_eq_class
class Nguyen_3(KnownEquation):
    _eq_name = 'Nguyen-3'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0] ** 5 + x[0] ** 4 + x[0] ** 3 + x[0] ** 2 + x[0]


@register_nguyen_eq_class
class Nguyen_4(KnownEquation):
    _eq_name = 'Nguyen-4'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0] ** 6 + x[0] ** 5 + x[0] ** 4 + x[0] ** 3 + x[0] ** 2 + x[0]


@register_nguyen_eq_class
class Nguyen_5(KnownEquation):
    _eq_name = 'Nguyen-5'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(x[0] ** 2) * sympy.cos(x[0]) - 1


@register_nguyen_eq_class
class Nguyen_6(KnownEquation):
    _eq_name = 'Nguyen-6'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(x[0]) + sympy.sin(x[0] + x[0] ** 2)


@register_nguyen_eq_class
class Nguyen_7(KnownEquation):
    _eq_name = 'Nguyen-7'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0] + 1) + sympy.log(x[0] ** 2 + 1)


@register_nguyen_eq_class
class Nguyen_8(KnownEquation):
    _eq_name = 'Nguyen-8'

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0])


@register_nguyen_eq_class
class Nguyen_9(KnownEquation):
    _eq_name = 'Nguyen-9'

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.sin(x[0]) + sympy.sin(x[1] ** 2)


@register_nguyen_eq_class
class Nguyen_10(KnownEquation):
    _eq_name = 'Nguyen-10'

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2 * sympy.sin(x[0]) * sympy.cos(x[1])


@register_nguyen_eq_class
class Nguyen_11(KnownEquation):
    _eq_name = 'Nguyen-11'

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0] ** x[1]
