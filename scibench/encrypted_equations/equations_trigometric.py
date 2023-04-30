from collections import OrderedDict
import sympy
from base import KnownEquation

EQUATION_CLASS_DICT = OrderedDict()


def register_eq_class(cls):
    EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls

def get_eq_obj(key, **kwargs):
    if key in EQUATION_CLASS_DICT:
        return EQUATION_CLASS_DICT[key](**kwargs)
    raise KeyError(f'`{key}` is not expected as a equation object key')

@register_eq_class
class sincos_nv5_nt55_prog_46(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.5787 * x[0] * x[2] - 0.2875 * x[2] * sympy.cos(x[1]) - 0.7874 * x[4] * sympy.sin(x[2]) + 0.7182 * x[
            4] * sympy.cos(x[3]) + 0.1074 * x[4] - 0.9161 * sympy.sin(x[0]) - 0.0204 * sympy.sin(x[1]) * sympy.cos(
            x[4]) - 0.7368 * sympy.sin(x[1]) + 0.8269 * sympy.sin(x[2]) + 0.6944 * sympy.cos(x[3]) + 0.6334


@register_eq_class
class sincos_nv5_nt55_prog_0(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4156 * x[0] * x[1] - 0.1399 * x[2] * sympy.cos(x[1]) + 0.0438 * x[2] + 0.9508 * x[3] * sympy.sin(x[1]) + 0.2319 * \
                        x[3] - 0.6808 * x[4] * sympy.cos(x[3]) - 0.4468 * x[4] + 0.0585 * sympy.sin(x[0]) + 0.6224 * sympy.cos(
            x[1]) - 0.8638 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.959


@register_eq_class
class sincos_nv5_nt55_prog_35(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9207 * x[0] * sympy.cos(x[1]) - 0.1841 * x[0] * sympy.cos(x[2]) + 0.8054 * x[1] * sympy.sin(x[2]) - 0.3703 * x[
            1] - 0.3074 * x[2] + 0.4904 * x[4] * sympy.cos(x[2]) - 0.7115 * x[4] + 0.3894 * sympy.sin(x[2]) * sympy.cos(
            x[3]) + 0.9755 * sympy.cos(x[0]) - 0.5161 * sympy.cos(x[3]) - 0.6391


@register_eq_class
class sincos_nv5_nt55_prog_8(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.105 * x[0] * sympy.sin(x[2]) + 0.8919 * x[3] * sympy.sin(x[1]) + 0.114 * x[3] * sympy.cos(x[2]) - 0.3825 * x[
            3] - 0.1461 * x[4] * sympy.sin(x[0]) + 0.9091 * x[4] * sympy.sin(x[1]) - 0.6847 * sympy.sin(x[0]) + 0.9993 * sympy.sin(
            x[2]) - 0.1952 * sympy.cos(x[1]) + 0.6173 * sympy.cos(x[4]) - 0.4588


@register_eq_class
class sincos_nv5_nt55_prog_42(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6125 * x[1] * sympy.sin(x[3]) - 0.5366 * x[1] * sympy.cos(x[2]) - 0.2809 * x[1] + 0.5727 * x[2] * x[3] + 0.9892 * \
                        x[2] * sympy.cos(x[0]) + 0.3661 * sympy.sin(x[3]) * sympy.cos(x[4]) + 0.4818 * sympy.sin(x[3]) + 0.5415 * sympy.cos(
            x[0]) + 0.1912 * sympy.cos(x[2]) - 0.6532 * sympy.cos(x[4]) + 0.0389


@register_eq_class
class sincos_nv5_nt55_prog_33(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9434 * x[1] + 0.2114 * x[3] * x[4] - 0.7506 * x[3] - 0.8779 * x[4] - 0.1833 * sympy.sin(x[0]) * sympy.sin(
            x[3]) + 0.6278 * sympy.sin(x[0]) + 0.3212 * sympy.sin(x[2]) * sympy.cos(x[0]) - 0.6912 * sympy.sin(x[2]) - 0.6526 * sympy.sin(
            x[3]) * sympy.cos(x[2]) - 0.2583 * sympy.sin(x[4]) * sympy.cos(x[1]) + 0.633


@register_eq_class
class sincos_nv5_nt55_prog_20(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7427 * x[0] * x[1] + 0.9279 * x[1] * x[3] - 0.2783 * x[1] - 0.1435 * x[2] * x[4] + 0.8656 * x[2] * sympy.sin(
            x[1]) - 0.7885 * x[2] - 0.799 * x[4] + 0.6343 * sympy.sin(x[0]) - 0.4339 * sympy.sin(x[2]) * sympy.cos(
            x[3]) + 0.5624 * sympy.sin(x[3]) - 0.7827


@register_eq_class
class sincos_nv5_nt55_prog_14(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0075 * x[0] * x[3] - 0.511 * x[0] + 0.4354 * x[1] * x[2] + 0.7477 * x[1] - 0.0735 * x[2] * sympy.sin(
            x[3]) - 0.1042 * x[3] + 0.3656 * x[4] * sympy.cos(x[3]) - 0.8323 * sympy.sin(x[4]) - 0.7584 * sympy.cos(x[1]) * sympy.cos(
            x[3]) - 0.7782 * sympy.cos(x[2]) - 0.6947


@register_eq_class
class sincos_nv5_nt55_prog_31(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3837 * x[0] * sympy.sin(x[3]) + 0.9283 * x[0] * sympy.cos(x[4]) + 0.0725 * x[1] * x[4] - 0.4834 * x[
            2] - 0.0961 * sympy.sin(x[0]) + 0.1647 * sympy.sin(x[1]) * sympy.sin(x[2]) + 0.0261 * sympy.sin(x[1]) + 0.7502 * sympy.sin(
            x[3]) * sympy.cos(x[1]) - 0.2599 * sympy.cos(x[3]) - 0.7838 * sympy.cos(x[4]) - 0.3193


@register_eq_class
class sincos_nv5_nt55_prog_48(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.444 * x[0] * x[4] - 0.6382 * x[0] * sympy.cos(x[3]) - 0.6096 * x[0] + 0.8462 * x[1] - 0.7352 * x[2] * x[
            4] - 0.2887 * x[2] - 0.4212 * x[3] - 0.5073 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.9785 * sympy.sin(x[1]) * sympy.cos(
            x[3]) + 0.0688 * sympy.sin(x[4]) + 0.2438


@register_eq_class
class sincos_nv5_nt55_prog_41(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.7972 * x[0] - 0.8678 * x[1] + 0.4763 * x[2] * sympy.cos(x[0]) - 0.0667 * x[2] * sympy.cos(x[4]) + 0.2519 * x[
            3] * sympy.cos(x[0]) + 0.7383 * x[3] * sympy.cos(x[2]) + 0.5964 * x[3] - 0.0404 * x[4] - 0.7571 * sympy.sin(
            x[2]) + 0.5132 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.2354


@register_eq_class
class sincos_nv5_nt55_prog_7(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6449 * x[0] * x[4] + 0.1764 * x[0] + 0.9283 * x[1] * sympy.sin(x[0]) + 0.1174 * x[1] - 0.7397 * x[2] * sympy.cos(
            x[4]) - 0.8867 * x[2] + 0.244 * x[3] * sympy.cos(x[4]) + 0.3295 * x[3] - 0.1753 * x[4] + 0.177 * sympy.sin(x[2]) * sympy.cos(
            x[3]) - 0.381


@register_eq_class
class sincos_nv5_nt55_prog_37(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8393 * x[0] + 0.3647 * x[1] - 0.3716 * x[2] * sympy.sin(x[3]) + 0.4563 * x[2] * sympy.cos(x[1]) + 0.1183 * x[
            3] * sympy.cos(x[1]) + 0.7451 * x[4] * sympy.cos(x[0]) + 0.6221 * x[4] + 0.6797 * sympy.sin(x[2]) * sympy.sin(
            x[4]) + 0.4268 * sympy.sin(x[2]) + 0.7971 * sympy.cos(x[3]) + 0.3363


@register_eq_class
class sincos_nv5_nt55_prog_15(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8363 * x[0] * x[3] + 0.2892 * x[0] + 0.3887 * x[1] - 0.1758 * x[2] * x[4] - 0.9924 * x[2] * sympy.cos(
            x[3]) - 0.8585 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.1965 * sympy.sin(x[3]) - 0.8502 * sympy.sin(x[4]) + 0.8562 * sympy.cos(
            x[2]) + 0.822 * sympy.cos(x[3]) * sympy.cos(x[4]) - 0.0978


@register_eq_class
class sincos_nv5_nt55_prog_23(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1194 * x[0] * sympy.sin(x[1]) - 0.2908 * x[1] * sympy.cos(x[4]) - 0.4886 * x[2] * sympy.sin(x[0]) - 0.0681 * x[
            2] + 0.7659 * x[3] * sympy.sin(x[4]) - 0.6997 * x[3] + 0.1923 * x[4] * sympy.cos(x[0]) + 0.1667 * sympy.cos(
            x[0]) - 0.7861 * sympy.cos(x[1]) - 0.4293 * sympy.cos(x[4]) - 0.2977


@register_eq_class
class sincos_nv5_nt55_prog_30(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1525 * x[1] * sympy.cos(x[4]) + 0.8588 * x[2] + 0.3317 * x[4] * sympy.cos(x[0]) + 0.3854 * x[4] * sympy.cos(
            x[2]) + 0.1675 * x[4] - 0.1942 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.795 * sympy.sin(x[0]) * sympy.cos(
            x[2]) + 0.5016 * sympy.cos(x[0]) - 0.8176 * sympy.cos(x[1]) - 0.476 * sympy.cos(x[3]) - 0.5536


@register_eq_class
class sincos_nv5_nt55_prog_28(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1884 * x[0] * x[4] - 0.7616 * x[0] + 0.4412 * x[1] * x[2] - 0.1637 * x[2] * x[3] + 0.4994 * x[3] + 0.6989 * x[
            4] + 0.8379 * sympy.sin(x[1]) + 0.658 * sympy.sin(x[2]) - 0.5612 * sympy.sin(x[4]) * sympy.cos(x[1]) + 0.608 * sympy.cos(
            x[3]) * sympy.cos(x[4]) + 0.5312


@register_eq_class
class sincos_nv5_nt55_prog_17(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9463 * x[0] * x[3] + 0.4448 * x[1] * sympy.sin(x[2]) - 0.8179 * x[1] + 0.9812 * x[4] * sympy.sin(
            x[3]) + 0.4985 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.4823 * sympy.sin(x[2]) + 0.0901 * sympy.sin(x[3]) + 0.6817 * sympy.cos(
            x[0]) + 0.579 * sympy.cos(x[1]) * sympy.cos(x[3]) - 0.3676 * sympy.cos(x[4]) + 0.433


@register_eq_class
class sincos_nv5_nt55_prog_43(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5576 * x[0] * x[1] - 0.2429 * x[0] - 0.7134 * x[1] * x[2] + 0.4669 * x[2] + 0.1219 * x[3] * sympy.sin(
            x[2]) - 0.527 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.6424 * sympy.sin(x[2]) * sympy.cos(x[4]) - 0.851 * sympy.cos(
            x[1]) - 0.3604 * sympy.cos(x[3]) - 0.0475 * sympy.cos(x[4]) + 0.8624


@register_eq_class
class sincos_nv5_nt55_prog_2(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3012 * x[0] * x[3] - 0.2348 * x[0] - 0.8727 * x[1] * sympy.cos(x[4]) - 0.4123 * x[1] - 0.1288 * x[2] * sympy.sin(
            x[4]) + 0.2243 * x[3] + 0.8088 * x[4] + 0.974 * sympy.sin(x[2]) + 0.3582 * sympy.cos(x[2]) * sympy.cos(
            x[3]) - 0.5457 * sympy.cos(x[3]) * sympy.cos(x[4]) - 0.2387


@register_eq_class
class sincos_nv5_nt55_prog_4(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0203 * x[0] * sympy.sin(x[4]) + 0.6056 * x[0] + 0.8209 * x[1] * sympy.cos(x[4]) + 0.1261 * x[1] + 0.5846 * x[
            2] * sympy.cos(x[1]) - 0.92 * x[3] * sympy.cos(x[4]) - 0.7875 * x[4] * sympy.cos(x[2]) + 0.1995 * x[4] - 0.474 * sympy.sin(
            x[2]) + 0.5068 * sympy.cos(x[3]) - 0.8695


@register_eq_class
class sincos_nv5_nt55_prog_45(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3045 * x[0] * x[1] + 0.7926 * x[0] * sympy.sin(x[3]) - 0.7072 * x[1] + 0.1823 * x[2] * sympy.cos(x[4]) - 0.3647 * \
                        x[2] + 0.308 * x[4] - 0.0992 * sympy.sin(x[0]) * sympy.cos(x[4]) - 0.9136 * sympy.sin(x[1]) * sympy.cos(
            x[2]) + 0.0345 * sympy.cos(x[0]) - 0.3145 * sympy.cos(x[3]) + 0.5744


@register_eq_class
class sincos_nv5_nt55_prog_49(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2291 * x[0] * sympy.cos(x[2]) - 0.6606 * x[1] * sympy.sin(x[4]) + 0.6109 * x[1] * sympy.cos(x[0]) - 0.0533 * x[
            3] - 0.0485 * x[4] * sympy.sin(x[3]) - 0.9368 * x[4] * sympy.cos(x[0]) - 0.2694 * sympy.sin(x[0]) - 0.0993 * sympy.sin(
            x[1]) - 0.3054 * sympy.sin(x[2]) + 0.5861 * sympy.cos(x[4]) - 0.8222


@register_eq_class
class sincos_nv5_nt55_prog_11(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9806 * x[0] * x[4] - 0.4982 * x[0] * sympy.cos(x[2]) + 0.2006 * x[1] * sympy.cos(x[4]) + 0.3465 * x[1] - 0.3135 * \
                        x[3] + 0.4243 * x[4] * sympy.sin(x[3]) + 0.3339 * x[4] + 0.986 * sympy.sin(x[0]) * sympy.sin(
            x[3]) - 0.2671 * sympy.cos(x[0]) + 0.3868 * sympy.cos(x[2]) - 0.5088


@register_eq_class
class sincos_nv5_nt55_prog_10(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9706 * x[0] * sympy.cos(x[2]) - 0.795 * x[1] * x[3] - 0.8507 * x[1] + 0.3411 * x[2] * sympy.cos(x[4]) - 0.4596 * \
                        x[3] - 0.4345 * x[4] * sympy.cos(x[3]) - 0.785 * sympy.sin(x[0]) + 0.3201 * sympy.sin(x[1]) * sympy.sin(
            x[2]) - 0.8577 * sympy.sin(x[2]) - 0.563 * sympy.sin(x[4]) - 0.0398


@register_eq_class
class sincos_nv5_nt55_prog_1(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5417 * x[0] * x[3] + 0.4562 * x[1] * sympy.sin(x[3]) + 0.0297 * x[1] + 0.3659 * x[2] + 0.638 * x[3] * sympy.sin(
            x[2]) - 0.0682 * x[3] - 0.7869 * sympy.sin(x[0]) - 0.7653 * sympy.sin(x[3]) * sympy.sin(x[4]) - 0.5842 * sympy.sin(
            x[4]) * sympy.cos(x[0]) + 0.1699 * sympy.sin(x[4]) + 0.7374


@register_eq_class
class sincos_nv5_nt55_prog_40(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8196 * x[0] * x[1] - 0.2372 * x[0] * sympy.sin(x[3]) + 0.3257 * x[0] + 0.5802 * x[1] * sympy.cos(x[4]) - 0.3062 * \
                        x[1] + 0.2672 * x[2] * x[3] - 0.6417 * x[2] - 0.8347 * x[4] - 0.7887 * sympy.sin(x[1]) * sympy.sin(
            x[2]) - 0.3309 * sympy.cos(x[3]) + 0.279


@register_eq_class
class sincos_nv5_nt55_prog_29(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4791 * x[0] * x[4] - 0.6679 * x[0] * sympy.sin(x[1]) + 0.8089 * x[0] * sympy.sin(x[2]) - 0.6979 * x[
            0] * sympy.cos(x[3]) + 0.7299 * x[0] + 0.8357 * x[1] - 0.4728 * x[3] - 0.1912 * x[4] * sympy.sin(x[1]) + 0.9518 * sympy.sin(
            x[2]) - 0.5176 * sympy.cos(x[4]) - 0.2955


@register_eq_class
class sincos_nv5_nt55_prog_22(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1572 * x[0] * x[3] + 0.0928 * x[0] * sympy.sin(x[1]) + 0.6332 * x[0] * sympy.cos(x[4]) + 0.2938 * x[2] * x[
            3] - 0.3791 * x[2] + 0.6417 * x[3] - 0.7172 * x[4] + 0.0884 * sympy.sin(x[0]) - 0.5745 * sympy.sin(x[1]) + 0.3306 * sympy.sin(
            x[2]) * sympy.sin(x[4]) + 0.7766


@register_eq_class
class sincos_nv5_nt55_prog_27(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.5146 * x[0] * x[2] + 0.9339 * x[0] * sympy.sin(x[4]) + 0.645 * x[0] * sympy.cos(x[1]) - 0.8743 * x[0] + 0.8909 * \
                        x[1] + 0.7102 * x[2] + 0.8397 * sympy.sin(x[0]) * sympy.cos(x[3]) - 0.3065 * sympy.sin(x[3]) * sympy.cos(
            x[1]) - 0.9238 * sympy.sin(x[3]) + 0.6125 * sympy.cos(x[4]) - 0.8132


@register_eq_class
class sincos_nv5_nt55_prog_34(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6701 * x[0] * x[4] - 0.2159 * x[1] * sympy.sin(x[0]) - 0.4882 * x[2] * sympy.cos(x[3]) + 0.8728 * x[3] + 0.3807 * \
                        x[4] - 0.0945 * sympy.sin(x[1]) * sympy.cos(x[3]) - 0.2305 * sympy.sin(x[1]) * sympy.cos(x[4]) - 0.0952 * sympy.sin(
            x[2]) - 0.8856 * sympy.cos(x[0]) + 0.4833 * sympy.cos(x[1]) - 0.972


@register_eq_class
class sincos_nv5_nt55_prog_16(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.662 * x[0] * sympy.sin(x[3]) - 0.4207 * x[2] * sympy.cos(x[3]) + 0.0691 * x[3] * sympy.sin(x[1]) + 0.4195 * x[
            4] - 0.1608 * sympy.sin(x[1]) * sympy.sin(x[4]) + 0.0626 * sympy.sin(x[1]) - 0.5921 * sympy.sin(x[2]) + 0.124 * sympy.sin(
            x[3]) * sympy.cos(x[4]) + 0.1266 * sympy.sin(x[3]) + 0.5609 * sympy.cos(x[0]) + 0.3959


@register_eq_class
class sincos_nv5_nt55_prog_13(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2848 * x[0] * x[1] + 0.0184 * x[0] * sympy.cos(x[3]) - 0.2304 * x[0] - 0.6309 * x[2] * x[3] + 0.6466 * x[
            3] + 0.1282 * x[4] * sympy.cos(x[2]) + 0.4273 * x[4] + 0.6431 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.452 * sympy.sin(
            x[2]) - 0.7125 * sympy.cos(x[1]) - 0.9915


@register_eq_class
class sincos_nv5_nt55_prog_47(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1142 * x[1] * x[4] - 0.1594 * x[2] * sympy.sin(x[1]) + 0.8363 * x[2] - 0.2502 * x[3] * x[4] + 0.9133 * x[
            3] * sympy.cos(x[0]) + 0.5465 * x[4] - 0.9156 * sympy.sin(x[0]) - 0.6482 * sympy.cos(x[1]) * sympy.cos(
            x[3]) + 0.8679 * sympy.cos(x[1]) - 0.4098 * sympy.cos(x[3]) - 0.4313


@register_eq_class
class sincos_nv5_nt55_prog_36(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4445 * x[0] * x[3] + 0.887 * x[0] - 0.3572 * x[1] * x[4] - 0.2507 * x[1] - 0.1232 * x[2] * sympy.cos(
            x[0]) - 0.0303 * x[2] + 0.4994 * x[4] * sympy.sin(x[3]) - 0.4732 * x[4] * sympy.cos(x[0]) - 0.3467 * x[4] + 0.6612 * sympy.sin(
            x[3]) + 0.6719


@register_eq_class
class sincos_nv5_nt55_prog_44(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0852 * x[0] * x[3] - 0.6047 * x[1] * sympy.sin(x[3]) + 0.1821 * x[1] - 0.9785 * x[2] * sympy.sin(x[4]) - 0.1164 * \
                        x[4] * sympy.sin(x[1]) + 0.1626 * x[4] + 0.2932 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.8309 * sympy.sin(
            x[3]) + 0.3372 * sympy.cos(x[0]) - 0.6081 * sympy.cos(x[2]) + 0.6697


@register_eq_class
class sincos_nv5_nt55_prog_6(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.7666 * x[0] * x[2] + 0.2223 * x[1] * x[2] + 0.3913 * x[1] - 0.8791 * x[2] - 0.3625 * x[3] * sympy.sin(
            x[1]) - 0.8499 * x[3] * sympy.cos(x[0]) + 0.3701 * x[3] - 0.1628 * x[4] * sympy.sin(x[0]) - 0.3167 * x[4] - 0.8401 * sympy.sin(
            x[0]) - 0.6255


@register_eq_class
class sincos_nv5_nt55_prog_18(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9341 * x[0] * x[4] - 0.1507 * x[0] + 0.9571 * x[2] * sympy.cos(x[3]) - 0.2251 * x[2] * sympy.cos(x[4]) + 0.7349 * \
                        x[3] * sympy.sin(x[1]) + 0.6049 * x[4] * sympy.cos(x[3]) + 0.5397 * sympy.sin(x[1]) - 0.6474 * sympy.sin(
            x[3]) + 0.2255 * sympy.sin(x[4]) - 0.3534 * sympy.cos(x[2]) + 0.7562


@register_eq_class
class sincos_nv5_nt55_prog_3(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4818 * x[0] * sympy.sin(x[4]) - 0.8507 * x[0] - 0.0966 * x[1] - 0.9748 * x[2] * x[3] - 0.7097 * x[3] * x[
            4] - 0.4638 * x[3] * sympy.cos(x[0]) - 0.191 * x[4] - 0.0154 * sympy.sin(x[2]) * sympy.cos(x[4]) + 0.16 * sympy.cos(
            x[2]) + 0.2525 * sympy.cos(x[3]) + 0.4967


@register_eq_class
class sincos_nv5_nt55_prog_24(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4328 * x[0] - 0.9792 * x[1] * sympy.sin(x[0]) - 0.9778 * x[1] - 0.7173 * x[2] * sympy.sin(x[1]) + 0.4948 * x[
            4] - 0.6809 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.2273 * sympy.sin(x[1]) * sympy.cos(x[3]) - 0.7999 * sympy.sin(
            x[2]) * sympy.cos(x[3]) + 0.3536 * sympy.cos(x[2]) + 0.0806 * sympy.cos(x[3]) + 0.5596


@register_eq_class
class sincos_nv5_nt55_prog_12(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9169 * x[0] * x[1] - 0.4231 * x[0] * x[3] - 0.4985 * x[0] - 0.7829 * x[1] * sympy.sin(x[4]) + 0.9568 * x[
            1] - 0.8462 * x[2] * x[4] - 0.3897 * x[3] * sympy.cos(x[4]) + 0.426 * x[3] + 0.9025 * x[4] - 0.8952 * sympy.cos(x[2]) + 0.0054


@register_eq_class
class sincos_nv5_nt55_prog_25(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6466 * x[0] * x[2] - 0.2874 * x[0] - 0.4222 * x[2] * sympy.sin(x[4]) - 0.0897 * x[3] * sympy.sin(x[1]) + 0.8373 * \
                        x[3] - 0.174 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.2267 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.9745 * sympy.cos(
            x[1]) - 0.8666 * sympy.cos(x[2]) + 0.2417 * sympy.cos(x[4]) - 0.1574


@register_eq_class
class sincos_nv5_nt55_prog_21(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4942 * x[0] * x[3] + 0.622 * x[0] * sympy.sin(x[1]) - 0.4379 * x[0] * sympy.sin(x[4]) + 0.2319 * x[1] * sympy.sin(
            x[4]) - 0.6406 * x[1] - 0.9133 * x[3] * x[4] - 0.3618 * x[4] - 0.34 * sympy.cos(x[0]) - 0.5876 * sympy.cos(
            x[2]) - 0.9215 * sympy.cos(x[3]) + 0.2742


@register_eq_class
class sincos_nv5_nt55_prog_26(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3487 * x[1] * x[2] + 0.9566 * x[1] * x[3] + 0.4933 * x[2] - 0.0431 * x[3] * sympy.cos(x[0]) - 0.518 * x[
            3] + 0.4407 * x[4] - 0.4382 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.1734 * sympy.sin(x[0]) + 0.2738 * sympy.sin(
            x[1]) + 0.1763 * sympy.sin(x[2]) * sympy.sin(x[4]) - 0.5366


@register_eq_class
class sincos_nv5_nt55_prog_39(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5869 * x[1] * x[2] + 0.8837 * x[1] - 0.3193 * x[3] - 0.9903 * x[4] * sympy.sin(x[3]) + 0.1064 * x[
            4] + 0.9787 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.0641 * sympy.sin(x[0]) - 0.7479 * sympy.sin(x[2]) * sympy.cos(
            x[4]) - 0.0421 * sympy.sin(x[2]) + 0.0949 * sympy.cos(x[0]) * sympy.cos(x[2]) - 0.4646


@register_eq_class
class sincos_nv5_nt55_prog_19(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7187 * x[0] * x[2] + 0.6208 * x[1] * x[3] + 0.5727 * x[1] - 0.8438 * x[3] * sympy.cos(x[0]) - 0.1925 * x[
            3] + 0.5285 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.2671 * sympy.sin(x[4]) + 0.9874 * sympy.cos(x[0]) + 0.0494 * sympy.cos(
            x[2]) * sympy.cos(x[3]) + 0.7118 * sympy.cos(x[2]) + 0.7308


@register_eq_class
class sincos_nv5_nt55_prog_38(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4376 * x[0] * sympy.sin(x[2]) + 0.8594 * x[0] * sympy.sin(x[4]) + 0.8437 * x[0] - 0.3183 * x[2] * sympy.cos(
            x[4]) - 0.3793 * x[3] + 0.3901 * x[4] - 0.754 * sympy.sin(x[1]) + 0.9048 * sympy.sin(x[3]) * sympy.sin(
            x[4]) + 0.1145 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.7263 * sympy.cos(x[2]) + 0.4902


@register_eq_class
class sincos_nv5_nt55_prog_9(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7066 * x[0] * x[3] + 0.5513 * x[0] + 0.6577 * x[2] * x[3] - 0.7612 * x[4] * sympy.sin(x[3]) + 0.9294 * x[
            4] - 0.2314 * sympy.sin(x[2]) * sympy.cos(x[4]) + 0.5847 * sympy.sin(x[2]) + 0.5884 * sympy.sin(x[3]) + 0.3221 * sympy.cos(
            x[1]) * sympy.cos(x[3]) + 0.2867 * sympy.cos(x[1]) - 0.801


@register_eq_class
class sincos_nv5_nt55_prog_32(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2211 * x[0] - 0.6423 * x[1] * sympy.sin(x[2]) - 0.8074 * x[2] * x[4] - 0.5497 * x[3] + 0.7833 * x[4] * sympy.cos(
            x[1]) + 0.2617 * sympy.sin(x[0]) * sympy.sin(x[4]) + 0.1922 * sympy.cos(x[1]) - 0.0114 * sympy.cos(x[2]) * sympy.cos(
            x[3]) - 0.4358 * sympy.cos(x[2]) - 0.0398 * sympy.cos(x[4]) + 0.0741


@register_eq_class
class sincos_nv5_nt55_prog_5(KnownEquation):
    _eq_name = 'sincos_nv5_nt55_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8973 * x[0] - 0.8648 * x[1] * x[3] + 0.261 * x[1] * sympy.sin(x[2]) - 0.3262 * x[1] - 0.6032 * x[2] * sympy.cos(
            x[0]) - 0.6415 * x[2] - 0.0452 * x[3] - 0.8909 * x[4] * sympy.cos(x[2]) - 0.3137 * x[4] + 0.2508 * sympy.sin(x[2]) * sympy.sin(
            x[3]) - 0.0501


@register_eq_class
class inv_nv5_nt58_prog_46(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0756 * x[0] * x[4] - 0.5613 * x[1] * x[4] + 0.3006 * x[1] + 0.2882 * x[2] / x[3] + 0.7436 + 0.62 / x[4] - 0.7426 / \
                        x[3] + 0.6361 * x[4] / x[2] + 0.2377 / x[2] - 0.3767 / (x[1] * x[3]) + 0.0745 * x[2] / x[0] - 0.3124 / x[
                            0] + 0.699 / (x[0] * x[3]) + 0.191 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_0(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9546 * x[0] - 0.8991 * x[1] - 0.2923 * x[2] / x[3] + 0.3753 * x[3] + 0.0876 * x[4] + 0.8835 + 0.3459 / (
                x[3] * x[4]) - 0.6193 * x[4] / x[2] + 0.1259 / x[2] - 0.2869 * x[2] / x[1] - 0.8869 / (x[1] * x[3]) + 0.3782 * x[1] / x[
                            0] + 0.5851 * x[4] / x[0] - 0.7377 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_35(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3487 * x[0] * x[1] - 0.2375 * x[1] * x[4] + 0.3883 * x[1] - 0.9959 * x[1] / x[3] - 0.2522 * x[2] / x[
            3] - 0.1016 * x[3] + 0.2537 * x[3] / x[4] + 0.4962 * x[4] + 0.829 + 0.7153 / x[2] - 0.2187 * x[2] / x[1] - 0.9942 * x[2] / x[
                            0] + 0.2293 / x[0] - 0.9517 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_8(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4031 * x[0] * x[2] + 0.2271 * x[0] / x[3] - 0.6512 * x[1] + 0.6392 * x[2] - 0.3789 * x[2] / x[4] - 0.3944 * x[
            3] + 0.9057 * x[4] - 0.4267 - 0.3047 * x[4] / x[3] + 0.6291 / (x[1] * x[4]) + 0.115 / (x[1] * x[3]) + 0.8634 / (
                                x[1] * x[2]) + 0.1853 * x[4] / x[0] + 0.2171 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_42(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9681 * x[0] + 0.2916 * x[1] * x[2] - 0.27 * x[1] * x[4] + 0.7248 * x[2] * x[3] - 0.2846 * x[2] + 0.3634 + 0.436 / \
                        x[4] + 0.1087 * x[4] / x[3] + 0.0899 / x[3] + 0.9038 * x[4] / x[2] - 0.0726 / x[1] + 0.5618 / (
                                x[1] * x[3]) - 0.1514 * x[4] / x[0] + 0.9699 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt58_prog_33(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3651 * x[0] * x[2] + 0.6874 * x[0] * x[3] + 0.7134 * x[0] / x[1] + 0.2164 * x[1] / x[3] + 0.7969 * x[2] * x[
            4] - 0.4539 * x[3] + 0.1967 + 0.6337 / x[4] - 0.7757 / x[2] - 0.6968 * x[2] / x[1] - 0.5424 * x[4] / x[1] + 0.1859 / x[
                            1] + 0.689 * x[4] / x[0] - 0.492 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_20(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1357 * x[0] + 0.6296 * x[0] / x[2] - 0.4232 * x[1] - 0.1916 * x[1] / x[4] + 0.5741 * x[2] + 0.1722 + 0.5001 / x[
            4] + 0.3231 / x[3] + 0.1632 * x[3] / x[2] + 0.4704 * x[4] / x[2] - 0.2608 * x[2] / x[1] + 0.5667 * x[3] / x[1] + 0.9889 * x[4] / \
                        x[0] - 0.0923 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_14(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8034 * x[0] * x[3] + 0.138 * x[0] + 0.6025 * x[0] / x[1] - 0.9665 * x[1] * x[2] - 0.3222 * x[1] - 0.1112 * x[2] * \
                        x[3] + 0.7179 * x[2] / x[4] + 0.7408 * x[4] + 0.3718 - 0.6135 * x[4] / x[3] + 0.7583 / x[3] - 0.5801 / x[
                            2] + 0.7132 * x[3] / x[1] + 0.5432 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt58_prog_31(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4568 * x[0] * x[1] + 0.9314 * x[0] * x[4] + 0.1101 * x[0] / x[2] + 0.3202 * x[1] * x[3] + 0.9037 * x[2] / x[
            3] + 0.5119 * x[4] + 0.2193 - 0.9712 * x[4] / x[3] + 0.7934 / x[3] - 0.7128 / x[2] + 0.4225 * x[2] / x[1] - 0.3368 * x[4] / x[
                            1] - 0.6663 / x[1] - 0.2321 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_48(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0546 * x[0] * x[2] + 0.5333 * x[0] - 0.0766 * x[0] / x[4] + 0.1163 * x[0] / x[3] + 0.3706 * x[1] * x[
            2] + 0.1221 * x[2] - 0.1618 * x[3] + 0.5575 * x[4] - 0.0763 + 0.308 * x[3] / x[2] + 0.1392 / (x[2] * x[4]) - 0.7185 * x[4] / x[
                            1] + 0.6703 / x[1] + 0.5267 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_41(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6291 * x[0] * x[4] + 0.786 * x[1] * x[2] - 0.4788 * x[1] * x[3] + 0.754 * x[1] - 0.891 * x[2] * x[3] + 0.9282 * \
                        x[3] + 0.6112 - 0.7173 / x[4] - 0.5969 * x[4] / x[3] - 0.1041 * x[4] / x[2] - 0.2392 / x[2] - 0.8816 / x[
                            0] + 0.7571 / (x[0] * x[3]) + 0.448 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_7(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6126 * x[0] * x[1] - 0.8209 * x[0] - 0.2491 * x[0] / x[3] - 0.927 * x[0] / x[2] + 0.9981 * x[3] - 0.6348 * x[
            4] + 0.0494 - 0.2517 * x[4] / x[3] - 0.2815 / x[2] + 0.3988 * x[3] / x[1] + 0.742 / x[1] + 0.3665 / (x[1] * x[4]) + 0.4477 / (
                                x[1] * x[2]) + 0.8045 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt58_prog_37(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2279 * x[0] * x[3] - 0.5527 * x[0] * x[4] + 0.3438 * x[1] * x[2] - 0.9016 * x[1] * x[3] - 0.2521 * x[
            1] - 0.1224 * x[2] * x[3] - 0.5949 * x[2] + 0.0372 - 0.9973 / x[4] + 0.0048 / x[3] - 0.2906 / (x[2] * x[4]) + 0.4654 / (
                                x[1] * x[4]) + 0.7196 * x[2] / x[0] - 0.4399 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_15(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4302 * x[0] * x[3] + 0.7799 * x[0] - 0.1554 * x[1] / x[4] - 0.1721 * x[2] - 0.7817 * x[3] - 0.2164 * x[3] / x[
            4] + 0.4197 - 0.2945 / x[4] - 0.3652 * x[4] / x[2] + 0.2129 / (x[2] * x[3]) - 0.0964 * x[2] / x[1] - 0.4474 / x[1] - 0.7136 / (
                                x[1] * x[3]) + 0.1485 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt58_prog_23(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.7538 * x[0] * x[2] - 0.4271 * x[0] / x[4] + 0.1815 * x[0] / x[3] + 0.8716 * x[1] / x[3] + 0.732 * x[2] / x[
            3] - 0.8512 - 0.0732 / x[4] - 0.5422 * x[4] / x[3] - 0.7772 / x[3] + 0.8006 * x[4] / x[2] - 0.8919 / x[2] - 0.1645 / x[
                            1] - 0.6321 / (x[1] * x[2]) + 0.5269 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_30(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9033 * x[0] - 0.8285 * x[1] / x[4] + 0.6975 * x[2] - 0.8636 * x[3] - 0.9199 * x[3] / x[4] + 0.847 - 0.699 / x[
            4] - 0.098 / (x[2] * x[3]) - 0.0584 * x[2] / x[1] + 0.9471 / x[1] - 0.7776 / (x[1] * x[3]) + 0.1196 * x[3] / x[0] + 0.8311 / (
                                x[0] * x[2]) - 0.5859 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_28(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6958 * x[0] + 0.2175 * x[0] / x[1] + 0.1117 * x[1] * x[3] - 0.8707 * x[1] + 0.1638 * x[2] * x[3] + 0.2496 * x[2] * \
                        x[4] - 0.5764 * x[4] - 0.8356 + 0.8713 / x[3] - 0.2541 / x[2] - 0.5692 * x[2] / x[1] + 0.5007 * x[4] / x[
                            1] + 0.715 / (x[0] * x[4]) + 0.4093 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_17(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4401 * x[0] * x[2] + 0.495 * x[1] * x[2] + 0.9814 * x[1] * x[3] - 0.9514 * x[1] * x[4] + 0.4241 * x[2] * x[
            3] - 0.5919 * x[3] + 0.215 + 0.636 / x[4] - 0.9466 * x[4] / x[2] - 0.5277 / x[2] + 0.9069 / x[1] + 0.5951 * x[3] / x[
                            0] + 0.361 / x[0] - 0.5124 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_43(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9396 * x[0] * x[2] - 0.6979 * x[0] * x[3] + 0.9429 * x[0] / x[4] + 0.087 * x[1] / x[3] - 0.2645 * x[3] / x[
            4] - 0.4638 + 0.1023 / x[4] - 0.6406 / x[3] + 0.3104 / x[2] - 0.1522 / x[1] + 0.5157 / (x[1] * x[4]) - 0.7581 / (
                                x[1] * x[2]) - 0.6057 / x[0] + 0.4961 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_2(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9921 * x[0] * x[2] + 0.4997 * x[0] * x[3] - 0.96 * x[1] * x[3] + 0.8794 * x[1] / x[2] + 0.0047 + 0.5907 / x[
            4] + 0.6458 / x[3] - 0.0517 / (x[3] * x[4]) + 0.8556 / x[2] + 0.0646 / (x[2] * x[4]) - 0.8514 / (x[2] * x[3]) + 0.5637 / x[
                            1] - 0.8888 / x[0] - 0.7514 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_4(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9258 * x[0] + 0.8994 * x[1] * x[2] - 0.4938 * x[1] * x[3] - 0.1923 * x[1] - 0.5802 * x[1] / x[4] - 0.9055 * x[
            2] + 0.3016 * x[3] + 0.0308 - 0.356 / x[4] - 0.2749 / (x[2] * x[4]) + 0.7712 / (x[2] * x[3]) - 0.6073 * x[1] / x[0] + 0.7146 * \
                        x[4] / x[0] - 0.9913 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt58_prog_45(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.222 * x[0] * x[3] - 0.4108 * x[0] + 0.6815 * x[0] / x[4] - 0.4312 * x[0] / x[1] + 0.6817 * x[1] * x[4] - 0.0183 * \
                        x[3] - 0.0325 * x[4] + 0.3479 + 0.9444 / (x[3] * x[4]) + 0.0001 * x[3] / x[2] + 0.2751 / x[2] + 0.6304 * x[2] / x[
                            1] + 0.7334 * x[3] / x[1] + 0.4883 / x[1]


@register_eq_class
class inv_nv5_nt58_prog_49(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5805 * x[0] * x[4] - 0.2965 * x[0] - 0.2523 * x[0] / x[1] - 0.8343 * x[1] / x[3] + 0.789 * x[2] * x[4] - 0.4207 * \
                        x[2] - 0.0656 - 0.5739 / x[4] - 0.953 * x[4] / x[3] - 0.0857 / x[3] - 0.2608 / (x[2] * x[3]) - 0.376 * x[2] / x[
                            1] - 0.3723 / x[1] - 0.0597 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_11(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9556 * x[0] * x[3] + 0.3246 * x[0] * x[4] + 0.7382 * x[0] - 0.6311 * x[1] * x[4] + 0.8821 * x[1] / x[2] - 0.305 * \
                        x[2] + 0.3021 * x[2] / x[3] + 0.278 * x[4] - 0.9626 + 0.9902 / x[3] + 0.4732 * x[4] / x[2] + 0.1409 / x[
                            1] - 0.0436 * x[1] / x[0] - 0.3521 * x[2] / x[0]


@register_eq_class
class inv_nv5_nt58_prog_10(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2996 * x[0] * x[3] + 0.4344 * x[0] * x[4] + 0.0326 * x[1] * x[3] + 0.9677 * x[3] - 0.605 - 0.3599 / x[
            4] + 0.8327 * x[4] / x[3] - 0.9722 * x[3] / x[2] - 0.9615 / x[2] - 0.7482 / (x[2] * x[4]) - 0.516 * x[2] / x[1] - 0.9585 * x[
                            4] / x[1] - 0.0635 / x[1] + 0.0545 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_1(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6988 * x[0] * x[2] - 0.0226 * x[0] + 0.4165 * x[0] / x[3] - 0.0406 * x[1] * x[4] + 0.4339 * x[2] / x[4] + 0.1149 * \
                        x[3] - 0.3902 * x[3] / x[4] + 0.623 * x[4] + 0.7394 - 0.2818 / x[2] - 0.5019 / (x[2] * x[3]) + 0.9326 / x[
                            1] + 0.5013 / (x[0] * x[4]) - 0.3232 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_40(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2082 * x[1] - 0.0141 * x[1] / x[4] - 0.7833 * x[1] / x[3] + 0.2168 * x[1] / x[2] - 0.4174 * x[
            4] + 0.5934 - 0.6219 / x[3] - 0.5115 / (x[3] * x[4]) + 0.7406 * x[3] / x[2] - 0.5422 / x[2] + 0.1532 / x[0] - 0.9973 / (
                                x[0] * x[4]) + 0.8748 / (x[0] * x[2]) - 0.8836 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_29(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3741 * x[0] + 0.3896 * x[0] / x[4] - 0.7381 * x[0] / x[3] + 0.0063 * x[0] / x[2] + 0.5815 * x[1] - 0.4935 * x[
            2] - 0.283 * x[3] + 0.6351 + 0.5509 / x[4] - 0.5528 / (x[3] * x[4]) - 0.127 / (x[2] * x[4]) - 0.9055 / (
                                x[2] * x[3]) + 0.6046 / (x[1] * x[3]) - 0.6785 * x[1] / x[0]


@register_eq_class
class inv_nv5_nt58_prog_22(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7504 * x[1] - 0.3531 * x[1] / x[2] + 0.5948 * x[3] / x[4] + 0.7651 + 0.9565 / x[4] - 0.3716 / x[3] - 0.5466 / x[
            2] - 0.6532 / (x[2] * x[4]) + 0.7485 * x[3] / x[1] - 0.9248 * x[4] / x[1] - 0.1942 * x[1] / x[0] + 0.8157 * x[4] / x[
                            0] + 0.2774 / x[0] - 0.9597 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_27(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5615 * x[0] * x[1] + 0.0579 * x[1] * x[2] - 0.0511 * x[1] * x[4] + 0.1607 * x[3] + 0.2715 + 0.9996 / x[
            4] + 0.1419 / x[2] - 0.7826 / (x[2] * x[4]) - 0.9529 / (x[2] * x[3]) - 0.1602 * x[3] / x[1] + 0.9397 / x[1] + 0.866 * x[3] / x[
                            0] + 0.6542 / x[0] - 0.9481 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt58_prog_34(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8369 * x[0] * x[1] - 0.7274 * x[0] / x[4] + 0.0851 * x[1] * x[2] - 0.1284 * x[1] * x[4] + 0.4047 * x[
            3] + 0.8342 + 0.8975 / x[4] - 0.9477 / x[2] - 0.5969 / (x[2] * x[4]) - 0.4931 / x[1] - 0.3009 / (x[1] * x[3]) + 0.122 * x[2] / \
                        x[0] + 0.3399 * x[3] / x[0] - 0.3387 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_16(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.605 * x[0] + 0.0788 * x[1] / x[4] - 0.6287 * x[1] / x[3] + 0.6235 * x[1] / x[2] + 0.9486 * x[2] / x[4] - 0.511 * \
                        x[3] / x[4] + 0.7664 - 0.7401 / x[4] + 0.7065 / x[3] + 0.0581 * x[3] / x[2] + 0.706 / x[2] - 0.7209 / x[
                            1] + 0.7618 / (x[0] * x[4]) - 0.2797 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_13(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5292 * x[0] * x[4] - 0.0561 * x[0] / x[3] + 0.431 * x[1] + 0.7578 * x[1] / x[4] + 0.2621 * x[2] * x[3] + 0.6671 * \
                        x[2] - 0.4056 - 0.6286 / x[4] + 0.2501 / x[3] - 0.4767 / (x[3] * x[4]) - 0.7164 * x[2] / x[1] + 0.3594 / (
                                x[1] * x[3]) + 0.9037 * x[2] / x[0] - 0.9211 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_47(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1072 * x[0] * x[2] + 0.6065 * x[0] * x[4] + 0.51 * x[0] + 0.2788 * x[3] * x[4] - 0.7893 - 0.5371 / x[4] + 0.3783 / \
                        x[3] + 0.3501 * x[3] / x[2] - 0.1583 / x[2] + 0.0603 / (x[2] * x[4]) - 0.1461 * x[4] / x[1] - 0.5074 / x[
                            1] + 0.3686 * x[3] / x[0] + 0.565 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_36(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9113 * x[0] * x[1] + 0.0503 * x[0] + 0.8964 * x[0] / x[3] - 0.2656 * x[1] - 0.2258 * x[1] / x[3] - 0.4425 * x[1] / \
                        x[2] + 0.3989 * x[3] - 0.0027 * x[4] + 0.9302 + 0.9018 / (x[3] * x[4]) - 0.8052 / x[2] - 0.3449 / (
                                x[1] * x[4]) + 0.3043 * x[4] / x[0] - 0.5036 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt58_prog_44(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.7046 * x[0] + 0.2356 * x[0] / x[4] + 0.3615 * x[0] / x[1] + 0.609 * x[1] * x[4] + 0.6671 * x[2] / x[
            3] + 0.6433 + 0.8436 / x[4] - 0.6643 * x[4] / x[3] + 0.9538 / x[3] - 0.0649 / x[2] - 0.1753 / (x[2] * x[4]) + 0.5065 * x[2] / x[
                            1] + 0.4167 / x[1] + 0.2617 / (x[1] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_6(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1202 * x[0] * x[2] + 0.0558 * x[0] / x[1] - 0.0012 * x[1] - 0.5695 * x[1] / x[4] - 0.4794 * x[2] * x[
            3] - 0.6333 + 0.2444 / x[4] + 0.5185 / x[3] + 0.8041 * x[4] / x[2] - 0.8505 / x[2] + 0.0368 / (x[1] * x[3]) + 0.0118 / (
                                x[1] * x[2]) + 0.5616 * x[3] / x[0] - 0.3379 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_18(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3495 * x[0] * x[3] - 0.1881 * x[0] + 0.8964 * x[0] / x[1] + 0.3185 * x[1] / x[2] + 0.6938 * x[2] * x[4] - 0.5692 * \
                        x[3] / x[4] + 0.2199 * x[4] - 0.1214 - 0.8198 / x[3] + 0.9159 / x[2] - 0.5803 / x[1] + 0.8297 / (
                                x[1] * x[4]) - 0.262 / (x[1] * x[3]) - 0.0108 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt58_prog_3(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8197 * x[0] - 0.3893 * x[0] / x[4] - 0.3391 * x[0] / x[2] + 0.4624 * x[2] * x[3] + 0.4623 * x[3] * x[4] - 0.902 * \
                        x[3] + 0.7213 * x[4] - 0.2791 + 0.7562 / x[2] + 0.2099 / (x[2] * x[4]) + 0.5831 * x[2] / x[1] - 0.8335 * x[4] / x[
                            1] - 0.5976 / x[1] - 0.9722 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_24(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3653 * x[0] + 0.9756 * x[0] / x[4] - 0.6674 * x[0] / x[3] - 0.9338 * x[1] * x[4] - 0.8238 * x[1] / x[3] - 0.3892 * \
                        x[1] / x[2] - 0.134 * x[2] - 0.5946 * x[3] - 0.054 * x[3] / x[4] - 0.7025 * x[4] + 0.0073 + 0.1922 / (
                                x[2] * x[3]) + 0.331 / x[1] + 0.2151 * x[1] / x[0]


@register_eq_class
class inv_nv5_nt58_prog_12(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8576 * x[0] - 0.8605 * x[1] - 0.2824 * x[1] / x[3] + 0.5857 * x[2] / x[4] + 0.7621 * x[3] + 0.0739 * x[
            4] + 0.7589 - 0.0275 / (x[3] * x[4]) - 0.2566 / x[2] - 0.915 / (x[2] * x[3]) + 0.0872 / (x[1] * x[4]) + 0.4614 / (
                                x[1] * x[2]) + 0.0404 * x[3] / x[0] - 0.5022 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt58_prog_25(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8898 * x[0] * x[3] + 0.1515 * x[0] - 0.8173 * x[1] * x[3] - 0.2721 * x[1] * x[4] - 0.8763 * x[1] + 0.2598 * x[1] / \
                        x[2] - 0.7582 * x[2] + 0.3623 * x[2] / x[4] - 0.9642 - 0.1461 / x[4] + 0.7705 * x[4] / x[3] - 0.3694 / x[
                            3] - 0.0292 * x[1] / x[0] + 0.2611 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt58_prog_21(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2517 * x[0] * x[2] - 0.7786 * x[1] - 0.6943 * x[2] + 0.8146 * x[2] / x[3] - 0.6849 * x[3] * x[4] + 0.2833 * x[
            4] - 0.7931 + 0.9379 / x[3] - 0.1736 * x[3] / x[1] - 0.8682 * x[4] / x[1] - 0.8866 / (x[1] * x[2]) + 0.5644 * x[3] / x[
                            0] - 0.3916 * x[4] / x[0] + 0.7048 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_26(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3539 * x[0] / x[3] + 0.7936 * x[0] / x[1] + 0.4031 * x[1] * x[4] - 0.5577 * x[1] + 0.4626 * x[2] * x[3] - 0.5229 * \
                        x[2] * x[4] + 0.328 * x[3] / x[4] + 0.987 - 0.6582 / x[4] + 0.2302 / x[3] - 0.2587 / x[2] - 0.0026 / (
                                x[1] * x[3]) + 0.578 * x[4] / x[0] + 0.3027 / x[0]


@register_eq_class
class inv_nv5_nt58_prog_39(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6264 * x[0] * x[2] + 0.3941 * x[0] - 0.0911 * x[1] / x[3] + 0.6629 * x[2] - 0.7426 * x[2] / x[4] - 0.3939 * x[
            3] + 0.5223 * x[3] / x[4] - 0.3339 - 0.2553 / x[4] + 0.7237 / (x[2] * x[3]) - 0.1804 * x[4] / x[1] - 0.4603 / x[1] + 0.2337 / (
                                x[1] * x[2]) + 0.5613 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_19(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2455 * x[0] * x[1] + 0.4286 * x[0] * x[2] + 0.7202 * x[0] * x[4] + 0.3262 * x[0] + 0.8754 * x[1] / x[3] - 0.656 * \
                        x[2] * x[3] - 0.7004 * x[3] - 0.547 * x[4] + 0.6766 - 0.6653 / (x[3] * x[4]) - 0.314 / x[2] - 0.247 / x[
                            1] + 0.3448 / (x[1] * x[4]) - 0.6086 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_38(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7339 * x[0] * x[1] - 0.5827 * x[0] * x[2] + 0.3851 * x[0] - 0.0293 * x[1] * x[2] - 0.8418 * x[1] / x[
            4] + 0.9456 * x[2] * x[3] + 0.9623 * x[3] + 0.5577 * x[3] / x[4] + 0.3934 - 0.3267 / x[4] + 0.1923 / x[2] - 0.5694 / x[
                            1] - 0.9863 * x[3] / x[0] + 0.7292 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt58_prog_9(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6866 * x[0] * x[1] + 0.8214 * x[0] + 0.1005 * x[0] / x[4] - 0.8418 * x[0] / x[2] + 0.476 * x[1] + 0.572 * x[1] / \
                        x[4] + 0.3011 * x[3] + 0.821 * x[3] / x[4] - 0.4329 - 0.6008 / x[4] + 0.5262 * x[3] / x[2] + 0.067 / x[
                            2] - 0.875 / (x[1] * x[3]) + 0.8797 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt58_prog_32(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1733 * x[0] * x[3] + 0.3195 * x[0] + 0.9992 * x[1] - 0.7859 * x[1] / x[3] - 0.2418 * x[3] - 0.5564 - 0.0516 / x[
            4] - 0.2226 * x[4] / x[3] + 0.9796 / x[2] + 0.3122 / (x[2] * x[4]) - 0.2103 * x[2] / x[1] + 0.304 * x[4] / x[0] + 0.863 / (
                                x[0] * x[2]) - 0.5647 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt58_prog_5(KnownEquation):
    _eq_name = 'inv_nv5_nt58_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3896 * x[0] * x[2] + 0.6053 * x[0] - 0.2761 * x[0] / x[4] + 0.0716 * x[0] / x[3] - 0.5392 * x[0] / x[1] - 0.2885 * \
                        x[2] + 0.227 * x[2] / x[3] - 0.1509 * x[3] * x[4] - 0.3481 + 0.2968 / x[4] + 0.0247 / x[3] + 0.0899 * x[4] / x[
                            1] - 0.5146 / x[1] + 0.1518 / (x[1] * x[3])


@register_eq_class
class sincosinv_nv6_nt610_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5143 * x[0] * x[5] + 0.7706 * x[0] * sympy.cos(x[2]) + 0.2905 * x[1] * sympy.cos(x[2]) + 0.8135 * x[1] - 0.0213 * \
                        x[2] * sympy.sin(x[3]) + 0.3248 * x[3] * sympy.cos(x[1]) + 0.8605 * x[4] * x[5] - 0.1253 * sympy.sin(
            x[2]) - 0.9207 * sympy.cos(x[3]) - 0.1135 * sympy.cos(x[4]) + 0.1307 + 0.4391 / x[5] - 0.9769 * sympy.cos(x[5]) / x[
                            3] + 0.9602 / (x[2] * x[5]) - 0.0538 * sympy.sin(x[0]) / x[1] + 0.4273 * sympy.cos(x[4]) / x[1] - 0.3116 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1481 * x[0] * sympy.cos(x[5]) + 0.5648 * x[1] + 0.732 * x[1] / x[5] + 0.6517 * x[2] * x[3] - 0.6963 * x[2] * x[
            4] + 0.4181 * x[2] - 0.84 * x[3] - 0.6423 * sympy.sin(x[1]) * sympy.sin(x[4]) - 0.3677 * sympy.sin(x[3]) * sympy.cos(
            x[5]) + 0.849 * sympy.sin(x[4]) + 0.1678 * sympy.sin(x[5]) + 0.4244 * sympy.cos(x[0]) - 0.1083 - 0.5092 * x[4] / x[
                            3] + 0.087 * sympy.sin(x[2]) / x[0] + 0.2959 * sympy.sin(x[4]) / x[0] - 0.7543 / (x[0] * x[3])


@register_eq_class
class sincosinv_nv6_nt610_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1151 * x[1] * x[2] + 0.2143 * x[1] * x[3] - 0.1302 * x[1] * x[5] - 0.8524 * x[2] / x[5] - 0.9727 * x[2] / x[
            4] - 0.6002 * sympy.sin(x[0]) + 0.4302 * sympy.sin(x[2]) - 0.8828 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.7962 * sympy.sin(
            x[3]) + 0.9034 * sympy.sin(x[4]) - 0.0096 * sympy.sin(x[5]) - 0.522 * sympy.cos(x[1]) - 0.7545 + 0.4157 / (
                                x[4] * x[5]) + 0.1481 * x[5] / x[3] + 0.2448 * x[1] / x[0] + 0.5763 * x[5] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2804 * x[0] * sympy.cos(x[2]) - 0.9279 * x[0] + 0.0835 * x[1] * x[5] + 0.616 * x[1] - 0.8557 * x[2] + 0.1145 * x[
            3] * sympy.sin(x[0]) - 0.5479 * x[4] * x[5] + 0.0134 * x[4] * sympy.sin(x[3]) - 0.7126 * x[4] * sympy.cos(x[2]) - 0.3294 * x[
                            4] + 0.1158 * x[5] * sympy.cos(x[2]) + 0.2415 * sympy.sin(x[1]) * sympy.sin(x[4]) - 0.3189 * sympy.sin(
            x[3]) - 0.1251 * sympy.cos(x[0]) * sympy.cos(x[5]) + 0.5493 - 0.3513 / x[5] - 0.8372 * sympy.sin(x[0]) / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2704 * x[0] - 0.775 * x[0] / x[5] - 0.2931 * x[1] * sympy.cos(x[0]) - 0.4507 * x[1] / x[4] + 0.7938 * x[1] / x[
            2] - 0.0266 * x[3] - 0.3267 * x[4] * x[5] - 0.227 * x[4] * sympy.cos(x[0]) - 0.5082 * x[4] * sympy.cos(x[2]) + 0.0422 * x[
                            5] * sympy.cos(x[2]) - 0.9147 * x[5] + 0.6982 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.1755 * sympy.sin(
            x[1]) + 0.6357 * sympy.sin(x[3]) * sympy.sin(x[5]) + 0.9509 * sympy.cos(x[2]) - 0.5134 - 0.4452 / x[4]


@register_eq_class
class sincosinv_nv6_nt610_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1793 * x[0] * x[5] + 0.2415 * x[0] + 0.9439 * x[0] / x[4] - 0.0855 * x[0] / x[2] + 0.9573 * x[1] + 0.0626 * x[
            2] - 0.3631 * x[3] * x[4] + 0.6834 * x[3] * sympy.sin(x[1]) - 0.8988 * x[3] * sympy.sin(x[2]) + 0.9999 * x[
                            3] + 0.379 * sympy.cos(x[4]) + 0.8217 * sympy.cos(x[5]) + 0.398 + 0.3179 * sympy.sin(x[2]) / x[
                            5] + 0.7649 * sympy.sin(x[3]) / x[5] - 0.7101 * sympy.cos(x[5]) / x[4] - 0.0304 * sympy.cos(x[0]) / x[3]


@register_eq_class
class sincosinv_nv6_nt610_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2404 * x[0] * x[3] - 0.4577 * x[0] * sympy.cos(x[5]) - 0.8164 * x[1] * x[3] - 0.8218 * x[1] * x[4] - 0.2385 * x[
            1] * x[5] + 0.6939 * x[2] * x[3] - 0.8953 * x[3] * sympy.sin(x[4]) - 0.7171 * x[4] * sympy.sin(x[0]) + 0.3988 * x[4] - 0.5157 * \
                        x[5] + 0.8872 * sympy.sin(x[3]) + 0.0857 * sympy.cos(x[0]) - 0.1785 * sympy.cos(x[1]) - 0.3058 + 0.9326 * x[5] / x[
                            4] - 0.4983 / x[2] - 0.8459 * x[2] / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4274 * x[0] * x[3] + 0.151 * x[0] * sympy.sin(x[4]) + 0.0005 * x[1] * sympy.cos(x[0]) + 0.4897 * x[1] - 0.4229 * \
                        x[2] * x[3] - 0.2371 * x[2] * sympy.cos(x[0]) + 0.4864 * x[2] + 0.525 * x[2] / x[5] + 0.7093 * x[3] * sympy.sin(
            x[1]) + 0.7505 * x[4] + 0.193 * sympy.sin(x[0]) - 0.7901 * sympy.sin(x[2]) * sympy.cos(x[4]) + 0.5999 * sympy.sin(
            x[3]) - 0.0479 * sympy.sin(x[4]) * sympy.sin(x[5]) - 0.8697 - 0.6859 / x[5] + 0.4523 * sympy.sin(x[5]) / x[3]


@register_eq_class
class sincosinv_nv6_nt610_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1149 * x[0] * sympy.cos(x[3]) - 0.9255 * x[0] / x[5] + 0.0017 * x[1] * x[4] + 0.1728 * x[2] * x[3] + 0.8081 * x[
            2] * sympy.sin(x[0]) - 0.6521 * x[2] * sympy.cos(x[1]) - 0.043 * x[2] - 0.2144 * x[3] - 0.061 * x[4] * sympy.sin(
            x[2]) + 0.0639 * x[4] - 0.299 * x[5] * sympy.sin(x[2]) - 0.0271 * x[5] * sympy.cos(x[1]) + 0.7515 * sympy.sin(
            x[0]) - 0.7447 * sympy.sin(x[1]) - 0.4969 + 0.6066 / x[5] - 0.4742 * sympy.cos(x[5]) / x[3]


@register_eq_class
class sincosinv_nv6_nt610_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2444 * x[1] + 0.1914 * x[2] * x[3] - 0.0542 * x[2] * sympy.sin(x[1]) + 0.6127 * x[3] * x[4] - 0.6725 * x[3] * x[
            5] - 0.7395 * x[4] * sympy.cos(x[2]) + 0.5106 * x[5] + 0.1067 * sympy.sin(x[0]) * sympy.sin(x[5]) - 0.6465 * sympy.sin(
            x[0]) - 0.3381 * sympy.sin(x[2]) + 0.587 * sympy.sin(x[4]) + 0.6255 * sympy.cos(x[3]) - 0.173 - 0.008 * x[4] / x[1] + 0.3307 * \
                        x[5] / x[1] - 0.0165 * sympy.cos(x[3]) / x[1] + 0.8179 * x[2] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9169 * x[0] + 0.0192 * x[1] * sympy.sin(x[5]) - 0.8868 * x[2] * sympy.cos(x[1]) - 0.928 * x[3] * sympy.cos(
            x[1]) - 0.348 * x[3] * sympy.cos(x[4]) + 0.6405 * x[4] * x[5] - 0.4699 * x[4] + 0.2386 * x[5] * sympy.cos(x[3]) + 0.2258 * x[
                            5] + 0.6158 * sympy.sin(x[0]) * sympy.cos(x[5]) - 0.7803 * sympy.cos(x[3]) + 0.2696 - 0.1272 / x[
                            2] + 0.6591 * sympy.sin(x[4]) / x[1] - 0.2952 / x[1] - 0.655 * x[1] / x[0] - 0.6836 * sympy.sin(x[3]) / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0931 * x[0] * x[3] - 0.6005 * x[1] * x[3] + 0.7618 * x[1] - 0.9348 * x[2] - 0.6655 * x[3] * x[5] + 0.6531 * x[
            3] * sympy.sin(x[2]) - 0.957 * x[4] * x[5] + 0.7149 * x[4] - 0.276 * x[5] - 0.0087 * sympy.sin(x[0]) * sympy.sin(
            x[2]) + 0.7536 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.465 * sympy.cos(x[3]) - 0.505 + 0.3974 * sympy.sin(x[0]) / x[
                            4] + 0.0387 / (x[3] * x[4]) + 0.4872 * x[5] / x[2] - 0.3514 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3884 * x[0] * x[4] - 0.8486 * x[0] * sympy.sin(x[1]) + 0.6664 * x[0] / x[5] + 0.8409 * x[1] + 0.0687 * x[1] / x[
            5] + 0.3997 * x[2] * sympy.sin(x[1]) - 0.3367 * x[2] * sympy.sin(x[3]) - 0.9989 * x[2] - 0.757 * x[3] * sympy.sin(
            x[5]) + 0.3186 * x[3] + 0.9739 * x[5] - 0.4224 * sympy.sin(x[1]) * sympy.cos(x[3]) - 0.73 * sympy.cos(
            x[0]) + 0.6786 * sympy.cos(x[4]) - 0.6191 - 0.6462 * sympy.sin(x[1]) / x[4] + 0.558 * sympy.cos(x[5]) / x[4]


@register_eq_class
class sincosinv_nv6_nt610_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3935 * x[0] / x[5] + 0.2067 * x[1] * x[2] - 0.5088 * x[1] * sympy.cos(x[3]) - 0.1661 * x[1] * sympy.cos(
            x[4]) - 0.0455 * x[1] * sympy.cos(x[5]) + 0.9132 * x[1] + 0.4682 * x[3] * sympy.sin(x[2]) - 0.1114 * x[4] - 0.4587 * x[
                            5] - 0.5155 * sympy.sin(x[0]) - 0.8024 * sympy.sin(x[2]) - 0.5111 * sympy.sin(x[3]) - 0.9883 * sympy.cos(
            x[3]) * sympy.cos(x[4]) - 0.0568 + 0.7541 * sympy.sin(x[2]) / x[5] - 0.5728 * sympy.sin(x[0]) / x[3] + 0.3841 * x[1] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3663 * x[0] * x[2] + 0.7921 * x[1] * x[3] - 0.2714 * x[1] * x[4] + 0.7974 * x[1] + 0.648 * x[2] * x[4] + 0.1846 * \
                        x[4] + 0.384 * x[5] * sympy.sin(x[0]) + 0.7184 * x[5] * sympy.cos(x[4]) - 0.7237 * sympy.sin(x[3]) * sympy.cos(
            x[5]) + 0.5669 * sympy.sin(x[4]) * sympy.cos(x[0]) - 0.2923 * sympy.cos(x[0]) + 0.1797 * sympy.cos(x[2]) - 0.7745 * sympy.cos(
            x[5]) - 0.7327 - 0.7743 / x[3] + 0.4118 * x[5] / x[1] - 0.9269 * sympy.sin(x[1]) / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5626 * x[0] * x[1] + 0.2733 * x[0] / x[2] + 0.0249 * x[1] - 0.8805 * x[1] / x[5] - 0.3832 * x[5] * sympy.cos(
            x[4]) - 0.7453 * x[5] + 0.5929 * sympy.sin(x[3]) * sympy.cos(x[5]) + 0.7537 * sympy.cos(x[0]) * sympy.cos(
            x[5]) + 0.2413 * sympy.cos(x[3]) + 0.4553 * sympy.cos(x[4]) - 0.4156 + 0.8728 / x[2] - 0.835 / (x[2] * x[4]) + 0.1793 * x[3] / \
                        x[1] - 0.968 * x[4] / x[1] - 0.3697 * sympy.sin(x[4]) / x[0] - 0.0544 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3521 * x[0] * x[1] + 0.9682 * x[0] * x[3] - 0.5447 * x[1] * x[4] - 0.2057 * x[1] - 0.3003 * x[2] * sympy.cos(
            x[4]) - 0.7742 * x[2] / x[3] - 0.4612 * x[4] - 0.7768 * x[5] - 0.5464 * sympy.sin(x[0]) * sympy.cos(x[4]) + 0.4174 * sympy.sin(
            x[3]) * sympy.cos(x[5]) - 0.7718 * sympy.sin(x[3]) - 0.7201 * sympy.sin(x[5]) * sympy.cos(x[2]) - 0.9273 * sympy.cos(
            x[1]) * sympy.cos(x[5]) - 0.1998 - 0.3887 * sympy.sin(x[5]) / x[4] - 0.8474 / x[2] - 0.7362 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0612 * x[0] * x[4] + 0.4771 * x[0] - 0.2964 * x[0] / x[5] + 0.7403 * x[1] * sympy.cos(x[4]) - 0.5583 * x[
            1] + 0.2422 * x[1] / x[3] + 0.7001 * x[2] * x[5] - 0.1102 * x[3] / x[5] + 0.3773 * x[4] * sympy.sin(x[3]) - 0.9597 * x[
                            4] + 0.0955 * x[5] * sympy.sin(x[1]) - 0.3673 * sympy.sin(x[0]) * sympy.sin(x[3]) - 0.2293 * sympy.cos(
            x[2]) - 0.0525 * sympy.cos(x[5]) + 0.7732 - 0.4807 * sympy.cos(x[5]) / x[4] - 0.8531 / x[3]


@register_eq_class
class sincosinv_nv6_nt610_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8069 * x[0] * sympy.sin(x[5]) + 0.3823 * x[0] - 0.7875 * x[1] * x[4] + 0.959 * x[2] * x[5] - 0.1327 * x[
            2] * sympy.cos(x[0]) - 0.2059 * x[3] * sympy.cos(x[4]) - 0.1236 * x[3] - 0.1337 * x[3] / x[5] + 0.6778 * x[
                            5] + 0.6323 * sympy.sin(x[1]) + 0.1649 * sympy.cos(x[2]) + 0.7551 * sympy.cos(
            x[4]) + 0.1068 + 0.5401 * sympy.sin(x[0]) / x[3] - 0.0103 * sympy.sin(x[2]) / x[3] - 0.9176 * x[4] / x[2] + 0.5459 * x[3] / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9972 * x[0] * x[1] - 0.1836 * x[0] * x[2] + 0.958 * x[0] * x[4] - 0.0889 * x[0] * sympy.cos(x[3]) + 0.6081 * x[
            0] + 0.1212 * x[1] * x[2] - 0.9236 * x[3] * sympy.sin(x[4]) + 0.3805 * x[4] - 0.8282 * x[5] * sympy.sin(
            x[2]) + 0.13 * sympy.sin(x[2]) - 0.2938 * sympy.cos(x[3]) * sympy.cos(x[5]) - 0.5431 * sympy.cos(x[3]) - 0.7249 * sympy.cos(
            x[5]) + 0.3368 - 0.1695 * sympy.sin(x[4]) / x[5] + 0.7456 * sympy.cos(x[1]) / x[3] + 0.6059 / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8493 * x[0] * sympy.sin(x[2]) + 0.6611 * x[0] * sympy.sin(x[4]) + 0.5324 * x[0] + 0.6563 * x[1] / x[4] - 0.0599 * \
                        x[2] * sympy.sin(x[3]) + 0.9418 * x[2] + 0.0985 * x[2] / x[5] + 0.0689 * x[3] - 0.4058 * x[4] * x[5] - 0.9096 * x[
                            4] * sympy.cos(x[3]) + 0.8931 * x[4] + 0.5456 * x[5] * sympy.sin(x[3]) - 0.3713 * x[5] - 0.7495 * sympy.sin(
            x[1]) * sympy.cos(x[3]) + 0.3733 * sympy.sin(x[1]) - 0.6192 + 0.539 / (x[0] * x[1])


@register_eq_class
class sincosinv_nv6_nt610_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4697 * x[0] * sympy.sin(x[4]) + 0.7347 * x[0] * sympy.cos(x[3]) - 0.1258 * x[0] + 0.1642 * x[1] * x[5] + 0.3664 * \
                        x[1] - 0.0182 * x[2] * sympy.sin(x[4]) + 0.3208 * x[2] * sympy.sin(x[5]) + 0.4975 * x[4] * sympy.cos(
            x[3]) - 0.4133 * x[5] * sympy.sin(x[3]) + 0.0197 * x[5] + 0.3194 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.7148 * sympy.sin(
            x[2]) + 0.1875 * sympy.sin(x[4]) + 0.3059 * sympy.cos(x[0]) * sympy.cos(x[2]) - 0.8337 * sympy.cos(x[3]) - 0.7804 + 0.4422 * x[
                            3] / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.212 * x[0] * x[2] - 0.2894 * x[0] * x[3] - 0.4943 * x[0] * x[4] + 0.6245 * x[0] * sympy.sin(x[5]) - 0.6789 * x[
            0] + 0.6994 * x[1] - 0.7495 * x[2] - 0.6175 * x[3] * sympy.sin(x[1]) + 0.04 * x[4] * sympy.cos(x[2]) + 0.9086 * x[
                            5] * sympy.sin(x[2]) - 0.0055 * x[5] * sympy.cos(x[3]) - 0.1703 * x[5] * sympy.cos(x[4]) + 0.8838 * sympy.sin(
            x[1]) * sympy.sin(x[2]) - 0.168 * sympy.sin(x[3]) + 0.632 + 0.8106 / x[5] + 0.6135 / x[4]


@register_eq_class
class sincosinv_nv6_nt610_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5577 * x[0] * x[4] + 0.8615 * x[0] * x[5] + 0.5434 * x[0] - 0.1352 * x[1] * x[5] - 0.0882 * x[1] + 0.851 * x[2] * \
                        x[5] + 0.2349 * x[2] * sympy.sin(x[3]) - 0.705 * x[2] * sympy.cos(x[4]) + 0.6411 * x[3] * x[4] - 0.9263 * x[
                            4] * sympy.cos(x[1]) - 0.0996 * x[4] + 0.6514 * x[5] + 0.0207 * sympy.cos(x[3]) - 0.8517 - 0.3399 * sympy.cos(
            x[1]) / x[3] - 0.4563 / x[2] + 0.4975 * x[2] / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0199 * x[0] / x[3] + 0.6927 * x[1] * x[4] + 0.129 * x[1] * sympy.sin(x[0]) + 0.7431 * x[1] * sympy.cos(
            x[5]) - 0.8857 * x[2] * x[4] + 0.9709 * x[3] * x[4] + 0.8292 * x[4] * sympy.cos(x[5]) - 0.7476 * x[5] + 0.4771 * sympy.sin(
            x[3]) + 0.0424 * sympy.sin(x[4]) - 0.7987 * sympy.sin(x[5]) * sympy.cos(x[3]) + 0.4197 * sympy.cos(x[0]) + 0.719 * sympy.cos(
            x[1]) + 0.8681 - 0.3456 * sympy.cos(x[0]) / x[2] + 0.2683 / x[2] + 0.2392 * x[2] / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8845 * x[0] * x[3] + 0.7161 * x[1] * sympy.cos(x[3]) + 0.464 * x[1] - 0.2602 * x[2] * sympy.cos(x[5]) - 0.4324 * \
                        x[3] + 0.3818 * x[4] * x[5] - 0.0808 * x[4] * sympy.sin(x[0]) - 0.9607 * x[4] + 0.8731 * x[5] * sympy.cos(
            x[1]) + 0.4322 * sympy.sin(x[4]) * sympy.cos(x[3]) - 0.009 * sympy.sin(x[5]) + 0.0471 * sympy.cos(x[1]) * sympy.cos(
            x[2]) + 0.1941 - 0.8415 * x[4] / x[2] + 0.5765 / x[2] + 0.1719 * x[4] / x[1] - 0.1037 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8267 * x[0] * sympy.cos(x[5]) + 0.3515 * x[0] - 0.0898 * x[1] * sympy.sin(x[0]) - 0.9099 * x[1] * sympy.cos(
            x[5]) - 0.5769 * x[2] * x[5] + 0.5072 * x[2] * sympy.cos(x[3]) + 0.8909 * x[2] - 0.7132 * x[3] - 0.6814 * x[3] / x[4] - 0.4706 * \
                        x[4] * sympy.cos(x[1]) - 0.104 * x[4] - 0.1835 * x[5] - 0.9252 * sympy.sin(x[1]) * sympy.cos(
            x[3]) - 0.2644 * sympy.cos(x[0]) * sympy.cos(x[2]) + 0.0635 * sympy.cos(x[2]) * sympy.cos(x[4]) - 0.7522 + 0.8441 / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0254 * x[0] * x[1] + 0.8096 * x[0] * x[4] - 0.2048 * x[0] + 0.9179 * x[1] * sympy.cos(x[3]) + 0.6995 * x[2] * x[
            3] + 0.9694 * x[2] / x[4] - 0.0522 * x[3] * sympy.cos(x[4]) - 0.5431 * x[3] + 0.4026 * sympy.sin(x[0]) * sympy.sin(
            x[5]) + 0.9727 * sympy.sin(x[1]) * sympy.sin(x[5]) - 0.6213 * sympy.sin(x[1]) - 0.2107 * sympy.sin(x[3]) * sympy.cos(
            x[5]) + 0.3721 * sympy.cos(x[2]) + 0.3366 * sympy.cos(x[5]) + 0.6963 + 0.6468 / x[4] - 0.9434 * sympy.sin(x[0]) / x[2]


@register_eq_class
class sincosinv_nv6_nt610_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1499 * x[1] + 0.268 * x[2] - 0.1504 * x[4] * sympy.sin(x[0]) + 0.5361 * x[4] - 0.6653 * x[5] * sympy.cos(
            x[2]) - 0.5643 * x[5] + 0.1958 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.6876 * sympy.sin(x[1]) * sympy.cos(
            x[0]) + 0.3974 * sympy.cos(x[0]) - 0.4783 - 0.9248 * sympy.cos(x[0]) / x[5] + 0.6775 * sympy.cos(x[3]) / x[
                            5] + 0.4136 * sympy.cos(x[4]) / x[5] + 0.6609 / x[3] + 0.6359 * x[4] / x[2] - 0.07 * sympy.sin(x[3]) / x[
                            2] - 0.6066 * x[2] / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1844 * x[0] * x[1] - 0.0582 * x[0] * x[5] - 0.4108 * x[0] * sympy.cos(x[3]) + 0.7881 * x[1] + 0.228 * x[1] / x[
            3] - 0.3152 * x[3] / x[5] - 0.9251 * x[5] - 0.1559 * sympy.sin(x[0]) - 0.6528 * sympy.sin(x[2]) * sympy.cos(
            x[4]) - 0.5422 * sympy.sin(x[2]) - 0.6656 * sympy.sin(x[3]) - 0.2561 * sympy.cos(x[4]) + 0.8766 + 0.2755 * sympy.sin(x[1]) / x[
                            5] - 0.1885 * sympy.sin(x[3]) / x[2] - 0.1049 / (x[2] * x[5]) - 0.8933 * x[4] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0399 * x[0] * sympy.cos(x[4]) + 0.5841 * x[1] - 0.1669 * x[1] / x[4] + 0.5347 * x[2] * sympy.sin(x[3]) + 0.0659 * \
                        x[2] * sympy.sin(x[4]) - 0.8998 * x[2] * sympy.cos(x[5]) + 0.6388 * x[2] - 0.1305 * x[3] * x[4] + 0.6335 * x[
                            3] - 0.1727 * x[4] + 0.114 * x[5] + 0.1485 * sympy.sin(x[0]) + 0.1568 - 0.4253 * sympy.sin(x[3]) / x[
                            5] - 0.0834 * sympy.cos(x[0]) / x[3] + 0.5539 * x[5] / x[1] - 0.7788 * x[5] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5095 * x[0] * x[1] - 0.4064 * x[0] * sympy.cos(x[2]) + 0.0333 * x[0] / x[3] - 0.9207 * x[1] + 0.3813 * x[2] * x[
            3] - 0.1849 * x[3] - 0.5554 * x[4] - 0.5547 * x[5] * sympy.cos(x[0]) + 0.9937 * x[5] + 0.9681 * sympy.sin(
            x[0]) + 0.6199 * sympy.sin(x[2]) * sympy.cos(x[5]) - 0.0046 * sympy.sin(x[3]) * sympy.cos(x[4]) - 0.2321 * sympy.cos(
            x[1]) * sympy.cos(x[4]) + 0.4495 * sympy.cos(x[2]) - 0.7413 - 0.7493 * sympy.cos(x[5]) / x[3] + 0.9742 / (x[1] * x[3])


@register_eq_class
class sincosinv_nv6_nt610_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7202 * x[0] * sympy.cos(x[3]) - 0.7906 * x[0] - 0.2431 * x[1] * x[5] + 0.9869 * x[1] * sympy.sin(x[2]) - 0.1632 * \
                        x[1] * sympy.cos(x[4]) + 0.1377 * x[2] * x[5] - 0.3193 * x[2] + 0.4807 * x[3] * x[5] - 0.1459 * x[4] * sympy.sin(
            x[3]) - 0.6165 * x[5] + 0.7558 * sympy.sin(x[1]) + 0.283 * sympy.cos(x[3]) - 0.5043 * sympy.cos(
            x[4]) + 0.6299 + 0.7127 * sympy.sin(x[4]) / x[2] - 0.3681 * x[1] / x[0] - 0.9148 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv6_nt610_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0074 * x[0] * sympy.sin(x[1]) + 0.5373 * x[0] - 0.1744 * x[1] * x[5] + 0.914 * x[2] * sympy.cos(x[0]) + 0.0674 * \
                        x[2] * sympy.cos(x[4]) - 0.4129 * x[2] - 0.1901 * x[3] * sympy.cos(x[4]) + 0.9661 * x[4] * x[5] + 0.6754 * x[
                            4] + 0.147 * sympy.sin(x[5]) * sympy.cos(x[3]) + 0.6038 * sympy.cos(x[3]) + 0.7573 + 0.0238 / x[5] + 0.4325 / (
                                x[2] * x[3]) - 0.3948 / x[1] - 0.0405 * x[5] / x[0] - 0.6816 * sympy.cos(x[3]) / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4039 * x[0] * x[4] + 0.0866 * x[0] * x[5] + 0.0826 * x[1] * sympy.sin(x[4]) - 0.5075 * x[1] + 0.989 * x[1] / x[
            3] + 0.6254 * x[2] * sympy.sin(x[3]) + 0.9394 * x[3] * sympy.cos(x[4]) - 0.7427 * x[4] * x[5] + 0.9068 * x[
                            4] + 0.145 * sympy.sin(x[5]) * sympy.cos(x[1]) - 0.1473 * sympy.sin(x[5]) - 0.4011 * sympy.cos(
            x[0]) + 0.2063 * sympy.cos(x[2]) + 0.5407 + 0.5207 / x[3] - 0.6208 * x[2] / x[1] - 0.0863 * x[2] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8984 * x[0] * x[5] - 0.3281 * x[1] * x[3] + 0.0324 * x[1] * sympy.cos(x[0]) + 0.8693 * x[2] * x[4] + 0.6386 * x[
            2] * sympy.sin(x[0]) + 0.2842 * x[2] + 0.307 * x[2] / x[3] - 0.9598 * x[3] * x[4] + 0.0451 * x[5] * sympy.cos(x[4]) - 0.4985 * \
                        x[5] - 0.4037 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.3815 * sympy.sin(x[0]) + 0.7408 * sympy.sin(
            x[1]) + 0.2408 * sympy.sin(x[4]) + 0.7589 * sympy.cos(x[3]) + 0.2599 - 0.9757 * sympy.cos(x[1]) / x[5]


@register_eq_class
class sincosinv_nv6_nt610_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0332 * x[0] * x[1] + 0.7895 * x[0] + 0.1642 * x[1] / x[4] + 0.0819 * x[3] * x[4] - 0.9654 * x[3] * sympy.cos(
            x[1]) + 0.2122 * x[3] - 0.5177 * x[5] * sympy.cos(x[3]) + 0.6269 * x[5] * sympy.cos(x[4]) + 0.8285 * sympy.cos(
            x[1]) * sympy.cos(x[5]) - 0.457 * sympy.cos(x[5]) - 0.5723 + 0.5344 * sympy.sin(x[0]) / x[5] + 0.8386 / x[4] + 0.1807 * x[4] / \
                        x[2] - 0.0163 / x[2] - 0.3162 / x[1] - 0.4765 / (x[0] * x[3])


@register_eq_class
class sincosinv_nv6_nt610_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4578 * x[0] * x[2] + 0.8632 * x[0] * x[4] - 0.3667 * x[0] + 0.792 * x[0] / x[1] - 0.7837 * x[1] + 0.1038 * x[1] / \
                        x[3] + 0.8416 * x[2] * x[4] - 0.3889 * x[2] + 0.6409 * x[3] - 0.4815 * x[5] + 0.4558 * sympy.sin(x[1]) * sympy.sin(
            x[2]) + 0.4146 * sympy.sin(x[2]) * sympy.sin(x[3]) + 0.8339 * sympy.sin(x[4]) + 0.8255 * sympy.sin(x[5]) * sympy.cos(
            x[0]) - 0.9613 + 0.2354 * sympy.sin(x[4]) / x[3] + 0.4704 / (x[1] * x[5])


@register_eq_class
class sincosinv_nv6_nt610_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7652 * x[0] / x[5] + 0.8578 * x[1] * sympy.sin(x[4]) + 0.2058 * x[1] * sympy.sin(x[5]) + 0.9524 * x[
            1] * sympy.cos(x[0]) - 0.185 * x[1] + 0.6918 * x[3] * x[4] + 0.2692 * x[3] * sympy.cos(x[1]) + 0.8925 * x[3] * sympy.cos(
            x[2]) + 0.3929 * x[5] + 0.0112 * sympy.sin(x[0]) * sympy.cos(x[4]) - 0.3208 * sympy.cos(x[4]) * sympy.cos(
            x[5]) + 0.8416 - 0.148 / x[4] + 0.4646 / x[3] - 0.1737 * x[5] / x[2] + 0.4436 / x[2] + 0.0801 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6189 * x[0] * x[4] + 0.9745 * x[1] - 0.0045 * x[2] * x[3] - 0.5664 * x[2] * sympy.cos(x[1]) + 0.7015 * x[
            2] - 0.128 * x[4] * sympy.sin(x[3]) + 0.0555 * x[4] * sympy.cos(x[5]) - 0.1472 * x[5] - 0.0648 * sympy.sin(
            x[0]) + 0.4315 * sympy.sin(x[3]) + 0.802 * sympy.sin(x[4]) * sympy.cos(x[2]) - 0.7324 * sympy.cos(
            x[4]) - 0.8239 + 0.0315 * sympy.sin(x[5]) / x[3] - 0.7538 * sympy.cos(x[4]) / x[1] - 0.9398 * sympy.cos(x[5]) / x[
                            1] + 0.7932 * sympy.cos(x[2]) / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.615 * x[0] * x[4] - 0.2158 * x[0] * sympy.sin(x[1]) - 0.6224 * x[0] * sympy.sin(x[5]) + 0.3104 * x[0] - 0.3789 * \
                        x[1] * sympy.sin(x[3]) - 0.2676 * x[1] + 0.2137 * x[2] * x[4] + 0.8821 * x[2] * sympy.cos(x[5]) + 0.8055 * x[
                            2] - 0.9798 * x[3] * sympy.sin(x[0]) + 0.1731 * x[3] * sympy.cos(x[5]) + 0.4919 * x[4] * x[5] - 0.0556 * x[
                            4] - 0.467 * x[5] - 0.0724 * sympy.sin(x[3]) + 0.7732 - 0.3914 * sympy.sin(x[4]) / x[3]


@register_eq_class
class sincosinv_nv6_nt610_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2004 * x[0] * sympy.sin(x[5]) + 0.89 * x[0] / x[1] + 0.322 * x[1] * sympy.sin(x[4]) - 0.617 * x[1] - 0.6091 * x[
            2] * x[5] - 0.2564 * x[3] * x[4] + 0.1553 * x[3] * sympy.cos(x[0]) + 0.5444 * x[3] / x[5] - 0.1301 * x[4] * x[
                            5] - 0.8061 * sympy.sin(x[0]) - 0.12 * sympy.cos(x[2]) + 0.1785 * sympy.cos(x[3]) + 0.4469 * sympy.cos(
            x[4]) + 0.1471 * sympy.cos(x[5]) + 0.5884 + 0.6504 * x[3] / x[1] + 0.0732 * x[2] / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2412 * x[0] * x[3] - 0.7331 * x[0] / x[4] - 0.6568 * x[1] + 0.2913 * x[2] * x[3] + 0.5065 * x[2] * sympy.sin(
            x[0]) + 0.6049 * x[2] + 0.4623 * x[3] * x[5] + 0.2173 * x[4] / x[5] - 0.0193 * sympy.sin(x[2]) * sympy.sin(
            x[4]) - 0.7688 * sympy.sin(x[2]) * sympy.cos(x[5]) + 0.4421 * sympy.sin(x[3]) + 0.0386 * sympy.cos(x[4]) - 0.1609 * sympy.cos(
            x[5]) + 0.7066 - 0.6 * x[5] / x[1] - 0.694 * sympy.sin(x[2]) / x[1] - 0.2902 / x[0]


@register_eq_class
class sincosinv_nv6_nt610_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0329 * x[0] * x[2] - 0.3253 * x[0] * x[4] + 0.3916 * x[0] * sympy.sin(x[5]) - 0.0783 * x[1] * sympy.sin(
            x[5]) - 0.197 * x[1] + 0.0745 * x[2] * sympy.sin(x[4]) - 0.1185 * x[2] * sympy.cos(x[1]) - 0.4816 * x[2] + 0.8662 * x[
                            3] * sympy.sin(x[1]) + 0.1554 * x[3] / x[5] - 0.3059 * x[4] + 0.6132 * sympy.sin(x[0]) * sympy.cos(
            x[3]) + 0.0369 * sympy.sin(x[4]) * sympy.cos(x[5]) + 0.6073 * sympy.sin(x[5]) - 0.6887 * sympy.cos(x[3]) + 0.8113 + 0.5983 / x[
                            0]


@register_eq_class
class sincosinv_nv6_nt610_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7473 * x[0] + 0.496 * x[1] * x[4] - 0.9479 * x[1] - 0.3917 * x[2] * x[4] + 0.738 * x[2] * sympy.cos(
            x[0]) + 0.6238 * x[2] - 0.6332 * x[3] * sympy.cos(x[2]) + 0.5263 * x[3] * sympy.cos(x[5]) + 0.9801 * x[3] - 0.9015 * x[
                            4] - 0.4616 * x[5] + 0.3709 * sympy.sin(x[0]) * sympy.sin(x[3]) - 0.2299 * sympy.cos(x[1]) * sympy.cos(
            x[3]) - 0.2653 + 0.9172 * sympy.sin(x[1]) / x[5] - 0.8909 * sympy.cos(x[2]) / x[5] - 0.7237 / (x[1] * x[2])


@register_eq_class
class sincosinv_nv6_nt610_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5638 * x[0] * x[1] - 0.1978 * x[0] + 0.586 * x[1] * x[2] - 0.4323 * x[1] * sympy.sin(x[5]) - 0.3037 * x[
            2] * sympy.cos(x[5]) - 0.3108 * x[2] + 0.9611 * x[3] * sympy.cos(x[1]) + 0.9158 * x[4] * x[5] - 0.1214 * x[4] * sympy.sin(
            x[0]) + 0.797 * x[4] * sympy.cos(x[2]) - 0.647 * x[4] + 0.5526 * x[5] * sympy.cos(x[0]) + 0.1996 * sympy.sin(x[0]) * sympy.sin(
            x[2]) + 0.1871 * sympy.sin(x[1]) + 0.2104 * sympy.cos(x[3]) + 0.7755 - 0.4314 / x[5]


@register_eq_class
class sincosinv_nv6_nt610_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5558 * x[0] * x[2] + 0.2081 * x[0] * x[5] + 0.5398 * x[0] - 0.1876 * x[1] - 0.8205 * x[2] * x[4] - 0.0074 * x[
            2] * sympy.sin(x[1]) + 0.5188 * x[2] * sympy.sin(x[5]) - 0.2114 * x[2] + 0.4386 * x[3] + 0.5686 * x[4] * sympy.sin(
            x[1]) + 0.0132 * x[4] - 0.1217 - 0.1585 / x[5] - 0.0763 * x[5] / x[4] - 0.1853 * sympy.sin(x[0]) / x[3] - 0.8635 * sympy.cos(
            x[2]) / x[3] + 0.4533 / (x[3] * x[5])


@register_eq_class
class sincosinv_nv6_nt610_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0004 * x[0] * sympy.cos(x[5]) - 0.3349 * x[1] * x[2] + 0.1709 * x[1] * x[4] + 0.492 * x[1] * sympy.sin(
            x[5]) - 0.7115 * x[1] - 0.6293 * x[2] * x[3] - 0.3979 * x[2] / x[5] + 0.1148 * x[3] * sympy.cos(x[5]) + 0.8052 * x[
                            4] * sympy.cos(x[2]) - 0.7595 * x[4] + 0.3271 * x[5] - 0.3778 * sympy.sin(x[0]) - 0.7405 * sympy.cos(
            x[2]) - 0.996 * sympy.cos(x[3]) + 0.9112 + 0.0044 * sympy.cos(x[5]) / x[4] + 0.1344 * sympy.sin(x[3]) / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8079 * x[0] * x[1] - 0.4398 * x[0] * x[5] - 0.2676 * x[1] * x[2] - 0.0729 * x[1] * x[3] - 0.6118 * x[
            1] * sympy.cos(x[4]) - 0.4865 * x[2] * x[5] - 0.86 * x[3] * sympy.sin(x[0]) + 0.3384 * x[3] + 0.2795 * x[4] * sympy.cos(
            x[3]) - 0.3727 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.9254 * sympy.sin(x[0]) + 0.2197 * sympy.sin(x[1]) * sympy.cos(
            x[5]) - 0.1565 * sympy.sin(x[2]) + 0.0853 - 0.3185 / x[5] + 0.7685 / x[4] - 0.271 / x[1]


@register_eq_class
class sincosinv_nv6_nt610_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt610_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4774 * x[0] * x[2] - 0.4297 * x[0] * sympy.sin(x[4]) + 0.8262 * x[1] * x[2] - 0.5655 * x[1] * sympy.sin(
            x[0]) - 0.2181 * x[1] - 0.3888 * x[2] * x[5] - 0.3332 * x[2] * sympy.sin(x[4]) + 0.0652 * x[3] - 0.5119 * sympy.sin(
            x[2]) - 0.4924 * sympy.sin(x[4]) - 0.8598 * sympy.cos(x[3]) * sympy.cos(x[5]) - 0.0608 - 0.4061 * sympy.sin(x[1]) / x[
                            5] + 0.7821 / x[5] - 0.6251 * sympy.cos(x[2]) / x[3] + 0.2907 / (x[3] * x[4]) - 0.5652 / x[0]


@register_eq_class
class sincos_nv6_nt68_prog_46(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5353 * x[0] * x[2] + 0.4872 * x[0] - 0.061 * x[1] * x[4] - 0.2879 * x[1] * x[5] + 0.1296 * x[1] + 0.3926 * x[
            4] * sympy.cos(x[5]) + 0.3564 * x[4] + 0.1994 * x[5] * sympy.sin(x[0]) - 0.1618 * x[5] * sympy.cos(x[2]) - 0.271 * sympy.sin(
            x[2]) * sympy.cos(x[1]) + 0.032 * sympy.sin(x[2]) + 0.6054 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.5013 * sympy.sin(
            x[3]) - 0.6801 * sympy.cos(x[5]) - 0.975


@register_eq_class
class sincos_nv6_nt68_prog_0(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7472 * x[0] * sympy.sin(x[2]) - 0.8618 * x[0] + 0.6079 * x[1] * x[4] - 0.3932 * x[1] - 0.9092 * x[2] * sympy.sin(
            x[1]) - 0.1783 * x[2] + 0.5012 * x[3] + 0.2833 * x[4] * sympy.sin(x[3]) + 0.1309 * x[4] * sympy.cos(x[5]) - 0.4885 * x[
                            4] + 0.193 * x[5] * sympy.cos(x[1]) - 0.4969 * x[5] + 0.5665 * sympy.sin(x[0]) * sympy.cos(
            x[4]) - 0.1601 * sympy.sin(x[2]) * sympy.sin(x[5]) - 0.228


@register_eq_class
class sincos_nv6_nt68_prog_35(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6743 * x[0] - 0.3905 * x[1] * x[2] + 0.4641 * x[1] * x[4] + 0.3654 * x[1] * x[5] - 0.7352 * x[1] - 0.864 * x[2] * \
                        x[5] + 0.2909 * x[2] * sympy.sin(x[3]) + 0.839 * x[2] - 0.7522 * x[4] * sympy.sin(x[3]) - 0.3993 * x[5] * sympy.sin(
            x[4]) + 0.2012 * x[5] + 0.3029 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.0722 * sympy.sin(x[3]) + 0.5705 * sympy.sin(
            x[4]) - 0.2143


@register_eq_class
class sincos_nv6_nt68_prog_8(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.757 * x[0] * sympy.cos(x[5]) + 0.653 * x[1] * sympy.sin(x[5]) + 0.0718 * x[1] * sympy.cos(x[4]) - 0.9549 * x[
            3] * sympy.sin(x[5]) - 0.6986 * x[3] + 0.6606 * x[4] * sympy.sin(x[0]) - 0.0054 * x[4] * sympy.cos(x[2]) - 0.2229 * x[
                            5] - 0.6219 * sympy.sin(x[1]) + 0.9306 * sympy.sin(x[2]) + 0.3154 * sympy.cos(x[0]) - 0.5793 * sympy.cos(
            x[1]) * sympy.cos(x[2]) + 0.1479 * sympy.cos(x[2]) * sympy.cos(x[5]) - 0.5655 * sympy.cos(x[4]) + 0.0651


@register_eq_class
class sincos_nv6_nt68_prog_42(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7711 * x[0] * sympy.sin(x[1]) + 0.892 * x[0] - 0.7955 * x[1] * x[3] + 0.6318 * x[1] * sympy.sin(x[2]) - 0.9151 * \
                        x[1] + 0.5641 * x[2] * sympy.cos(x[0]) + 0.7736 * x[4] * sympy.sin(x[1]) - 0.7542 * x[4] + 0.928 * x[
                            5] - 0.3324 * sympy.cos(x[0]) * sympy.cos(x[4]) + 0.6027 * sympy.cos(x[2]) * sympy.cos(
            x[5]) - 0.583 * sympy.cos(x[2]) - 0.4453 * sympy.cos(x[3]) * sympy.cos(x[5]) + 0.0241 * sympy.cos(x[3]) - 0.7236


@register_eq_class
class sincos_nv6_nt68_prog_33(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2919 * x[0] * x[4] + 0.4638 * x[0] * sympy.cos(x[1]) - 0.346 * x[0] * sympy.cos(x[5]) - 0.3181 * x[1] * x[
            5] - 0.3373 * x[1] - 0.3614 * x[2] - 0.1354 * x[3] * x[5] - 0.8462 * x[3] * sympy.sin(x[0]) + 0.6051 * sympy.sin(
            x[0]) * sympy.cos(x[2]) + 0.5089 * sympy.sin(x[1]) * sympy.sin(x[2]) - 0.5471 * sympy.sin(x[3]) + 0.127 * sympy.sin(
            x[4]) - 0.9144 * sympy.cos(x[0]) - 0.6653 * sympy.cos(x[5]) + 0.6081


@register_eq_class
class sincos_nv6_nt68_prog_20(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3876 * x[0] * x[1] - 0.6771 * x[0] * sympy.sin(x[4]) + 0.3678 * x[1] * x[4] + 0.022 * x[1] * sympy.sin(
            x[5]) - 0.6941 * x[1] * sympy.cos(x[2]) + 0.6178 * x[3] * x[5] - 0.0756 * x[4] - 0.6093 * x[5] * sympy.cos(x[2]) + 0.3004 * x[
                            5] + 0.2307 * sympy.sin(x[0]) - 0.3523 * sympy.sin(x[1]) + 0.4959 * sympy.sin(x[2]) * sympy.cos(
            x[0]) - 0.3634 * sympy.cos(x[2]) - 0.2641 * sympy.cos(x[3]) + 0.7134


@register_eq_class
class sincos_nv6_nt68_prog_14(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0113 * x[0] + 0.6209 * x[1] * x[3] - 0.2723 * x[1] * x[5] - 0.6707 * x[1] * sympy.sin(x[2]) - 0.6007 * x[
            1] - 0.1601 * x[2] + 0.5315 * x[3] * sympy.sin(x[4]) + 0.1081 * x[3] - 0.8374 * x[4] * sympy.cos(x[5]) - 0.2546 * x[
                            4] + 0.1558 * x[5] - 0.4752 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.8062 * sympy.sin(x[5]) * sympy.cos(
            x[3]) - 0.7384 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.385


@register_eq_class
class sincos_nv6_nt68_prog_31(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1452 * x[0] * x[2] + 0.8637 * x[0] + 0.2784 * x[1] * x[3] + 0.8336 * x[3] * sympy.sin(x[5]) + 0.0079 * x[
            3] - 0.5995 * x[4] * sympy.cos(x[1]) + 0.223 * x[4] * sympy.cos(x[3]) + 0.3646 * x[5] * sympy.sin(x[0]) + 0.3623 * sympy.sin(
            x[1]) * sympy.sin(x[2]) + 0.4808 * sympy.sin(x[1]) - 0.7649 * sympy.sin(x[2]) * sympy.sin(x[3]) + 0.2266 * sympy.sin(
            x[4]) - 0.4403 * sympy.cos(x[2]) - 0.6189 * sympy.cos(x[5]) - 0.1754


@register_eq_class
class sincos_nv6_nt68_prog_48(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8584 * x[0] * sympy.sin(x[1]) - 0.7141 * x[0] * sympy.cos(x[2]) + 0.8425 * x[0] * sympy.cos(x[4]) + 0.0559 * x[
            0] - 0.2068 * x[1] + 0.9208 * x[2] * x[4] + 0.5754 * x[3] * x[4] - 0.7105 * x[4] * sympy.cos(x[1]) + 0.2498 * x[5] * sympy.cos(
            x[0]) + 0.6383 * sympy.sin(x[2]) + 0.1612 * sympy.sin(x[3]) * sympy.cos(x[5]) + 0.2628 * sympy.sin(x[3]) - 0.1249 * sympy.cos(
            x[4]) - 0.945 * sympy.cos(x[5]) - 0.7409


@register_eq_class
class sincos_nv6_nt68_prog_41(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5415 * x[0] * x[1] + 0.1968 * x[0] * x[2] + 0.6791 * x[0] * sympy.sin(x[3]) + 0.1873 * x[0] + 0.8473 * x[1] * x[
            2] + 0.5904 * x[1] * x[3] - 0.2864 * x[1] + 0.5872 * x[2] + 0.9345 * x[5] * sympy.cos(x[4]) - 0.9506 * sympy.sin(
            x[3]) + 0.625 * sympy.sin(x[4]) * sympy.cos(x[2]) - 0.4986 * sympy.sin(x[5]) * sympy.cos(x[0]) + 0.4451 * sympy.sin(
            x[5]) - 0.4701 * sympy.cos(x[4]) - 0.5199


@register_eq_class
class sincos_nv6_nt68_prog_7(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7292 * x[0] * sympy.sin(x[2]) + 0.6347 * x[1] * sympy.sin(x[5]) + 0.9619 * x[1] * sympy.cos(x[0]) + 0.8546 * x[
            2] * sympy.sin(x[3]) + 0.2769 * x[2] - 0.877 * x[4] * sympy.sin(x[3]) + 0.3558 * x[4] * sympy.cos(x[0]) + 0.0593 * x[
                            5] * sympy.sin(x[0]) - 0.039 * sympy.sin(x[0]) - 0.8814 * sympy.sin(x[1]) * sympy.cos(
            x[4]) - 0.5511 * sympy.sin(x[1]) - 0.7954 * sympy.sin(x[3]) + 0.6011 * sympy.sin(x[4]) + 0.9599 * sympy.cos(x[5]) - 0.2931


@register_eq_class
class sincos_nv6_nt68_prog_37(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9907 * x[0] * x[5] - 0.3607 * x[1] + 0.4743 * x[2] * sympy.sin(x[4]) - 0.6208 * x[2] * sympy.sin(x[5]) + 0.0431 * \
                        x[2] - 0.8503 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.0728 * sympy.sin(x[0]) + 0.0545 * sympy.sin(x[1]) * sympy.cos(
            x[3]) - 0.6408 * sympy.sin(x[3]) * sympy.sin(x[4]) - 0.2974 * sympy.sin(x[4]) - 0.7884 * sympy.sin(x[5]) * sympy.cos(
            x[1]) - 0.1294 * sympy.sin(x[5]) - 0.9424 * sympy.cos(x[0]) * sympy.cos(x[3]) - 0.273 * sympy.cos(x[3]) - 0.7171


@register_eq_class
class sincos_nv6_nt68_prog_15(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.847 * x[0] * sympy.sin(x[1]) + 0.6905 * x[0] * sympy.sin(x[4]) - 0.1053 * x[0] + 0.5511 * x[1] * sympy.sin(
            x[2]) + 0.0596 * x[2] * sympy.cos(x[3]) - 0.054 * x[3] * sympy.cos(x[1]) + 0.6747 * x[3] - 0.0846 * x[4] - 0.7053 * x[
                            5] * sympy.sin(x[4]) - 0.9933 * x[5] - 0.6707 * sympy.sin(x[4]) * sympy.cos(x[2]) + 0.6882 * sympy.sin(
            x[5]) * sympy.cos(x[1]) + 0.0163 * sympy.cos(x[1]) + 0.2841 * sympy.cos(x[2]) - 0.9482


@register_eq_class
class sincos_nv6_nt68_prog_23(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3234 * x[0] * sympy.cos(x[5]) + 0.4372 * x[0] - 0.2842 * x[1] * x[3] - 0.7974 * x[1] * sympy.cos(x[0]) - 0.7611 * \
                        x[1] + 0.709 * x[2] * sympy.cos(x[3]) + 0.601 * x[2] + 0.0107 * x[3] * x[4] - 0.2816 * x[3] + 0.2559 * x[
                            4] - 0.4851 * sympy.sin(x[0]) * sympy.sin(x[3]) - 0.1698 * sympy.cos(x[1]) * sympy.cos(
            x[4]) + 0.899 * sympy.cos(x[1]) * sympy.cos(x[5]) - 0.7178 * sympy.cos(x[5]) + 0.4132


@register_eq_class
class sincos_nv6_nt68_prog_30(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1943 * x[0] * sympy.sin(x[3]) + 0.9876 * x[1] * x[2] - 0.9468 * x[1] * sympy.cos(x[0]) + 0.0091 * x[
            1] * sympy.cos(x[4]) + 0.6564 * x[1] + 0.9776 * x[2] + 0.7789 * x[3] * sympy.sin(x[1]) + 0.3784 * x[5] * sympy.cos(
            x[1]) - 0.6093 * x[5] - 0.327 * sympy.sin(x[3]) + 0.5628 * sympy.sin(x[4]) - 0.5364 * sympy.cos(x[0]) + 0.3984 * sympy.cos(
            x[2]) * sympy.cos(x[4]) - 0.5104 * sympy.cos(x[3]) * sympy.cos(x[5]) - 0.2135


@register_eq_class
class sincos_nv6_nt68_prog_28(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.861 * x[0] * sympy.sin(x[5]) - 0.8827 * x[0] + 0.3577 * x[1] * sympy.sin(x[2]) + 0.0235 * x[1] * sympy.sin(
            x[3]) + 0.9343 * x[1] - 0.3637 * x[2] * sympy.cos(x[0]) + 0.3847 * x[2] * sympy.cos(x[3]) - 0.2854 * x[2] - 0.784 * x[3] * x[
                            5] - 0.814 * x[3] - 0.8243 * x[4] * sympy.sin(x[3]) + 0.3121 * x[4] + 0.8187 * sympy.sin(
            x[5]) + 0.0577 * sympy.cos(x[0]) * sympy.cos(x[4]) + 0.2522


@register_eq_class
class sincos_nv6_nt68_prog_17(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7518 * x[0] * x[5] - 0.8165 * x[1] * x[3] + 0.2704 * x[1] * sympy.sin(x[0]) + 0.982 * x[1] * sympy.cos(
            x[2]) + 0.902 * x[1] - 0.4211 * x[2] + 0.0895 * x[5] + 0.3126 * sympy.sin(x[2]) * sympy.sin(x[3]) + 0.7768 * sympy.sin(
            x[2]) * sympy.cos(x[4]) - 0.1915 * sympy.sin(x[3]) - 0.8788 * sympy.sin(x[4]) * sympy.cos(x[3]) + 0.5331 * sympy.cos(
            x[0]) * sympy.cos(x[2]) + 0.5672 * sympy.cos(x[0]) - 0.6096 * sympy.cos(x[4]) - 0.4848


@register_eq_class
class sincos_nv6_nt68_prog_43(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3538 * x[0] * x[1] + 0.9436 * x[1] * x[4] + 0.1096 * x[1] * sympy.cos(x[2]) + 0.4695 * x[1] - 0.7663 * x[
            2] * sympy.cos(x[0]) + 0.5448 * x[3] * x[5] - 0.4202 * x[3] * sympy.sin(x[0]) - 0.8624 * x[3] - 0.3679 * x[4] * x[5] + 0.9067 * \
                        x[4] * sympy.sin(x[2]) - 0.5444 * sympy.sin(x[0]) + 0.451 * sympy.sin(x[4]) - 0.9957 * sympy.cos(
            x[2]) - 0.6509 * sympy.cos(x[5]) - 0.6731


@register_eq_class
class sincos_nv6_nt68_prog_2(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7649 * x[0] * x[4] - 0.1473 * x[0] + 0.1029 * x[1] * sympy.cos(x[3]) - 0.8555 * x[1] - 0.2482 * x[2] * x[
            4] + 0.3682 * x[2] - 0.6907 * x[3] * sympy.cos(x[2]) - 0.363 * x[4] * sympy.cos(x[5]) - 0.924 * x[5] * sympy.cos(
            x[3]) + 0.9557 * x[5] - 0.4291 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.261 * sympy.sin(x[0]) * sympy.sin(
            x[5]) + 0.1877 * sympy.sin(x[3]) - 0.7424 * sympy.cos(x[4]) - 0.813


@register_eq_class
class sincos_nv6_nt68_prog_4(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2087 * x[0] * sympy.cos(x[5]) - 0.5856 * x[1] - 0.812 * x[2] * sympy.cos(x[0]) - 0.9521 * x[3] * x[5] - 0.2097 * \
                        x[3] * sympy.sin(x[1]) + 0.1516 * x[3] * sympy.sin(x[2]) + 0.4772 * x[3] * sympy.sin(x[4]) + 0.1 * x[4] + 0.198 * x[
                            5] + 0.8366 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.8888 * sympy.sin(x[3]) * sympy.cos(
            x[0]) - 0.5781 * sympy.cos(x[0]) - 0.2709 * sympy.cos(x[2]) - 0.4807 * sympy.cos(x[3]) - 0.7954


@register_eq_class
class sincos_nv6_nt68_prog_45(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0559 * x[0] * x[3] - 0.8756 * x[0] - 0.296 * x[1] * sympy.sin(x[2]) - 0.4461 * x[2] + 0.8257 * x[4] - 0.9799 * x[
            5] * sympy.sin(x[2]) + 0.4826 * x[5] - 0.215 * sympy.sin(x[0]) * sympy.cos(x[2]) + 0.4349 * sympy.sin(
            x[1]) + 0.1625 * sympy.sin(x[4]) * sympy.cos(x[0]) - 0.7461 * sympy.sin(x[4]) * sympy.cos(x[1]) + 0.2663 * sympy.sin(
            x[4]) * sympy.cos(x[2]) + 0.1657 * sympy.sin(x[4]) * sympy.cos(x[5]) + 0.8041 * sympy.cos(x[3]) + 0.5804


@register_eq_class
class sincos_nv6_nt68_prog_49(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7054 * x[0] * x[1] - 0.7976 * x[0] * sympy.cos(x[2]) - 0.4614 * x[0] + 0.0852 * x[1] * x[2] + 0.8086 * x[
            1] * sympy.cos(x[5]) - 0.3854 * x[1] + 0.8543 * x[2] - 0.5901 * x[4] * sympy.sin(x[3]) + 0.4133 * x[4] * sympy.cos(
            x[0]) + 0.0608 * x[4] * sympy.cos(x[5]) + 0.7973 * x[4] + 0.2734 * x[5] * sympy.sin(x[2]) - 0.954 * sympy.sin(
            x[5]) - 0.9378 * sympy.cos(x[3]) - 0.3372


@register_eq_class
class sincos_nv6_nt68_prog_11(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.648 * x[1] + 0.3115 * x[2] * sympy.sin(x[4]) + 0.3963 * x[2] * sympy.cos(x[3]) + 0.4764 * x[3] * sympy.sin(
            x[0]) - 0.9788 * x[4] + 0.2182 * sympy.sin(x[0]) * sympy.sin(x[5]) - 0.0376 * sympy.sin(x[0]) - 0.663 * sympy.sin(
            x[1]) * sympy.cos(x[0]) - 0.4421 * sympy.sin(x[2]) + 0.8898 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.6165 * sympy.sin(
            x[4]) * sympy.cos(x[5]) + 0.4012 * sympy.cos(x[1]) * sympy.cos(x[5]) + 0.7488 * sympy.cos(x[3]) - 0.7798 * sympy.cos(
            x[5]) - 0.0255


@register_eq_class
class sincos_nv6_nt68_prog_10(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4924 * x[0] * sympy.sin(x[5]) + 0.9193 * x[1] * sympy.cos(x[0]) - 0.2075 * x[1] * sympy.cos(x[3]) - 0.4065 * x[
            2] * sympy.cos(x[4]) - 0.8639 * x[2] - 0.22 * x[5] * sympy.sin(x[4]) - 0.517 * sympy.sin(x[0]) + 0.7322 * sympy.sin(
            x[1]) + 0.3853 * sympy.sin(x[2]) * sympy.cos(x[3]) - 0.8127 * sympy.sin(x[4]) * sympy.cos(x[0]) - 0.6615 * sympy.cos(
            x[3]) * sympy.cos(x[4]) - 0.4194 * sympy.cos(x[3]) - 0.0604 * sympy.cos(x[4]) - 0.2489 * sympy.cos(x[5]) - 0.8421


@register_eq_class
class sincos_nv6_nt68_prog_1(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4238 * x[0] * x[1] + 0.8691 * x[0] * sympy.cos(x[3]) + 0.1904 * x[0] + 0.7298 * x[1] * x[2] - 0.8796 * x[
            1] * sympy.cos(x[3]) + 0.7143 * x[2] * sympy.sin(x[3]) + 0.77 * x[2] - 0.7943 * x[3] + 0.0569 * x[4] * sympy.cos(
            x[0]) + 0.7245 * x[5] * sympy.sin(x[0]) + 0.3887 * x[5] * sympy.sin(x[1]) + 0.4623 * sympy.sin(x[1]) + 0.8524 * sympy.sin(
            x[4]) + 0.022 * sympy.cos(x[5]) - 0.5906


@register_eq_class
class sincos_nv6_nt68_prog_40(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6389 * x[0] * x[5] - 0.4684 * x[0] + 0.3119 * x[1] * sympy.sin(x[0]) + 0.1313 * x[1] * sympy.sin(x[5]) + 0.6545 * \
                        x[2] * sympy.sin(x[4]) + 0.4244 * x[2] + 0.3702 * x[3] * sympy.sin(x[2]) + 0.7027 * x[3] - 0.4744 * x[
                            4] * sympy.sin(x[1]) + 0.2447 * x[4] - 0.7951 * x[5] - 0.7269 * sympy.sin(x[0]) * sympy.sin(
            x[2]) + 0.2868 * sympy.cos(x[0]) * sympy.cos(x[4]) + 0.1596 * sympy.cos(x[1]) - 0.7255


@register_eq_class
class sincos_nv6_nt68_prog_29(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6055 * x[3] * x[5] + 0.5075 * x[4] * sympy.sin(x[1]) - 0.6983 * x[4] - 0.7054 * x[5] * sympy.cos(x[2]) - 0.7719 * \
                        x[5] + 0.1879 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.7928 * sympy.sin(x[0]) * sympy.cos(x[5]) + 0.2441 * sympy.sin(
            x[0]) + 0.5113 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.9604 * sympy.sin(x[3]) - 0.2044 * sympy.sin(x[4]) * sympy.cos(
            x[2]) - 0.2362 * sympy.sin(x[4]) * sympy.cos(x[5]) + 0.8077 * sympy.cos(x[1]) + 0.3408 * sympy.cos(x[2]) - 0.2542


@register_eq_class
class sincos_nv6_nt68_prog_22(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1968 * x[0] * x[5] + 0.7771 * x[0] * sympy.sin(x[1]) + 0.53 * x[1] * x[3] + 0.6916 * x[1] - 0.5299 * x[
            2] * sympy.sin(x[4]) + 0.9964 * x[3] * sympy.sin(x[5]) - 0.7115 * x[3] + 0.1842 * x[4] * sympy.sin(x[1]) + 0.2107 * x[
                            5] * sympy.cos(x[4]) + 0.1189 * sympy.sin(x[0]) + 0.8164 * sympy.sin(x[1]) * sympy.cos(
            x[2]) - 0.1712 * sympy.sin(x[5]) - 0.3951 * sympy.cos(x[2]) + 0.1818 * sympy.cos(x[4]) + 0.4472


@register_eq_class
class sincos_nv6_nt68_prog_27(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0632 * x[0] - 0.0164 * x[1] * sympy.sin(x[3]) - 0.2157 * x[1] * sympy.cos(x[4]) - 0.361 * x[1] + 0.2889 * x[
            2] * sympy.sin(x[1]) - 0.8574 * x[3] * x[5] - 0.9119 * x[3] * sympy.cos(x[2]) + 0.7888 * x[4] * sympy.sin(
            x[5]) - 0.3896 * sympy.sin(x[0]) * sympy.sin(x[3]) - 0.3629 * sympy.sin(x[2]) - 0.5538 * sympy.sin(x[3]) - 0.9287 * sympy.sin(
            x[4]) - 0.5804 * sympy.sin(x[5]) - 0.9517 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.4875


@register_eq_class
class sincos_nv6_nt68_prog_34(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4624 * x[0] * sympy.sin(x[3]) - 0.2878 * x[2] * x[4] + 0.397 * x[2] - 0.9413 * x[3] * sympy.sin(x[4]) - 0.5753 * \
                        x[4] * sympy.sin(x[0]) + 0.6763 * x[4] * sympy.cos(x[1]) - 0.3658 * x[4] - 0.1413 * x[5] * sympy.cos(
            x[2]) - 0.3527 * sympy.sin(x[0]) + 0.8329 * sympy.sin(x[1]) + 0.1482 * sympy.sin(x[3]) * sympy.sin(x[5]) - 0.6887 * sympy.sin(
            x[3]) + 0.2223 * sympy.sin(x[4]) * sympy.cos(x[5]) + 0.1224 * sympy.cos(x[5]) + 0.9152


@register_eq_class
class sincos_nv6_nt68_prog_16(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6438 * x[0] * x[1] + 0.0298 * x[0] * x[5] + 0.9327 * x[1] * x[3] + 0.0779 * x[1] - 0.1318 * x[2] * sympy.cos(
            x[5]) + 0.0846 * x[2] + 0.6966 * x[3] * x[5] - 0.6517 * x[3] * sympy.sin(x[0]) + 0.8566 * x[3] - 0.3588 * x[4] + 0.3225 * x[
                            5] - 0.9155 * sympy.sin(x[0]) - 0.3923 * sympy.cos(x[1]) * sympy.cos(x[5]) - 0.4323 * sympy.cos(
            x[3]) * sympy.cos(x[4]) + 0.5773


@register_eq_class
class sincos_nv6_nt68_prog_13(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.854 * x[0] - 0.5133 * x[2] * x[5] - 0.174 * x[2] * sympy.cos(x[0]) + 0.7172 * x[2] - 0.085 * x[3] * x[
            4] - 0.2272 * x[3] * sympy.sin(x[2]) - 0.0721 * x[3] * sympy.cos(x[0]) - 0.1334 * x[4] * sympy.sin(x[1]) + 0.2072 * x[
                            4] * sympy.cos(x[0]) + 0.5844 * x[5] * sympy.cos(x[3]) - 0.5493 * x[5] + 0.0274 * sympy.sin(
            x[4]) - 0.0179 * sympy.cos(x[1]) - 0.367 * sympy.cos(x[3]) - 0.2137


@register_eq_class
class sincos_nv6_nt68_prog_47(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9736 * x[0] * x[1] - 0.8663 * x[0] * x[5] - 0.1654 * x[0] + 0.3461 * x[1] * sympy.cos(x[4]) - 0.8739 * x[
            1] + 0.2394 * x[2] * sympy.cos(x[0]) + 0.8408 * x[3] * x[5] + 0.3888 * x[4] * sympy.cos(x[2]) - 0.9609 * x[
                            4] + 0.3562 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.3805 * sympy.sin(x[2]) * sympy.sin(
            x[3]) - 0.7409 * sympy.sin(x[2]) + 0.0855 * sympy.sin(x[3]) - 0.8774 * sympy.cos(x[5]) + 0.1863


@register_eq_class
class sincos_nv6_nt68_prog_36(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6709 * x[0] * x[2] + 0.3414 * x[0] * sympy.sin(x[1]) - 0.0027 * x[1] + 0.2189 * x[2] - 0.7815 * x[3] * sympy.sin(
            x[2]) - 0.5663 * x[3] * sympy.cos(x[0]) - 0.5106 * x[4] * sympy.sin(x[5]) - 0.2663 * x[5] + 0.2637 * sympy.sin(
            x[1]) * sympy.cos(x[3]) - 0.2149 * sympy.sin(x[3]) + 0.6766 * sympy.sin(x[5]) * sympy.cos(x[0]) - 0.63 * sympy.cos(
            x[0]) - 0.7807 * sympy.cos(x[3]) * sympy.cos(x[4]) + 0.9869 * sympy.cos(x[4]) + 0.4553


@register_eq_class
class sincos_nv6_nt68_prog_44(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4232 * x[0] * x[2] + 0.4203 * x[0] * sympy.cos(x[3]) + 0.2427 * x[2] * x[3] + 0.8659 * x[2] * sympy.cos(
            x[4]) + 0.5528 * x[2] + 0.7046 * x[3] * sympy.sin(x[5]) - 0.1812 * x[3] - 0.8769 * x[4] + 0.9297 * x[5] * sympy.cos(
            x[1]) - 0.5761 * x[5] * sympy.cos(x[4]) - 0.7768 * x[5] + 0.7312 * sympy.sin(x[3]) * sympy.cos(x[4]) + 0.3367 * sympy.cos(
            x[0]) + 0.9716 * sympy.cos(x[1]) - 0.7191


@register_eq_class
class sincos_nv6_nt68_prog_6(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.788 * x[0] * x[1] + 0.933 * x[0] * sympy.sin(x[3]) + 0.3817 * x[0] - 0.7029 * x[1] * x[4] + 0.1066 * x[
            1] - 0.016 * x[2] * sympy.sin(x[0]) - 0.52 * x[2] * sympy.cos(x[4]) + 0.4698 * x[2] - 0.2633 * x[3] * sympy.sin(x[5]) - 0.2839 * \
                        x[3] + 0.8953 * x[4] * x[5] - 0.7737 * x[4] + 0.3366 * x[5] * sympy.sin(x[2]) + 0.4863 * x[5] + 0.4236


@register_eq_class
class sincos_nv6_nt68_prog_18(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4174 * x[0] * x[3] - 0.2978 * x[0] - 0.793 * x[1] * x[2] - 0.0793 * x[1] * sympy.sin(x[0]) - 0.6256 * x[
            1] * sympy.sin(x[3]) - 0.9323 * x[3] * x[5] + 0.0486 * x[5] + 0.1611 * sympy.sin(x[1]) + 0.3214 * sympy.sin(
            x[4]) - 0.041 * sympy.sin(x[5]) * sympy.cos(x[4]) + 0.9126 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.9936 * sympy.cos(
            x[2]) * sympy.cos(x[4]) + 0.0405 * sympy.cos(x[2]) + 0.1492 * sympy.cos(x[3]) - 0.4224


@register_eq_class
class sincos_nv6_nt68_prog_3(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1719 * x[0] * sympy.cos(x[2]) - 0.8355 * x[0] + 0.5465 * x[2] * sympy.cos(x[4]) + 0.0902 * x[2] - 0.6778 * x[
            3] * sympy.sin(x[5]) + 0.0868 * x[3] - 0.8897 * x[4] + 0.1555 * x[5] * sympy.cos(x[2]) + 0.0805 * sympy.sin(x[0]) * sympy.cos(
            x[3]) - 0.7364 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.9263 * sympy.sin(x[1]) * sympy.cos(x[4]) + 0.0824 * sympy.sin(
            x[3]) * sympy.cos(x[4]) + 0.3615 * sympy.cos(x[1]) - 0.4581 * sympy.cos(x[5]) - 0.4257


@register_eq_class
class sincos_nv6_nt68_prog_24(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8441 * x[0] * sympy.sin(x[2]) - 0.0067 * x[0] * sympy.cos(x[1]) + 0.8354 * x[1] * x[2] - 0.6822 * x[2] * x[
            5] - 0.2898 * x[2] + 0.4468 * x[3] * sympy.sin(x[0]) + 0.8796 * x[3] + 0.9664 * x[4] * sympy.sin(x[2]) - 0.5439 * x[4] - 0.636 * \
                        x[5] * sympy.cos(x[4]) + 0.4145 * sympy.sin(x[4]) * sympy.cos(x[3]) + 0.416 * sympy.cos(x[0]) - 0.3268 * sympy.cos(
            x[1]) + 0.4438 * sympy.cos(x[5]) - 0.0365


@register_eq_class
class sincos_nv6_nt68_prog_12(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3915 * x[0] * x[3] - 0.0011 * x[0] * x[4] - 0.3272 * x[1] * sympy.sin(x[4]) - 0.6898 * x[2] * x[3] + 0.0159 * x[
            2] * sympy.cos(x[5]) + 0.0116 * x[2] + 0.8577 * x[3] * sympy.sin(x[5]) - 0.8915 * x[4] + 0.7643 * x[5] * sympy.sin(
            x[4]) + 0.3949 * x[5] - 0.4531 * sympy.sin(x[0]) - 0.9465 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.3888 * sympy.cos(
            x[1]) + 0.2738 * sympy.cos(x[3]) + 0.2826


@register_eq_class
class sincos_nv6_nt68_prog_25(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.794 * x[0] * sympy.sin(x[4]) - 0.7209 * x[1] + 0.3866 * x[2] * x[5] - 0.6593 * x[2] + 0.1739 * x[3] * sympy.cos(
            x[0]) + 0.9174 * x[3] * sympy.cos(x[2]) - 0.3327 * x[3] - 0.7551 * x[4] - 0.9158 * x[5] * sympy.cos(x[1]) - 0.2836 * x[
                            5] * sympy.cos(x[3]) + 0.5408 * x[5] - 0.7612 * sympy.sin(x[0]) - 0.9046 * sympy.sin(x[2]) * sympy.cos(
            x[0]) + 0.5333 * sympy.cos(x[2]) * sympy.cos(x[4]) - 0.6502


@register_eq_class
class sincos_nv6_nt68_prog_21(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2696 * x[1] * sympy.sin(x[2]) + 0.8447 * x[1] * sympy.sin(x[4]) - 0.987 * x[2] * x[5] + 0.3588 * x[2] - 0.1775 * \
                        x[3] * sympy.sin(x[0]) + 0.5495 * x[4] * x[5] + 0.6549 * x[4] * sympy.cos(x[0]) + 0.3061 * x[5] * sympy.sin(
            x[1]) + 0.8093 * x[5] + 0.8497 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.0385 * sympy.sin(x[3]) + 0.4039 * sympy.sin(
            x[4]) + 0.0843 * sympy.cos(x[0]) - 0.3215 * sympy.cos(x[1]) + 0.795


@register_eq_class
class sincos_nv6_nt68_prog_26(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4378 * x[0] * sympy.cos(x[4]) - 0.0074 * x[1] * sympy.sin(x[0]) - 0.7713 * x[1] * sympy.sin(x[5]) + 0.4937 * x[
            2] - 0.1796 * x[3] * sympy.cos(x[1]) - 0.8724 * x[3] * sympy.cos(x[5]) + 0.7778 * x[4] - 0.5412 * x[5] * sympy.sin(
            x[4]) + 0.6322 * x[5] * sympy.cos(x[0]) + 0.1155 * x[5] + 0.2567 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.9419 * sympy.cos(
            x[0]) - 0.4388 * sympy.cos(x[1]) + 0.5788 * sympy.cos(x[3]) + 0.2489


@register_eq_class
class sincos_nv6_nt68_prog_39(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7159 * x[1] * x[3] - 0.5482 * x[1] * x[5] + 0.2791 * x[1] + 0.5193 * x[2] * x[5] + 0.7344 * x[3] * sympy.cos(
            x[2]) - 0.8247 * x[3] - 0.196 * x[4] * sympy.sin(x[5]) - 0.6714 * sympy.sin(x[0]) * sympy.sin(x[4]) + 0.4102 * sympy.sin(
            x[0]) + 0.1131 * sympy.sin(x[2]) * sympy.cos(x[1]) + 0.6992 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.3954 * sympy.sin(
            x[4]) - 0.6784 * sympy.cos(x[2]) - 0.2515 * sympy.cos(x[5]) - 0.4585


@register_eq_class
class sincos_nv6_nt68_prog_19(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.936 * x[0] * x[1] + 0.1609 * x[0] - 0.5844 * x[1] * x[4] + 0.0402 * x[1] * sympy.cos(x[3]) + 0.3809 * x[
            2] * sympy.cos(x[5]) - 0.3316 * x[2] - 0.429 * x[3] * x[5] - 0.0829 * x[3] * sympy.sin(x[4]) - 0.7529 * x[4] * sympy.cos(
            x[0]) + 0.6742 * sympy.sin(x[1]) - 0.6884 * sympy.sin(x[4]) - 0.0693 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.1412 * sympy.cos(
            x[3]) - 0.2797 * sympy.cos(x[5]) + 0.1429


@register_eq_class
class sincos_nv6_nt68_prog_38(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1872 * x[1] - 0.5632 * x[2] * sympy.sin(x[3]) + 0.1213 * x[2] - 0.4871 * x[4] * sympy.sin(x[1]) + 0.9532 * x[
            4] * sympy.sin(x[2]) - 0.4361 * x[4] * sympy.cos(x[3]) - 0.5452 * x[5] * sympy.sin(x[4]) + 0.1125 * x[5] * sympy.cos(
            x[3]) + 0.7234 * sympy.sin(x[0]) * sympy.sin(x[4]) - 0.6788 * sympy.sin(x[3]) - 0.4035 * sympy.sin(x[5]) * sympy.cos(
            x[0]) + 0.8173 * sympy.sin(x[5]) + 0.5207 * sympy.cos(x[0]) + 0.3184 * sympy.cos(x[4]) + 0.6359


@register_eq_class
class sincos_nv6_nt68_prog_9(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4156 * x[0] - 0.8627 * x[1] + 0.3798 * x[2] * x[3] - 0.7519 * x[2] - 0.4477 * x[3] * x[4] - 0.3972 * x[3] * x[
            5] + 0.7483 * x[3] + 0.2645 * x[4] * x[5] - 0.7134 * x[4] * sympy.sin(x[1]) + 0.7113 * x[4] + 0.2156 * x[
                            5] - 0.6523 * sympy.cos(x[0]) * sympy.cos(x[1]) - 0.3762 * sympy.cos(x[0]) * sympy.cos(
            x[5]) + 0.1562 * sympy.cos(x[2]) * sympy.cos(x[4]) + 0.0797


@register_eq_class
class sincos_nv6_nt68_prog_32(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4624 * x[0] * x[5] + 0.5904 * x[1] * x[3] - 0.4102 * x[1] * sympy.cos(x[4]) - 0.4217 * x[1] - 0.5334 * x[2] * x[
            4] - 0.8096 * x[3] * sympy.sin(x[2]) - 0.2258 * x[4] * sympy.sin(x[5]) - 0.3646 * x[5] - 0.5523 * sympy.sin(
            x[3]) - 0.3421 * sympy.sin(x[4]) - 0.5854 * sympy.cos(x[0]) * sympy.cos(x[4]) + 0.6167 * sympy.cos(x[0]) - 0.2058 * sympy.cos(
            x[1]) * sympy.cos(x[2]) - 0.5547 * sympy.cos(x[2]) - 0.7362


@register_eq_class
class sincos_nv6_nt68_prog_5(KnownEquation):
    _eq_name = 'sincos_nv6_nt68_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2462 * x[0] * x[4] - 0.155 * x[0] * sympy.sin(x[1]) - 0.6237 * x[0] * sympy.cos(x[3]) - 0.7908 * x[0] - 0.7171 * \
                        x[1] * x[2] + 0.2545 * x[2] * sympy.sin(x[5]) + 0.6264 * x[3] * x[4] + 0.4496 * x[3] + 0.2819 * x[
                            5] - 0.2497 * sympy.sin(x[2]) + 0.7844 * sympy.sin(x[4]) - 0.5904 * sympy.cos(x[1]) * sympy.cos(
            x[5]) - 0.0258 * sympy.cos(x[1]) + 0.8132 * sympy.cos(x[2]) * sympy.cos(x[4]) + 0.3874


@register_eq_class
class sincos_nv4_nt46_prog_46(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.728 * x[0] * x[2] + 0.0416 * x[1] * x[2] - 0.8613 * x[2] + 0.514 * x[3] * sympy.cos(x[2]) + 0.8656 * x[
            3] + 0.9462 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.3902 * sympy.sin(x[1]) * sympy.cos(x[3]) + 0.1608 * sympy.cos(
            x[0]) * sympy.cos(x[1]) + 0.5869 * sympy.cos(x[0]) - 0.2312 * sympy.cos(x[1]) + 0.0537


@register_eq_class
class sincos_nv4_nt46_prog_0(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0424 * x[1] * x[2] - 0.7582 * x[1] + 0.9181 * x[2] * x[3] - 0.587 * x[2] * sympy.cos(x[0]) + 0.2988 * x[
            2] - 0.9579 * x[3] + 0.2076 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.0865 * sympy.sin(x[0]) + 0.9965 * sympy.sin(
            x[1]) * sympy.cos(x[3]) + 0.8622 * sympy.cos(x[0]) * sympy.cos(x[3]) + 0.124


@register_eq_class
class sincos_nv4_nt46_prog_35(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2508 * x[1] * sympy.sin(x[0]) - 0.3516 * x[1] * sympy.sin(x[3]) + 0.5155 * x[2] * sympy.cos(x[1]) - 0.4028 * x[
            3] * sympy.cos(x[0]) - 0.3056 * x[3] * sympy.cos(x[2]) + 0.0979 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.8285 * sympy.sin(
            x[0]) - 0.9994 * sympy.sin(x[1]) + 0.5462 * sympy.sin(x[2]) - 0.6506 * sympy.sin(x[3]) + 0.989


@register_eq_class
class sincos_nv4_nt46_prog_8(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7331 * x[0] * x[1] + 0.7149 * x[0] * x[3] - 0.937 * x[0] * sympy.sin(x[2]) - 0.8632 * x[1] + 0.5757 * x[
            3] + 0.7605 * sympy.sin(x[0]) + 0.3964 * sympy.sin(x[1]) * sympy.sin(x[3]) + 0.3957 * sympy.sin(x[2]) * sympy.cos(
            x[1]) + 0.5416 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.7617 * sympy.sin(x[2]) + 0.8487


@register_eq_class
class sincos_nv4_nt46_prog_42(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4552 * x[0] * x[3] + 0.7343 * x[0] * sympy.cos(x[1]) - 0.0764 * x[0] * sympy.cos(x[2]) + 0.8594 * x[0] - 0.8933 * \
                        x[1] * x[2] + 0.4907 * x[3] * sympy.sin(x[1]) + 0.8648 * sympy.sin(x[2]) * sympy.sin(x[3]) - 0.1494 * sympy.cos(
            x[1]) + 0.0267 * sympy.cos(x[2]) + 0.8686 * sympy.cos(x[3]) - 0.2305


@register_eq_class
class sincos_nv4_nt46_prog_33(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0104 * x[0] * x[3] - 0.612 * x[0] * sympy.cos(x[2]) - 0.8134 * x[1] * x[2] - 0.8294 * x[1] * sympy.cos(
            x[0]) - 0.6552 * x[2] * x[3] + 0.9608 * sympy.sin(x[0]) - 0.6127 * sympy.sin(x[1]) * sympy.cos(x[3]) + 0.7974 * sympy.sin(
            x[1]) + 0.8163 * sympy.cos(x[2]) + 0.5541 * sympy.cos(x[3]) - 0.5612


@register_eq_class
class sincos_nv4_nt46_prog_20(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.25 * x[1] * sympy.cos(x[0]) + 0.1675 * x[1] + 0.7808 * x[2] * sympy.sin(x[0]) - 0.2374 * x[2] * sympy.cos(
            x[3]) - 0.2843 * x[3] * sympy.cos(x[1]) - 0.6355 * sympy.sin(x[0]) * sympy.sin(x[3]) - 0.3164 * sympy.sin(
            x[0]) - 0.6132 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.5603 * sympy.sin(x[2]) + 0.9756 * sympy.cos(x[3]) + 0.9528


@register_eq_class
class sincos_nv4_nt46_prog_14(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.8969 * x[0] * sympy.sin(x[1]) + 0.7809 * x[0] * sympy.cos(x[3]) - 0.3793 * x[1] * x[3] - 0.0101 * x[
            1] * sympy.sin(x[2]) - 0.4309 * x[2] * x[3] - 0.0778 * x[2] * sympy.cos(x[0]) + 0.4468 * sympy.sin(x[2]) + 0.8371 * sympy.cos(
            x[0]) + 0.5542 * sympy.cos(x[1]) + 0.987 * sympy.cos(x[3]) + 0.1084


@register_eq_class
class sincos_nv4_nt46_prog_31(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.6302 * x[1] * x[3] + 0.5137 * x[1] * sympy.sin(x[2]) - 0.7816 * x[1] - 0.1478 * x[2] * sympy.cos(x[0]) - 0.0134 * \
                        x[2] * sympy.cos(x[3]) + 0.5335 * x[2] + 0.2765 * x[3] * sympy.cos(x[0]) - 0.956 * x[3] - 0.2059 * sympy.sin(
            x[0]) * sympy.cos(x[1]) - 0.0345 * sympy.cos(x[0]) - 0.1258


@register_eq_class
class sincos_nv4_nt46_prog_48(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5453 * x[0] * x[2] + 0.0989 * x[0] * x[3] - 0.9633 * x[0] + 0.6513 * x[1] * sympy.cos(x[0]) + 0.5628 * x[
            1] + 0.3013 * x[2] * x[3] - 0.199 * x[2] * sympy.sin(x[1]) - 0.3247 * sympy.sin(x[1]) * sympy.sin(x[3]) + 0.2534 * sympy.cos(
            x[2]) + 0.8193 * sympy.cos(x[3]) + 0.6534


@register_eq_class
class sincos_nv4_nt46_prog_41(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.4496 * x[1] * sympy.sin(x[2]) + 0.4733 * x[1] * sympy.cos(x[0]) - 0.0485 * x[1] - 0.2316 * x[2] * sympy.sin(
            x[0]) + 0.9249 * x[2] * sympy.sin(x[3]) - 0.0888 * x[2] + 0.7611 * x[3] + 0.8474 * sympy.sin(x[0]) + 0.263 * sympy.sin(
            x[1]) * sympy.sin(x[3]) + 0.5684 * sympy.cos(x[0]) * sympy.cos(x[3]) - 0.8549


@register_eq_class
class sincos_nv4_nt46_prog_7(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5062 * x[0] * x[2] - 0.652 * x[0] * sympy.sin(x[3]) + 0.9153 * x[1] * x[3] - 0.7422 * x[1] + 0.0369 * x[
            2] - 0.2263 * x[3] - 0.7665 * sympy.sin(x[0]) - 0.5118 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.7336 * sympy.sin(
            x[3]) * sympy.cos(x[2]) - 0.1184 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.4495


@register_eq_class
class sincos_nv4_nt46_prog_37(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8383 * x[0] * sympy.sin(x[3]) - 0.6052 * x[0] * sympy.cos(x[1]) - 0.884 * x[1] * x[2] + 0.5739 * x[1] * sympy.cos(
            x[3]) - 0.0513 * x[1] - 0.1727 * x[2] * sympy.sin(x[3]) - 0.6141 * x[2] * sympy.cos(x[0]) + 0.9247 * sympy.sin(
            x[0]) + 0.8287 * sympy.sin(x[2]) - 0.0883 * sympy.sin(x[3]) - 0.8876


@register_eq_class
class sincos_nv4_nt46_prog_15(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8202 * x[0] * x[2] - 0.2091 * x[0] * sympy.sin(x[1]) + 0.6052 * x[0] * sympy.cos(x[3]) - 0.5521 * x[0] - 0.7434 * \
                        x[1] * x[2] + 0.7492 * x[3] * sympy.sin(x[1]) - 0.0204 * x[3] * sympy.cos(x[2]) + 0.0972 * x[
                            3] + 0.2149 * sympy.cos(x[1]) - 0.3556 * sympy.cos(x[2]) - 0.8022


@register_eq_class
class sincos_nv4_nt46_prog_23(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.5301 * x[1] * sympy.cos(x[0]) - 0.3861 * x[1] - 0.8507 * x[2] * sympy.cos(x[0]) + 0.9205 * x[2] + 0.6805 * x[
            3] * sympy.cos(x[1]) - 0.017 * x[3] - 0.5634 * sympy.sin(x[0]) + 0.4474 * sympy.sin(x[1]) * sympy.cos(
            x[2]) - 0.3874 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.5169 * sympy.cos(x[2]) * sympy.cos(x[3]) - 0.3755


@register_eq_class
class sincos_nv4_nt46_prog_30(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.6591 * x[0] * x[1] - 0.6296 * x[0] * sympy.sin(x[3]) - 0.2197 * x[0] + 0.4094 * x[1] * x[3] + 0.377 * x[
            2] * sympy.sin(x[0]) - 0.6691 * x[2] * sympy.sin(x[1]) + 0.9215 * x[2] - 0.1152 * x[3] - 0.706 * sympy.cos(
            x[1]) + 0.3577 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.8568


@register_eq_class
class sincos_nv4_nt46_prog_28(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.7405 * x[0] * x[2] - 0.4025 * x[0] * x[3] + 0.6825 * x[1] * x[3] + 0.9548 * x[1] * sympy.sin(x[2]) - 0.6135 * x[
            1] * sympy.cos(x[0]) + 0.2975 * x[2] + 0.2789 * sympy.sin(x[0]) - 0.7332 * sympy.sin(x[1]) + 0.5927 * sympy.sin(
            x[2]) * sympy.cos(x[3]) + 0.2373 * sympy.sin(x[3]) - 0.2082


@register_eq_class
class sincos_nv4_nt46_prog_17(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.4285 * x[0] * sympy.sin(x[3]) + 0.0138 * x[0] - 0.9014 * x[1] * sympy.cos(x[0]) + 0.2433 * x[1] + 0.2898 * x[
            2] * sympy.cos(x[0]) + 0.938 * x[2] + 0.2131 * x[3] * sympy.sin(x[1]) + 0.1013 * x[3] * sympy.cos(x[2]) - 0.5214 * x[
                            3] - 0.8189 * sympy.cos(x[1]) * sympy.cos(x[2]) - 0.2747


@register_eq_class
class sincos_nv4_nt46_prog_43(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6399 * x[0] * x[3] + 0.1875 * x[0] * sympy.sin(x[2]) - 0.2453 * x[0] - 0.686 * x[1] * x[3] - 0.6015 * x[
            1] * sympy.sin(x[0]) + 0.6776 * x[1] - 0.7486 * x[3] * sympy.cos(x[2]) + 0.6276 * sympy.sin(x[1]) * sympy.sin(
            x[2]) + 0.6023 * sympy.sin(x[2]) - 0.0484 * sympy.sin(x[3]) + 0.6352


@register_eq_class
class sincos_nv4_nt46_prog_2(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.9296 * x[0] + 0.6272 * x[1] * sympy.sin(x[0]) + 0.4468 * x[2] * x[3] + 0.7135 * sympy.sin(x[0]) * sympy.cos(
            x[3]) + 0.6816 * sympy.sin(x[2]) - 0.9374 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.5579 * sympy.sin(x[3]) - 0.5481 * sympy.cos(
            x[0]) * sympy.cos(x[2]) - 0.837 * sympy.cos(x[1]) * sympy.cos(x[2]) - 0.3081 * sympy.cos(x[1]) - 0.1092


@register_eq_class
class sincos_nv4_nt46_prog_4(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.3847 * x[0] * x[3] - 0.904 * x[1] * sympy.sin(x[0]) - 0.3458 * x[1] * sympy.sin(x[2]) + 0.2652 * x[1] * sympy.cos(
            x[3]) + 0.9379 * x[1] - 0.0158 * x[2] * sympy.cos(x[0]) - 0.0119 * x[2] - 0.6445 * x[3] * sympy.sin(x[2]) - 0.7881 * x[
                            3] + 0.1602 * sympy.sin(x[0]) + 0.0368


@register_eq_class
class sincos_nv4_nt46_prog_45(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.4064 * x[0] * x[2] - 0.3988 * x[0] * x[3] - 0.1441 * x[0] + 0.3797 * x[1] * x[2] - 0.2779 * x[1] * sympy.sin(
            x[3]) - 0.0508 * x[2] - 0.9168 * x[3] - 0.114 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.841 * sympy.sin(
            x[1]) + 0.5114 * sympy.sin(x[2]) * sympy.cos(x[3]) - 0.0655


@register_eq_class
class sincos_nv4_nt46_prog_49(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0778 * x[0] * x[1] + 0.806 * x[0] * x[2] - 0.9983 * x[0] * sympy.cos(x[3]) + 0.428 * x[2] + 0.9169 * x[
            3] * sympy.sin(x[2]) + 0.3283 * x[3] * sympy.cos(x[1]) - 0.9083 * x[3] - 0.655 * sympy.sin(x[0]) - 0.0637 * sympy.sin(
            x[1]) * sympy.sin(x[2]) + 0.7432 * sympy.cos(x[1]) + 0.9913


@register_eq_class
class sincos_nv4_nt46_prog_11(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.4738 * x[0] * sympy.sin(x[3]) - 0.2067 * x[1] * sympy.sin(x[0]) + 0.704 * x[2] - 0.4933 * x[3] * sympy.sin(
            x[2]) - 0.3171 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.7073 * sympy.sin(x[0]) - 0.8415 * sympy.sin(x[1]) * sympy.cos(
            x[3]) + 0.4587 * sympy.sin(x[1]) + 0.6535 * sympy.sin(x[2]) * sympy.cos(x[1]) - 0.5994 * sympy.sin(x[3]) + 0.8929


@register_eq_class
class sincos_nv4_nt46_prog_10(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0704 * x[0] * x[1] + 0.414 * x[0] * sympy.cos(x[3]) - 0.751 * x[2] * sympy.sin(x[0]) + 0.7486 * x[2] * sympy.sin(
            x[1]) - 0.2294 * x[2] + 0.8844 * sympy.sin(x[0]) - 0.836 * sympy.sin(x[1]) * sympy.sin(x[3]) + 0.2785 * sympy.sin(
            x[3]) - 0.1719 * sympy.cos(x[1]) + 0.4019 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.752


@register_eq_class
class sincos_nv4_nt46_prog_1(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5998 * x[0] * x[1] + 0.5148 * x[0] * x[2] + 0.0606 * x[0] * x[3] + 0.1105 * x[1] * x[3] - 0.8742 * x[1] - 0.8527 * \
                        x[2] * x[3] - 0.0896 * x[2] * sympy.sin(x[1]) + 0.2811 * x[2] + 0.8264 * sympy.sin(x[0]) + 0.0406 * sympy.sin(
            x[3]) + 0.4854


@register_eq_class
class sincos_nv4_nt46_prog_40(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.7165 * x[0] * x[2] - 0.1159 * x[0] + 0.2359 * x[1] * sympy.sin(x[2]) + 0.4703 * x[1] * sympy.cos(x[3]) - 0.7133 * \
                        x[1] + 0.5696 * x[3] * sympy.sin(x[2]) - 0.2506 * x[3] * sympy.cos(x[0]) + 0.0381 * x[3] - 0.234 * sympy.sin(
            x[0]) * sympy.cos(x[1]) - 0.7516 * sympy.sin(x[2]) - 0.7459


@register_eq_class
class sincos_nv4_nt46_prog_29(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8346 * x[0] * sympy.cos(x[3]) + 0.3711 * x[1] * sympy.sin(x[2]) - 0.3622 * x[1] * sympy.cos(x[0]) - 0.0722 * x[
            1] - 0.2886 * x[2] * x[3] + 0.2877 * x[3] - 0.6236 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.0251 * sympy.sin(x[1]) * sympy.sin(
            x[3]) + 0.5719 * sympy.cos(x[0]) + 0.0322 * sympy.cos(x[2]) + 0.5233


@register_eq_class
class sincos_nv4_nt46_prog_22(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4655 * x[0] * x[2] - 0.0067 * x[0] * x[3] - 0.1994 * x[0] * sympy.cos(x[1]) + 0.083 * x[0] + 0.746 * x[
            1] * sympy.sin(x[3]) + 0.7204 * x[2] * sympy.cos(x[1]) + 0.887 * sympy.sin(x[1]) + 0.5476 * sympy.sin(
            x[2]) + 0.5287 * sympy.sin(x[3]) - 0.3598 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.4726


@register_eq_class
class sincos_nv4_nt46_prog_27(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7025 * x[0] * x[1] - 0.8419 * x[0] - 0.4162 * x[1] * sympy.cos(x[3]) + 0.3138 * x[2] * sympy.sin(x[1]) + 0.1387 * \
                        x[3] * sympy.sin(x[0]) - 0.5351 * x[3] * sympy.cos(x[2]) + 0.6474 * sympy.sin(x[1]) - 0.645 * sympy.sin(
            x[2]) * sympy.cos(x[0]) - 0.4861 * sympy.sin(x[2]) + 0.0952 * sympy.cos(x[3]) + 0.2126


@register_eq_class
class sincos_nv4_nt46_prog_34(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0494 * x[0] * x[2] + 0.3735 * x[0] * sympy.sin(x[1]) + 0.1951 * x[0] - 0.3194 * x[1] * x[2] + 0.3963 * x[
            1] * sympy.cos(x[3]) + 0.0877 * x[2] * x[3] + 0.3669 * x[3] + 0.5849 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.5184 * sympy.sin(
            x[1]) - 0.6701 * sympy.sin(x[2]) - 0.7795


@register_eq_class
class sincos_nv4_nt46_prog_16(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5642 * x[0] * sympy.cos(x[1]) + 0.6919 * x[1] - 0.1201 * x[2] * x[3] + 0.7913 * x[2] * sympy.cos(x[0]) - 0.5961 * \
                        x[3] * sympy.cos(x[1]) + 0.7631 * x[3] - 0.4941 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.9847 * sympy.sin(
            x[2]) - 0.4792 * sympy.cos(x[0]) * sympy.cos(x[3]) - 0.9811 * sympy.cos(x[0]) - 0.3025


@register_eq_class
class sincos_nv4_nt46_prog_13(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.9934 * x[0] * sympy.sin(x[1]) + 0.7986 * x[0] + 0.6548 * x[1] - 0.6979 * x[2] * sympy.sin(x[0]) + 0.679 * x[
            2] * sympy.cos(x[1]) + 0.1954 * x[3] + 0.207 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.6338 * sympy.sin(
            x[2]) + 0.1706 * sympy.cos(x[0]) * sympy.cos(x[3]) + 0.4969 * sympy.cos(x[1]) * sympy.cos(x[3]) + 0.2811


@register_eq_class
class sincos_nv4_nt46_prog_47(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.629 * x[0] * x[2] + 0.0991 * x[0] - 0.369 * x[1] * sympy.sin(x[0]) - 0.1384 * x[1] * sympy.cos(x[3]) - 0.0122 * x[
            1] - 0.7737 * x[2] * sympy.sin(x[1]) - 0.6799 * x[2] - 0.686 * x[3] * sympy.sin(x[0]) - 0.2542 * x[3] * sympy.sin(
            x[2]) + 0.8127 * sympy.sin(x[3]) + 0.1989


@register_eq_class
class sincos_nv4_nt46_prog_36(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.3847 * x[0] + 0.5944 * x[1] * sympy.sin(x[0]) - 0.1396 * x[1] * sympy.sin(x[2]) - 0.0314 * x[2] * sympy.sin(
            x[3]) + 0.6838 * x[2] + 0.428 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.6278 * sympy.sin(x[0]) * sympy.cos(
            x[2]) + 0.5609 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.3807 * sympy.sin(x[1]) + 0.0081 * sympy.cos(x[3]) + 0.1114


@register_eq_class
class sincos_nv4_nt46_prog_44(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4925 * x[0] + 0.376 * x[1] * sympy.sin(x[0]) - 0.4555 * x[1] + 0.1944 * x[2] * sympy.cos(x[0]) + 0.0745 * x[
            2] * sympy.cos(x[1]) + 0.617 * x[2] + 0.5112 * x[3] * sympy.sin(x[1]) - 0.1236 * x[3] * sympy.cos(x[0]) - 0.8824 * sympy.sin(
            x[3]) * sympy.cos(x[2]) + 0.5164 * sympy.sin(x[3]) - 0.9741


@register_eq_class
class sincos_nv4_nt46_prog_6(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.6762 * x[0] * x[1] - 0.4155 * x[0] * sympy.sin(x[3]) + 0.3426 * x[1] * x[3] - 0.4999 * x[1] - 0.7566 * x[2] * x[
            3] + 0.666 * x[2] * sympy.sin(x[1]) - 0.7283 * x[2] + 0.5425 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.3538 * sympy.cos(
            x[0]) - 0.1851 * sympy.cos(x[3]) + 0.8117


@register_eq_class
class sincos_nv4_nt46_prog_18(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0241 * x[0] * x[1] + 0.4375 * x[0] * sympy.sin(x[3]) + 0.6853 * x[0] - 0.7489 * x[1] * sympy.sin(x[2]) - 0.8292 * \
                        x[1] - 0.9523 * x[2] * sympy.sin(x[3]) - 0.4335 * x[2] + 0.259 * x[3] * sympy.cos(x[1]) - 0.6301 * sympy.sin(
            x[0]) * sympy.cos(x[2]) + 0.4852 * sympy.cos(x[3]) + 0.5475


@register_eq_class
class sincos_nv4_nt46_prog_3(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.802 * x[0] * x[1] - 0.4736 * x[0] * x[2] + 0.8366 * x[0] * sympy.sin(x[3]) - 0.7204 * x[1] * sympy.cos(
            x[2]) + 0.5086 * x[2] * x[3] - 0.9419 * x[2] - 0.8707 * x[3] * sympy.cos(x[1]) + 0.5934 * sympy.sin(x[0]) - 0.1084 * sympy.sin(
            x[1]) + 0.6729 * sympy.sin(x[3]) + 0.0363


@register_eq_class
class sincos_nv4_nt46_prog_24(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7327 * x[0] * sympy.cos(x[1]) - 0.6692 * x[0] * sympy.cos(x[3]) - 0.8672 * x[0] - 0.9392 * x[2] * x[3] + 0.4865 * \
                        x[3] * sympy.sin(x[1]) + 0.4107 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.3971 * sympy.sin(x[1]) + 0.4494 * sympy.sin(
            x[2]) - 0.8175 * sympy.sin(x[3]) - 0.2144 * sympy.cos(x[1]) * sympy.cos(x[2]) - 0.1497


@register_eq_class
class sincos_nv4_nt46_prog_12(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0865 * x[0] * sympy.cos(x[2]) - 0.6456 * x[0] + 0.2842 * x[1] * sympy.sin(x[0]) + 0.7805 * x[2] - 0.9161 * x[
            3] * sympy.sin(x[1]) - 0.1108 * x[3] * sympy.sin(x[2]) - 0.5201 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.8397 * sympy.sin(
            x[1]) + 0.1382 * sympy.sin(x[3]) - 0.7996 * sympy.cos(x[1]) * sympy.cos(x[2]) - 0.3242


@register_eq_class
class sincos_nv4_nt46_prog_25(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7807 * x[0] * x[2] + 0.9254 * x[0] * x[3] + 0.9291 * x[0] * sympy.cos(x[1]) - 0.2045 * x[1] * x[2] + 0.5514 * x[
            1] * sympy.cos(x[3]) + 0.6492 * x[2] * x[3] + 0.1498 * sympy.sin(x[3]) + 0.6212 * sympy.cos(x[0]) + 0.3085 * sympy.cos(
            x[1]) + 0.0643 * sympy.cos(x[2]) + 0.7977


@register_eq_class
class sincos_nv4_nt46_prog_21(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2185 * x[0] * x[3] - 0.3275 * x[0] * sympy.sin(x[2]) - 0.3372 * x[0] - 0.69 * x[1] * sympy.sin(x[2]) + 0.1955 * \
                        x[1] + 0.3894 * x[3] * sympy.cos(x[1]) + 0.4341 * sympy.sin(x[2]) * sympy.sin(x[3]) + 0.8714 * sympy.sin(
            x[2]) - 0.3681 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.9319 * sympy.cos(x[3]) - 0.53


@register_eq_class
class sincos_nv4_nt46_prog_26(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.1525 * x[0] * x[3] + 0.2344 * x[0] * sympy.sin(x[2]) - 0.7654 * x[0] - 0.4518 * x[1] * x[2] - 0.7139 * x[1] * x[
            3] + 0.6036 * x[1] * sympy.sin(x[0]) - 0.373 * x[2] * x[3] - 0.6555 * x[2] + 0.0959 * sympy.sin(x[3]) + 0.276 * sympy.cos(
            x[1]) - 0.2666


@register_eq_class
class sincos_nv4_nt46_prog_39(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2829 * x[0] * sympy.sin(x[3]) + 0.2362 * x[1] * x[3] + 0.7106 * x[2] + 0.4593 * x[3] + 0.3379 * sympy.sin(
            x[1]) * sympy.cos(x[2]) - 0.997 * sympy.sin(x[1]) + 0.6589 * sympy.sin(x[2]) * sympy.cos(x[0]) - 0.7553 * sympy.cos(
            x[0]) * sympy.cos(x[1]) - 0.2695 * sympy.cos(x[0]) + 0.5946 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.6278


@register_eq_class
class sincos_nv4_nt46_prog_19(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7403 * x[0] * sympy.sin(x[1]) + 0.6895 * x[0] * sympy.cos(x[2]) + 0.225 * x[0] * sympy.cos(x[3]) - 0.5721 * x[
            0] - 0.4302 * x[1] * sympy.sin(x[2]) + 0.6373 * x[1] + 0.0259 * x[3] * sympy.sin(x[1]) - 0.4983 * x[3] * sympy.cos(
            x[2]) + 0.3258 * sympy.sin(x[2]) + 0.142 * sympy.cos(x[3]) - 0.5005


@register_eq_class
class sincos_nv4_nt46_prog_38(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5752 * x[0] * sympy.sin(x[1]) - 0.8646 * x[0] * sympy.cos(x[3]) - 0.3895 * x[0] - 0.6201 * x[1] * x[2] + 0.087 * \
                        x[1] * sympy.sin(x[3]) + 0.7914 * x[1] + 0.0854 * x[2] * sympy.cos(x[0]) + 0.8686 * x[3] + 0.5512 * sympy.sin(
            x[2]) * sympy.cos(x[3]) + 0.2514 * sympy.sin(x[2]) - 0.5091


@register_eq_class
class sincos_nv4_nt46_prog_9(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.1888 * x[0] * sympy.sin(x[2]) - 0.7688 * x[0] - 0.1821 * x[1] * x[3] + 0.7518 * x[1] * sympy.cos(x[0]) - 0.7683 * \
                        x[1] * sympy.cos(x[2]) - 0.3029 * x[1] + 0.5322 * x[2] * x[3] - 0.5291 * sympy.sin(x[0]) * sympy.cos(
            x[3]) - 0.3467 * sympy.sin(x[2]) + 0.9045 * sympy.sin(x[3]) - 0.8584


@register_eq_class
class sincos_nv4_nt46_prog_32(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0584 * x[0] * sympy.cos(x[2]) + 0.6582 * x[1] * x[3] + 0.7758 * x[1] * sympy.cos(x[0]) - 0.3515 * x[2] - 0.9395 * \
                        x[3] * sympy.sin(x[0]) - 0.4808 * x[3] * sympy.sin(x[2]) - 0.3188 * sympy.sin(x[1]) - 0.1994 * sympy.sin(
            x[2]) * sympy.cos(x[1]) + 0.2631 * sympy.cos(x[0]) + 0.1292 * sympy.cos(x[3]) - 0.1605


@register_eq_class
class sincos_nv4_nt46_prog_5(KnownEquation):
    _eq_name = 'sincos_nv4_nt46_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.1068 * x[0] * sympy.cos(x[1]) - 0.9693 * x[0] * sympy.cos(x[2]) + 0.7863 * x[1] * x[3] - 0.8555 * x[1] - 0.2549 * \
                        x[3] * sympy.sin(x[0]) + 0.3453 * sympy.sin(x[0]) + 0.2202 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.7538 * sympy.sin(
            x[2]) * sympy.cos(x[3]) + 0.2688 * sympy.sin(x[3]) - 0.6707 * sympy.cos(x[2]) + 0.1723


@register_eq_class
class sincos_nv2_nt11_prog_46(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.6861 * x[0] * sympy.cos(x[1]) - 0.9009 * x[1] + 0.9326


@register_eq_class
class sincos_nv2_nt11_prog_0(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.167 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.4467 * sympy.cos(x[0]) - 0.2736


@register_eq_class
class sincos_nv2_nt11_prog_35(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.6617 * x[1] * sympy.sin(x[0]) - 0.5454 * sympy.cos(x[0]) + 0.3147


@register_eq_class
class sincos_nv2_nt11_prog_8(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2582 * x[0] - 0.8355 * x[1] * sympy.cos(x[0]) - 0.5898


@register_eq_class
class sincos_nv2_nt11_prog_42(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7172 * x[0] * x[1] - 0.4351 * sympy.cos(x[0]) - 0.9745


@register_eq_class
class sincos_nv2_nt11_prog_33(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7168 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.2941 * sympy.sin(x[1]) + 0.6853


@register_eq_class
class sincos_nv2_nt11_prog_20(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.3038 * x[0] * sympy.sin(x[1]) - 0.6958 * x[0] + 0.5854


@register_eq_class
class sincos_nv2_nt11_prog_14(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7192 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.4738 * sympy.sin(x[1]) + 0.4297


@register_eq_class
class sincos_nv2_nt11_prog_31(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0091 * x[1] - 0.7699 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.0289


@register_eq_class
class sincos_nv2_nt11_prog_48(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2057 * x[1] * sympy.cos(x[0]) + 0.1897 * sympy.cos(x[1]) - 0.9226


@register_eq_class
class sincos_nv2_nt11_prog_41(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.9992 * x[0] * x[1] + 0.48 * sympy.sin(x[0]) + 0.1838


@register_eq_class
class sincos_nv2_nt11_prog_7(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2729 * x[0] * sympy.sin(x[1]) - 0.7014 * x[1] + 0.3248


@register_eq_class
class sincos_nv2_nt11_prog_37(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6497 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.85 * sympy.sin(x[1]) - 0.8125


@register_eq_class
class sincos_nv2_nt11_prog_15(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8262 * x[1] - 0.771 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.0562


@register_eq_class
class sincos_nv2_nt11_prog_23(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0962 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.279 * sympy.cos(x[1]) - 0.8582


@register_eq_class
class sincos_nv2_nt11_prog_30(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.4484 * x[0] * x[1] - 0.0989 * x[0] + 0.4505


@register_eq_class
class sincos_nv2_nt11_prog_28(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4798 * x[0] - 0.9697 * x[1] * sympy.sin(x[0]) - 0.3438


@register_eq_class
class sincos_nv2_nt11_prog_17(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.0779 * x[0] * x[1] - 0.6363 * x[0] - 0.5798


@register_eq_class
class sincos_nv2_nt11_prog_43(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.199 * x[0] * x[1] + 0.0581 * x[0] + 0.7273


@register_eq_class
class sincos_nv2_nt11_prog_2(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5784 * x[0] * x[1] + 0.556 * sympy.cos(x[1]) + 0.8266


@register_eq_class
class sincos_nv2_nt11_prog_4(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7262 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.006 * sympy.cos(x[1]) - 0.9218


@register_eq_class
class sincos_nv2_nt11_prog_45(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7689 * x[1] * sympy.sin(x[0]) - 0.1672 * sympy.sin(x[0]) - 0.1377


@register_eq_class
class sincos_nv2_nt11_prog_49(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8416 * x[0] * sympy.cos(x[1]) - 0.2762 * x[0] - 0.1864


@register_eq_class
class sincos_nv2_nt11_prog_11(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.9301 * x[0] * x[1] + 0.2202 * sympy.sin(x[0]) + 0.1094


@register_eq_class
class sincos_nv2_nt11_prog_10(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4451 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.6191 * sympy.cos(x[0]) - 0.0206


@register_eq_class
class sincos_nv2_nt11_prog_1(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6738 * x[0] - 0.5057 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.8987


@register_eq_class
class sincos_nv2_nt11_prog_40(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2243 * x[0] * sympy.sin(x[1]) + 0.601 * x[0] + 0.2198


@register_eq_class
class sincos_nv2_nt11_prog_29(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2216 * x[1] + 0.4868 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.7838


@register_eq_class
class sincos_nv2_nt11_prog_22(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1787 * x[0] * sympy.sin(x[1]) - 0.1813 * sympy.cos(x[0]) + 0.2354


@register_eq_class
class sincos_nv2_nt11_prog_27(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.3918 * sympy.cos(x[0]) * sympy.cos(x[1]) - 0.8759 * sympy.cos(x[1]) - 0.7446


@register_eq_class
class sincos_nv2_nt11_prog_34(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7664 * x[1] * sympy.sin(x[0]) - 0.7766 * sympy.cos(x[1]) + 0.0878


@register_eq_class
class sincos_nv2_nt11_prog_16(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.4292 * x[0] - 0.1864 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.044


@register_eq_class
class sincos_nv2_nt11_prog_13(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1768 * x[0] * sympy.sin(x[1]) + 0.7683 * x[0] + 0.7735


@register_eq_class
class sincos_nv2_nt11_prog_47(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2203 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.9112 * sympy.sin(x[1]) + 0.0243


@register_eq_class
class sincos_nv2_nt11_prog_36(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.9158 * x[0] * sympy.cos(x[1]) + 0.8628 * x[0] + 0.7752


@register_eq_class
class sincos_nv2_nt11_prog_44(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7334 * x[0] - 0.7289 * x[1] * sympy.sin(x[0]) + 0.8156


@register_eq_class
class sincos_nv2_nt11_prog_6(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2589 * x[0] * sympy.sin(x[1]) + 0.1977 * x[1] - 0.7504


@register_eq_class
class sincos_nv2_nt11_prog_18(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7026 * x[1] * sympy.sin(x[0]) + 0.5341 * x[1] + 0.8865


@register_eq_class
class sincos_nv2_nt11_prog_3(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0882 * x[0] - 0.7944 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.4847


@register_eq_class
class sincos_nv2_nt11_prog_24(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.3598 * x[1] * sympy.sin(x[0]) + 0.2365 * sympy.sin(x[1]) + 0.9575


@register_eq_class
class sincos_nv2_nt11_prog_12(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1161 * x[1] * sympy.cos(x[0]) - 0.9691 * sympy.cos(x[1]) - 0.1219


@register_eq_class
class sincos_nv2_nt11_prog_25(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2127 * x[0] + 0.4622 * x[1] * sympy.cos(x[0]) - 0.038


@register_eq_class
class sincos_nv2_nt11_prog_21(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1356 * x[1] * sympy.sin(x[0]) + 0.5691 * sympy.cos(x[1]) - 0.6327


@register_eq_class
class sincos_nv2_nt11_prog_26(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8712 * x[0] * sympy.cos(x[1]) + 0.1404 * sympy.sin(x[1]) + 0.6436


@register_eq_class
class sincos_nv2_nt11_prog_39(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2555 * x[0] - 0.1723 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.8334


@register_eq_class
class sincos_nv2_nt11_prog_19(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2987 * x[1] * sympy.sin(x[0]) + 0.7408 * sympy.cos(x[0]) + 0.4255


@register_eq_class
class sincos_nv2_nt11_prog_38(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8468 * x[1] + 0.5529 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.8165


@register_eq_class
class sincos_nv2_nt11_prog_9(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1052 * x[0] * x[1] + 0.0321 * x[0] - 0.9554


@register_eq_class
class sincos_nv2_nt11_prog_32(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8877 * x[0] * x[1] - 0.7408 * sympy.sin(x[0]) + 0.9163


@register_eq_class
class sincos_nv2_nt11_prog_5(KnownEquation):
    _eq_name = 'sincos_nv2_nt11_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.189 * x[0] * x[1] - 0.7125 * sympy.cos(x[1]) - 0.4207


@register_eq_class
class inv_nv3_nt22_prog_46(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6835 * x[0] / x[2] - 0.8249 - 0.2795 / x[2] + 0.3408 / (x[1] * x[2]) - 0.4295 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_0(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3064 * x[0] * x[2] - 0.1319 * x[0] + 0.6931 + 0.2953 / x[2] + 0.4379 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_35(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.859 * x[0] * x[2] - 0.0803 * x[0] / x[1] + 0.1178 * x[2] - 0.4891 + 0.583 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_8(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.9486 * x[0] - 0.0266 * x[0] / x[2] - 0.8253 * x[1] / x[2] - 0.1552 - 0.7192 / x[2]


@register_eq_class
class inv_nv3_nt22_prog_42(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.282 * x[0] + 0.1316 * x[1] - 0.7211 - 0.8474 / (x[1] * x[2]) - 0.2475 / (x[0] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_33(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.743 * x[1] - 0.2953 * x[1] / x[2] + 0.3435 - 0.5139 * x[1] / x[0] - 0.2981 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_20(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.8841 * x[0] * x[2] + 0.1334 * x[0] - 0.4856 * x[1] / x[2] - 0.0704 - 0.4559 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_14(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9834 * x[2] + 0.2095 + 0.6504 / (x[1] * x[2]) - 0.1075 * x[2] / x[0] - 0.9149 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_31(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8939 * x[1] * x[2] - 0.1892 * x[2] - 0.6728 + 0.3244 / x[0] - 0.0532 / (x[0] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_48(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.5293 * x[0] * x[2] + 0.1485 * x[0] - 0.2927 * x[1] * x[2] + 0.947 * x[1] + 0.7971


@register_eq_class
class inv_nv3_nt22_prog_41(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9897 * x[1] - 0.3365 * x[2] + 0.5377 + 0.7746 * x[2] / x[1] + 0.5029 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_7(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.0543 * x[0] * x[2] - 0.3312 * x[1] * x[2] + 0.369 * x[2] + 0.5777 - 0.0617 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_37(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3186 * x[0] * x[2] - 0.3933 * x[1] - 0.4753 - 0.8722 * x[1] / x[0] + 0.6246 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_15(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.438 * x[0] / x[1] + 0.8362 * x[2] + 0.7127 - 0.7646 * x[2] / x[1] + 0.8286 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_23(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9218 * x[0] * x[2] - 0.8093 * x[0] + 0.7478 * x[0] / x[1] - 0.1967 + 0.8354 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_30(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7596 * x[0] / x[2] - 0.6823 * x[1] + 0.1344 * x[2] - 0.3541 - 0.1697 * x[1] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_28(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6441 * x[1] / x[2] + 0.8259 - 0.0967 / x[2] + 0.4422 / x[1] - 0.2797 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_17(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2848 * x[0] * x[1] - 0.1324 * x[0] * x[2] + 0.0917 + 0.0735 / x[1] - 0.9276 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_43(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.0558 * x[0] * x[1] - 0.2339 * x[1] - 0.3034 * x[2] + 0.9586 + 0.7804 * x[2] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_2(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6029 * x[0] * x[1] + 0.7441 * x[0] + 0.0896 * x[1] / x[2] + 0.5615 + 0.5824 / x[2]


@register_eq_class
class inv_nv3_nt22_prog_4(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7979 * x[0] - 0.7806 + 0.4221 / x[1] + 0.3047 * x[1] / x[0] + 0.8485 / (x[0] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_45(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6654 * x[0] - 0.2075 * x[0] / x[2] - 0.3417 * x[0] / x[1] - 0.6721 * x[1] - 0.8421


@register_eq_class
class inv_nv3_nt22_prog_49(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7736 - 0.2989 / x[2] - 0.5779 / x[1] + 0.8131 / (x[1] * x[2]) + 0.2121 / (x[0] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_11(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.5894 * x[0] / x[2] + 0.2059 * x[1] - 0.6702 + 0.5887 / x[2] + 0.4879 * x[1] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_10(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3083 * x[0] * x[2] + 0.4141 + 0.1026 / x[2] - 0.7613 / x[0] + 0.6452 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_1(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6806 * x[0] - 0.7544 + 0.4417 * x[2] / x[1] - 0.1192 / x[1] - 0.7571 * x[2] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_40(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6825 * x[0] * x[2] - 0.783 * x[1] + 0.8902 * x[2] - 0.502 - 0.5852 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_29(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3641 - 0.811 / x[2] + 0.0387 * x[1] / x[0] + 0.3516 * x[2] / x[0] - 0.8175 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_22(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.9043 * x[1] - 0.0183 * x[2] + 0.1298 - 0.2956 * x[2] / x[1] - 0.9962 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_27(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.8 * x[1] * x[2] - 0.8106 * x[2] - 0.3854 - 0.8808 / x[1] + 0.2901 * x[2] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_34(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.9826 * x[0] / x[1] + 0.5364 * x[2] - 0.9811 - 0.8706 / x[0] + 0.7362 / (x[0] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_16(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8493 * x[0] / x[2] - 0.9254 * x[0] / x[1] + 0.2253 * x[2] - 0.8547 - 0.4495 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_13(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7233 * x[0] / x[2] + 0.1152 * x[1] - 0.4443 * x[2] + 0.7534 - 0.8898 * x[1] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_47(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.4962 * x[0] / x[2] - 0.0774 * x[1] + 0.7968 * x[1] / x[2] - 0.0238 + 0.7302 / x[2]


@register_eq_class
class inv_nv3_nt22_prog_36(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5333 * x[1] * x[2] + 0.5921 + 0.2216 / x[1] - 0.7662 * x[1] / x[0] - 0.4007 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_44(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8668 * x[0] * x[1] + 0.5314 * x[0] - 0.6473 - 0.9226 / x[1] + 0.5312 / (x[1] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_6(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6466 * x[0] / x[2] + 0.4946 + 0.7769 / x[1] + 0.5762 / (x[1] * x[2]) - 0.9955 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_18(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.5171 * x[0] + 0.5886 + 0.8002 / x[2] - 0.0745 / (x[1] * x[2]) - 0.0386 * x[1] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_3(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.8056 * x[0] - 0.4094 * x[1] / x[2] - 0.712 * x[2] - 0.3431 + 0.8616 / (x[0] * x[2])


@register_eq_class
class inv_nv3_nt22_prog_24(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0431 * x[0] / x[2] + 0.6119 + 0.8897 * x[2] / x[1] - 0.0809 / x[1] + 0.4351 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_12(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.506 * x[1] / x[2] - 0.8501 * x[2] - 0.228 - 0.3616 / x[1] + 0.6511 * x[1] / x[0]


@register_eq_class
class inv_nv3_nt22_prog_25(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8824 * x[0] * x[2] - 0.9724 * x[1] / x[2] - 0.8402 * x[2] + 0.2921 - 0.7005 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_21(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.3135 * x[0] * x[2] - 0.0162 * x[1] * x[2] - 0.8459 * x[1] + 0.1277 * x[2] - 0.2484


@register_eq_class
class inv_nv3_nt22_prog_26(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9959 * x[0] / x[1] + 0.6208 * x[1] / x[2] + 0.1435 * x[2] + 0.0405 + 0.8677 / x[1]


@register_eq_class
class inv_nv3_nt22_prog_39(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2322 * x[1] / x[2] + 0.0259 - 0.5619 / x[1] - 0.8577 / x[0] + 0.2556 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_19(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6045 * x[0] / x[2] - 0.134 * x[2] + 0.9389 - 0.7838 / (x[1] * x[2]) + 0.7349 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_38(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.3575 * x[1] - 0.2552 * x[1] / x[2] + 0.0809 - 0.7927 / x[0] + 0.7492 / (x[0] * x[1])


@register_eq_class
class inv_nv3_nt22_prog_9(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5903 * x[1] + 0.2167 * x[1] / x[2] + 0.0677 - 0.5233 * x[2] / x[0] + 0.8166 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_32(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9404 + 0.8221 / x[2] - 0.3882 / (x[1] * x[2]) + 0.8037 * x[1] / x[0] - 0.4332 / x[0]


@register_eq_class
class inv_nv3_nt22_prog_5(KnownEquation):
    _eq_name = 'inv_nv3_nt22_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2431 * x[0] * x[2] - 0.8808 * x[1] + 0.446 - 0.4419 / x[2] + 0.9671 / (x[0] * x[1])


@register_eq_class
class sincos_nv5_nt58_prog_46(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.921 * x[0] * x[2] + 0.3497 * x[0] * sympy.cos(x[4]) - 0.692 * x[1] * sympy.sin(x[0]) + 0.4334 * x[1] * sympy.cos(
            x[4]) - 0.2913 * x[2] * x[4] - 0.4576 * x[2] * sympy.sin(x[3]) - 0.868 * x[2] * sympy.cos(x[1]) + 0.556 * x[3] * x[4] + 0.4329 * \
                        x[3] + 0.8562 * x[4] - 0.9737 * sympy.sin(x[1]) + 0.7046 * sympy.sin(x[2]) - 0.7945 * sympy.cos(x[0]) + 0.6126


@register_eq_class
class sincos_nv5_nt58_prog_0(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7818 * x[0] * sympy.cos(x[2]) - 0.3407 * x[0] * sympy.cos(x[4]) + 0.9826 * x[0] + 0.968 * x[1] * x[4] + 0.3082 * \
                        x[1] * sympy.cos(x[2]) + 0.7949 * x[2] * x[3] - 0.886 * x[3] * sympy.sin(x[4]) - 0.6356 * x[3] - 0.169 * sympy.sin(
            x[1]) * sympy.cos(x[0]) + 0.6341 * sympy.sin(x[4]) + 0.8655 * sympy.cos(x[1]) - 0.9134 * sympy.cos(x[2]) * sympy.cos(
            x[4]) + 0.432 * sympy.cos(x[2]) - 0.2752


@register_eq_class
class sincos_nv5_nt58_prog_35(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8564 * x[0] * x[1] - 0.3514 * x[0] * x[2] + 0.2654 * x[0] * sympy.cos(x[4]) - 0.3275 * x[1] * sympy.sin(
            x[2]) + 0.6365 * x[1] * sympy.sin(x[3]) - 0.7343 * x[1] - 0.93 * x[2] * x[3] + 0.4006 * x[2] * x[4] + 0.3452 * x[3] * x[
                            4] + 0.982 * x[3] + 0.5857 * x[4] - 0.9635 * sympy.sin(x[2]) + 0.689 * sympy.cos(x[0]) - 0.9533


@register_eq_class
class sincos_nv5_nt58_prog_8(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.7856 * x[0] * sympy.cos(x[1]) + 0.4893 * x[0] - 0.1343 * x[1] + 0.7619 * x[2] * sympy.sin(x[4]) + 0.0341 * x[
            2] * sympy.cos(x[0]) + 0.791 * x[2] * sympy.cos(x[1]) - 0.263 * x[3] * x[4] + 0.5905 * x[3] * sympy.sin(x[1]) + 0.599 * x[
                            3] * sympy.sin(x[2]) + 0.4539 * sympy.sin(x[2]) + 0.9614 * sympy.sin(x[3]) + 0.1748 * sympy.sin(
            x[4]) + 0.5398 * sympy.cos(x[1]) * sympy.cos(x[4]) + 0.7705


@register_eq_class
class sincos_nv5_nt58_prog_42(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4312 * x[0] * x[1] + 0.3709 * x[0] * x[4] + 0.122 * x[0] * sympy.sin(x[3]) - 0.7478 * x[1] - 0.5616 * x[2] * x[
            3] - 0.1048 * x[2] + 0.1124 * x[3] + 0.3823 * x[4] * sympy.cos(x[1]) + 0.6066 * sympy.sin(x[2]) * sympy.sin(
            x[4]) + 0.4726 * sympy.sin(x[4]) - 0.4129 * sympy.cos(x[0]) * sympy.cos(x[2]) - 0.133 * sympy.cos(x[0]) - 0.6444 * sympy.cos(
            x[1]) * sympy.cos(x[3]) + 0.4777


@register_eq_class
class sincos_nv5_nt58_prog_33(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6484 * x[0] * x[2] - 0.6261 * x[0] * x[4] + 0.6699 * x[2] * sympy.sin(x[1]) + 0.4221 * x[3] * sympy.sin(
            x[0]) + 0.269 * x[3] * sympy.cos(x[2]) + 0.5191 * x[4] - 0.1075 * sympy.sin(x[0]) - 0.878 * sympy.sin(x[1]) * sympy.sin(
            x[3]) - 0.5135 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.8781 * sympy.sin(x[1]) * sympy.cos(x[4]) + 0.6763 * sympy.sin(
            x[2]) + 0.9345 * sympy.cos(x[1]) - 0.6509 * sympy.cos(x[3]) + 0.1562


@register_eq_class
class sincos_nv5_nt58_prog_20(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4405 * x[0] * x[2] - 0.0695 * x[0] * x[3] - 0.618 * x[1] * sympy.cos(x[0]) + 0.5535 * x[1] - 0.0171 * x[2] * x[
            4] + 0.2031 * x[2] + 0.4286 * x[3] + 0.2242 * x[4] + 0.832 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.8167 * sympy.sin(
            x[1]) * sympy.sin(x[4]) + 0.2788 * sympy.sin(x[2]) * sympy.sin(x[3]) + 0.263 * sympy.cos(x[0]) * sympy.cos(
            x[4]) + 0.7329 * sympy.cos(x[0]) + 0.833


@register_eq_class
class sincos_nv5_nt58_prog_14(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8865 * x[0] * sympy.cos(x[2]) + 0.3965 * x[0] + 0.231 * x[1] * x[2] + 0.7152 * x[3] * sympy.sin(x[0]) + 0.6119 * \
                        x[3] * sympy.sin(x[2]) + 0.9405 * x[3] * sympy.cos(x[1]) + 0.675 * x[3] + 0.4481 * sympy.sin(x[0]) * sympy.sin(
            x[4]) - 0.6164 * sympy.sin(x[1]) - 0.5573 * sympy.sin(x[2]) + 0.2261 * sympy.sin(x[4]) * sympy.cos(x[3]) - 0.7528 * sympy.cos(
            x[0]) * sympy.cos(x[1]) + 0.4088 * sympy.cos(x[4]) + 0.8027


@register_eq_class
class sincos_nv5_nt58_prog_31(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6162 * x[0] * x[3] + 0.9774 * x[0] + 0.4996 * x[1] * x[4] - 0.0137 * x[1] * sympy.cos(x[0]) + 0.6672 * x[
            1] - 0.5068 * x[3] * sympy.cos(x[1]) + 0.8065 * x[4] + 0.7652 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.4658 * sympy.sin(
            x[3]) * sympy.cos(x[2]) - 0.2585 * sympy.sin(x[3]) + 0.8501 * sympy.sin(x[4]) * sympy.cos(x[0]) - 0.5218 * sympy.sin(
            x[4]) * sympy.cos(x[2]) - 0.7121 * sympy.cos(x[2]) - 0.429


@register_eq_class
class sincos_nv5_nt58_prog_48(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6826 * x[0] * x[3] + 0.6697 * x[0] * x[4] + 0.7697 * x[0] - 0.8593 * x[1] * sympy.sin(x[2]) - 0.4168 * x[
            1] * sympy.cos(x[3]) + 0.335 * x[1] + 0.4295 * x[2] * x[3] + 0.6004 * x[2] * sympy.sin(x[0]) + 0.0336 * x[2] * sympy.sin(
            x[4]) + 0.0025 * x[3] - 0.5294 * sympy.sin(x[2]) - 0.5119 * sympy.sin(x[3]) * sympy.cos(x[4]) + 0.457 * sympy.cos(x[4]) - 0.0401


@register_eq_class
class sincos_nv5_nt58_prog_41(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8062 * x[0] * sympy.sin(x[2]) + 0.2817 * x[0] * sympy.cos(x[1]) + 0.0041 * x[0] + 0.1823 * x[1] + 0.572 * x[
            3] * sympy.sin(x[1]) - 0.6333 * x[4] * sympy.sin(x[0]) - 0.9241 * x[4] + 0.8137 * sympy.sin(x[0]) * sympy.cos(
            x[3]) - 0.4745 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.9566 * sympy.sin(x[3]) * sympy.cos(x[2]) - 0.0317 * sympy.sin(
            x[3]) + 0.4178 * sympy.sin(x[4]) * sympy.cos(x[3]) - 0.3241 * sympy.cos(x[2]) + 0.5573


@register_eq_class
class sincos_nv5_nt58_prog_7(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6118 * x[0] * x[2] + 0.3324 * x[0] * sympy.sin(x[3]) + 0.7482 * x[0] + 0.7389 * x[1] - 0.6703 * x[2] * x[
            4] + 0.9995 * x[3] * sympy.sin(x[4]) + 0.8962 * x[4] * sympy.cos(x[0]) + 0.8399 * x[4] * sympy.cos(x[1]) - 0.4683 * sympy.sin(
            x[3]) * sympy.cos(x[2]) + 0.8268 * sympy.sin(x[4]) - 0.831 * sympy.cos(x[1]) * sympy.cos(x[3]) + 0.8481 * sympy.cos(
            x[2]) + 0.8386 * sympy.cos(x[3]) + 0.8101


@register_eq_class
class sincos_nv5_nt58_prog_37(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0112 * x[0] * x[2] + 0.9063 * x[1] * sympy.sin(x[3]) + 0.5053 * x[1] + 0.7062 * x[2] * sympy.cos(x[1]) + 0.4403 * \
                        x[3] * sympy.cos(x[2]) - 0.753 * x[4] * sympy.sin(x[1]) + 0.175 * x[4] + 0.7139 * sympy.sin(x[0]) * sympy.sin(
            x[4]) + 0.2383 * sympy.sin(x[0]) * sympy.cos(x[3]) - 0.7864 * sympy.sin(x[2]) + 0.3444 * sympy.sin(x[3]) + 0.2725 * sympy.sin(
            x[4]) * sympy.cos(x[2]) - 0.3317 * sympy.cos(x[0]) + 0.278


@register_eq_class
class sincos_nv5_nt58_prog_15(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3678 * x[0] * sympy.sin(x[1]) - 0.6694 * x[0] - 0.0898 * x[1] * x[2] + 0.2492 * x[1] * sympy.cos(x[4]) - 0.4717 * \
                        x[2] * x[3] + 0.2889 * x[3] * sympy.sin(x[0]) - 0.6867 * x[3] * sympy.cos(x[1]) + 0.0928 * sympy.sin(
            x[0]) * sympy.sin(x[4]) - 0.4304 * sympy.sin(x[1]) + 0.8037 * sympy.sin(x[2]) * sympy.sin(x[4]) + 0.4672 * sympy.sin(
            x[2]) + 0.0333 * sympy.sin(x[3]) + 0.2085 * sympy.cos(x[4]) + 0.1276


@register_eq_class
class sincos_nv5_nt58_prog_23(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3785 * x[0] * x[2] - 0.9293 * x[0] * sympy.cos(x[4]) - 0.973 * x[0] - 0.9941 * x[3] * sympy.sin(x[2]) - 0.9936 * \
                        x[4] * sympy.sin(x[1]) - 0.6428 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.8189 * sympy.sin(x[1]) * sympy.sin(
            x[3]) - 0.4908 * sympy.sin(x[2]) * sympy.sin(x[4]) - 0.9742 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.8422 * sympy.sin(
            x[4]) - 0.6852 * sympy.cos(x[1]) + 0.4395 * sympy.cos(x[2]) + 0.6119 * sympy.cos(x[3]) - 0.8308


@register_eq_class
class sincos_nv5_nt58_prog_30(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2119 * x[0] * sympy.sin(x[2]) + 0.9866 * x[1] * x[3] - 0.624 * x[1] * x[4] + 0.5357 * x[1] - 0.1051 * x[
            2] * sympy.sin(x[4]) + 0.5117 * x[2] - 0.2257 * x[3] * sympy.cos(x[2]) - 0.6489 * x[4] * sympy.cos(x[3]) + 0.7427 * sympy.sin(
            x[0]) * sympy.sin(x[4]) - 0.9055 * sympy.sin(x[0]) + 0.4497 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.9206 * sympy.sin(
            x[3]) + 0.2276 * sympy.cos(x[4]) + 0.7228


@register_eq_class
class sincos_nv5_nt58_prog_28(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5833 * x[0] + 0.1619 * x[1] * x[2] + 0.9881 * x[1] * x[3] + 0.4494 * x[1] * x[4] - 0.5206 * x[1] + 0.6758 * x[3] * \
                        x[4] - 0.9668 * x[3] * sympy.cos(x[2]) - 0.9275 * x[3] + 0.0246 * x[4] * sympy.cos(x[2]) - 0.8028 * x[
                            4] + 0.6729 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.8641 * sympy.cos(x[0]) * sympy.cos(x[3]) + 0.19 * sympy.cos(
            x[2]) + 0.2605


@register_eq_class
class sincos_nv5_nt58_prog_17(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4827 * x[0] * x[1] - 0.2504 * x[0] * sympy.sin(x[4]) + 0.2045 * x[0] + 0.3185 * x[1] * x[3] + 0.4035 * x[
            1] * sympy.cos(x[4]) + 0.2092 * x[2] * x[3] - 0.2718 * x[2] * sympy.sin(x[1]) - 0.4989 * x[2] + 0.1158 * x[3] - 0.6322 * x[
                            4] * sympy.cos(x[3]) + 0.4071 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.3944 * sympy.sin(
            x[1]) + 0.2589 * sympy.cos(x[4]) + 0.0996


@register_eq_class
class sincos_nv5_nt58_prog_43(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6649 * x[0] * x[1] - 0.6766 * x[0] * x[2] - 0.8149 * x[1] * x[3] - 0.0307 * x[1] + 0.8612 * x[2] * sympy.cos(
            x[1]) - 0.0984 * x[3] * sympy.sin(x[4]) + 0.5429 * x[3] + 0.9147 * x[4] * sympy.sin(x[2]) + 0.2717 * x[4] * sympy.cos(
            x[0]) + 0.3789 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.6174 * sympy.sin(x[4]) + 0.4293 * sympy.cos(x[0]) + 0.6482 * sympy.cos(
            x[2]) - 0.5891


@register_eq_class
class sincos_nv5_nt58_prog_2(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1199 * x[0] * x[3] - 0.099 * x[0] * sympy.cos(x[4]) - 0.8 * x[1] * x[3] - 0.8756 * x[2] * x[3] + 0.6754 * x[
            2] + 0.3486 * x[3] - 0.2666 * x[4] * sympy.cos(x[1]) - 0.1829 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.6502 * sympy.sin(
            x[2]) * sympy.cos(x[1]) - 0.0993 * sympy.sin(x[3]) * sympy.sin(x[4]) - 0.0739 * sympy.cos(x[0]) - 0.014 * sympy.cos(
            x[1]) + 0.5388 * sympy.cos(x[4]) + 0.4422


@register_eq_class
class sincos_nv5_nt58_prog_4(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.435 * x[0] * x[1] + 0.7562 * x[0] - 0.8417 * x[1] * sympy.sin(x[4]) + 0.9661 * x[1] * sympy.cos(x[3]) - 0.9976 * \
                        x[2] * sympy.cos(x[4]) - 0.0127 * x[3] * sympy.cos(x[2]) - 0.6215 * x[4] * sympy.sin(x[3]) - 0.5449 * x[
                            4] - 0.9233 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.3996 * sympy.sin(x[2]) + 0.5538 * sympy.cos(
            x[1]) * sympy.cos(x[2]) + 0.8465 * sympy.cos(x[1]) + 0.1596 * sympy.cos(x[3]) - 0.1549


@register_eq_class
class sincos_nv5_nt58_prog_45(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2542 * x[0] * x[2] + 0.9037 * x[0] * sympy.sin(x[4]) + 0.7626 * x[0] + 0.7186 * x[2] * x[3] - 0.6788 * x[2] * x[
            4] + 0.973 * x[2] * sympy.sin(x[1]) - 0.5782 * x[2] - 0.6976 * x[3] - 0.4694 * x[4] + 0.9053 * sympy.sin(x[0]) * sympy.cos(
            x[1]) - 0.9228 * sympy.sin(x[1]) * sympy.cos(x[4]) - 0.8667 * sympy.cos(x[1]) * sympy.cos(x[3]) + 0.6646 * sympy.cos(
            x[1]) - 0.2507


@register_eq_class
class sincos_nv5_nt58_prog_49(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1715 * x[0] * x[2] + 0.2134 * x[0] * sympy.sin(x[4]) - 0.411 * x[1] * sympy.sin(x[3]) - 0.3464 * x[1] * sympy.sin(
            x[4]) - 0.1681 * x[1] * sympy.cos(x[2]) - 0.5467 * x[1] - 0.3245 * x[2] * x[3] + 0.8119 * x[2] * sympy.sin(x[4]) + 0.8185 * x[
                            2] - 0.9761 * x[3] - 0.2078 * x[4] + 0.4653 * sympy.sin(x[0]) + 0.1479 * sympy.cos(x[3]) * sympy.cos(
            x[4]) + 0.9071


@register_eq_class
class sincos_nv5_nt58_prog_11(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4381 * x[0] * x[4] - 0.3387 * x[0] * sympy.sin(x[2]) - 0.5883 * x[0] * sympy.sin(x[3]) + 0.071 * x[0] - 0.6085 * \
                        x[1] * sympy.sin(x[0]) - 0.7304 * x[1] + 0.4682 * x[3] * sympy.cos(x[1]) - 0.1922 * x[4] * sympy.sin(
            x[2]) - 0.3048 * sympy.sin(x[1]) * sympy.sin(x[2]) + 0.1836 * sympy.sin(x[3]) - 0.7145 * sympy.sin(x[4]) * sympy.cos(
            x[3]) - 0.9652 * sympy.sin(x[4]) - 0.6186 * sympy.cos(x[2]) + 0.7843


@register_eq_class
class sincos_nv5_nt58_prog_10(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0058 * x[0] * x[3] - 0.6252 * x[0] * sympy.sin(x[1]) - 0.8436 * x[0] * sympy.cos(x[2]) - 0.2158 * x[0] + 0.6422 * \
                        x[1] * sympy.cos(x[4]) - 0.2437 * x[2] * sympy.cos(x[1]) - 0.8599 * x[2] * sympy.cos(x[3]) + 0.9797 * x[
                            2] - 0.6522 * x[3] * sympy.sin(x[4]) - 0.2025 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.1763 * sympy.sin(
            x[4]) - 0.3679 * sympy.cos(x[1]) - 0.8545 * sympy.cos(x[3]) + 0.2429


@register_eq_class
class sincos_nv5_nt58_prog_1(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.707 * x[0] * x[2] + 0.2135 * x[0] * sympy.sin(x[3]) + 0.8683 * x[1] * x[4] - 0.112 * x[1] * sympy.cos(
            x[0]) + 0.6127 * x[2] * x[4] - 0.2153 * x[2] - 0.4737 * x[3] * sympy.cos(x[1]) - 0.7239 * x[3] * sympy.cos(x[4]) - 0.4069 * x[
                            3] + 0.113 * sympy.sin(x[0]) + 0.4836 * sympy.sin(x[1]) - 0.2883 * sympy.cos(x[0]) * sympy.cos(
            x[4]) - 0.3091 * sympy.cos(x[4]) - 0.5313


@register_eq_class
class sincos_nv5_nt58_prog_40(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7896 * x[0] * x[2] - 0.7919 * x[0] * x[3] - 0.8215 * x[1] - 0.3614 * x[2] * x[4] + 0.8729 * x[2] * sympy.sin(
            x[3]) - 0.193 * x[2] - 0.0783 * x[3] + 0.8005 * x[4] * sympy.cos(x[3]) + 0.6785 * x[4] + 0.9248 * sympy.sin(
            x[0]) - 0.7358 * sympy.sin(x[1]) * sympy.sin(x[4]) - 0.9523 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.8272 * sympy.cos(
            x[1]) * sympy.cos(x[2]) + 0.9133


@register_eq_class
class sincos_nv5_nt58_prog_29(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0065 * x[0] * sympy.sin(x[3]) + 0.2782 * x[1] * x[3] - 0.6378 * x[1] * sympy.sin(x[4]) - 0.068 * x[2] * x[
            3] + 0.9744 * x[2] * sympy.cos(x[4]) - 0.318 * x[3] * sympy.cos(x[4]) + 0.1015 * x[3] - 0.2364 * x[4] + 0.9391 * sympy.sin(
            x[0]) * sympy.cos(x[2]) + 0.2893 * sympy.sin(x[1]) - 0.0704 * sympy.sin(x[2]) - 0.0359 * sympy.cos(x[0]) * sympy.cos(
            x[1]) - 0.0562 * sympy.cos(x[0]) - 0.4123


@register_eq_class
class sincos_nv5_nt58_prog_22(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8033 * x[0] * sympy.cos(x[3]) - 0.0031 * x[1] * x[3] + 0.4615 * x[1] * sympy.sin(x[2]) + 0.2623 * x[1] + 0.5418 * \
                        x[2] * sympy.sin(x[4]) + 0.4317 * x[2] - 0.401 * x[3] - 0.8857 * x[4] * sympy.sin(x[1]) + 0.9511 * x[4] * sympy.cos(
            x[0]) - 0.0192 * x[4] - 0.671 * sympy.sin(x[0]) + 0.6605 * sympy.sin(x[3]) * sympy.sin(x[4]) + 0.9965 * sympy.cos(
            x[0]) * sympy.cos(x[2]) - 0.3869


@register_eq_class
class sincos_nv5_nt58_prog_27(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6101 * x[0] * x[2] + 0.4588 * x[0] - 0.2594 * x[1] * sympy.sin(x[2]) - 0.0212 * x[2] - 0.6297 * x[4] * sympy.sin(
            x[1]) + 0.3664 * x[4] * sympy.sin(x[3]) - 0.571 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.8482 * sympy.sin(x[2]) * sympy.cos(
            x[3]) - 0.4379 * sympy.sin(x[3]) - 0.0678 * sympy.sin(x[4]) * sympy.cos(x[2]) - 0.3841 * sympy.sin(x[4]) - 0.5396 * sympy.cos(
            x[0]) * sympy.cos(x[3]) + 0.543 * sympy.cos(x[1]) + 0.7983


@register_eq_class
class sincos_nv5_nt58_prog_34(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8823 * x[0] * x[2] + 0.1543 * x[0] * x[3] + 0.9692 * x[0] - 0.3564 * x[1] * x[3] + 0.4203 * x[1] * sympy.cos(
            x[2]) + 0.1209 * x[1] + 0.4355 * x[3] * sympy.cos(x[4]) - 0.0395 * x[3] - 0.983 * x[4] * sympy.sin(x[1]) - 0.5107 * x[
                            4] * sympy.sin(x[2]) - 0.2448 * x[4] - 0.9344 * sympy.sin(x[2]) + 0.609 * sympy.cos(x[0]) * sympy.cos(
            x[1]) + 0.172


@register_eq_class
class sincos_nv5_nt58_prog_16(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7891 * x[0] * x[1] + 0.521 * x[0] * x[3] + 0.9467 * x[0] * sympy.sin(x[2]) - 0.3876 * x[0] - 0.0475 * x[
            2] * sympy.cos(x[1]) - 0.171 * x[3] * x[4] - 0.6288 * x[3] * sympy.sin(x[2]) + 0.7555 * x[4] * sympy.cos(x[0]) + 0.6825 * x[
                            4] + 0.3508 * sympy.sin(x[3]) + 0.7647 * sympy.cos(x[1]) - 0.8116 * sympy.cos(x[2]) * sympy.cos(
            x[4]) - 0.5278 * sympy.cos(x[2]) - 0.728


@register_eq_class
class sincos_nv5_nt58_prog_13(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1688 * x[0] * sympy.cos(x[4]) - 0.2574 * x[0] + 0.3918 * x[1] * x[3] + 0.979 * x[1] * x[4] + 0.9922 * x[
            1] * sympy.sin(x[0]) + 0.1652 * x[1] - 0.8969 * x[2] * x[4] - 0.8695 * x[2] * sympy.cos(x[0]) + 0.3052 * x[2] * sympy.cos(
            x[3]) - 0.6194 * x[2] + 0.1489 * x[3] * sympy.sin(x[0]) + 0.5714 * x[3] + 0.4112 * sympy.sin(x[4]) - 0.2777


@register_eq_class
class sincos_nv5_nt58_prog_47(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.716 * x[0] * sympy.cos(x[1]) - 0.6128 * x[0] * sympy.cos(x[2]) - 0.7709 * x[0] * sympy.cos(x[3]) - 0.4782 * x[
            1] * sympy.cos(x[4]) - 0.785 * x[2] * x[3] - 0.0877 * x[2] * x[4] + 0.8189 * x[2] * sympy.cos(x[1]) + 0.5173 * x[
                            4] - 0.5168 * sympy.sin(x[0]) - 0.3491 * sympy.sin(x[1]) + 0.0009 * sympy.sin(x[3]) + 0.1538 * sympy.cos(
            x[0]) * sympy.cos(x[4]) + 0.922 * sympy.cos(x[2]) + 0.5147


@register_eq_class
class sincos_nv5_nt58_prog_36(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6986 * x[0] * sympy.sin(x[4]) - 0.1502 * x[0] * sympy.cos(x[1]) + 0.1108 * x[0] + 0.5353 * x[1] * x[2] - 0.9581 * \
                        x[1] * x[3] + 0.7238 * x[1] * sympy.sin(x[4]) + 0.8713 * x[2] * x[4] - 0.6156 * x[3] * sympy.sin(x[2]) - 0.3308 * x[
                            3] + 0.0393 * sympy.sin(x[1]) + 0.8967 * sympy.sin(x[4]) * sympy.cos(x[3]) - 0.8993 * sympy.cos(
            x[2]) - 0.3705 * sympy.cos(x[4]) - 0.6399


@register_eq_class
class sincos_nv5_nt58_prog_44(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9995 * x[0] * sympy.sin(x[2]) + 0.2076 * x[0] * sympy.sin(x[4]) + 0.2558 * x[0] * sympy.cos(x[3]) - 0.5662 * x[
            1] * x[3] + 0.488 * x[2] * sympy.cos(x[3]) - 0.608 * x[2] + 0.0082 * x[4] * sympy.cos(x[3]) - 0.5581 * sympy.sin(
            x[1]) * sympy.cos(x[0]) - 0.1821 * sympy.sin(x[1]) + 0.8734 * sympy.sin(x[3]) - 0.0925 * sympy.cos(x[0]) + 0.2516 * sympy.cos(
            x[1]) * sympy.cos(x[2]) + 0.3617 * sympy.cos(x[4]) - 0.8184


@register_eq_class
class sincos_nv5_nt58_prog_6(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6859 * x[0] - 0.4028 * x[1] + 0.4065 * x[2] * sympy.cos(x[1]) - 0.7974 * x[2] - 0.0553 * x[3] * sympy.cos(
            x[1]) + 0.8272 * x[3] - 0.152 * x[4] * sympy.cos(x[0]) - 0.8805 * x[4] * sympy.cos(x[3]) + 0.1827 * sympy.sin(x[0]) * sympy.sin(
            x[1]) + 0.1205 * sympy.sin(x[2]) * sympy.cos(x[0]) + 0.4764 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.7586 * sympy.cos(
            x[2]) * sympy.cos(x[4]) + 0.7633 * sympy.cos(x[4]) + 0.7716


@register_eq_class
class sincos_nv5_nt58_prog_18(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8689 * x[0] * x[2] - 0.0583 * x[0] * sympy.sin(x[1]) - 0.3433 * x[0] * sympy.sin(x[3]) + 0.1516 * x[1] * x[
            2] - 0.5599 * x[1] * x[3] - 0.8582 * x[2] * sympy.cos(x[4]) + 0.7799 * x[2] + 0.6823 * x[3] * sympy.cos(x[4]) - 0.3032 * x[
                            3] + 0.4985 * x[4] * sympy.sin(x[0]) - 0.8135 * sympy.sin(x[1]) - 0.1021 * sympy.cos(x[0]) + 0.1627 * sympy.cos(
            x[4]) + 0.4809


@register_eq_class
class sincos_nv5_nt58_prog_3(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6675 * x[1] * x[3] + 0.432 * x[2] * x[4] + 0.4471 * x[2] * sympy.sin(x[0]) - 0.2932 * x[2] * sympy.sin(
            x[1]) + 0.5429 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.6256 * sympy.sin(x[0]) - 0.3864 * sympy.sin(x[1]) + 0.8904 * sympy.sin(
            x[2]) - 0.5761 * sympy.sin(x[3]) - 0.5579 * sympy.sin(x[4]) * sympy.cos(x[1]) - 0.3225 * sympy.sin(x[4]) - 0.7818 * sympy.cos(
            x[0]) * sympy.cos(x[4]) + 0.5397 * sympy.cos(x[2]) * sympy.cos(x[3]) - 0.1086


@register_eq_class
class sincos_nv5_nt58_prog_24(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.731 * x[0] * sympy.sin(x[2]) - 0.0993 * x[0] - 0.0238 * x[1] * x[3] + 0.1457 * x[1] + 0.2739 * x[2] * sympy.sin(
            x[1]) + 0.1706 * x[4] * sympy.cos(x[2]) + 0.6624 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.2726 * sympy.sin(
            x[2]) - 0.0066 * sympy.sin(x[3]) * sympy.sin(x[4]) - 0.8127 * sympy.sin(x[4]) + 0.5951 * sympy.cos(x[0]) * sympy.cos(
            x[4]) - 0.1401 * sympy.cos(x[2]) * sympy.cos(x[3]) - 0.9474 * sympy.cos(x[3]) + 0.3792


@register_eq_class
class sincos_nv5_nt58_prog_12(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6805 * x[0] * x[2] + 0.7427 * x[0] * sympy.sin(x[3]) - 0.3909 * x[1] * x[4] - 0.0036 * x[2] * x[3] + 0.0866 * x[
            2] * sympy.sin(x[4]) - 0.008 * x[2] * sympy.cos(x[1]) + 0.0312 * x[2] + 0.3956 * x[3] * sympy.cos(x[4]) - 0.8756 * sympy.sin(
            x[1]) - 0.3463 * sympy.sin(x[4]) - 0.5073 * sympy.cos(x[0]) * sympy.cos(x[4]) - 0.6938 * sympy.cos(x[0]) - 0.1707 * sympy.cos(
            x[3]) - 0.6262


@register_eq_class
class sincos_nv5_nt58_prog_25(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4044 * x[0] * x[1] - 0.4518 * x[1] * x[3] - 0.3658 * x[1] * x[4] + 0.2013 * x[2] * x[4] + 0.1276 * x[
            2] * sympy.cos(x[0]) - 0.187 * x[2] * sympy.cos(x[1]) - 0.3115 * x[3] * sympy.cos(x[2]) - 0.6288 * x[4] * sympy.cos(
            x[3]) - 0.1442 * sympy.sin(x[2]) + 0.6251 * sympy.sin(x[4]) - 0.873 * sympy.cos(x[0]) + 0.9639 * sympy.cos(
            x[1]) + 0.9093 * sympy.cos(x[3]) - 0.2371


@register_eq_class
class sincos_nv5_nt58_prog_21(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4235 * x[0] * x[3] + 0.3976 * x[1] * sympy.sin(x[3]) - 0.71 * x[1] - 0.9317 * x[2] - 0.8098 * x[3] * sympy.sin(
            x[4]) + 0.2966 * x[3] * sympy.cos(x[2]) + 0.4983 * x[4] * sympy.cos(x[1]) - 0.2874 * x[4] * sympy.cos(
            x[2]) - 0.4931 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.8348 * sympy.sin(x[0]) - 0.1448 * sympy.cos(x[0]) * sympy.cos(
            x[1]) + 0.8741 * sympy.cos(x[3]) + 0.7413 * sympy.cos(x[4]) - 0.9951


@register_eq_class
class sincos_nv5_nt58_prog_26(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0579 * x[0] * x[1] - 0.0284 * x[0] * x[4] - 0.9795 * x[0] - 0.6223 * x[1] * sympy.sin(x[2]) - 0.5635 * x[
            1] + 0.5249 * x[2] * x[4] + 0.9282 * x[2] * sympy.sin(x[3]) + 0.6648 * x[2] + 0.0047 * x[3] * x[4] + 0.4624 * x[
                            4] + 0.4945 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.4762 * sympy.sin(x[1]) * sympy.sin(
            x[4]) - 0.4093 * sympy.cos(x[3]) - 0.2045


@register_eq_class
class sincos_nv5_nt58_prog_39(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.646 * x[0] * x[1] - 0.1122 * x[0] * x[2] + 0.1971 * x[0] * sympy.sin(x[4]) + 0.6119 * x[0] + 0.3303 * x[
            1] * sympy.sin(x[4]) - 0.7419 * x[1] + 0.6151 * x[3] * sympy.cos(x[1]) + 0.58 * x[3] * sympy.cos(x[4]) - 0.3239 * x[3] - 0.057 * \
                        x[4] * sympy.cos(x[2]) + 0.1178 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.5561 * sympy.sin(x[2]) + 0.1269 * sympy.sin(
            x[4]) - 0.5694


@register_eq_class
class sincos_nv5_nt58_prog_19(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2451 * x[0] * sympy.sin(x[2]) + 0.5269 * x[0] * sympy.cos(x[1]) - 0.6637 * x[1] * x[3] - 0.765 * x[1] * sympy.sin(
            x[2]) + 0.0468 * x[1] + 0.2857 * x[2] * sympy.sin(x[4]) + 0.5333 * x[3] * sympy.sin(x[2]) - 0.6314 * sympy.sin(
            x[0]) * sympy.cos(x[3]) - 0.5125 * sympy.sin(x[3]) + 0.9617 * sympy.sin(x[4]) * sympy.cos(x[0]) + 0.6849 * sympy.cos(
            x[0]) - 0.781 * sympy.cos(x[2]) - 0.2681 * sympy.cos(x[4]) - 0.1931


@register_eq_class
class sincos_nv5_nt58_prog_38(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0768 * x[0] * x[1] + 0.1056 * x[0] * sympy.cos(x[2]) - 0.4817 * x[0] * sympy.cos(x[3]) - 0.6247 * x[1] * x[
            4] + 0.1171 * x[1] + 0.6193 * x[2] * x[3] - 0.164 * x[2] + 0.8401 * x[3] - 0.1951 * sympy.sin(x[0]) * sympy.cos(
            x[4]) + 0.5395 * sympy.sin(x[0]) + 0.541 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.6388 * sympy.sin(x[4]) * sympy.cos(
            x[3]) - 0.6669 * sympy.sin(x[4]) + 0.135


@register_eq_class
class sincos_nv5_nt58_prog_9(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2064 * x[0] * x[3] + 0.6052 * x[0] * sympy.cos(x[4]) - 0.9259 * x[1] * x[2] + 0.5821 * x[1] * x[4] - 0.126 * x[
            1] + 0.2304 * x[2] * sympy.sin(x[4]) + 0.8702 * x[2] - 0.6107 * x[3] * sympy.sin(x[2]) - 0.9991 * x[3] + 0.0481 * sympy.sin(
            x[0]) * sympy.sin(x[1]) + 0.1448 * sympy.cos(x[0]) - 0.8402 * sympy.cos(x[1]) * sympy.cos(x[3]) + 0.7772 * sympy.cos(
            x[4]) - 0.9099


@register_eq_class
class sincos_nv5_nt58_prog_32(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4404 * x[0] * x[1] - 0.8371 * x[0] * sympy.sin(x[2]) + 0.7684 * x[0] * sympy.sin(x[4]) + 0.9051 * x[
            0] * sympy.cos(x[3]) - 0.4799 * x[2] * sympy.sin(x[4]) - 0.9476 * x[3] * sympy.cos(x[1]) - 0.2303 * x[4] + 0.3119 * sympy.sin(
            x[0]) - 0.9118 * sympy.sin(x[1]) * sympy.cos(x[4]) + 0.5497 * sympy.sin(x[3]) + 0.5454 * sympy.cos(x[1]) - 0.4262 * sympy.cos(
            x[2]) * sympy.cos(x[3]) - 0.265 * sympy.cos(x[2]) - 0.6639


@register_eq_class
class sincos_nv5_nt58_prog_5(KnownEquation):
    _eq_name = 'sincos_nv5_nt58_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5615 * x[0] * x[1] + 0.0278 * x[1] + 0.4186 * x[2] * x[3] + 0.047 * x[2] * x[4] + 0.5213 * x[3] - 0.174 * x[
            4] * sympy.sin(x[3]) - 0.2694 * x[4] + 0.0746 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.8043 * sympy.sin(x[0]) * sympy.cos(
            x[4]) - 0.3802 * sympy.sin(x[1]) * sympy.sin(x[3]) + 0.6582 * sympy.sin(x[2]) * sympy.cos(x[1]) + 0.3901 * sympy.sin(
            x[2]) - 0.3937 * sympy.cos(x[0]) - 0.6712


@register_eq_class
class sincosinv_nv5_nt58_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7024 * x[0] * sympy.sin(x[1]) + 0.5904 * x[0] * sympy.sin(x[4]) + 0.6265 * x[0] * sympy.cos(x[2]) + 0.9767 * x[
            1] * x[2] - 0.548 * x[1] * sympy.sin(x[3]) + 0.0916 * x[2] * x[3] + 0.6892 * x[2] * sympy.cos(x[4]) + 0.5362 * x[3] * x[
                            4] - 0.3763 * x[3] - 0.1625 * x[4] + 0.6946 * sympy.sin(x[1]) - 0.979 + 0.3265 / x[2] - 0.196 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9828 * x[0] / x[4] - 0.5507 * x[1] * x[2] - 0.8694 * x[1] - 0.0192 * x[2] * sympy.cos(x[0]) - 0.6758 * x[2] / x[
            3] - 0.9464 * x[3] / x[4] - 0.4063 * sympy.cos(x[1]) * sympy.cos(x[3]) - 0.06 * sympy.cos(x[4]) - 0.8192 + 0.6229 * sympy.cos(
            x[1]) / x[4] - 0.2749 / x[3] - 0.8515 / x[2] - 0.7265 * sympy.sin(x[3]) / x[0] - 0.5853 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7994 * x[0] * x[1] - 0.2697 * x[0] * sympy.cos(x[2]) - 0.2069 * x[0] * sympy.cos(x[4]) + 0.5921 * x[1] * x[
            3] + 0.5241 * x[1] - 0.5817 * x[2] * x[3] - 0.7647 * x[3] * sympy.sin(x[0]) - 0.3451 * x[3] * sympy.cos(x[4]) - 0.9708 * x[
                            3] + 0.5327 * x[4] + 0.9332 * sympy.cos(x[2]) + 0.2008 + 0.716 * x[2] / x[1] + 0.9881 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3482 * x[0] * x[3] - 0.6848 * x[0] + 0.5927 * x[0] / x[4] - 0.0681 * x[1] * sympy.sin(x[4]) - 0.5273 * x[
            2] * sympy.sin(x[3]) + 0.6339 * x[2] * sympy.sin(x[4]) - 0.7098 * x[2] - 0.1649 * x[3] * sympy.cos(x[1]) + 0.5594 * x[
                            4] + 0.1447 * sympy.sin(x[1]) + 0.188 * sympy.sin(x[3]) + 0.1288 - 0.0727 * x[4] / x[3] + 0.1928 * sympy.sin(
            x[1]) / x[2]


@register_eq_class
class sincosinv_nv5_nt58_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6576 * x[1] - 0.2057 * x[1] / x[4] - 0.479 * x[4] * sympy.sin(x[0]) - 0.7958 * sympy.sin(
            x[0]) - 0.4574 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.5996 * sympy.sin(x[2]) * sympy.sin(x[3]) - 0.5293 * sympy.sin(
            x[2]) + 0.2487 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.9346 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.4683 * sympy.sin(
            x[4]) * sympy.cos(x[2]) + 0.1131 * sympy.cos(x[3]) + 0.468 * sympy.cos(x[4]) + 0.6773 - 0.5545 * sympy.sin(x[0]) / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9955 * x[0] * x[1] - 0.2446 * x[0] * sympy.sin(x[2]) + 0.1288 * x[0] - 0.1328 * x[1] * x[3] + 0.9742 * x[
            1] + 0.4773 * x[1] / x[2] - 0.03 * x[2] * sympy.sin(x[3]) + 0.3631 * x[2] - 0.2932 * x[3] * sympy.sin(x[4]) + 0.3771 * x[
                            3] * sympy.cos(x[0]) + 0.6795 * sympy.sin(x[4]) - 0.835 * sympy.cos(x[2]) * sympy.cos(x[4]) + 0.3443 - 0.0379 / \
                        x[3]


@register_eq_class
class sincosinv_nv5_nt58_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6025 * x[0] * x[3] + 0.796 * x[1] * sympy.cos(x[2]) + 0.7227 * x[1] * sympy.cos(x[4]) - 0.713 * x[2] * sympy.cos(
            x[4]) + 0.0198 * x[3] - 0.7995 * x[4] - 0.6661 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.4212 * sympy.sin(
            x[1]) - 0.7864 * sympy.cos(x[2]) - 0.4594 + 0.9562 * sympy.cos(x[2]) / x[3] - 0.8615 * sympy.cos(x[0]) / x[
                            2] + 0.4641 * sympy.sin(x[4]) / x[0] + 0.5678 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9972 * x[0] * sympy.sin(x[4]) + 0.742 * x[0] - 0.4815 * x[1] * x[2] + 0.9852 * x[1] * sympy.sin(x[0]) - 0.766 * x[
            2] * x[3] + 0.0571 * x[3] + 0.2233 * x[4] * sympy.cos(x[2]) - 0.521 * x[4] * sympy.cos(x[3]) + 0.7095 * x[
                            4] - 0.9613 * sympy.sin(x[1]) - 0.6946 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.4746 + 0.5899 / x[2] + 0.1415 * \
                        x[2] / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1936 * x[0] + 0.2106 * x[1] * x[3] - 0.5392 * x[1] + 0.1002 * x[2] * x[4] - 0.7305 * x[2] * sympy.sin(
            x[0]) - 0.5273 * x[2] - 0.2391 * x[3] * x[4] + 0.238 * x[3] * sympy.cos(x[0]) - 0.2011 * x[4] * sympy.cos(x[0]) - 0.2995 * x[
                            4] * sympy.cos(x[1]) - 0.3076 * sympy.cos(x[4]) - 0.6358 + 0.4252 / x[3] + 0.952 * x[3] / x[2]


@register_eq_class
class sincosinv_nv5_nt58_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4645 * x[0] * x[1] + 0.5295 * x[2] * sympy.cos(x[3]) - 0.2493 * x[2] + 0.0484 * x[3] * sympy.cos(x[0]) + 0.2961 * \
                        x[3] * sympy.cos(x[1]) - 0.5817 * x[4] * sympy.sin(x[2]) + 0.0738 * x[4] * sympy.cos(x[0]) + 0.1595 * x[
                            4] + 0.9273 * sympy.sin(x[2]) * sympy.cos(x[0]) - 0.9003 * sympy.cos(x[1]) * sympy.cos(
            x[2]) + 0.6316 * sympy.cos(x[1]) + 0.6489 * sympy.cos(x[3]) - 0.7356 + 0.1451 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2535 * x[0] * sympy.sin(x[1]) + 0.8185 * x[0] * sympy.sin(x[2]) + 0.4538 * x[1] * sympy.cos(x[2]) + 0.4577 * x[
            1] - 0.8145 * x[2] - 0.7447 * x[3] * sympy.sin(x[2]) + 0.7313 * x[3] + 0.992 * sympy.sin(x[1]) * sympy.sin(
            x[3]) - 0.5763 * sympy.cos(x[1]) * sympy.cos(x[4]) - 0.9241 - 0.9617 / x[4] - 0.0747 * sympy.sin(x[4]) / x[3] - 0.1775 * x[4] / \
                        x[0] - 0.4439 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5739 * x[0] * sympy.sin(x[1]) + 0.7299 * x[0] * sympy.cos(x[4]) + 0.2443 * x[1] * sympy.sin(x[3]) - 0.2651 * x[
            1] * sympy.cos(x[4]) - 0.3703 * x[1] - 0.6409 * x[1] / x[2] - 0.566 * x[2] - 0.8473 * x[3] * x[4] - 0.1847 * x[4] * sympy.sin(
            x[2]) + 0.8555 * x[4] + 0.8011 * sympy.sin(x[3]) - 0.0877 - 0.7239 * sympy.cos(x[2]) / x[0] - 0.7552 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4981 * x[0] * x[1] - 0.5048 * x[0] * x[2] + 0.9381 * x[1] * sympy.sin(x[3]) + 0.3292 * x[1] - 0.0891 * x[2] * x[
            3] + 0.331 * x[2] / x[4] + 0.6818 * x[4] * sympy.cos(x[1]) + 0.3052 * x[4] + 0.1758 * sympy.sin(x[4]) * sympy.cos(
            x[3]) + 0.9199 * sympy.cos(x[0]) - 0.3989 * sympy.cos(x[2]) + 0.1533 * sympy.cos(x[3]) + 0.4036 + 0.2202 / (x[0] * x[3])


@register_eq_class
class sincosinv_nv5_nt58_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8887 * x[0] * x[3] - 0.6789 * x[0] * x[4] + 0.0157 * x[0] + 0.4926 * x[1] * x[4] - 0.7134 * x[1] * sympy.cos(
            x[0]) - 0.0871 * x[1] / x[3] + 0.4276 * x[2] * sympy.cos(x[0]) + 0.2111 * x[3] * sympy.cos(x[2]) + 0.756 * x[
                            3] - 0.476 * sympy.sin(x[2]) - 0.2739 * sympy.cos(x[1]) + 0.0233 + 0.6091 / x[4] + 0.6269 * sympy.sin(x[4]) / x[
                            2]


@register_eq_class
class sincosinv_nv5_nt58_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3212 * x[0] * x[3] + 0.6621 * x[0] * sympy.cos(x[2]) + 0.4879 * x[1] * x[2] - 0.9568 * x[1] * x[3] + 0.0196 * x[
            1] + 0.6938 * x[2] + 0.682 * x[4] * sympy.sin(x[0]) - 0.8443 * sympy.sin(x[3]) + 0.6874 * sympy.sin(x[4]) * sympy.cos(
            x[1]) + 0.7541 * sympy.cos(x[2]) * sympy.cos(x[4]) - 0.9256 * sympy.cos(x[4]) - 0.7093 + 0.2604 * sympy.cos(x[4]) / x[
                            3] + 0.0922 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0269 * x[1] - 0.2697 * x[2] * x[4] - 0.7596 * x[2] * sympy.cos(x[3]) - 0.113 * x[3] * x[4] + 0.6173 * x[
            3] * sympy.sin(x[1]) - 0.2698 * x[4] - 0.2894 * sympy.sin(x[0]) - 0.2562 * sympy.sin(x[2]) - 0.1669 * sympy.sin(
            x[4]) * sympy.cos(x[1]) - 0.051 * sympy.cos(x[3]) - 0.0405 + 0.8065 * sympy.cos(x[2]) / x[1] - 0.8384 * sympy.sin(x[2]) / x[
                            0] - 0.6776 * sympy.cos(x[3]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8496 * x[0] * x[2] - 0.7956 * x[0] * sympy.sin(x[3]) + 0.1437 * x[0] / x[1] - 0.7988 * x[1] + 0.5579 * x[1] / x[
            4] - 0.2139 * x[2] * sympy.sin(x[1]) - 0.7275 * x[2] + 0.883 * x[3] * sympy.sin(x[4]) - 0.998 * sympy.sin(x[0]) * sympy.cos(
            x[4]) + 0.6507 * sympy.sin(x[0]) - 0.2861 * sympy.sin(x[2]) * sympy.cos(x[4]) - 0.4473 * sympy.sin(x[3]) + 0.1223 + 0.5586 / x[
                            4]


@register_eq_class
class sincosinv_nv5_nt58_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.09 * x[0] * sympy.sin(x[2]) + 0.9064 * x[0] / x[1] - 0.9246 * x[1] * x[2] - 0.6851 * x[1] * sympy.sin(
            x[4]) - 0.1892 * x[1] - 0.2385 * x[2] * sympy.sin(x[4]) + 0.3742 * x[2] + 0.6359 * x[3] * sympy.sin(x[0]) - 0.7038 * x[
                            3] + 0.0115 * x[4] * sympy.cos(x[0]) + 0.6722 * sympy.sin(x[2]) * sympy.sin(x[3]) + 0.8718 * sympy.cos(
            x[4]) - 0.0861 - 0.1118 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0846 * x[0] * sympy.cos(x[1]) - 0.9903 * x[0] + 0.7514 * x[0] / x[4] - 0.4495 * x[1] * sympy.sin(x[4]) - 0.5949 * \
                        x[1] - 0.9346 * x[2] - 0.3292 * x[3] * sympy.cos(x[0]) + 0.6751 * x[3] - 0.0467 * sympy.sin(
            x[4]) + 0.8751 + 0.1189 * x[4] / x[3] - 0.5349 * sympy.sin(x[2]) / x[3] + 0.8105 * x[2] / x[1] + 0.2274 * sympy.cos(x[2]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3752 * x[0] * x[3] - 0.3347 * x[0] * sympy.cos(x[4]) + 0.4766 * x[0] + 0.2401 * x[1] * x[4] + 0.2755 * x[
            1] * sympy.sin(x[0]) + 0.9062 * x[1] - 0.2573 * x[2] * sympy.cos(x[0]) - 0.9042 * x[2] * sympy.cos(x[1]) + 0.1414 * x[
                            3] - 0.4598 * sympy.cos(x[2]) - 0.0053 * sympy.cos(x[4]) + 0.8093 - 0.2295 * sympy.cos(x[2]) / x[3] + 0.3336 / (
                                x[3] * x[4])


@register_eq_class
class sincosinv_nv5_nt58_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7745 * x[0] * x[3] - 0.6903 * x[0] + 0.3771 * x[1] * sympy.cos(x[2]) + 0.9339 * x[1] - 0.4872 * x[1] / x[
            4] + 0.775 * x[2] - 0.7613 * x[3] * sympy.cos(x[1]) - 0.9603 * x[3] * sympy.cos(x[4]) - 0.9807 * x[4] * sympy.cos(
            x[2]) - 0.5186 * x[4] - 0.0308 * sympy.sin(x[0]) * sympy.cos(x[4]) - 0.5395 * sympy.cos(x[3]) + 0.4796 - 0.8968 * sympy.cos(
            x[1]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8512 * x[0] * x[2] + 0.5861 * x[0] * sympy.sin(x[1]) - 0.4603 * x[0] + 0.3091 * x[1] + 0.1433 * x[2] * sympy.sin(
            x[1]) - 0.9628 * x[3] * sympy.cos(x[1]) - 0.228 * x[3] + 0.8629 * x[4] * sympy.cos(x[0]) + 0.7663 * x[4] * sympy.cos(
            x[1]) + 0.9297 * sympy.sin(x[0]) * sympy.cos(x[3]) - 0.3018 * sympy.sin(x[2]) - 0.872 * sympy.cos(
            x[4]) - 0.3223 + 0.7207 * sympy.sin(x[3]) / x[2]


@register_eq_class
class sincosinv_nv5_nt58_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5457 * x[0] * x[2] - 0.8715 * x[0] - 0.1311 * x[1] * x[4] - 0.1852 * x[1] * sympy.cos(x[2]) - 0.7702 * x[
            2] - 0.8778 * x[2] / x[4] + 0.4993 * x[3] * x[4] + 0.8192 * x[3] * sympy.cos(x[2]) - 0.3618 * x[3] - 0.4219 * x[
                            4] + 0.0574 * sympy.cos(x[1]) + 0.5815 + 0.0777 * sympy.sin(x[1]) / x[3] + 0.1775 * sympy.sin(x[1]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2849 * x[0] * x[1] + 0.3231 * x[0] * x[4] + 0.2718 * x[1] * x[4] + 0.4149 * x[2] * sympy.cos(x[0]) + 0.7534 * x[
            2] - 0.9668 * x[2] / x[4] + 0.4932 * x[3] * sympy.sin(x[2]) - 0.1892 * x[3] / x[4] + 0.3617 * sympy.sin(
            x[4]) - 0.0634 * sympy.cos(x[0]) + 0.7082 * sympy.cos(x[3]) - 0.3133 - 0.871 * x[3] / x[1] + 0.2127 / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1745 * x[0] * sympy.cos(x[2]) + 0.6641 * x[1] * x[3] - 0.6492 * x[1] * sympy.cos(x[4]) - 0.6752 * x[1] + 0.4833 * \
                        x[2] * x[4] + 0.2998 * x[3] * sympy.sin(x[0]) + 0.5132 * x[3] + 0.3213 * sympy.sin(x[2]) + 0.2898 * sympy.cos(
            x[3]) * sympy.cos(x[4]) - 0.5658 * sympy.cos(x[4]) + 0.7066 - 0.2194 * x[2] / x[1] + 0.964 * x[1] / x[0] - 0.4758 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0608 * x[0] * x[4] + 0.8064 * x[0] * sympy.cos(x[1]) - 0.8478 * x[0] * sympy.cos(x[2]) - 0.0844 * x[0] - 0.1891 * \
                        x[1] * x[2] + 0.8387 * x[1] * x[3] + 0.0641 * x[3] / x[4] - 0.397 * x[4] - 0.7741 + 0.7417 / x[3] - 0.5138 * x[3] / \
                        x[2] + 0.7211 / x[2] - 0.5854 / x[1] + 0.9217 / (x[0] * x[3])


@register_eq_class
class sincosinv_nv5_nt58_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1527 * x[1] * x[4] - 0.1111 * x[1] * sympy.cos(x[2]) - 0.1444 * x[2] * x[4] + 0.5786 * x[2] + 0.5928 * x[
            3] * sympy.sin(x[1]) + 0.0243 * x[3] / x[4] - 0.9521 * x[4] - 0.5871 * sympy.sin(x[1]) + 0.9458 * sympy.cos(
            x[3]) - 0.1035 + 0.5581 * sympy.cos(x[0]) / x[3] + 0.3828 * x[3] / x[2] - 0.3374 * sympy.sin(x[1]) / x[0] - 0.5697 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2388 * x[0] + 0.5708 * x[0] / x[4] + 0.5337 * x[1] * sympy.cos(x[0]) - 0.2186 * x[1] + 0.5618 * x[2] * sympy.sin(
            x[4]) - 0.906 * x[4] * sympy.sin(x[1]) + 0.2803 * x[4] - 0.2564 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.7589 * sympy.sin(
            x[1]) * sympy.cos(x[2]) - 0.5654 * sympy.cos(x[2]) - 0.6736 * sympy.cos(x[3]) + 0.3434 + 0.7844 * sympy.cos(x[3]) / x[
                            2] - 0.3942 * sympy.cos(x[3]) / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8021 * x[0] * x[1] + 0.5313 * x[0] * sympy.sin(x[3]) - 0.9899 * x[0] + 0.0734 * x[1] * x[2] + 0.3785 * x[
            2] * sympy.sin(x[0]) + 0.101 * x[2] + 0.2724 * x[3] * x[4] + 0.7056 * x[3] - 0.7999 * sympy.sin(x[1]) + 0.6479 * sympy.sin(
            x[4]) - 0.5983 + 0.5032 * sympy.sin(x[0]) / x[4] + 0.9541 * x[4] / x[2] + 0.2852 * x[4] / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0675 * x[0] * x[4] + 0.0424 * x[1] / x[3] + 0.546 * x[1] / x[2] + 0.0051 * x[2] + 0.3084 * x[3] * x[4] - 0.4425 * \
                        x[4] + 0.7424 * sympy.cos(x[0]) - 0.1957 * sympy.cos(x[1]) * sympy.cos(x[4]) + 0.0491 * sympy.cos(
            x[1]) + 0.9658 + 0.8377 / x[3] - 0.0549 * sympy.sin(x[3]) / x[2] + 0.5014 * x[2] / x[0] + 0.6535 * sympy.sin(x[1]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9691 * x[0] * x[2] + 0.1824 * x[0] * sympy.sin(x[1]) - 0.01 * x[0] + 0.2401 * x[0] / x[4] - 0.3216 * x[1] / x[
            3] + 0.7353 * x[2] * x[3] - 0.6735 * x[2] * sympy.cos(x[1]) - 0.4709 * x[2] / x[4] + 0.6553 * sympy.sin(
            x[3]) - 0.8037 * sympy.sin(x[4]) - 0.6276 - 0.2097 * sympy.cos(x[0]) / x[3] - 0.266 / x[2] + 0.1973 / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1549 * x[0] * x[3] - 0.7732 * x[1] * x[4] - 0.567 * x[1] * sympy.sin(x[0]) - 0.5373 * x[2] / x[3] - 0.2751 * x[
            3] * sympy.cos(x[1]) - 0.7993 * x[3] + 0.2852 * sympy.cos(x[1]) + 0.6143 + 0.0923 / x[4] - 0.7142 * x[4] / x[
                            2] - 0.6311 * sympy.cos(x[0]) / x[2] + 0.9129 / x[2] + 0.0638 * x[2] / x[1] + 0.6894 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6798 * x[0] * x[3] + 0.2467 * x[0] * x[4] - 0.8332 * x[0] + 0.7851 * x[1] * x[3] + 0.5738 * x[2] * x[3] - 0.9713 * \
                        x[3] - 0.3124 * x[4] * sympy.sin(x[1]) - 0.5524 * sympy.cos(x[2]) - 0.6983 - 0.0927 / x[4] - 0.211 / (
                                x[3] * x[4]) - 0.9307 * sympy.cos(x[0]) / x[1] - 0.3236 / x[1] - 0.1762 * x[2] / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4599 * x[1] * sympy.cos(x[0]) + 0.9961 * x[1] * sympy.cos(x[2]) + 0.8417 * x[1] + 0.1732 * x[2] * x[3] - 0.6373 * \
                        x[2] * sympy.cos(x[4]) + 0.4712 * x[3] * x[4] - 0.0004 * x[3] - 0.8386 * sympy.sin(x[2]) - 0.7473 * sympy.sin(
            x[4]) - 0.4485 * sympy.cos(x[0]) * sympy.cos(x[2]) - 0.9151 - 0.8089 * x[3] / x[1] + 0.4493 * sympy.sin(x[3]) / x[0] + 0.5289 / \
                        x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3131 * x[0] - 0.0441 * x[2] + 0.0132 * x[3] * sympy.sin(x[0]) - 0.5901 * x[3] - 0.4863 * x[4] * sympy.sin(
            x[0]) + 0.0389 * sympy.sin(x[3]) * sympy.cos(x[2]) - 0.7098 * sympy.cos(x[1]) - 0.8049 * sympy.cos(x[4]) + 0.9889 + 0.7944 * x[
                            4] / x[3] + 0.3998 * sympy.cos(x[4]) / x[2] - 0.7934 * x[3] / x[1] - 0.2221 * x[4] / x[1] - 0.6744 * sympy.cos(
            x[2]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7601 * x[0] * sympy.sin(x[1]) - 0.0602 * x[1] * x[2] + 0.619 * x[1] * x[3] - 0.8271 * x[1] * sympy.sin(
            x[4]) + 0.5074 * x[2] * x[3] - 0.4258 * x[2] * x[4] - 0.6277 * x[3] * sympy.cos(x[4]) - 0.8306 * x[3] + 0.4492 * x[
                            4] - 0.8784 * sympy.sin(x[0]) + 0.2515 * sympy.cos(x[1]) + 0.46 - 0.4073 / x[2] - 0.9799 / (x[0] * x[4])


@register_eq_class
class sincosinv_nv5_nt58_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9401 * x[0] * x[2] + 0.079 * x[0] + 0.5507 * x[0] / x[1] - 0.9713 * x[1] * x[3] + 0.7546 * x[1] * x[4] + 0.5788 * \
                        x[2] * sympy.cos(x[1]) + 0.537 * x[3] * sympy.cos(x[0]) - 0.7735 * x[3] + 0.6009 * x[3] / x[4] + 0.3529 * sympy.sin(
            x[0]) * sympy.cos(x[4]) + 0.4049 * sympy.sin(x[2]) + 0.6874 - 0.3228 / x[4] - 0.9025 / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2961 * x[0] * x[2] - 0.9639 * x[0] * x[3] + 0.0126 * x[0] * sympy.sin(x[1]) + 0.9045 * x[1] - 0.1188 * x[1] / x[
            2] + 0.6496 * x[2] / x[4] - 0.5181 * x[3] - 0.3632 * x[4] * sympy.sin(x[1]) - 0.9102 * x[4] * sympy.sin(x[3]) + 0.2288 * x[
                            4] - 0.1874 * sympy.sin(x[0]) * sympy.cos(x[4]) + 0.5001 * sympy.sin(x[0]) + 0.2359 * sympy.sin(x[2]) - 0.5385


@register_eq_class
class sincosinv_nv5_nt58_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4934 * x[0] * x[1] + 0.1686 * x[0] * x[3] + 0.4038 * x[0] * x[4] - 0.1661 * x[1] * x[4] + 0.0469 * x[1] + 0.2193 * \
                        x[2] * sympy.cos(x[0]) + 0.0641 * x[2] - 0.3706 * x[3] * x[4] + 0.9477 * x[3] * sympy.sin(x[2]) - 0.8101 * x[
                            3] + 0.5669 * x[4] - 0.6504 * sympy.sin(x[0]) - 0.1907 * sympy.sin(x[1]) * sympy.sin(x[3]) + 0.6334


@register_eq_class
class sincosinv_nv5_nt58_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9476 * x[0] * x[1] + 0.3741 * x[0] + 0.5084 * x[0] / x[3] - 0.22 * x[1] * sympy.sin(x[3]) - 0.3511 * x[
            1] + 0.907 * x[2] * sympy.sin(x[1]) - 0.7578 * x[4] - 0.0891 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.4694 * sympy.cos(
            x[1]) * sympy.cos(x[4]) + 0.7357 * sympy.cos(x[3]) + 0.6709 - 0.9694 * sympy.cos(x[0]) / x[4] - 0.2732 / (
                                x[3] * x[4]) + 0.9085 / x[2]


@register_eq_class
class sincosinv_nv5_nt58_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.672 * x[0] * sympy.sin(x[3]) + 0.2585 * x[0] + 0.6843 * x[1] * x[3] - 0.0014 * x[1] * sympy.sin(x[0]) + 0.6377 * \
                        x[2] + 0.7007 * x[3] - 0.9069 * sympy.cos(x[1]) + 0.0159 - 0.3358 / x[4] + 0.4777 * sympy.sin(x[2]) / x[
                            3] + 0.58 * sympy.sin(x[4]) / x[3] - 0.6125 * sympy.sin(x[0]) / x[2] - 0.999 * sympy.cos(x[4]) / x[
                            1] - 0.0336 / (x[1] * x[2])


@register_eq_class
class sincosinv_nv5_nt58_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9386 * x[0] * x[3] - 0.242 * x[0] - 0.7972 * x[0] / x[1] - 0.447 * x[1] + 0.0692 * x[1] / x[4] - 0.4032 * x[2] * \
                        x[3] - 0.4453 * x[3] * sympy.cos(x[4]) + 0.8911 * sympy.cos(x[2]) - 0.2208 * sympy.cos(x[3]) - 0.3996 * sympy.cos(
            x[4]) - 0.5434 - 0.0228 * sympy.cos(x[1]) / x[3] + 0.9045 * x[4] / x[0] - 0.6002 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv5_nt58_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3022 * x[0] * x[2] - 0.3928 * x[0] * x[3] + 0.8192 * x[1] * x[2] - 0.3264 * x[1] + 0.5548 * x[2] * sympy.cos(
            x[4]) + 0.3088 * x[2] / x[3] - 0.4307 * sympy.sin(x[0]) + 0.8742 * sympy.sin(x[2]) + 0.3657 * sympy.sin(
            x[3]) + 0.4466 + 0.1278 / x[4] + 0.1214 * sympy.sin(x[1]) / x[3] - 0.379 * x[4] / x[1] + 0.078 * sympy.cos(x[0]) / x[1]


@register_eq_class
class sincosinv_nv5_nt58_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7892 * x[0] * x[2] + 0.1208 * x[0] - 0.3193 * x[1] * sympy.cos(x[4]) + 0.3324 * x[1] - 0.3749 * x[1] / x[
            3] - 0.2687 * x[2] * x[3] + 0.0033 * x[2] - 0.1269 * x[3] * sympy.sin(x[0]) + 0.0747 * x[3] + 0.6063 * x[
                            4] + 0.9636 * sympy.sin(x[4]) * sympy.cos(x[2]) - 0.9343 - 0.8735 * x[1] / x[0] + 0.1061 * sympy.cos(x[4]) / x[
                            0]


@register_eq_class
class sincosinv_nv5_nt58_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7208 * x[0] * sympy.cos(x[4]) - 0.2409 * x[0] / x[2] - 0.6131 * x[2] * x[4] - 0.1833 * x[3] * x[4] - 0.9105 * x[
            3] * sympy.cos(x[0]) - 0.367 * x[3] - 0.6266 * sympy.sin(x[4]) - 0.8777 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.9063 - 0.5012 / \
                        x[2] - 0.8841 / x[1] + 0.8398 / (x[1] * x[4]) + 0.1564 / (x[1] * x[3]) - 0.3117 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8837 * x[0] * sympy.sin(x[2]) - 0.7323 * x[1] * sympy.cos(x[2]) + 0.0381 * x[1] + 0.6405 * x[3] * x[4] + 0.8908 * \
                        x[4] * sympy.sin(x[2]) + 0.3901 * x[4] + 0.3779 * sympy.cos(x[0]) + 0.1752 * sympy.cos(x[1]) * sympy.cos(
            x[4]) - 0.8459 * sympy.cos(x[3]) - 0.1212 - 0.0528 / x[2] + 0.284 / (x[2] * x[3]) - 0.2546 * sympy.cos(x[1]) / x[
                            0] - 0.5521 * sympy.cos(x[3]) / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0916 * x[0] / x[4] - 0.5134 * x[1] * x[2] - 0.9718 * x[1] * sympy.cos(x[0]) + 0.2825 * x[1] * sympy.cos(
            x[4]) + 0.6173 * x[2] * x[3] + 0.4989 * x[2] * x[4] + 0.3305 * x[3] * x[4] + 0.5582 * x[3] * sympy.sin(
            x[0]) + 0.1934 * sympy.sin(x[1]) + 0.3248 * sympy.sin(x[2]) + 0.5677 * sympy.sin(x[3]) - 0.2927 + 0.1921 / x[4] - 0.695 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2724 * x[0] * x[1] - 0.0996 * x[0] * sympy.cos(x[3]) - 0.8485 * x[0] * sympy.cos(x[4]) + 0.1976 * x[
            1] * sympy.sin(x[3]) - 0.0715 * x[1] * sympy.cos(x[2]) - 0.8703 * x[1] + 0.6213 * x[2] * x[3] + 0.0903 * x[3] + 0.7227 * x[
                            4] * sympy.sin(x[3]) - 0.9111 * sympy.sin(x[2]) - 0.6571 * sympy.sin(x[4]) - 0.3997 - 0.8981 * x[2] / x[
                            0] - 0.0576 / x[0]


@register_eq_class
class sincosinv_nv5_nt58_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4923 * x[0] * x[4] + 0.3919 * x[1] * x[3] + 0.2488 * x[1] + 0.5499 * x[2] * x[3] + 0.5399 * x[2] * sympy.cos(
            x[4]) + 0.0865 * x[3] * x[4] - 0.0491 * x[3] * sympy.cos(x[0]) + 0.863 * x[3] - 0.4539 * x[4] * sympy.cos(
            x[1]) - 0.0374 * sympy.sin(x[2]) + 0.2728 * sympy.cos(x[4]) + 0.2493 + 0.9712 / x[0] - 0.1667 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv5_nt58_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt58_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4047 * x[1] - 0.4755 * x[1] / x[4] - 0.9958 * x[2] * sympy.cos(x[4]) - 0.4962 * x[3] * sympy.cos(x[0]) - 0.6666 * \
                        x[3] / x[4] - 0.8231 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.3035 * sympy.sin(x[2]) + 0.2506 * sympy.sin(
            x[3]) - 0.8604 * sympy.cos(x[0]) * sympy.cos(x[2]) - 0.4629 * sympy.cos(x[4]) - 0.4648 + 0.9777 * sympy.cos(x[2]) / x[
                            1] + 0.2099 * sympy.sin(x[1]) / x[0] + 0.5127 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3839 * x[0] * x[3] - 0.6455 * x[1] * sympy.sin(x[0]) + 0.9851 * x[4] * sympy.sin(x[3]) + 0.1099 * x[
            4] - 0.6444 * sympy.sin(x[0]) - 0.0219 * sympy.sin(x[3]) - 0.4525 + 0.2948 / x[2] - 0.4557 / x[1] + 0.0927 * x[2] / x[
                            0] - 0.4583 / (x[0] * x[4])


@register_eq_class
class sincosinv_nv5_nt55_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2688 * x[0] * x[3] - 0.019 * x[0] * sympy.sin(x[2]) + 0.2902 * x[1] - 0.0519 * x[1] / x[3] - 0.8224 * x[
            4] * sympy.cos(x[0]) - 0.1144 * sympy.sin(x[1]) * sympy.cos(x[4]) - 0.8883 * sympy.sin(x[2]) - 0.8444 * sympy.cos(
            x[0]) - 0.3521 - 0.3948 / x[4] + 0.2068 / x[3]


@register_eq_class
class sincosinv_nv5_nt55_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8242 * x[0] * sympy.cos(x[2]) - 0.8507 * x[0] + 0.7126 * x[1] * x[2] - 0.9391 * x[1] - 0.1869 * x[3] - 0.4554 * \
                        x[4] * sympy.sin(x[0]) - 0.8964 * x[4] * sympy.sin(x[2]) - 0.1401 * sympy.sin(x[4]) + 0.5107 * sympy.cos(
            x[0]) * sympy.cos(x[3]) - 0.6833 * sympy.cos(x[2]) + 0.6603


@register_eq_class
class sincosinv_nv5_nt55_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.5992 * x[0] * sympy.cos(x[1]) - 0.1067 * x[1] * x[3] + 0.5484 * x[1] - 0.9418 * x[2] * x[3] + 0.2037 * x[
            2] - 0.0754 * x[3] - 0.0493 * x[3] / x[4] - 0.4199 * x[4] + 0.2418 + 0.9531 * sympy.cos(x[3]) / x[0] - 0.7376 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2778 * x[0] * x[1] - 0.2348 * x[0] + 0.4211 * x[1] * sympy.sin(x[3]) + 0.9809 * x[2] + 0.674 * x[3] - 0.5215 * x[
            3] / x[4] - 0.3758 * x[4] * sympy.cos(x[1]) - 0.747 * x[4] - 0.9094 * sympy.sin(x[1]) + 0.8298 - 0.4396 * sympy.cos(x[2]) / x[3]


@register_eq_class
class sincosinv_nv5_nt55_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1037 * x[0] * sympy.sin(x[1]) + 0.4914 * x[0] * sympy.cos(x[2]) + 0.9098 * x[1] * x[2] - 0.509 * x[1] - 0.7258 * \
                        x[2] + 0.1579 * x[3] * x[4] + 0.3655 * x[3] + 0.3464 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.6791 * sympy.cos(
            x[4]) - 0.5481 + 0.4377 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.903 * x[0] * x[1] + 0.0751 * x[1] * x[2] - 0.6972 * x[1] * x[3] - 0.2161 * x[1] * x[4] + 0.2764 * x[1] + 0.7891 * \
                        x[2] * sympy.sin(x[3]) + 0.3227 * x[2] - 0.5038 * sympy.cos(x[0]) - 0.1452 * sympy.cos(x[3]) + 0.541 * sympy.cos(
            x[4]) - 0.0382


@register_eq_class
class sincosinv_nv5_nt55_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1048 * x[0] * sympy.sin(x[2]) + 0.6001 * x[1] * x[3] + 0.7887 * x[1] * sympy.sin(x[2]) - 0.9184 * x[2] + 0.8044 * \
                        x[3] - 0.7361 * x[4] * sympy.cos(x[0]) - 0.6929 * sympy.cos(x[1]) + 0.5101 - 0.6821 / x[4] - 0.2508 * sympy.sin(
            x[4]) / x[1] - 0.8717 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6606 * x[0] * x[3] - 0.9736 * x[0] * x[4] + 0.6413 * x[0] / x[1] + 0.4838 * x[1] + 0.4561 * x[3] - 0.5326 * x[
            4] * sympy.sin(x[3]) + 0.7901 * sympy.sin(x[2]) + 0.3493 - 0.939 / x[4] + 0.2679 * x[2] / x[1] + 0.6581 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0315 * x[0] * x[3] + 0.4498 * x[0] / x[4] + 0.989 * x[2] * x[3] - 0.8958 * x[2] + 0.8058 * x[3] * sympy.sin(
            x[1]) - 0.083 * sympy.sin(x[1]) + 0.0064 * sympy.sin(x[3]) - 0.2127 * sympy.sin(x[4]) - 0.5178 + 0.9858 * x[1] / x[0] - 0.5154 / \
                        x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8563 * x[1] + 0.2854 * x[2] + 0.4641 * x[3] * sympy.sin(x[1]) + 0.0588 * x[3] * sympy.sin(x[4]) + 0.2293 * x[
            4] - 0.1927 * sympy.sin(x[0]) + 0.2674 * sympy.sin(x[1]) * sympy.cos(x[4]) + 0.1433 * sympy.cos(
            x[3]) - 0.5329 + 0.4534 * sympy.cos(x[2]) / x[4] + 0.5021 * sympy.sin(x[0]) / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3873 * x[0] * sympy.sin(x[3]) + 0.2354 * x[1] * x[2] + 0.3482 * x[2] - 0.5008 * x[4] + 0.9534 * sympy.sin(
            x[0]) * sympy.sin(x[4]) + 0.5897 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.9198 * sympy.sin(x[4]) * sympy.cos(
            x[2]) + 0.0123 * sympy.cos(x[3]) + 0.3905 + 0.8586 / x[1] - 0.5652 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9499 * x[0] + 0.7427 * x[1] - 0.9714 * x[1] / x[2] - 0.0907 * x[2] - 0.3517 * x[3] * sympy.sin(x[2]) + 0.6787 * x[
            3] * sympy.cos(x[0]) - 0.9052 * x[3] - 0.205 * x[4] + 0.6978 + 0.4123 * sympy.sin(x[0]) / x[1] + 0.668 * sympy.cos(x[2]) / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2132 * x[0] + 0.4848 * x[1] * x[4] + 0.2559 * x[2] * sympy.sin(x[4]) + 0.4081 * x[3] - 0.2882 * x[3] / x[
            4] - 0.1651 * x[4] * sympy.cos(x[0]) + 0.4083 * sympy.cos(x[1]) + 0.2969 * sympy.cos(x[4]) - 0.8328 + 0.3462 / x[
                            2] + 0.4497 * sympy.cos(x[3]) / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8093 * x[0] * sympy.cos(x[4]) - 0.6402 * x[0] / x[2] + 0.0607 * x[3] - 0.742 * x[3] / x[4] + 0.3434 * x[
            4] - 0.5306 * sympy.cos(x[0]) - 0.4964 * sympy.cos(x[1]) - 0.5508 * sympy.cos(x[2]) - 0.3863 + 0.8584 * sympy.sin(x[4]) / x[
                            1] - 0.8995 * x[1] / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4161 * x[0] - 0.0741 * x[1] * x[4] + 0.5204 * x[2] * x[4] - 0.0828 * x[2] + 0.0537 * sympy.sin(
            x[1]) - 0.3254 * sympy.cos(x[0]) * sympy.cos(x[3]) - 0.7604 * sympy.cos(x[4]) + 0.9986 - 0.0117 * sympy.sin(x[0]) / x[
                            4] - 0.0072 * sympy.cos(x[1]) / x[3] + 0.2822 / x[3]


@register_eq_class
class sincosinv_nv5_nt55_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1325 * x[0] * x[1] - 0.5422 * x[0] * x[4] + 0.7761 * x[1] * x[4] + 0.5857 * x[3] * x[4] + 0.9245 * x[
            4] + 0.6447 * sympy.sin(x[1]) - 0.2189 * sympy.sin(x[3]) + 0.352 * sympy.cos(x[1]) * sympy.cos(x[3]) + 0.8667 * sympy.cos(
            x[2]) - 0.3755 - 0.3624 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3821 * x[0] * sympy.cos(x[2]) - 0.2928 * x[0] - 0.7451 * x[1] * x[2] - 0.3306 * x[1] * x[3] - 0.5817 * x[
            1] - 0.3777 * x[2] - 0.36 * x[3] + 0.9749 * x[4] * sympy.cos(x[3]) - 0.1424 + 0.512 / x[4] + 0.3607 * x[4] / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1705 * x[1] * x[4] + 0.4216 * x[2] / x[3] - 0.9411 * x[4] * sympy.sin(x[3]) + 0.1881 * sympy.sin(
            x[0]) * sympy.sin(x[2]) - 0.5411 * sympy.sin(x[0]) + 0.6174 * sympy.sin(x[1]) + 0.6013 * sympy.sin(x[2]) + 0.8383 * sympy.sin(
            x[3]) - 0.8883 * sympy.cos(x[4]) - 0.0273 - 0.4746 * x[2] / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1685 * x[0] * x[3] + 0.3232 * x[0] + 0.4831 * x[1] * sympy.sin(x[0]) - 0.6749 * x[2] * x[3] - 0.2471 * x[2] * x[
            4] - 0.0487 * x[2] - 0.3123 * x[3] - 0.813 * x[4] - 0.7818 * sympy.sin(x[1]) - 0.5276 - 0.4813 / (x[1] * x[4])


@register_eq_class
class sincosinv_nv5_nt55_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1368 * x[0] * x[4] + 0.5969 * x[0] * sympy.sin(x[2]) - 0.5205 * x[0] + 0.1085 * x[1] * sympy.cos(x[3]) - 0.4614 * \
                        x[1] - 0.4588 * x[2] * x[3] + 0.662 * x[4] * sympy.sin(x[3]) - 0.2726 * x[4] + 0.8105 * sympy.sin(
            x[2]) - 0.6413 * sympy.sin(x[3]) + 0.3214


@register_eq_class
class sincosinv_nv5_nt55_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6687 * x[0] * x[3] - 0.4792 * x[1] * x[2] - 0.0518 * x[3] * sympy.sin(x[2]) - 0.5484 * x[3] * sympy.cos(
            x[4]) - 0.7669 * x[4] - 0.5204 * sympy.sin(x[4]) * sympy.cos(x[1]) - 0.5739 * sympy.cos(x[0]) + 0.5274 * sympy.cos(
            x[1]) - 0.0886 * sympy.cos(x[2]) - 0.3667 - 0.9534 / x[3]


@register_eq_class
class sincosinv_nv5_nt55_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8121 * x[0] * x[2] + 0.9564 * x[0] - 0.6809 * x[0] / x[4] - 0.0225 * x[1] + 0.0563 * x[1] / x[4] + 0.883 * x[
            2] - 0.0052 * x[3] + 0.6506 * x[4] * sympy.sin(x[2]) - 0.7459 + 0.0663 / x[4] - 0.1624 * sympy.sin(x[0]) / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.043 * x[0] + 0.0617 * x[1] + 0.1872 * x[2] + 0.0023 * x[3] * x[4] - 0.5722 * x[3] * sympy.sin(x[2]) - 0.0009 * x[
            3] + 0.2948 * x[4] * sympy.sin(x[1]) - 0.6176 * x[4] + 0.6143 * sympy.sin(x[2]) * sympy.cos(x[0]) - 0.1288 * sympy.sin(
            x[2]) * sympy.cos(x[1]) - 0.0435


@register_eq_class
class sincosinv_nv5_nt55_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8782 * x[2] * sympy.cos(x[1]) - 0.2409 * x[2] + 0.4774 * x[3] + 0.1526 * x[4] + 0.0751 * sympy.sin(
            x[1]) * sympy.sin(x[4]) - 0.1312 * sympy.sin(x[1]) + 0.3423 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.2435 * sympy.sin(
            x[4]) * sympy.cos(x[3]) + 0.4866 * sympy.cos(x[0]) + 0.094 - 0.3544 / (x[0] * x[1])


@register_eq_class
class sincosinv_nv5_nt55_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4174 * x[0] * sympy.sin(x[1]) + 0.44 * x[1] * x[4] + 0.7524 * x[2] - 0.2644 * x[4] * sympy.cos(
            x[2]) - 0.1318 * sympy.sin(x[0]) + 0.0195 * sympy.cos(x[0]) * sympy.cos(x[2]) - 0.0215 * sympy.cos(x[2]) * sympy.cos(
            x[3]) - 0.0569 * sympy.cos(x[4]) - 0.8479 + 0.8017 / x[3] + 0.0915 / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3412 * x[0] + 0.4519 * x[0] / x[4] - 0.9383 * x[1] * x[3] - 0.6632 * x[1] * sympy.sin(x[2]) - 0.3826 * x[
            3] * sympy.cos(x[2]) + 0.2164 * x[4] + 0.849 * sympy.sin(x[1]) + 0.4463 * sympy.cos(x[2]) + 0.9491 + 0.793 / x[3] + 0.8485 * x[
                            4] / x[2]


@register_eq_class
class sincosinv_nv5_nt55_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2121 * x[0] * x[3] - 0.8309 * x[0] * sympy.cos(x[2]) + 0.066 * x[1] * sympy.sin(x[4]) + 0.4041 * x[1] - 0.0659 * \
                        x[2] * sympy.sin(x[3]) - 0.2744 * x[3] * sympy.sin(x[1]) - 0.0177 * x[4] + 0.6856 * sympy.cos(
            x[3]) - 0.2831 - 0.9279 / x[2] + 0.5692 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.5752 * x[0] * x[4] + 0.6264 * x[0] * sympy.cos(x[3]) - 0.3909 * x[0] / x[1] + 0.9897 * x[3] * x[4] - 0.6106 * x[
            3] + 0.9415 * x[4] - 0.7787 * sympy.cos(x[0]) - 0.5773 * sympy.cos(x[1]) - 0.7172 * sympy.cos(
            x[2]) + 0.275 + 0.7602 * sympy.sin(x[3]) / x[2]


@register_eq_class
class sincosinv_nv5_nt55_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0228 * x[0] * sympy.cos(x[4]) - 0.8706 * x[0] + 0.239 * x[1] * sympy.sin(x[3]) + 0.4729 * x[2] * sympy.cos(
            x[3]) - 0.6838 * x[2] - 0.1041 * x[3] - 0.5349 * x[4] + 0.5985 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.4649 * sympy.cos(
            x[1]) + 0.334 - 0.8107 * sympy.sin(x[4]) / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6204 * x[0] * x[3] - 0.8768 * x[0] / x[1] + 0.9747 * x[1] + 0.0349 * x[2] + 0.1019 * x[4] * sympy.cos(
            x[1]) - 0.2359 * sympy.sin(x[4]) + 0.6056 * sympy.cos(x[0]) + 0.5865 - 0.1723 * sympy.cos(x[0]) / x[4] + 0.4383 / x[3] + 0.909 * \
                        x[2] / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4438 * x[0] + 0.2171 * x[0] / x[4] + 0.0016 * x[1] * sympy.cos(x[2]) - 0.7576 * x[1] - 0.0097 * x[3] * sympy.sin(
            x[4]) + 0.0442 * sympy.sin(x[2]) - 0.3027 * sympy.sin(x[4]) + 0.6531 + 0.1267 / x[3] - 0.1846 / (
                                x[1] * x[4]) + 0.4711 * sympy.sin(x[1]) / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2707 * x[0] * x[1] + 0.5316 * x[0] - 0.414 * x[1] * x[3] - 0.8968 * x[1] * x[4] + 0.2564 * x[2] - 0.6233 * x[
            3] - 0.0945 * x[4] * sympy.sin(x[0]) + 0.2155 * x[4] * sympy.sin(x[3]) + 0.41 * x[4] - 0.7647 * sympy.cos(x[1]) + 0.2447


@register_eq_class
class sincosinv_nv5_nt55_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0357 * x[1] + 0.0043 * x[2] * x[3] - 0.7512 * x[3] * sympy.sin(x[4]) - 0.813 * sympy.sin(x[1]) * sympy.cos(
            x[2]) - 0.1528 * sympy.sin(x[2]) - 0.3243 * sympy.cos(x[0]) - 0.8361 * sympy.cos(x[3]) - 0.2356 * sympy.cos(
            x[4]) - 0.552 - 0.8814 * x[4] / x[1] - 0.4448 * x[1] / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.296 * x[0] * sympy.sin(x[3]) - 0.5619 * x[0] - 0.2651 * x[1] * sympy.sin(x[4]) + 0.883 * x[1] - 0.5722 * x[
            2] * sympy.cos(x[3]) + 0.7901 * x[2] + 0.8484 * x[3] - 0.6635 * x[4] * sympy.cos(x[3]) + 0.1179 * x[4] - 0.2581 * sympy.sin(
            x[2]) * sympy.cos(x[1]) + 0.2461


@register_eq_class
class sincosinv_nv5_nt55_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2244 * x[0] * sympy.sin(x[2]) + 0.0684 * x[0] / x[4] - 0.3865 * x[1] + 0.0669 * x[2] * sympy.cos(x[3]) + 0.9166 * \
                        x[3] * sympy.cos(x[0]) + 0.3977 * x[4] * sympy.cos(x[2]) - 0.1187 * x[4] - 0.8154 * sympy.cos(
            x[2]) - 0.0681 + 0.6973 / x[3] - 0.3926 / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.002 * x[0] - 0.9687 * x[1] * sympy.cos(x[4]) - 0.0433 * x[2] * x[3] - 0.9179 * x[3] * sympy.cos(x[0]) - 0.9805 * \
                        x[3] * sympy.cos(x[4]) - 0.7139 * x[4] + 0.0684 * sympy.cos(x[1]) - 0.2883 * sympy.cos(x[2]) - 0.5086 * sympy.cos(
            x[3]) - 0.1632 - 0.0969 * x[2] / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.909 * x[0] * x[1] - 0.7293 * x[0] * x[4] - 0.2344 * x[0] + 0.2479 * x[1] * sympy.sin(x[3]) - 0.9423 * x[3] * x[
            4] - 0.4687 * x[3] + 0.2719 * x[4] - 0.7983 * sympy.sin(x[1]) * sympy.sin(x[2]) + 0.0905 * sympy.sin(x[1]) - 0.1875 - 0.8767 / \
                        x[2]


@register_eq_class
class sincosinv_nv5_nt55_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4095 * x[0] * sympy.cos(x[4]) + 0.0616 * x[0] - 0.2679 * x[1] * x[3] + 0.9039 * x[3] * sympy.sin(x[0]) + 0.4303 * \
                        x[4] * sympy.cos(x[1]) + 0.5388 * x[4] * sympy.cos(x[2]) - 0.8611 * x[4] - 0.2568 * sympy.cos(
            x[1]) - 0.061 * sympy.cos(x[3]) + 0.1487 - 0.677 / x[2]


@register_eq_class
class sincosinv_nv5_nt55_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8277 * x[0] * x[2] + 0.9948 * x[0] * x[3] - 0.1689 * x[0] * x[4] + 0.6065 * x[0] + 0.55 * x[1] * sympy.cos(
            x[2]) + 0.3325 * x[3] + 0.4574 * sympy.cos(x[1]) - 0.6495 * sympy.cos(x[2]) + 0.4457 * sympy.cos(x[4]) - 0.1172 - 0.1061 / (
                                x[2] * x[3])


@register_eq_class
class sincosinv_nv5_nt55_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2165 * x[0] * x[1] + 0.2577 * x[0] * x[2] - 0.636 * x[0] + 0.8443 * x[1] * sympy.sin(x[2]) + 0.9143 * x[2] / x[
            4] + 0.7022 * x[4] - 0.0598 * sympy.cos(x[1]) + 0.1157 * sympy.cos(x[2]) - 0.8684 * sympy.cos(
            x[3]) + 0.8195 - 0.5136 * sympy.sin(x[3]) / x[2]


@register_eq_class
class sincosinv_nv5_nt55_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1102 * x[0] + 0.5331 * x[2] * sympy.sin(x[0]) - 0.0402 * x[2] + 0.9071 * x[4] * sympy.sin(x[0]) + 0.2739 * x[
            4] + 0.4763 * sympy.sin(x[3]) + 0.9043 * sympy.sin(x[4]) * sympy.cos(x[2]) - 0.1426 * sympy.cos(
            x[1]) + 0.4271 + 0.0157 * sympy.cos(x[3]) / x[4] + 0.583 * x[1] / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3215 * x[0] * x[1] - 0.6389 * x[0] + 0.9491 * x[1] + 0.9449 * x[3] * sympy.cos(x[1]) + 0.6718 * x[3] - 0.1483 * x[
            4] * sympy.sin(x[3]) - 0.1254 * x[4] - 0.89 * sympy.sin(x[2]) * sympy.cos(x[0]) - 0.0681 + 0.1929 * sympy.sin(x[4]) / x[
                            2] - 0.0666 / x[2]


@register_eq_class
class sincosinv_nv5_nt55_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5209 * x[0] * sympy.cos(x[1]) + 0.1232 * x[0] + 0.2891 * x[2] * sympy.cos(x[3]) + 0.5386 * x[2] + 0.1646 * x[
            4] * sympy.cos(x[3]) + 0.5203 * sympy.cos(x[2]) * sympy.cos(x[4]) + 0.2069 + 0.8632 / x[4] - 0.8306 / x[3] - 0.5195 / x[
                            1] + 0.3346 * sympy.cos(x[2]) / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3791 * x[0] * x[3] - 0.356 * x[0] * sympy.sin(x[2]) + 0.2145 * x[1] - 0.5659 * x[3] * sympy.sin(x[1]) + 0.0569 * \
                        x[3] * sympy.sin(x[4]) + 0.1374 * x[3] - 0.3963 * x[4] - 0.2752 * sympy.cos(x[0]) - 0.945 * sympy.cos(
            x[2]) * sympy.cos(x[3]) - 0.5419 * sympy.cos(x[2]) + 0.6774


@register_eq_class
class sincosinv_nv5_nt55_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.5322 * x[1] * x[3] + 0.5855 * x[1] - 0.138 * x[2] + 0.6416 * x[2] / x[3] + 0.7627 * x[4] * sympy.sin(
            x[2]) + 0.8715 * x[4] * sympy.cos(x[3]) + 0.3288 * x[4] - 0.9098 * sympy.sin(x[3]) + 0.0459 - 0.9228 * x[1] / x[0] + 0.9079 / x[
                            0]


@register_eq_class
class sincosinv_nv5_nt55_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4967 * x[0] + 0.3962 * x[1] * x[2] - 0.8015 * x[1] - 0.3511 * x[3] * sympy.sin(x[2]) - 0.2088 * x[3] - 0.8275 * x[
            4] * sympy.cos(x[1]) - 0.838 * x[4] - 0.7452 - 0.8801 * sympy.sin(x[4]) / x[2] + 0.1139 / x[2] - 0.0029 * x[3] / x[1]


@register_eq_class
class sincosinv_nv5_nt55_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8284 * x[0] * x[3] + 0.1522 * x[1] * sympy.sin(x[3]) + 0.8477 * x[1] - 0.1921 * x[3] - 0.6749 * x[3] / x[
            4] - 0.3645 * x[4] - 0.6272 * sympy.cos(x[0]) + 0.6536 * sympy.cos(x[1]) * sympy.cos(x[4]) - 0.8818 + 0.9271 / x[
                            2] - 0.4017 * sympy.sin(x[4]) / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.9999 * x[0] / x[1] - 0.2215 * x[1] + 0.0664 * x[2] * x[4] + 0.4739 * x[2] - 0.3123 * x[3] * sympy.cos(
            x[2]) + 0.6753 * x[3] * sympy.cos(x[4]) + 0.0542 * x[3] - 0.1573 * x[4] - 0.4185 * sympy.cos(
            x[0]) - 0.8879 + 0.6402 * sympy.cos(x[2]) / x[0]


@register_eq_class
class sincosinv_nv5_nt55_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv5_nt55_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1039 * x[0] - 0.4796 * x[1] - 0.4059 * x[2] * sympy.sin(x[0]) - 0.8391 * x[3] + 0.7527 * sympy.sin(
            x[1]) * sympy.cos(x[4]) + 0.3404 * sympy.cos(x[4]) - 0.6225 - 0.3333 * sympy.cos(x[1]) / x[3] + 0.7861 / x[2] - 0.8281 / (
                                x[1] * x[2]) - 0.9668 * x[4] / x[0]


@register_eq_class
class sincos_nv6_nt610_prog_46(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8462 * x[0] * sympy.cos(x[1]) + 0.9411 * x[1] * x[4] - 0.4099 * x[1] * sympy.cos(x[5]) - 0.3963 * x[1] - 0.0705 * \
                        x[2] * x[3] - 0.4996 * x[2] + 0.497 * x[3] * x[5] + 0.2803 * x[3] + 0.3972 * x[4] * sympy.cos(x[3]) + 0.7747 * x[
                            4] * sympy.cos(x[5]) - 0.6875 * x[4] + 0.2869 * x[5] + 0.0465 * sympy.sin(x[0]) * sympy.cos(
            x[5]) + 0.1743 * sympy.sin(x[0]) - 0.5183 * sympy.sin(x[2]) * sympy.cos(x[5]) - 0.8507 * sympy.cos(x[0]) * sympy.cos(
            x[3]) + 0.7171


@register_eq_class
class sincos_nv6_nt610_prog_0(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7731 * x[0] * x[3] - 0.3506 * x[0] * x[5] + 0.5987 * x[1] * sympy.cos(x[2]) + 0.3325 * x[1] + 0.5694 * x[2] * x[
            5] + 0.7267 * x[2] * sympy.cos(x[0]) - 0.0842 * x[3] * x[5] + 0.2041 * x[3] * sympy.cos(x[1]) + 0.4305 * x[4] * sympy.sin(
            x[0]) - 0.018 * x[4] * sympy.sin(x[1]) + 0.8218 * x[4] * sympy.cos(x[2]) + 0.849 * x[4] + 0.8105 * x[5] - 0.532 * sympy.sin(
            x[3]) - 0.7069 * sympy.cos(x[0]) + 0.2711 * sympy.cos(x[2]) + 0.7697


@register_eq_class
class sincos_nv6_nt610_prog_35(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5504 * x[0] * sympy.sin(x[5]) - 0.3048 * x[1] * x[2] + 0.243 * x[1] * x[5] - 0.3299 * x[1] * sympy.sin(
            x[0]) - 0.3566 * x[2] * x[5] - 0.7585 * x[2] - 0.2045 * x[3] * x[4] - 0.1848 * x[3] * sympy.cos(x[5]) - 0.141 * x[4] - 0.1819 * \
                        x[5] * sympy.sin(x[4]) - 0.6369 * x[5] - 0.6423 * sympy.sin(x[0]) * sympy.cos(x[2]) + 0.3625 * sympy.sin(
            x[0]) + 0.3312 * sympy.sin(x[1]) * sympy.sin(x[4]) - 0.6063 * sympy.sin(x[1]) + 0.6193 * sympy.cos(x[3]) + 0.2926


@register_eq_class
class sincos_nv6_nt610_prog_8(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9819 * x[0] * x[1] - 0.6092 * x[0] * x[3] + 0.4401 * x[0] + 0.2961 * x[1] - 0.2039 * x[2] * sympy.cos(
            x[0]) + 0.6163 * x[2] - 0.9343 * x[3] * sympy.sin(x[1]) - 0.5927 * x[4] * sympy.sin(x[1]) + 0.9 * x[5] * sympy.cos(
            x[1]) + 0.1278 * x[5] * sympy.cos(x[2]) - 0.4896 * x[5] + 0.8773 * sympy.sin(x[3]) * sympy.cos(x[2]) - 0.1269 * sympy.sin(
            x[4]) * sympy.cos(x[0]) + 0.2907 * sympy.sin(x[4]) + 0.5118 * sympy.cos(x[2]) * sympy.cos(x[4]) + 0.551 * sympy.cos(
            x[3]) + 0.1761


@register_eq_class
class sincos_nv6_nt610_prog_42(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6958 * x[0] * sympy.cos(x[5]) + 0.9287 * x[2] * sympy.sin(x[1]) - 0.0706 * x[2] * sympy.cos(x[0]) - 0.1355 * x[
            2] * sympy.cos(x[5]) - 0.8364 * x[3] * sympy.cos(x[5]) + 0.4013 * x[4] * sympy.cos(x[2]) - 0.2103 * x[5] + 0.1063 * sympy.sin(
            x[0]) * sympy.cos(x[4]) - 0.697 * sympy.sin(x[0]) + 0.6717 * sympy.sin(x[1]) * sympy.sin(x[5]) - 0.1354 * sympy.sin(
            x[1]) - 0.0908 * sympy.sin(x[3]) * sympy.cos(x[2]) - 0.8188 * sympy.sin(x[3]) - 0.995 * sympy.sin(x[4]) * sympy.sin(
            x[5]) + 0.1709 * sympy.cos(x[2]) - 0.1522 * sympy.cos(x[4]) - 0.9763


@register_eq_class
class sincos_nv6_nt610_prog_33(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6514 * x[0] * x[2] - 0.7522 * x[0] * x[4] - 0.525 * x[1] * x[5] - 0.144 * x[1] * sympy.sin(x[2]) - 0.7494 * x[
            1] * sympy.sin(x[3]) + 0.338 * x[1] * sympy.cos(x[4]) + 0.695 * x[3] * x[5] - 0.7536 * x[4] * sympy.sin(x[2]) + 0.1883 * x[
                            4] - 0.4557 * x[5] * sympy.sin(x[4]) + 0.1077 * x[5] - 0.3044 * sympy.sin(x[1]) * sympy.cos(
            x[0]) - 0.975 * sympy.sin(x[3]) - 0.4665 * sympy.cos(x[0]) - 0.939 * sympy.cos(x[1]) + 0.6059 * sympy.cos(x[2]) + 0.0456


@register_eq_class
class sincos_nv6_nt610_prog_20(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8835 * x[0] * sympy.cos(x[4]) + 0.6739 * x[0] + 0.6027 * x[1] * sympy.cos(x[2]) + 0.5483 * x[2] * x[3] + 0.0653 * \
                        x[2] * x[5] - 0.4592 * x[3] * sympy.sin(x[4]) - 0.6333 * x[4] * sympy.sin(x[5]) - 0.8237 * x[4] * sympy.cos(
            x[1]) - 0.3266 * x[4] - 0.1169 * sympy.sin(x[2]) * sympy.cos(x[0]) + 0.3863 * sympy.sin(x[3]) - 0.6596 * sympy.sin(
            x[5]) * sympy.cos(x[0]) - 0.3907 * sympy.sin(x[5]) - 0.3198 * sympy.cos(x[1]) + 0.0341 * sympy.cos(x[2]) - 0.7348 * sympy.cos(
            x[3]) * sympy.cos(x[5]) + 0.4006


@register_eq_class
class sincos_nv6_nt610_prog_14(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4345 * x[0] * x[5] - 0.5487 * x[0] - 0.8675 * x[1] * sympy.sin(x[2]) - 0.4642 * x[1] * sympy.sin(x[4]) - 0.5311 * \
                        x[1] * sympy.cos(x[3]) - 0.9496 * x[2] * sympy.cos(x[3]) - 0.222 * x[3] + 0.4563 * x[4] * sympy.cos(x[0]) - 0.7258 * \
                        x[4] + 0.9879 * x[5] * sympy.cos(x[1]) - 0.8447 * x[5] * sympy.cos(x[3]) - 0.0026 * sympy.sin(
            x[1]) - 0.7264 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.5478 * sympy.cos(x[2]) * sympy.cos(x[4]) + 0.1542 * sympy.cos(
            x[2]) + 0.425 * sympy.cos(x[5]) - 0.9939


@register_eq_class
class sincos_nv6_nt610_prog_31(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6017 * x[0] * x[2] - 0.2392 * x[0] * x[5] - 0.8877 * x[1] + 0.4563 * x[2] * x[3] + 0.9055 * x[2] - 0.399 * x[
            3] - 0.5713 * x[4] * sympy.sin(x[5]) - 0.6388 * x[4] * sympy.cos(x[3]) + 0.6378 * x[5] * sympy.cos(x[3]) + 0.322 * x[
                            5] - 0.5993 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.5728 * sympy.sin(x[2]) * sympy.cos(
            x[1]) - 0.6543 * sympy.sin(x[2]) * sympy.cos(x[4]) + 0.1389 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.378 * sympy.sin(
            x[4]) + 0.1431 * sympy.cos(x[0]) + 0.4821


@register_eq_class
class sincos_nv6_nt610_prog_48(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.958 * x[0] * x[5] - 0.3818 * x[0] * sympy.sin(x[2]) - 0.765 * x[1] * sympy.cos(x[0]) - 0.2982 * x[1] + 0.7717 * x[
            2] * x[4] - 0.9655 * x[2] * x[5] + 0.487 * x[2] + 0.0179 * x[3] * x[5] - 0.374 * x[3] * sympy.sin(x[1]) - 0.1935 * x[
                            3] * sympy.sin(x[2]) + 0.5473 * x[3] * sympy.sin(x[4]) + 0.8769 * x[3] - 0.0075 * x[4] * sympy.sin(
            x[1]) + 0.602 * x[5] - 0.8679 * sympy.sin(x[0]) + 0.0113 * sympy.sin(x[4]) + 0.9715


@register_eq_class
class sincos_nv6_nt610_prog_41(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0625 * x[0] * sympy.sin(x[4]) - 0.9084 * x[0] * sympy.cos(x[1]) + 0.2186 * x[0] + 0.5149 * x[1] * x[2] - 0.395 * \
                        x[2] * sympy.cos(x[0]) + 0.5492 * x[3] * sympy.cos(x[1]) + 0.2526 * x[3] - 0.7963 * x[4] * sympy.sin(
            x[1]) - 0.8447 * x[4] * sympy.sin(x[3]) + 0.3985 * x[4] * sympy.cos(x[2]) - 0.6691 * x[4] - 0.8332 * x[5] - 0.4199 * sympy.sin(
            x[1]) + 0.259 * sympy.sin(x[2]) * sympy.cos(x[5]) + 0.8813 * sympy.sin(x[3]) * sympy.cos(x[5]) - 0.083 * sympy.cos(
            x[2]) + 0.8714


@register_eq_class
class sincos_nv6_nt610_prog_7(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5442 * x[0] * x[3] - 0.6705 * x[0] * sympy.sin(x[1]) - 0.2059 * x[0] * sympy.sin(x[5]) - 0.1459 * x[0] + 0.2314 * \
                        x[1] - 0.5685 * x[2] * sympy.sin(x[1]) - 0.9793 * x[2] - 0.9266 * x[3] * sympy.sin(x[5]) - 0.5021 * x[3] + 0.6073 * \
                        x[4] * sympy.sin(x[0]) + 0.4199 * x[4] * sympy.sin(x[1]) - 0.3315 * x[5] * sympy.sin(x[2]) + 0.4563 * x[
                            5] * sympy.cos(x[4]) + 0.5843 * sympy.sin(x[4]) + 0.3916 * sympy.sin(x[5]) + 0.1 * sympy.cos(x[2]) * sympy.cos(
            x[3]) + 0.9413


@register_eq_class
class sincos_nv6_nt610_prog_37(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6862 * x[0] * x[3] + 0.3438 * x[0] - 0.7103 * x[1] * x[2] + 0.0987 * x[1] * x[3] - 0.034 * x[1] * x[4] - 0.3652 * \
                        x[1] * sympy.sin(x[0]) - 0.5653 * x[2] * x[5] - 0.5038 * x[2] - 0.8538 * x[3] * sympy.sin(x[2]) + 0.7046 * x[
                            3] + 0.4984 * x[4] + 0.3786 * x[5] * sympy.cos(x[3]) - 0.8921 * x[5] + 0.7693 * sympy.sin(x[1]) * sympy.sin(
            x[5]) - 0.0254 * sympy.sin(x[4]) * sympy.cos(x[2]) + 0.0916 * sympy.cos(x[1]) + 0.4871


@register_eq_class
class sincos_nv6_nt610_prog_15(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7184 * x[0] + 0.4423 * x[1] * sympy.sin(x[4]) - 0.863 * x[2] * sympy.cos(x[1]) + 0.1132 * x[2] * sympy.cos(
            x[5]) - 0.2578 * x[2] + 0.3483 * x[3] * x[5] - 0.2772 * x[3] * sympy.sin(x[1]) - 0.6803 * x[3] + 0.2941 * x[4] * x[5] + 0.8381 * \
                        x[4] * sympy.sin(x[3]) - 0.4671 * x[4] + 0.8075 * x[5] * sympy.sin(x[0]) - 0.7491 * sympy.sin(x[0]) * sympy.sin(
            x[4]) + 0.0936 * sympy.sin(x[2]) * sympy.sin(x[3]) - 0.4918 * sympy.sin(x[5]) - 0.932 * sympy.cos(x[1]) - 0.2621


@register_eq_class
class sincos_nv6_nt610_prog_23(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0375 * x[0] * x[1] + 0.7675 * x[0] * x[3] + 0.1165 * x[0] * x[4] + 0.7413 * x[1] * sympy.sin(x[2]) + 0.962 * x[
            2] * sympy.sin(x[0]) + 0.6041 * x[2] * sympy.cos(x[3]) + 0.213 * x[2] + 0.3039 * x[5] + 0.4895 * sympy.sin(x[0]) * sympy.sin(
            x[5]) - 0.6536 * sympy.sin(x[1]) * sympy.cos(x[5]) - 0.119 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.229 * sympy.sin(
            x[4]) * sympy.cos(x[2]) + 0.298 * sympy.sin(x[4]) + 0.2437 * sympy.cos(x[0]) - 0.5857 * sympy.cos(x[1]) - 0.0335 * sympy.cos(
            x[3]) + 0.1319


@register_eq_class
class sincos_nv6_nt610_prog_30(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0151 * x[0] * sympy.sin(x[5]) - 0.1436 * x[0] * sympy.cos(x[1]) + 0.7362 * x[0] * sympy.cos(x[3]) + 0.6602 * x[
            1] * x[4] + 0.8594 * x[1] + 0.8031 * x[2] * x[5] - 0.7247 * x[2] * sympy.sin(x[1]) - 0.0598 * x[3] + 0.9413 * x[4] + 0.9636 * x[
                            5] * sympy.sin(x[4]) - 0.3435 * x[5] - 0.453 * sympy.sin(x[0]) * sympy.sin(x[4]) + 0.622 * sympy.sin(
            x[0]) - 0.74 * sympy.sin(x[2]) * sympy.sin(x[4]) + 0.0665 * sympy.sin(x[5]) * sympy.cos(x[3]) - 0.8033 * sympy.cos(
            x[2]) - 0.2446


@register_eq_class
class sincos_nv6_nt610_prog_28(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4397 * x[0] * sympy.cos(x[5]) + 0.7902 * x[0] + 0.397 * x[1] * sympy.sin(x[3]) + 0.5074 * x[1] * sympy.cos(
            x[0]) - 0.716 * x[1] + 0.2146 * x[2] * sympy.cos(x[0]) + 0.7792 * x[3] * sympy.sin(x[5]) - 0.5198 * x[4] * x[5] + 0.3498 * x[
                            4] * sympy.sin(x[3]) - 0.1006 * x[4] - 0.9798 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.1311 * sympy.sin(
            x[1]) * sympy.sin(x[5]) + 0.5172 * sympy.sin(x[2]) * sympy.sin(x[3]) - 0.4751 * sympy.sin(x[3]) - 0.1884 * sympy.sin(
            x[5]) - 0.6573 * sympy.cos(x[2]) - 0.7019


@register_eq_class
class sincos_nv6_nt610_prog_17(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1814 * x[0] * x[4] + 0.7304 * x[0] * sympy.cos(x[2]) - 0.6544 * x[1] * sympy.sin(x[5]) - 0.5632 * x[
            1] * sympy.cos(x[2]) + 0.2566 * x[1] * sympy.cos(x[3]) + 0.6425 * x[2] * x[3] + 0.8552 * x[2] * x[5] - 0.4162 * x[2] - 0.2588 * \
                        x[3] * sympy.cos(x[5]) + 0.9424 * sympy.sin(x[1]) + 0.8374 * sympy.sin(x[4]) - 0.4506 * sympy.sin(x[5]) * sympy.cos(
            x[0]) + 0.4485 * sympy.sin(x[5]) * sympy.cos(x[4]) - 0.2894 * sympy.sin(x[5]) - 0.4582 * sympy.cos(x[0]) + 0.6933 * sympy.cos(
            x[3]) - 0.1869


@register_eq_class
class sincos_nv6_nt610_prog_43(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2573 * x[0] * x[5] - 0.474 * x[1] * sympy.cos(x[4]) + 0.2981 * x[1] + 0.3053 * x[2] * x[4] + 0.3359 * x[
            2] * sympy.cos(x[5]) - 0.1541 * x[2] - 0.2784 * x[3] * x[4] - 0.5586 * x[3] * sympy.sin(x[0]) + 0.1332 * x[3] - 0.6808 * x[
                            4] * sympy.cos(x[0]) + 0.3434 * x[5] * sympy.sin(x[1]) - 0.9934 * x[5] * sympy.sin(x[4]) + 0.2376 * sympy.sin(
            x[2]) * sympy.sin(x[3]) - 0.0837 * sympy.cos(x[0]) - 0.3153 * sympy.cos(x[4]) + 0.0639 * sympy.cos(x[5]) + 0.9182


@register_eq_class
class sincos_nv6_nt610_prog_2(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8018 * x[0] * x[3] - 0.6804 * x[0] * sympy.cos(x[1]) + 0.7706 * x[0] * sympy.cos(x[2]) + 0.4093 * x[0] - 0.0784 * \
                        x[1] * x[3] - 0.5774 * x[1] * x[4] - 0.321 * x[1] * sympy.sin(x[2]) + 0.7504 * x[1] + 0.9339 * x[2] * x[
                            3] + 0.4978 * x[2] * x[5] + 0.1041 * x[4] * x[5] + 0.1329 * x[4] - 0.4371 * x[5] + 0.776 * sympy.sin(
            x[0]) * sympy.sin(x[4]) + 0.87 * sympy.sin(x[2]) - 0.0628 * sympy.cos(x[3]) + 0.8015


@register_eq_class
class sincos_nv6_nt610_prog_4(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3458 * x[0] * x[1] - 0.3348 * x[0] * x[2] - 0.2813 * x[0] * x[5] - 0.9722 * x[0] * sympy.sin(x[3]) - 0.5237 * x[
            1] * sympy.sin(x[4]) - 0.827 * x[2] * sympy.cos(x[5]) - 0.8674 * x[3] * sympy.sin(x[4]) - 0.4151 * x[3] * sympy.cos(
            x[5]) - 0.473 * x[3] + 0.5282 * x[4] * sympy.cos(x[0]) - 0.9929 * x[4] * sympy.cos(x[5]) - 0.2496 * x[5] - 0.8814 * sympy.sin(
            x[0]) - 0.441 * sympy.cos(x[1]) - 0.5553 * sympy.cos(x[2]) + 0.0649 * sympy.cos(x[4]) + 0.1151


@register_eq_class
class sincos_nv6_nt610_prog_45(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3171 * x[0] * x[4] - 0.7958 * x[0] - 0.6086 * x[1] * x[3] - 0.3311 * x[1] * sympy.cos(x[5]) - 0.9689 * x[
            2] * sympy.sin(x[5]) + 0.015 * x[2] * sympy.cos(x[3]) + 0.5518 * x[2] + 0.7589 * x[3] * sympy.sin(x[0]) + 0.7128 * x[
                            4] + 0.0116 * x[5] * sympy.sin(x[3]) - 0.328 * x[5] + 0.2472 * sympy.sin(x[2]) * sympy.sin(
            x[4]) + 0.9959 * sympy.sin(x[3]) * sympy.cos(x[4]) + 0.0206 * sympy.cos(x[1]) * sympy.cos(x[2]) + 0.4224 * sympy.cos(
            x[1]) + 0.2593 * sympy.cos(x[3]) - 0.6689


@register_eq_class
class sincos_nv6_nt610_prog_49(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8835 * x[0] * sympy.cos(x[5]) + 0.4925 * x[1] * x[2] + 0.9246 * x[2] * sympy.sin(x[5]) + 0.264 * x[4] * x[
            5] + 0.919 * x[4] * sympy.sin(x[1]) + 0.6984 * x[4] * sympy.cos(x[0]) - 0.2174 * sympy.sin(x[0]) * sympy.cos(
            x[3]) - 0.9743 * sympy.sin(x[2]) + 0.484 * sympy.sin(x[3]) * sympy.cos(x[2]) + 0.7804 * sympy.sin(x[3]) + 0.6594 * sympy.sin(
            x[4]) - 0.7142 * sympy.sin(x[5]) * sympy.cos(x[3]) + 0.464 * sympy.sin(x[5]) - 0.7601 * sympy.cos(x[0]) * sympy.cos(
            x[1]) - 0.2113 * sympy.cos(x[0]) + 0.7859 * sympy.cos(x[1]) + 0.6994


@register_eq_class
class sincos_nv6_nt610_prog_11(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9422 * x[0] * sympy.cos(x[4]) - 0.6774 * x[1] * sympy.cos(x[3]) - 0.3297 * x[1] + 0.3733 * x[2] * sympy.sin(
            x[3]) - 0.1672 * x[3] * sympy.sin(x[0]) - 0.4339 * x[3] * sympy.sin(x[5]) + 0.9285 * x[4] - 0.4022 * x[5] * sympy.cos(
            x[1]) + 0.4573 * x[5] - 0.3359 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.853 * sympy.sin(x[0]) - 0.0593 * sympy.sin(
            x[1]) * sympy.cos(x[0]) - 0.4007 * sympy.sin(x[2]) - 0.4099 * sympy.sin(x[3]) * sympy.cos(x[4]) + 0.1853 * sympy.cos(
            x[2]) * sympy.cos(x[5]) - 0.862 * sympy.cos(x[3]) + 0.753


@register_eq_class
class sincos_nv6_nt610_prog_10(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4254 * x[0] * x[4] - 0.6028 * x[1] * sympy.sin(x[3]) + 0.941 * x[3] * x[4] + 0.8712 * x[5] * sympy.sin(
            x[0]) + 0.2619 * x[5] * sympy.sin(x[2]) + 0.3351 * x[5] * sympy.cos(x[1]) - 0.5154 * x[5] * sympy.cos(x[4]) + 0.69 * sympy.sin(
            x[1]) * sympy.cos(x[0]) + 0.3338 * sympy.sin(x[1]) + 0.0011 * sympy.sin(x[3]) * sympy.cos(x[2]) + 0.596 * sympy.cos(
            x[0]) * sympy.cos(x[2]) + 0.7039 * sympy.cos(x[0]) + 0.2768 * sympy.cos(x[2]) + 0.0619 * sympy.cos(x[3]) - 0.3516 * sympy.cos(
            x[4]) + 0.1951 * sympy.cos(x[5]) - 0.6243


@register_eq_class
class sincos_nv6_nt610_prog_1(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4795 * x[0] * x[3] + 0.3408 * x[0] * x[5] - 0.2836 * x[0] * sympy.sin(x[1]) - 0.3653 * x[0] * sympy.sin(
            x[4]) - 0.4185 * x[2] * sympy.sin(x[1]) - 0.5214 * x[2] * sympy.cos(x[5]) + 0.0565 * x[4] - 0.7513 * sympy.sin(
            x[2]) * sympy.sin(x[4]) - 0.9501 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.2445 * sympy.sin(x[2]) + 0.6213 * sympy.sin(
            x[3]) * sympy.cos(x[1]) - 0.1544 * sympy.sin(x[3]) - 0.7689 * sympy.sin(x[5]) + 0.1492 * sympy.cos(x[0]) + 0.9059 * sympy.cos(
            x[1]) - 0.9596 * sympy.cos(x[4]) * sympy.cos(x[5]) - 0.2943


@register_eq_class
class sincos_nv6_nt610_prog_40(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6589 * x[0] * sympy.cos(x[4]) - 0.3383 * x[0] + 0.734 * x[1] * sympy.cos(x[0]) + 0.3269 * x[1] + 0.2452 * x[
            2] * sympy.cos(x[0]) - 0.1042 * x[2] - 0.4846 * x[4] * sympy.sin(x[1]) - 0.2812 * x[4] * sympy.cos(x[3]) - 0.7161 * x[
                            5] * sympy.sin(x[1]) + 0.4299 * x[5] * sympy.sin(x[2]) - 0.653 * x[5] + 0.7882 * sympy.sin(x[1]) * sympy.sin(
            x[3]) - 0.5936 * sympy.sin(x[3]) * sympy.cos(x[5]) + 0.165 * sympy.sin(x[4]) * sympy.sin(x[5]) + 0.8983 * sympy.cos(
            x[3]) + 0.6602 * sympy.cos(x[4]) + 0.0766


@register_eq_class
class sincos_nv6_nt610_prog_29(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2837 * x[0] * sympy.sin(x[1]) - 0.8044 * x[0] * sympy.cos(x[2]) + 0.8145 * x[0] * sympy.cos(x[3]) - 0.2289 * x[
            0] * sympy.cos(x[5]) - 0.8845 * x[0] - 0.3607 * x[1] + 0.7604 * x[2] * sympy.cos(x[5]) - 0.321 * x[2] - 0.1943 * x[
                            4] * sympy.sin(x[3]) + 0.4276 * x[4] - 0.576 * x[5] * sympy.cos(x[3]) + 0.9814 * x[5] - 0.8621 * sympy.sin(
            x[1]) * sympy.cos(x[2]) + 0.7559 * sympy.sin(x[2]) * sympy.cos(x[3]) - 0.3234 * sympy.sin(x[2]) * sympy.cos(
            x[4]) + 0.0853 * sympy.cos(x[3]) - 0.6675


@register_eq_class
class sincos_nv6_nt610_prog_22(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3778 * x[0] - 0.7445 * x[1] * x[3] + 0.5623 * x[1] - 0.3279 * x[2] * x[3] + 0.5927 * x[3] * x[5] + 0.6204 * x[
            3] + 0.8558 * x[4] * x[5] - 0.2864 * x[4] * sympy.sin(x[0]) - 0.8964 * x[4] - 0.815 * x[5] * sympy.cos(x[0]) - 0.911 * x[
                            5] + 0.6993 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.4956 * sympy.sin(x[1]) * sympy.cos(
            x[4]) - 0.7731 * sympy.sin(x[2]) + 0.8125 * sympy.sin(x[4]) * sympy.cos(x[3]) - 0.6381 * sympy.cos(x[2]) * sympy.cos(
            x[4]) + 0.4077


@register_eq_class
class sincos_nv6_nt610_prog_27(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9309 * x[0] * x[4] - 0.8659 * x[0] * sympy.cos(x[3]) - 0.2029 * x[1] - 0.9084 * x[2] * x[3] - 0.5797 * x[
            3] * sympy.cos(x[5]) - 0.8044 * x[3] - 0.1109 * x[4] * sympy.cos(x[5]) + 0.1866 * x[4] + 0.7883 * x[5] * sympy.sin(
            x[1]) - 0.7236 * x[5] + 0.1621 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.1686 * sympy.sin(x[1]) * sympy.cos(
            x[4]) - 0.7535 * sympy.sin(x[2]) * sympy.cos(x[5]) - 0.6891 * sympy.cos(x[0]) - 0.9738 * sympy.cos(x[2]) * sympy.cos(
            x[4]) + 0.5046 * sympy.cos(x[2]) + 0.0172


@register_eq_class
class sincos_nv6_nt610_prog_34(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9006 * x[0] * sympy.sin(x[1]) - 0.3972 * x[0] * sympy.sin(x[3]) - 0.0228 * x[2] * sympy.cos(x[4]) - 0.2511 * x[
            2] - 0.8182 * x[3] * sympy.sin(x[1]) + 0.2134 * x[3] * sympy.sin(x[5]) - 0.2045 * x[4] * sympy.sin(x[0]) - 0.2895 * x[
                            4] + 0.9093 * x[5] * sympy.sin(x[1]) + 0.2002 * x[5] * sympy.cos(x[2]) + 0.265 * x[5] - 0.448 * sympy.sin(
            x[0]) * sympy.sin(x[2]) - 0.4932 * sympy.sin(x[0]) * sympy.cos(x[5]) + 0.6728 * sympy.sin(x[1]) - 0.7952 * sympy.sin(
            x[3]) - 0.2419 * sympy.cos(x[0]) - 0.0274


@register_eq_class
class sincos_nv6_nt610_prog_16(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4375 * x[0] * sympy.cos(x[3]) + 0.5003 * x[1] * x[3] - 0.211 * x[1] * x[5] - 0.0023 * x[1] + 0.9089 * x[
            3] * sympy.sin(x[4]) - 0.6774 * x[3] * sympy.cos(x[5]) + 0.4337 * x[4] * sympy.cos(x[2]) - 0.6934 * sympy.sin(
            x[0]) + 0.2522 * sympy.sin(x[1]) * sympy.sin(x[2]) - 0.542 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.5064 * sympy.sin(
            x[2]) * sympy.cos(x[5]) - 0.4327 * sympy.sin(x[2]) - 0.4351 * sympy.sin(x[3]) - 0.7772 * sympy.sin(x[4]) * sympy.cos(
            x[0]) + 0.9243 * sympy.sin(x[5]) - 0.463 * sympy.cos(x[4]) + 0.9895


@register_eq_class
class sincos_nv6_nt610_prog_13(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1366 * x[0] * x[1] + 0.3837 * x[0] * sympy.cos(x[5]) + 0.229 * x[0] + 0.6688 * x[1] * sympy.sin(x[2]) - 0.1706 * \
                        x[1] * sympy.sin(x[3]) + 0.0222 * x[1] - 0.8677 * x[2] * x[3] - 0.3936 * x[2] * sympy.sin(x[0]) - 0.2015 * x[
                            3] * sympy.sin(x[4]) - 0.967 * x[3] - 0.1446 * x[4] * sympy.sin(x[0]) + 0.455 * x[4] * sympy.cos(
            x[5]) + 0.8916 * x[4] + 0.7414 * x[5] * sympy.sin(x[1]) - 0.3663 * sympy.sin(x[2]) - 0.2613 * sympy.cos(x[5]) - 0.6554


@register_eq_class
class sincos_nv6_nt610_prog_47(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5693 * x[0] * x[2] - 0.3488 * x[1] * sympy.sin(x[5]) - 0.3458 * x[2] * sympy.cos(x[3]) - 0.8653 * x[2] + 0.7414 * \
                        x[3] * sympy.sin(x[1]) + 0.0479 * x[3] * sympy.sin(x[4]) + 0.4632 * x[3] + 0.1358 * sympy.sin(
            x[0]) + 0.3379 * sympy.sin(x[1]) * sympy.sin(x[2]) - 0.7756 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.7168 * sympy.sin(
            x[1]) - 0.2208 * sympy.sin(x[2]) * sympy.cos(x[4]) + 0.3604 * sympy.cos(x[0]) * sympy.cos(x[4]) - 0.1006 * sympy.cos(
            x[2]) * sympy.cos(x[5]) - 0.7855 * sympy.cos(x[4]) - 0.2493 * sympy.cos(x[5]) + 0.1641


@register_eq_class
class sincos_nv6_nt610_prog_36(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0317 * x[0] * x[2] - 0.0727 * x[0] * x[5] + 0.6654 * x[0] + 0.1344 * x[1] * x[2] + 0.1948 * x[1] * x[4] + 0.1764 * \
                        x[1] - 0.8634 * x[2] * sympy.sin(x[5]) + 0.1089 * x[3] * sympy.cos(x[4]) + 0.0974 * x[4] * sympy.sin(
            x[0]) + 0.6082 * x[5] * sympy.sin(x[3]) + 0.2086 * x[5] * sympy.sin(x[4]) - 0.7881 * x[5] * sympy.cos(x[1]) - 0.5079 * x[
                            5] - 0.2715 * sympy.sin(x[3]) + 0.2935 * sympy.cos(x[2]) + 0.3519 * sympy.cos(x[4]) - 0.6466


@register_eq_class
class sincos_nv6_nt610_prog_44(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5512 * x[0] * sympy.sin(x[5]) - 0.2871 * x[0] * sympy.cos(x[1]) + 0.6091 * x[1] * sympy.sin(x[4]) - 0.4358 * x[
            2] * sympy.cos(x[4]) - 0.9076 * x[3] * sympy.sin(x[0]) - 0.4187 * x[3] + 0.3999 * x[4] - 0.1023 * sympy.sin(x[1]) * sympy.sin(
            x[5]) + 0.6101 * sympy.sin(x[2]) * sympy.cos(x[1]) + 0.1789 * sympy.sin(x[2]) - 0.7603 * sympy.sin(x[3]) * sympy.sin(
            x[4]) - 0.4865 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.3047 * sympy.cos(x[0]) - 0.8689 * sympy.cos(x[1]) + 0.356 * sympy.cos(
            x[2]) * sympy.cos(x[5]) + 0.5696 * sympy.cos(x[5]) - 0.2477


@register_eq_class
class sincos_nv6_nt610_prog_6(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4904 * x[0] * sympy.sin(x[4]) + 0.4611 * x[0] * sympy.cos(x[5]) - 0.9855 * x[1] * sympy.sin(x[5]) - 0.6639 * x[
            1] + 0.8481 * x[2] * sympy.sin(x[0]) + 0.7883 * x[3] + 0.3918 * x[4] * x[5] - 0.2737 * x[5] * sympy.cos(
            x[3]) + 0.56 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.455 * sympy.sin(x[3]) * sympy.cos(x[2]) + 0.0465 * sympy.sin(
            x[4]) - 0.1309 * sympy.cos(x[0]) + 0.6162 * sympy.cos(x[2]) * sympy.cos(x[4]) - 0.7968 * sympy.cos(x[2]) - 0.7076 * sympy.cos(
            x[3]) * sympy.cos(x[4]) + 0.8198 * sympy.cos(x[5]) + 0.1901


@register_eq_class
class sincos_nv6_nt610_prog_18(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8233 * x[0] * x[4] + 0.505 * x[1] * x[3] - 0.7096 * x[1] * sympy.sin(x[0]) - 0.2074 * x[1] + 0.0624 * x[
            2] * sympy.sin(x[5]) - 0.3218 * x[2] * sympy.cos(x[1]) + 0.0771 * x[2] + 0.5976 * x[3] + 0.5608 * x[4] * sympy.sin(
            x[2]) + 0.532 * x[4] * sympy.cos(x[1]) + 0.5827 * x[4] + 0.1466 * sympy.sin(x[3]) * sympy.sin(x[4]) - 0.1725 * sympy.sin(
            x[3]) * sympy.sin(x[5]) - 0.0592 * sympy.sin(x[5]) * sympy.cos(x[0]) - 0.6045 * sympy.sin(x[5]) - 0.9472 * sympy.cos(
            x[0]) + 0.4675


@register_eq_class
class sincos_nv6_nt610_prog_3(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0879 * x[0] * sympy.sin(x[2]) + 0.2186 * x[0] * sympy.cos(x[4]) + 0.3456 * x[1] - 0.3001 * x[2] * x[5] + 0.1501 * \
                        x[2] * sympy.cos(x[1]) - 0.4833 * x[3] * sympy.sin(x[1]) - 0.9198 * x[3] * sympy.cos(x[4]) + 0.3471 * x[
                            4] * sympy.sin(x[1]) + 0.5014 * x[4] * sympy.cos(x[2]) + 0.8932 * sympy.sin(x[0]) * sympy.cos(
            x[3]) + 0.0212 * sympy.sin(x[0]) * sympy.cos(x[5]) + 0.2926 * sympy.sin(x[2]) + 0.1891 * sympy.sin(x[4]) + 0.3658 * sympy.sin(
            x[5]) - 0.3094 * sympy.cos(x[0]) + 0.1978 * sympy.cos(x[3]) - 0.3057


@register_eq_class
class sincos_nv6_nt610_prog_24(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5749 * x[0] * x[3] - 0.1646 * x[1] * sympy.cos(x[0]) - 0.4608 * x[2] * sympy.cos(x[5]) + 0.6019 * x[2] - 0.4337 * \
                        x[3] * sympy.cos(x[2]) + 0.9545 * x[4] * x[5] + 0.1981 * x[5] * sympy.sin(x[1]) + 0.1983 * x[5] + 0.799 * sympy.sin(
            x[1]) * sympy.cos(x[4]) - 0.6945 * sympy.sin(x[1]) - 0.5767 * sympy.sin(x[2]) * sympy.cos(x[0]) + 0.3697 * sympy.sin(
            x[4]) * sympy.cos(x[3]) + 0.3629 * sympy.sin(x[4]) + 0.5245 * sympy.sin(x[5]) * sympy.cos(x[0]) + 0.8088 * sympy.cos(
            x[0]) + 0.0996 * sympy.cos(x[3]) - 0.1017


@register_eq_class
class sincos_nv6_nt610_prog_12(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9235 * x[0] * sympy.cos(x[4]) - 0.0531 * x[0] + 0.1855 * x[1] + 0.5823 * x[3] * sympy.sin(x[5]) + 0.3126 * x[
            3] + 0.3952 * x[4] * x[5] + 0.2063 * x[4] * sympy.sin(x[3]) - 0.5276 * x[5] * sympy.cos(x[2]) - 0.0544 * x[
                            5] - 0.3512 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.2219 * sympy.sin(x[0]) * sympy.cos(
            x[5]) + 0.9306 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.4905 * sympy.sin(x[2]) * sympy.cos(x[3]) - 0.8512 * sympy.sin(
            x[3]) * sympy.cos(x[1]) - 0.1546 * sympy.cos(x[2]) - 0.1561 * sympy.cos(x[4]) + 0.715


@register_eq_class
class sincos_nv6_nt610_prog_25(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1614 * x[0] * sympy.sin(x[5]) + 0.4546 * x[0] - 0.9634 * x[1] * x[4] - 0.3897 * x[1] * sympy.cos(x[3]) + 0.5252 * \
                        x[1] + 0.1233 * x[2] * sympy.sin(x[5]) + 0.3817 * x[2] - 0.8248 * x[3] - 0.3776 * x[5] * sympy.sin(
            x[3]) + 0.8657 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.6175 * sympy.sin(x[4]) * sympy.cos(x[2]) + 0.8931 * sympy.cos(
            x[0]) * sympy.cos(x[1]) + 0.5805 * sympy.cos(x[0]) * sympy.cos(x[2]) + 0.9809 * sympy.cos(x[2]) * sympy.cos(
            x[3]) + 0.3703 * sympy.cos(x[4]) + 0.9551 * sympy.cos(x[5]) + 0.3925


@register_eq_class
class sincos_nv6_nt610_prog_21(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7398 * x[0] * sympy.cos(x[3]) - 0.4879 * x[1] * sympy.cos(x[5]) - 0.5038 * x[2] * sympy.cos(x[3]) + 0.1012 * x[
            2] + 0.1909 * x[3] * sympy.cos(x[5]) + 0.962 * x[3] - 0.9858 * x[4] * x[5] - 0.4768 * x[5] - 0.3298 * sympy.sin(
            x[0]) * sympy.sin(x[5]) + 0.1673 * sympy.sin(x[0]) + 0.9754 * sympy.sin(x[1]) * sympy.sin(x[4]) - 0.26 * sympy.sin(
            x[3]) * sympy.cos(x[1]) + 0.1618 * sympy.sin(x[5]) * sympy.cos(x[2]) - 0.092 * sympy.cos(x[0]) * sympy.cos(
            x[1]) + 0.2066 * sympy.cos(x[1]) - 0.999 * sympy.cos(x[4]) - 0.0576


@register_eq_class
class sincos_nv6_nt610_prog_26(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8653 * x[0] * sympy.cos(x[5]) - 0.443 * x[1] * sympy.cos(x[5]) + 0.1665 * x[2] * sympy.cos(x[0]) + 0.7048 * x[
            2] - 0.1212 * x[3] * sympy.sin(x[4]) + 0.0661 * x[3] * sympy.cos(x[1]) - 0.4374 * x[4] * sympy.cos(x[1]) - 0.4586 * x[
                            4] * sympy.cos(x[2]) + 0.41 * x[4] + 0.6355 * x[5] * sympy.sin(x[4]) + 0.8105 * x[5] * sympy.cos(
            x[3]) + 0.284 * sympy.sin(x[0]) + 0.7876 * sympy.sin(x[1]) - 0.8458 * sympy.sin(x[5]) - 0.5358 * sympy.cos(x[2]) * sympy.cos(
            x[3]) - 0.656 * sympy.cos(x[3]) - 0.0994


@register_eq_class
class sincos_nv6_nt610_prog_39(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4276 * x[0] * x[2] - 0.6182 * x[0] * x[4] - 0.8576 * x[0] - 0.7147 * x[1] * sympy.cos(x[2]) + 0.6013 * x[
            1] - 0.3015 * x[2] * x[5] - 0.1657 * x[3] * sympy.cos(x[0]) - 0.3133 * x[3] * sympy.cos(x[4]) - 0.5031 * x[3] - 0.6445 * x[
                            4] * sympy.cos(x[2]) - 0.2642 * x[4] * sympy.cos(x[5]) - 0.234 * x[5] * sympy.cos(x[1]) - 0.9106 * sympy.sin(
            x[0]) * sympy.cos(x[1]) + 0.1068 * sympy.sin(x[2]) + 0.3046 * sympy.sin(x[4]) + 0.5543 * sympy.cos(x[5]) + 0.6851


@register_eq_class
class sincos_nv6_nt610_prog_19(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9924 * x[0] * x[2] + 0.4894 * x[0] - 0.6228 * x[1] * x[2] + 0.202 * x[1] * sympy.cos(x[4]) + 0.2949 * x[
            1] - 0.35 * x[2] * sympy.cos(x[4]) + 0.2074 * x[2] - 0.4563 * x[3] * sympy.sin(x[4]) - 0.308 * x[3] + 0.6303 * x[4] * sympy.sin(
            x[0]) - 0.36 * x[5] * sympy.sin(x[3]) + 0.9382 * x[5] + 0.5192 * sympy.sin(x[1]) * sympy.cos(x[5]) - 0.5777 * sympy.sin(
            x[2]) * sympy.sin(x[5]) - 0.0156 * sympy.sin(x[3]) * sympy.cos(x[2]) + 0.6808 * sympy.cos(x[4]) - 0.5296


@register_eq_class
class sincos_nv6_nt610_prog_38(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7274 * x[0] * x[3] + 0.041 * x[0] * x[5] - 0.334 * x[0] * sympy.sin(x[1]) - 0.7997 * x[1] * sympy.cos(
            x[4]) + 0.1536 * x[1] - 0.3256 * x[2] * sympy.sin(x[3]) + 0.7356 * x[2] * sympy.cos(x[5]) + 0.8017 * x[2] + 0.0407 * x[
                            3] * sympy.cos(x[1]) + 0.4206 * x[3] - 0.0879 * x[4] * sympy.sin(x[5]) + 0.7109 * x[5] * sympy.sin(
            x[1]) + 0.4715 * x[5] + 0.6147 * sympy.sin(x[0]) + 0.9371 * sympy.cos(x[3]) * sympy.cos(x[5]) - 0.1712 * sympy.cos(
            x[4]) + 0.1613


@register_eq_class
class sincos_nv6_nt610_prog_9(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9442 * x[0] * x[1] + 0.1517 * x[0] * sympy.cos(x[4]) + 0.1251 * x[0] - 0.3271 * x[1] * sympy.sin(x[5]) + 0.6235 * \
                        x[1] * sympy.cos(x[3]) - 0.6685 * x[1] + 0.4334 * x[2] * x[4] + 0.7275 * x[2] * sympy.sin(x[0]) - 0.8994 * x[
                            2] * sympy.sin(x[5]) + 0.2948 * x[3] * x[4] - 0.2455 * x[3] + 0.0392 * x[5] * sympy.sin(
            x[0]) + 0.1698 * sympy.sin(x[4]) + 0.5975 * sympy.cos(x[1]) * sympy.cos(x[2]) + 0.1082 * sympy.cos(x[2]) + 0.0244 * sympy.cos(
            x[5]) + 0.0606


@register_eq_class
class sincos_nv6_nt610_prog_32(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2712 * x[0] * sympy.cos(x[1]) - 0.065 * x[1] * x[5] - 0.0833 * x[1] * sympy.sin(x[3]) + 0.8786 * x[2] * x[
            3] - 0.8379 * x[2] * x[4] - 0.0895 * x[3] * x[5] + 0.0241 * x[3] * sympy.cos(x[4]) - 0.9299 * x[3] + 0.6421 * x[4] * sympy.sin(
            x[5]) - 0.6179 * x[5] * sympy.sin(x[0]) - 0.4132 * x[5] - 0.5023 * sympy.sin(x[0]) + 0.308 * sympy.sin(
            x[1]) - 0.0163 * sympy.sin(x[4]) - 0.5789 * sympy.sin(x[5]) * sympy.cos(x[2]) - 0.5306 * sympy.cos(x[2]) + 0.5955


@register_eq_class
class sincos_nv6_nt610_prog_5(KnownEquation):
    _eq_name = 'sincos_nv6_nt610_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7659 * x[0] * x[1] + 0.5859 * x[0] * x[4] + 0.5457 * x[0] * sympy.sin(x[5]) - 0.7902 * x[0] - 0.2567 * x[
            1] * sympy.sin(x[4]) + 0.1881 * x[1] * sympy.cos(x[3]) - 0.9726 * x[2] * x[3] + 0.215 * x[2] * sympy.sin(x[5]) + 0.3626 * x[
                            2] + 0.0368 * x[3] * sympy.cos(x[4]) + 0.2092 * x[5] * sympy.sin(x[3]) + 0.4324 * x[5] + 0.8765 * sympy.sin(
            x[0]) * sympy.sin(x[3]) - 0.7358 * sympy.sin(x[1]) + 0.6927 * sympy.sin(x[3]) + 0.2547 * sympy.sin(x[4]) - 0.0298


@register_eq_class
class inv_nv6_nt68_prog_46(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3433 * x[0] - 0.2872 * x[0] / x[4] - 0.3191 * x[0] / x[2] - 0.0196 * x[0] / x[1] - 0.1735 * x[1] * x[4] - 0.5461 * \
                        x[2] - 0.9009 * x[3] / x[4] - 0.727 - 0.4953 / x[5] - 0.3685 / x[4] - 0.1763 / x[3] + 0.6828 / (
                                x[2] * x[5]) + 0.9965 * x[5] / x[1] + 0.0655 / x[1] - 0.1349 * x[3] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_0(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4114 * x[0] * x[1] - 0.2054 * x[0] * x[5] + 0.722 * x[0] + 0.8236 * x[0] / x[2] - 0.9467 * x[1] * x[3] + 0.4969 * \
                        x[1] - 0.9178 * x[1] / x[2] + 0.9156 * x[3] * x[4] + 0.1293 * x[3] - 0.1138 * x[4] - 0.652 * x[
                            5] + 0.6261 - 0.2877 / (x[3] * x[5]) + 0.1702 * x[3] / x[2] + 0.6721 / x[2]


@register_eq_class
class inv_nv6_nt68_prog_35(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.287 * x[0] * x[4] + 0.516 * x[1] / x[5] - 0.2794 * x[1] / x[3] - 0.0467 * x[2] + 0.3273 * x[4] / x[
            5] + 0.0335 + 0.6105 / x[5] - 0.1998 / x[4] + 0.1868 * x[4] / x[3] + 0.3518 / x[3] - 0.511 * x[3] / x[2] + 0.0037 / x[
                            1] + 0.009 / (x[1] * x[2]) - 0.1778 * x[2] / x[0] + 0.5582 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_8(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5817 * x[1] / x[5] - 0.0447 * x[1] / x[2] - 0.4223 * x[2] - 0.5767 * x[3] * x[4] - 0.2543 * x[
            4] + 0.2845 - 0.8409 / x[5] + 0.1099 / (x[4] * x[5]) - 0.9798 / x[3] + 0.2792 / (x[2] * x[4]) + 0.8729 / x[1] - 0.3345 * x[2] / \
                        x[0] - 0.2944 * x[3] / x[0] + 0.9109 / x[0] + 0.7204 / (x[0] * x[5])


@register_eq_class
class inv_nv6_nt68_prog_42(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1284 * x[0] * x[4] + 0.0152 * x[0] + 0.5419 * x[1] - 0.0401 * x[1] / x[2] + 0.3523 * x[4] * x[5] + 0.4177 * x[
            4] + 0.4663 - 0.9332 / x[5] - 0.2511 / x[3] - 0.5899 / (x[3] * x[5]) - 0.3122 * x[4] / x[2] + 0.4389 / x[2] - 0.2876 / (
                                x[2] * x[5]) + 0.2896 * x[3] / x[1] + 0.8449 * x[2] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_33(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.109 * x[0] * x[1] - 0.3298 * x[0] * x[5] - 0.599 * x[1] + 0.0872 * x[1] / x[5] - 0.7373 * x[2] * x[4] + 0.3544 * \
                        x[2] + 0.0856 * x[2] / x[3] - 0.6845 * x[3] * x[4] + 0.915 * x[3] - 0.6199 * x[5] - 0.3871 - 0.6499 / x[
                            4] - 0.6906 / (x[1] * x[4]) + 0.5521 / x[0] + 0.7748 / (x[0] * x[4])


@register_eq_class
class inv_nv6_nt68_prog_20(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6779 * x[0] - 0.9886 * x[1] - 0.0707 * x[1] / x[5] + 0.1113 * x[1] / x[4] - 0.6686 * x[2] + 0.0202 + 0.9551 / x[
            5] - 0.5224 / x[4] - 0.7914 * x[5] / x[3] - 0.2822 / x[3] - 0.6152 * x[3] / x[2] - 0.9569 * x[3] / x[1] - 0.4179 * x[3] / x[
                            0] + 0.3952 / (x[0] * x[5]) + 0.5181 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_14(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3886 * x[0] + 0.3595 * x[0] / x[3] + 0.8805 * x[1] / x[3] - 0.4494 * x[2] * x[4] + 0.7009 * x[3] / x[
            5] + 0.0672 * x[4] + 0.7899 * x[4] / x[5] - 0.5615 * x[5] + 0.1185 + 0.5342 / x[3] - 0.8086 * x[5] / x[2] - 0.4554 / x[
                            2] - 0.0836 / x[1] + 0.0382 * x[2] / x[0] + 0.7216 * x[4] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_31(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2946 * x[0] + 0.6345 * x[0] / x[1] - 0.1076 * x[1] / x[4] - 0.6171 * x[2] / x[5] + 0.8928 * x[2] / x[
            4] + 0.0246 * x[4] - 0.0442 * x[5] - 0.6927 - 0.6371 * x[5] / x[4] + 0.9877 / x[3] - 0.5869 / (x[3] * x[4]) - 0.2782 / x[
                            2] - 0.8855 / x[1] - 0.0441 / (x[1] * x[2]) + 0.3877 * x[5] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_48(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0756 * x[0] * x[2] + 0.2378 * x[0] - 0.5064 * x[1] * x[3] + 0.5451 * x[1] - 0.3267 * x[2] - 0.0254 * x[2] / x[
            4] + 0.5541 * x[4] + 0.8655 * x[5] + 0.4731 + 0.4405 * x[5] / x[3] + 0.363 / x[3] + 0.2509 / (x[3] * x[4]) + 0.2275 / (
                                x[2] * x[3]) - 0.2076 / (x[0] * x[4]) - 0.5052 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt68_prog_41(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0214 * x[1] - 0.8823 * x[2] * x[4] - 0.8982 * x[2] - 0.4002 * x[2] / x[5] + 0.2129 * x[3] * x[4] - 0.6205 * x[
            3] - 0.6608 * x[5] - 0.8974 - 0.2915 * x[5] / x[4] - 0.3379 / x[4] - 0.9773 / (x[1] * x[2]) + 0.0361 * x[1] / x[0] - 0.6146 * x[
                            4] / x[0] - 0.4212 / x[0] + 0.0369 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_7(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3686 * x[0] * x[1] + 0.1329 * x[0] * x[3] - 0.7423 * x[1] * x[5] - 0.7669 * x[2] - 0.6049 * x[3] + 0.4539 * x[3] / \
                        x[4] + 0.3276 * x[4] * x[5] - 0.7098 - 0.9163 / x[5] - 0.111 / x[4] - 0.2208 * x[5] / x[3] - 0.6792 / (
                                x[2] * x[4]) - 0.6507 * x[2] / x[1] - 0.881 / x[1] + 0.7974 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_37(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9554 * x[0] * x[3] - 0.2957 * x[0] + 0.1194 * x[1] / x[3] - 0.071 * x[2] * x[3] - 0.5624 * x[2] * x[4] - 0.7485 * \
                        x[2] * x[5] + 0.1235 * x[2] - 0.6799 * x[3] * x[4] - 0.1845 * x[4] - 0.2261 - 0.1389 / x[5] + 0.3779 / x[
                            3] + 0.3025 * x[2] / x[1] - 0.3913 / x[1] + 0.2587 / (x[0] * x[4])


@register_eq_class
class inv_nv6_nt68_prog_15(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2324 * x[0] - 0.3663 * x[0] / x[1] - 0.4602 * x[1] * x[3] + 0.1665 * x[2] * x[5] + 0.1915 * x[3] * x[5] + 0.6014 * \
                        x[4] - 0.7737 * x[5] - 0.5044 - 0.3862 / x[3] - 0.205 * x[3] / x[2] + 0.6856 * x[4] / x[2] - 0.4445 / x[
                            2] - 0.0798 * x[5] / x[1] - 0.1516 / x[1] + 0.8433 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_23(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4929 * x[0] * x[1] - 0.9613 * x[0] / x[5] - 0.6659 * x[1] / x[4] + 0.1361 * x[2] + 0.2677 * x[2] / x[5] + 0.8777 * \
                        x[2] / x[4] - 0.6145 * x[3] + 0.9051 * x[4] + 0.137 * x[5] + 0.7925 - 0.3008 * x[4] / x[3] - 0.747 * x[2] / x[
                            1] + 0.4838 / x[1] + 0.6525 / x[0] - 0.0343 / (x[0] * x[4])


@register_eq_class
class inv_nv6_nt68_prog_30(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5245 * x[0] / x[5] - 0.2673 * x[1] - 0.8841 * x[2] * x[3] + 0.7714 * x[2] * x[4] + 0.3496 * x[2] * x[5] + 0.4112 * \
                        x[2] + 0.0143 * x[3] / x[5] + 0.0794 * x[3] / x[4] + 0.8989 * x[4] + 0.4622 + 0.1318 / x[5] - 0.3361 / x[
                            3] - 0.2378 * x[4] / x[1] + 0.061 / (x[1] * x[2]) + 0.5126 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_28(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3697 * x[0] + 0.3774 * x[1] * x[5] + 0.3574 * x[2] + 0.8603 * x[2] / x[3] + 0.8958 * x[4] + 0.35 * x[
            5] - 0.5863 + 0.6178 / x[3] + 0.7927 / (x[3] * x[5]) + 0.3349 / (x[3] * x[4]) - 0.0392 * x[4] / x[2] + 0.7869 / x[
                            1] - 0.2073 / (x[1] * x[3]) + 0.8135 / (x[1] * x[2]) - 0.4707 * x[2] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_17(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8933 * x[0] - 0.9516 * x[0] / x[2] - 0.1704 * x[1] * x[3] + 0.2738 * x[1] - 0.7635 * x[1] / x[2] - 0.9382 * x[
            2] + 0.3424 * x[2] / x[5] - 0.4663 * x[3] - 0.9229 + 0.4027 / x[5] + 0.1277 / x[4] + 0.1979 * x[4] / x[3] - 0.009 / (
                                x[1] * x[4]) - 0.066 * x[1] / x[0] - 0.1056 / (x[0] * x[4])


@register_eq_class
class inv_nv6_nt68_prog_43(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9985 * x[0] * x[3] + 0.7329 * x[0] / x[5] - 0.3433 * x[0] / x[2] - 0.2305 * x[1] * x[4] + 0.6011 * x[
            1] - 0.3229 * x[2] * x[3] + 0.5926 * x[3] + 0.025 * x[4] - 0.9049 - 0.2081 / x[5] + 0.7054 / (x[3] * x[5]) + 0.8084 / (
                                x[3] * x[4]) - 0.6172 / x[2] - 0.0159 * x[5] / x[1] + 0.1595 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_2(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8325 * x[0] - 0.1762 * x[2] * x[3] + 0.2646 * x[2] - 0.707 * x[3] + 0.1382 * x[4] / x[5] + 0.1124 + 0.5501 / x[
            5] - 0.164 / x[4] - 0.6925 / (x[2] * x[5]) + 0.7592 * x[4] / x[1] - 0.3616 * x[5] / x[1] + 0.4476 / x[1] + 0.571 / (
                                x[1] * x[3]) + 0.7891 / (x[1] * x[2]) + 0.7373 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_4(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1324 * x[0] * x[3] - 0.7112 * x[0] / x[4] + 0.5471 * x[2] - 0.626 * x[2] / x[5] - 0.3535 * x[3] + 0.6347 * x[3] / \
                        x[4] - 0.8756 * x[4] + 0.167 * x[5] + 0.7206 - 0.3185 * x[5] / x[3] + 0.373 / x[1] - 0.1351 / (
                                x[1] * x[4]) + 0.5876 / (x[1] * x[2]) + 0.5943 * x[1] / x[0] + 0.0484 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_45(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0648 * x[0] / x[3] + 0.2487 * x[1] * x[4] + 0.2337 * x[1] + 0.736 * x[1] / x[5] - 0.0365 * x[2] / x[3] + 0.2695 * \
                        x[3] + 0.8803 * x[4] - 0.2828 * x[4] / x[5] + 0.7224 * x[5] + 0.9157 + 0.9218 / x[2] + 0.5066 / (
                                x[2] * x[5]) - 0.1137 * x[2] / x[1] - 0.989 * x[1] / x[0] - 0.3904 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_49(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6598 * x[0] + 0.8464 * x[0] / x[3] + 0.7959 * x[1] / x[3] + 0.3035 * x[2] * x[5] + 0.6126 * x[3] * x[5] - 0.786 * \
                        x[4] * x[5] + 0.7044 * x[5] + 0.3156 + 0.0765 / x[4] + 0.4442 / x[3] - 0.825 / x[2] + 0.0949 / x[1] - 0.4411 * x[
                            2] / x[0] + 0.7601 * x[5] / x[0] - 0.9314 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt68_prog_11(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7531 * x[0] * x[5] - 0.1158 * x[1] * x[5] - 0.3009 * x[2] + 0.0811 * x[2] / x[4] - 0.4907 * x[2] / x[
            3] + 0.6243 * x[3] - 0.0509 * x[3] / x[5] + 0.9176 - 0.4187 / x[5] - 0.6375 / x[4] + 0.4837 / (x[3] * x[4]) - 0.672 / x[
                            1] + 0.9417 / x[0] + 0.3699 / (x[0] * x[3]) - 0.8724 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt68_prog_10(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0507 * x[1] - 0.2063 * x[1] / x[2] + 0.1752 * x[2] * x[5] - 0.0582 * x[3] + 0.18 * x[4] - 0.7553 + 0.6822 / x[
            5] + 0.0042 * x[5] / x[4] - 0.9351 / (x[3] * x[5]) + 0.7428 * x[3] / x[2] - 0.1255 / x[2] + 0.6817 / (x[1] * x[5]) + 0.6042 / x[
                            0] - 0.0907 / (x[0] * x[5]) + 0.2061 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt68_prog_1(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4031 * x[0] * x[5] - 0.951 * x[1] + 0.6184 * x[1] / x[5] + 0.1349 * x[2] * x[5] + 0.9977 * x[3] + 0.8746 * x[3] / \
                        x[5] - 0.6516 - 0.7905 / x[5] - 0.5703 / x[4] + 0.38 * x[3] / x[2] - 0.3547 / x[2] + 0.7279 * x[2] / x[1] - 0.8155 * \
                        x[4] / x[1] - 0.6742 / x[0] - 0.1608 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_40(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9253 * x[0] - 0.4133 * x[0] / x[4] + 0.3584 * x[1] + 0.3329 * x[4] / x[5] + 0.1146 * x[5] - 0.9667 + 0.9129 / x[
            4] - 0.5583 / x[3] + 0.173 * x[4] / x[2] + 0.6482 / x[2] + 0.8514 * x[4] / x[1] - 0.284 * x[5] / x[1] + 0.2013 / (
                                x[1] * x[3]) - 0.8637 * x[1] / x[0] + 0.052 * x[3] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_29(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9959 * x[1] - 0.7347 * x[2] * x[5] + 0.808 * x[2] + 0.6805 * x[2] / x[3] + 0.1613 * x[4] * x[5] + 0.917 * x[
            4] - 0.1249 - 0.2528 / x[5] - 0.7872 * x[4] / x[3] - 0.37 / x[3] - 0.3169 / (x[1] * x[2]) - 0.2401 * x[3] / x[0] + 0.5312 * x[
                            4] / x[0] - 0.3974 * x[5] / x[0] - 0.3239 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_22(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9098 * x[0] - 0.3303 * x[0] / x[2] + 0.7598 * x[1] * x[3] + 0.1762 * x[1] - 0.4011 * x[2] + 0.2772 * x[3] / x[
            5] + 0.2525 * x[3] / x[4] - 0.1545 * x[4] + 0.5256 * x[5] - 0.7117 - 0.2112 / x[3] + 0.3758 / (x[2] * x[4]) + 0.9678 * x[2] / x[
                            1] + 0.3476 * x[5] / x[1] + 0.7675 / (x[1] * x[4])


@register_eq_class
class inv_nv6_nt68_prog_27(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8629 * x[0] * x[4] + 0.796 * x[0] - 0.7721 * x[0] / x[5] - 0.5538 * x[1] * x[5] - 0.1942 * x[3] - 0.3315 * x[3] / \
                        x[4] - 0.2139 * x[4] + 0.1071 + 0.8129 / x[5] + 0.5902 / x[2] + 0.688 * x[3] / x[1] - 0.6229 / x[1] + 0.3004 / (
                                x[1] * x[2]) + 0.2691 * x[1] / x[0] - 0.7823 * x[3] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_34(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3593 * x[0] * x[5] + 0.2698 * x[0] / x[2] - 0.1152 * x[1] + 0.6464 * x[1] / x[2] + 0.0995 * x[2] * x[
            4] + 0.4785 * x[3] - 0.362 - 0.1442 / x[5] + 0.2403 / x[4] + 0.6029 / (x[3] * x[4]) + 0.5566 * x[5] / x[2] - 0.5163 / x[
                            2] - 0.5207 * x[3] / x[0] + 0.1501 * x[4] / x[0] + 0.1794 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_16(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.32 * x[0] - 0.9812 * x[0] / x[4] - 0.2683 * x[0] / x[2] - 0.5624 * x[2] - 0.2846 * x[3] * x[4] - 0.8503 * x[
            3] - 0.5269 * x[3] / x[5] + 0.8651 * x[4] + 0.9094 * x[5] - 0.2113 - 0.2463 * x[4] / x[2] - 0.0782 / (x[2] * x[3]) - 0.6168 / x[
                            1] + 0.9462 / (x[1] * x[5]) - 0.1817 / (x[0] * x[5])


@register_eq_class
class inv_nv6_nt68_prog_13(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1189 * x[0] * x[2] + 0.0564 * x[0] / x[4] + 0.972 * x[0] / x[3] + 0.2569 * x[0] / x[1] + 0.9679 * x[1] * x[
            2] - 0.5399 * x[1] + 0.5961 * x[2] / x[5] - 0.412 * x[3] * x[5] - 0.857 * x[3] - 0.9642 * x[3] / x[4] - 0.0534 * x[4] - 0.612 * \
                        x[5] - 0.7602 - 0.583 / x[2] - 0.5396 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_47(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1442 * x[0] - 0.3955 * x[0] / x[4] - 0.1675 * x[0] / x[1] - 0.7089 * x[1] / x[2] - 0.0184 * x[2] * x[4] - 0.4797 * \
                        x[3] + 0.3361 * x[4] + 0.8609 - 0.5124 / x[5] - 0.0509 * x[5] / x[3] - 0.1093 / x[2] - 0.7011 / x[1] - 0.5541 / (
                                x[1] * x[3]) + 0.9139 * x[5] / x[0] + 0.8363 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_36(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4966 * x[0] * x[3] - 0.3445 * x[0] * x[4] + 0.5163 * x[0] + 0.972 * x[1] * x[3] + 0.1994 * x[2] / x[5] + 0.9732 * \
                        x[4] - 0.2866 * x[5] + 0.8634 - 0.9712 / x[3] + 0.7841 / (x[3] * x[5]) + 0.7728 / x[2] - 0.8474 / x[1] - 0.2377 / (
                                x[1] * x[4]) + 0.0744 * x[5] / x[0] - 0.0213 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_44(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8763 * x[0] / x[5] - 0.4263 * x[0] / x[3] - 0.4855 * x[1] + 0.3649 * x[3] - 0.6759 * x[4] / x[
            5] - 0.0181 - 0.3373 / x[5] + 0.521 / x[4] - 0.3619 * x[4] / x[3] - 0.4606 * x[4] / x[2] + 0.4252 / x[2] - 0.3888 / (
                                x[2] * x[3]) - 0.5188 * x[2] / x[0] + 0.3252 * x[4] / x[0] + 0.7059 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_6(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7954 * x[1] * x[5] - 0.8306 * x[1] / x[3] - 0.379 * x[3] * x[4] - 0.9493 * x[3] + 0.7942 * x[3] / x[5] - 0.6964 * \
                        x[4] - 0.2211 * x[5] - 0.9758 + 0.5503 * x[5] / x[4] + 0.1708 / x[2] + 0.1447 / (x[2] * x[5]) - 0.0429 / x[
                            1] + 0.8073 * x[1] / x[0] - 0.8567 * x[4] / x[0] + 0.86 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_18(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6076 * x[0] / x[3] + 0.599 * x[1] * x[2] + 0.2017 * x[2] * x[4] + 0.6812 * x[2] * x[5] + 0.6589 * x[2] + 0.9037 * \
                        x[3] / x[5] - 0.2276 * x[4] + 0.9879 * x[5] + 0.2039 + 0.9524 / x[3] + 0.3783 / (x[2] * x[3]) + 0.371 * x[5] / x[
                            1] - 0.7887 / x[1] + 0.4615 / x[0] + 0.4626 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_3(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1449 * x[0] * x[5] - 0.6044 * x[0] / x[4] + 0.5804 * x[1] * x[4] - 0.4166 * x[1] + 0.7844 * x[1] / x[2] - 0.235 * \
                        x[2] * x[5] + 0.5702 * x[2] + 0.5918 * x[3] + 0.4172 + 0.7677 / x[5] - 0.4394 / x[4] - 0.1996 * x[4] / x[
                            3] + 0.1375 * x[4] / x[2] + 0.534 / x[0] - 0.8248 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt68_prog_24(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6623 * x[0] - 0.0461 * x[1] * x[2] - 0.4849 * x[2] / x[4] + 0.9139 * x[2] / x[3] - 0.957 * x[3] / x[5] + 0.6042 * \
                        x[5] - 0.9361 - 0.2181 / x[4] - 0.8778 / x[3] + 0.166 / x[2] - 0.8631 * x[3] / x[1] + 0.0287 * x[5] / x[
                            1] - 0.2466 / x[1] + 0.0929 * x[2] / x[0] - 0.3135 * x[5] / x[0]


@register_eq_class
class inv_nv6_nt68_prog_12(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0661 * x[0] - 0.6351 * x[3] - 0.802 * x[5] - 0.6169 - 0.5008 / x[4] - 0.0473 * x[3] / x[2] - 0.2931 / x[
            2] + 0.0799 / (x[2] * x[5]) - 0.3977 * x[4] / x[1] + 0.1717 / x[1] + 0.621 / (x[1] * x[5]) + 0.5295 * x[1] / x[0] - 0.9247 * x[
                            2] / x[0] + 0.6257 * x[4] / x[0] - 0.132 / (x[0] * x[5])


@register_eq_class
class inv_nv6_nt68_prog_25(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7376 * x[0] * x[4] + 0.258 * x[0] / x[5] - 0.499 * x[0] / x[1] - 0.7835 * x[1] + 0.483 * x[4] + 0.9077 * x[
            5] + 0.8214 + 0.7819 / x[3] + 0.1462 / (x[3] * x[5]) - 0.2118 / x[2] - 0.6188 / (x[2] * x[5]) + 0.2911 * x[2] / x[1] - 0.7969 * \
                        x[4] / x[1] - 0.984 / (x[1] * x[5]) + 0.0706 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_21(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6589 * x[0] * x[1] - 0.6115 * x[0] / x[3] + 0.9601 * x[1] / x[3] + 0.3898 * x[2] * x[5] - 0.5501 * x[3] / x[
            4] + 0.1211 * x[4] - 0.757 * x[4] / x[5] + 0.4769 - 0.7132 / x[5] + 0.6291 / x[3] + 0.1304 * x[4] / x[2] + 0.6684 / x[
                            2] - 0.8482 * x[2] / x[1] + 0.6642 / x[1] - 0.8737 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_26(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3627 * x[0] - 0.0144 * x[0] / x[4] + 0.0266 * x[1] / x[4] + 0.8313 * x[1] / x[3] + 0.9395 * x[3] / x[5] - 0.921 * \
                        x[4] - 0.3431 * x[5] - 0.0542 - 0.4744 / x[3] - 0.7001 * x[5] / x[2] - 0.8668 / x[2] + 0.6416 * x[5] / x[
                            1] - 0.589 / x[1] - 0.7175 / (x[0] * x[5]) - 0.699 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_39(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8381 * x[0] * x[5] - 0.8237 * x[0] - 0.6372 * x[0] / x[2] + 0.9953 * x[1] * x[2] + 0.7981 * x[4] - 0.3504 * x[
            5] - 0.9086 - 0.9554 / x[3] - 0.2821 / x[2] + 0.8493 / (x[2] * x[5]) - 0.1782 / (x[2] * x[4]) - 0.1055 / (
                                x[2] * x[3]) - 0.1261 / x[1] - 0.9477 / (x[1] * x[4]) - 0.1585 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt68_prog_19(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0168 * x[0] * x[3] - 0.1144 * x[1] / x[2] + 0.7272 * x[2] - 0.5781 * x[2] / x[5] - 0.7532 * x[2] / x[
            4] - 0.3433 * x[3] * x[4] + 0.7652 * x[4] + 0.0554 * x[4] / x[5] - 0.1906 * x[5] - 0.8918 + 0.536 / x[3] - 0.5103 * x[4] / x[
                            1] + 0.9879 / x[1] - 0.2898 / (x[1] * x[5]) - 0.6359 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_38(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3338 * x[1] * x[3] + 0.2369 * x[2] + 0.6243 * x[3] + 0.1634 * x[3] / x[4] + 0.403 * x[4] - 0.618 * x[
            5] + 0.5055 + 0.3096 / (x[3] * x[5]) + 0.1545 * x[5] / x[2] - 0.9689 / (x[2] * x[4]) - 0.8602 * x[5] / x[1] + 0.8419 / x[
                            1] + 0.3444 / x[0] - 0.9837 / (x[0] * x[5]) + 0.8571 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt68_prog_9(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7464 * x[0] + 0.02 * x[2] + 0.3799 * x[2] / x[5] - 0.1001 * x[2] / x[4] - 0.7595 * x[2] / x[3] - 0.0307 * x[3] * \
                        x[4] + 0.2405 * x[4] + 0.7376 * x[5] - 0.0105 - 0.8397 / x[3] + 0.457 * x[5] / x[1] - 0.8899 / x[1] + 0.1973 / (
                                x[1] * x[2]) - 0.5558 * x[5] / x[0] + 0.581 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt68_prog_32(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6752 * x[0] * x[5] + 0.4409 * x[0] / x[2] + 0.5015 * x[1] / x[2] - 0.3736 * x[2] * x[4] + 0.8455 * x[2] - 0.75 * \
                        x[2] / x[3] + 0.167 * x[4] * x[5] - 0.0496 * x[4] + 0.6082 * x[5] + 0.0203 + 0.6569 * x[5] / x[3] - 0.0999 / x[
                            3] - 0.7329 / (x[3] * x[4]) + 0.0612 / x[1] + 0.9375 / x[0]


@register_eq_class
class inv_nv6_nt68_prog_5(KnownEquation):
    _eq_name = 'inv_nv6_nt68_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5241 * x[0] * x[4] + 0.0756 * x[0] + 0.1971 * x[0] / x[2] - 0.8796 * x[1] / x[3] + 0.1362 * x[2] * x[
            4] - 0.3959 * x[3] / x[4] + 0.9541 * x[4] - 0.564 * x[5] + 0.2712 - 0.0195 / x[3] + 0.9619 * x[3] / x[2] - 0.4919 / x[
                            2] - 0.0024 / x[1] - 0.3969 / (x[1] * x[4]) - 0.4275 / (x[0] * x[5])


@register_eq_class
class sincos_nv3_nt22_prog_46(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_46'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.3721 * x[0] * x[1] + 0.8273 * x[1] + 0.8787 * x[2] + 0.9742 * sympy.sin(x[2]) * sympy.cos(x[1]) - 0.4598


@register_eq_class
class sincos_nv3_nt22_prog_0(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_0'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6098 * x[1] * sympy.sin(x[0]) + 0.66 * x[2] - 0.5542 * sympy.sin(x[2]) * sympy.cos(x[1]) - 0.5932 * sympy.cos(
            x[0]) + 0.1835


@register_eq_class
class sincos_nv3_nt22_prog_35(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_35'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3378 * x[0] * sympy.cos(x[1]) - 0.221 * x[2] * sympy.cos(x[1]) - 0.5689 * x[2] - 0.3145 * sympy.cos(x[1]) - 0.9189


@register_eq_class
class sincos_nv3_nt22_prog_8(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_8'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.4681 * x[0] + 0.4856 * x[1] * x[2] - 0.8895 * x[2] * sympy.sin(x[0]) - 0.6741 * sympy.cos(x[1]) - 0.8204


@register_eq_class
class sincos_nv3_nt22_prog_42(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_42'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7703 * x[0] + 0.0163 * x[1] * x[2] - 0.6396 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.1059 * sympy.sin(
            x[2]) - 0.6208


@register_eq_class
class sincos_nv3_nt22_prog_33(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_33'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.963 * x[0] * x[1] + 0.8657 * x[1] * x[2] - 0.6227 * x[1] - 0.2414 * x[2] - 0.7007


@register_eq_class
class sincos_nv3_nt22_prog_20(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_20'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.428 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.4468 * sympy.sin(x[0]) + 0.7476 * sympy.sin(x[2]) * sympy.cos(
            x[1]) + 0.4228 * sympy.cos(x[1]) + 0.3848


@register_eq_class
class sincos_nv3_nt22_prog_14(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_14'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.4846 * x[0] * x[1] + 0.5464 * x[0] * x[2] - 0.8801 * x[2] + 0.433 * sympy.cos(x[0]) + 0.3454


@register_eq_class
class sincos_nv3_nt22_prog_31(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_31'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8317 * x[1] * x[2] + 0.6996 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.4712 * sympy.sin(x[0]) - 0.9464 * sympy.sin(
            x[2]) - 0.8792


@register_eq_class
class sincos_nv3_nt22_prog_48(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_48'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9068 * x[0] - 0.1009 * x[1] * sympy.cos(x[2]) + 0.5344 * x[2] + 0.4388 * sympy.cos(x[0]) * sympy.cos(
            x[2]) - 0.9489


@register_eq_class
class sincos_nv3_nt22_prog_41(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_41'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6591 * x[0] * sympy.cos(x[1]) + 0.432 * x[0] - 0.1235 * x[1] * sympy.sin(x[2]) - 0.4621 * x[1] - 0.223


@register_eq_class
class sincos_nv3_nt22_prog_7(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_7'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7621 * x[0] * x[1] - 0.5348 * x[1] - 0.8292 * x[2] + 0.4458 * sympy.sin(x[2]) * sympy.cos(x[1]) + 0.2351


@register_eq_class
class sincos_nv3_nt22_prog_37(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_37'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.0936 * x[0] * sympy.cos(x[1]) - 0.881 * x[1] * sympy.cos(x[2]) + 0.4227 * sympy.sin(x[1]) - 0.2872 * sympy.sin(
            x[2]) - 0.8627


@register_eq_class
class sincos_nv3_nt22_prog_15(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_15'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6025 * x[0] * sympy.sin(x[2]) - 0.5496 * x[0] * sympy.cos(x[1]) + 0.4535 * x[1] + 0.5149 * sympy.cos(
            x[0]) - 0.2065


@register_eq_class
class sincos_nv3_nt22_prog_23(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_23'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.093 * x[0] * x[2] - 0.7615 * x[1] * x[2] - 0.0183 * sympy.sin(x[1]) - 0.9447 * sympy.cos(x[0]) - 0.8627


@register_eq_class
class sincos_nv3_nt22_prog_30(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_30'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7637 * x[1] * x[2] - 0.8318 * x[1] * sympy.sin(x[0]) - 0.5168 * sympy.sin(x[0]) + 0.465 * sympy.sin(x[1]) + 0.5632


@register_eq_class
class sincos_nv3_nt22_prog_28(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_28'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0503 * x[0] - 0.772 * x[1] * sympy.sin(x[0]) - 0.4019 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.1934 * sympy.cos(
            x[1]) + 0.8389


@register_eq_class
class sincos_nv3_nt22_prog_17(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_17'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2717 * x[0] * x[2] - 0.4907 * x[1] * x[2] - 0.7372 * sympy.sin(x[0]) + 0.3959 * sympy.sin(x[2]) - 0.063


@register_eq_class
class sincos_nv3_nt22_prog_43(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_43'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.187 * x[0] * x[2] - 0.4271 * x[0] * sympy.cos(x[1]) + 0.7882 * x[0] + 0.454 * sympy.sin(x[1]) + 0.2095


@register_eq_class
class sincos_nv3_nt22_prog_2(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_2'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0951 * x[0] * x[2] + 0.0127 * x[2] * sympy.sin(x[1]) - 0.5768 * x[2] - 0.2143 * sympy.cos(x[0]) - 0.6254


@register_eq_class
class sincos_nv3_nt22_prog_4(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_4'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7774 * x[0] - 0.5646 * x[1] * sympy.sin(x[0]) - 0.8781 * x[2] + 0.7823 * sympy.sin(x[2]) * sympy.cos(
            x[1]) + 0.4612


@register_eq_class
class sincos_nv3_nt22_prog_45(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_45'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2523 * x[0] * x[1] - 0.6748 * x[0] - 0.5454 * sympy.sin(x[1]) + 0.7667 * sympy.cos(x[1]) * sympy.cos(
            x[2]) + 0.6172


@register_eq_class
class sincos_nv3_nt22_prog_49(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_49'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.1133 * x[1] * x[2] + 0.5056 * x[1] * sympy.cos(x[0]) + 0.4184 * x[1] + 0.8798 * x[2] - 0.6481


@register_eq_class
class sincos_nv3_nt22_prog_11(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_11'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0562 * x[0] - 0.5496 * x[1] * x[2] - 0.9238 * x[1] + 0.8805 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.3597


@register_eq_class
class sincos_nv3_nt22_prog_10(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_10'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.2249 * x[0] * x[2] - 0.6969 * x[0] * sympy.cos(x[1]) + 0.6579 * x[0] - 0.435 * sympy.sin(x[2]) - 0.0474


@register_eq_class
class sincos_nv3_nt22_prog_1(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_1'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.9272 * x[0] * sympy.cos(x[1]) - 0.8311 * x[0] - 0.7951 * x[1] + 0.5114 * sympy.cos(x[1]) * sympy.cos(
            x[2]) - 0.8436


@register_eq_class
class sincos_nv3_nt22_prog_40(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_40'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3959 * x[0] - 0.1851 * x[1] * sympy.sin(x[2]) + 0.767 * x[1] + 0.1021 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.7059


@register_eq_class
class sincos_nv3_nt22_prog_29(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_29'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3211 * x[1] * x[2] - 0.3687 * x[2] + 0.7306 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.8431 * sympy.sin(
            x[1]) + 0.4654


@register_eq_class
class sincos_nv3_nt22_prog_22(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_22'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.4617 * x[0] * x[1] + 0.0336 * x[2] * sympy.sin(x[0]) - 0.989 * sympy.sin(x[1]) + 0.903 * sympy.sin(x[2]) + 0.3172


@register_eq_class
class sincos_nv3_nt22_prog_27(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_27'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7937 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.829 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.8686 * sympy.cos(
            x[0]) + 0.4996 * sympy.cos(x[2]) + 0.0415


@register_eq_class
class sincos_nv3_nt22_prog_34(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_34'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.2254 * x[0] * x[1] + 0.79 * x[0] * sympy.cos(x[2]) - 0.7763 * x[0] + 0.433 * x[2] - 0.8635


@register_eq_class
class sincos_nv3_nt22_prog_16(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_16'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.51 * x[1] * sympy.cos(x[0]) + 0.0205 * x[1] - 0.0062 * x[2] * sympy.cos(x[1]) - 0.265 * sympy.sin(x[2]) + 0.0291


@register_eq_class
class sincos_nv3_nt22_prog_13(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_13'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6207 * x[0] - 0.0461 * x[1] * sympy.sin(x[0]) + 0.5772 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.6804 * sympy.cos(
            x[1]) + 0.7425


@register_eq_class
class sincos_nv3_nt22_prog_47(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_47'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.9665 * x[1] - 0.6733 * x[2] * sympy.sin(x[1]) - 0.6714 * x[2] + 0.9293 * sympy.cos(x[0]) * sympy.cos(
            x[1]) - 0.8833


@register_eq_class
class sincos_nv3_nt22_prog_36(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_36'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7929 * x[0] * sympy.cos(x[1]) + 0.2097 * x[1] * sympy.sin(x[2]) + 0.2733 * x[2] + 0.1863 * sympy.sin(
            x[1]) + 0.805


@register_eq_class
class sincos_nv3_nt22_prog_44(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_44'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6891 * x[2] * sympy.sin(x[1]) - 0.2068 * sympy.sin(x[1]) + 0.6579 * sympy.sin(x[2]) + 0.2658 * sympy.cos(
            x[0]) * sympy.cos(x[2]) - 0.5964


@register_eq_class
class sincos_nv3_nt22_prog_6(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_6'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6162 * x[0] * x[1] - 0.8577 * x[2] * sympy.sin(x[0]) - 0.8295 * x[2] + 0.3185 * sympy.sin(x[1]) - 0.0956


@register_eq_class
class sincos_nv3_nt22_prog_18(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_18'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6197 * x[0] + 0.6726 * x[1] * x[2] + 0.9922 * x[1] * sympy.cos(x[0]) - 0.3569 * sympy.cos(x[2]) - 0.2766


@register_eq_class
class sincos_nv3_nt22_prog_3(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_3'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.3162 * x[0] * x[2] - 0.6406 * x[1] * x[2] - 0.802 * x[1] + 0.3979 * sympy.cos(x[0]) + 0.0068


@register_eq_class
class sincos_nv3_nt22_prog_24(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_24'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5384 * x[1] * x[2] + 0.8192 * x[2] - 0.1976 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.0087 * sympy.sin(
            x[1]) + 0.5779


@register_eq_class
class sincos_nv3_nt22_prog_12(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_12'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2256 * x[1] * sympy.sin(x[0]) - 0.1766 * x[1] - 0.738 * x[2] - 0.6864 * sympy.cos(x[1]) * sympy.cos(
            x[2]) - 0.1109


@register_eq_class
class sincos_nv3_nt22_prog_25(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_25'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7365 * x[0] - 0.8659 * x[2] * sympy.cos(x[1]) - 0.1495 * x[2] + 0.4855 * sympy.sin(x[0]) * sympy.cos(
            x[1]) - 0.8791


@register_eq_class
class sincos_nv3_nt22_prog_21(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_21'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.4148 * x[1] * x[2] - 0.3903 * x[2] * sympy.cos(x[0]) + 0.1409 * sympy.cos(x[0]) - 0.7498 * sympy.cos(
            x[2]) + 0.8734


@register_eq_class
class sincos_nv3_nt22_prog_26(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_26'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9266 * x[0] * sympy.sin(x[1]) + 0.7378 * x[0] * sympy.sin(x[2]) + 0.0345 * sympy.sin(x[0]) + 0.097 * sympy.sin(
            x[2]) - 0.9298


@register_eq_class
class sincos_nv3_nt22_prog_39(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_39'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6229 * x[1] + 0.9731 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.6387 * sympy.sin(x[1]) * sympy.cos(
            x[2]) - 0.6516 * sympy.cos(x[2]) - 0.4348


@register_eq_class
class sincos_nv3_nt22_prog_19(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_19'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5409 * x[0] * sympy.cos(x[2]) - 0.9215 * x[2] - 0.9796 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.6415 * sympy.sin(
            x[1]) - 0.7867


@register_eq_class
class sincos_nv3_nt22_prog_38(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_38'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.4397 * x[0] * x[1] + 0.9576 * x[1] + 0.7222 * sympy.sin(x[2]) * sympy.cos(x[1]) + 0.4394 * sympy.sin(x[2]) + 0.048


@register_eq_class
class sincos_nv3_nt22_prog_9(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_9'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.4634 * x[0] * sympy.sin(x[2]) - 0.7682 * x[2] - 0.4991 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.1834 * sympy.sin(
            x[1]) + 0.3475


@register_eq_class
class sincos_nv3_nt22_prog_32(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_32'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.971 * x[2] * sympy.sin(x[1]) - 0.0681 * x[2] - 0.5666 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.1852 * sympy.cos(
            x[0]) + 0.9738


@register_eq_class
class sincos_nv3_nt22_prog_5(KnownEquation):
    _eq_name = 'sincos_nv3_nt22_prog_5'
    _function_set = ['add', 'sub', 'mul', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0999 * x[0] * sympy.sin(x[1]) - 0.4304 * x[0] * sympy.cos(x[2]) + 0.5153 * x[1] - 0.6365 * sympy.cos(
            x[0]) - 0.1823


@register_eq_class
class inv_nv2_nt11_prog_46(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.314 * x[1] + 0.1198 + 0.3448 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_0(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2601 * x[1] + 0.1308 + 0.7592 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_35(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8336 - 0.7592 / x[1] + 0.0437 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_8(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1929 + 0.1776 * x[1] / x[0] + 0.0639 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_42(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0882 + 0.3893 * x[1] / x[0] + 0.9648 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_33(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2831 * x[0] / x[1] - 0.8468 - 0.1914 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_20(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.4598 * x[0] * x[1] - 0.3877 * x[1] - 0.7395


@register_eq_class
class inv_nv2_nt11_prog_14(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8289 * x[0] * x[1] + 0.8285 + 0.9109 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_31(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.4156 - 0.7314 / x[0] - 0.7943 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_48(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.0674 * x[0] * x[1] + 0.9305 + 0.6926 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_41(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.9187 * x[0] * x[1] + 0.1593 - 0.5941 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_7(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4967 - 0.6824 / x[1] - 0.7346 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_37(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8385 - 0.8348 / x[1] - 0.4444 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_15(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8005 * x[0] / x[1] + 0.7949 + 0.9788 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_23(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7152 * x[1] + 0.0617 - 0.3753 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_30(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.69 - 0.6649 * x[1] / x[0] - 0.4537 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_28(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1678 * x[0] / x[1] - 0.8587 + 0.0514 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_17(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.3603 * x[0] * x[1] - 0.787 + 0.9185 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_43(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8601 * x[0] / x[1] - 0.6006 * x[1] + 0.4494


@register_eq_class
class inv_nv2_nt11_prog_2(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8801 * x[0] + 0.8796 * x[0] / x[1] - 0.6178


@register_eq_class
class inv_nv2_nt11_prog_4(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8279 * x[1] + 0.9474 - 0.8815 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_45(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.9094 * x[0] + 0.2885 - 0.4975 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_49(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.3284 * x[0] * x[1] - 0.8058 * x[0] + 0.1953


@register_eq_class
class inv_nv2_nt11_prog_11(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5972 + 0.4671 / x[1] - 0.924 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_10(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.3277 * x[0] / x[1] + 0.5276 + 0.5136 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_1(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8754 * x[0] + 0.3998 * x[0] / x[1] - 0.4015


@register_eq_class
class inv_nv2_nt11_prog_40(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4522 * x[1] + 0.9977 + 0.7913 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_29(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.5015 * x[0] * x[1] - 0.8278 + 0.5491 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_22(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.3278 * x[0] / x[1] - 0.7698 * x[1] + 0.0482


@register_eq_class
class inv_nv2_nt11_prog_27(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.3214 * x[0] + 0.3282 + 0.8423 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_34(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8861 * x[1] + 0.0794 - 0.6432 * x[1] / x[0]


@register_eq_class
class inv_nv2_nt11_prog_16(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6698 * x[0] * x[1] - 0.1868 + 0.51 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_13(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.878 * x[0] / x[1] - 0.3892 - 0.389 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_47(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.9922 * x[0] / x[1] - 0.1579 * x[1] + 0.6279


@register_eq_class
class inv_nv2_nt11_prog_36(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1646 + 0.6009 / x[1] - 0.9663 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_44(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1825 * x[0] * x[1] + 0.5823 * x[1] + 0.046


@register_eq_class
class inv_nv2_nt11_prog_6(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.4199 * x[0] * x[1] - 0.4005 * x[1] - 0.2386


@register_eq_class
class inv_nv2_nt11_prog_18(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5125 * x[0] * x[1] + 0.6889 * x[0] - 0.6084


@register_eq_class
class inv_nv2_nt11_prog_3(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1938 * x[1] - 0.6887 - 0.3478 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_24(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5529 * x[0] * x[1] - 0.7265 + 0.6929 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_12(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8655 * x[0] / x[1] - 0.4646 + 0.3587 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_25(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2441 + 0.2698 * x[1] / x[0] + 0.1515 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_21(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4806 * x[0] * x[1] + 0.1686 + 0.1064 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_26(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.6349 + 0.2902 / x[0] - 0.8301 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_39(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5376 * x[0] * x[1] - 0.3187 + 0.8011 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_19(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2968 - 0.6589 * x[1] / x[0] + 0.0673 / x[0]


@register_eq_class
class inv_nv2_nt11_prog_38(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2915 - 0.7225 / x[0] + 0.1778 / (x[0] * x[1])


@register_eq_class
class inv_nv2_nt11_prog_9(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.345 * x[0] * x[1] + 0.9499 + 0.7541 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_32(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6805 * x[0] * x[1] - 0.8503 - 0.2268 / x[1]


@register_eq_class
class inv_nv2_nt11_prog_5(KnownEquation):
    _eq_name = 'inv_nv2_nt11_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.0323 * x[0] / x[1] - 0.5534 + 0.4415 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.6652 * x[0] / x[3] - 0.5047 * x[0] / x[1] + 0.7036 * x[1] * x[2] + 0.7598 * x[1] + 0.7504 * x[2] * x[3] - 0.778 * \
                        x[2] - 0.9726 * x[3] + 0.1232 * sympy.sin(x[0]) + 0.7531 - 0.4557 * x[3] / x[1] + 0.9631 * x[2] / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.6704 * x[0] * sympy.sin(x[3]) - 0.803 * x[0] * sympy.cos(x[2]) + 0.3626 * x[1] / x[2] - 0.4276 * x[
            2] * sympy.cos(x[3]) - 0.0087 * x[2] + 0.1943 * x[3] - 0.8471 * sympy.sin(x[3]) * sympy.cos(x[1]) - 0.1086 * sympy.cos(
            x[0]) * sympy.cos(x[1]) - 0.9234 * sympy.cos(x[1]) - 0.1656 + 0.4438 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.2821 * x[0] * x[2] + 0.1172 * x[0] * x[3] + 0.7747 * x[0] - 0.2158 * x[1] * sympy.cos(x[0]) - 0.8243 * x[
            1] - 0.3375 * x[2] * sympy.cos(x[3]) - 0.6229 * x[2] + 0.9938 * x[3] * sympy.sin(x[1]) + 0.3902 * sympy.cos(
            x[3]) - 0.7072 + 0.4826 / (x[1] * x[2])


@register_eq_class
class sincosinv_nv4_nt46_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.967 * x[0] - 0.4896 * x[0] / x[2] + 0.0513 * x[1] * x[2] - 0.7603 * x[1] / x[3] + 0.9927 * x[2] * x[3] + 0.8231 * \
                        x[2] + 0.8992 * x[3] + 0.3147 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.1108 * sympy.cos(x[0]) * sympy.cos(
            x[3]) + 0.1804 + 0.7123 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.9298 * x[0] * x[2] - 0.3551 * x[0] / x[1] + 0.9114 * x[1] * sympy.sin(x[2]) - 0.9456 * x[1] - 0.3601 * x[
            3] - 0.9586 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.1608 * sympy.sin(x[0]) + 0.4918 * sympy.sin(
            x[2]) - 0.0477 + 0.7557 * sympy.sin(x[2]) / x[3] - 0.9517 * sympy.cos(x[3]) / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.1873 * x[0] / x[2] - 0.113 * x[0] / x[1] + 0.4512 * x[1] * x[2] - 0.2437 * x[1] / x[3] - 0.7485 * x[2] * x[
            3] - 0.8706 * x[2] + 0.3916 * sympy.sin(x[1]) - 0.8457 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.9239 * sympy.cos(
            x[0]) + 0.8226 - 0.2733 / x[3]


@register_eq_class
class sincosinv_nv4_nt46_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4669 * x[0] * x[1] + 0.7169 * x[0] + 0.0922 * x[1] * sympy.sin(x[2]) - 0.9061 * x[1] * sympy.cos(x[3]) + 0.813 * \
                        x[2] + 0.9821 * x[3] - 0.0393 * sympy.sin(x[3]) * sympy.cos(x[2]) - 0.8546 - 0.5855 * sympy.sin(x[0]) / x[
                            3] - 0.0042 * sympy.cos(x[0]) / x[2] + 0.5433 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.192 * x[0] * sympy.sin(x[1]) - 0.3725 * x[0] - 0.3357 * x[1] * sympy.sin(x[3]) - 0.2745 * x[1] - 0.6084 * x[2] * \
                        x[3] + 0.8162 * x[2] * sympy.cos(x[1]) - 0.0679 * x[3] + 0.6308 * sympy.sin(x[0]) * sympy.sin(
            x[3]) - 0.2809 * sympy.cos(x[2]) - 0.5234 - 0.9143 * sympy.cos(x[0]) / x[2]


@register_eq_class
class sincosinv_nv4_nt46_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.658 * x[0] * x[1] + 0.0425 * x[0] * x[2] + 0.102 * x[0] * x[3] + 0.8848 * x[1] * x[2] - 0.1131 * x[1] * x[
            3] - 0.8721 * x[2] * x[3] - 0.7778 * sympy.sin(x[2]) - 0.0324 * sympy.cos(x[0]) - 0.8756 * sympy.cos(x[3]) + 0.5433 + 0.8928 / \
                        x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6464 * x[0] * x[1] - 0.8219 * x[0] / x[2] - 0.4688 * x[1] * x[3] + 0.6198 * sympy.sin(x[0]) * sympy.sin(
            x[3]) - 0.3408 * sympy.sin(x[0]) - 0.0064 * sympy.cos(x[3]) - 0.7134 + 0.9782 * x[3] / x[2] - 0.7937 / x[2] - 0.6944 * x[2] / x[
                            1] - 0.4949 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8961 * x[0] * sympy.sin(x[1]) + 0.7448 * x[0] * sympy.cos(x[3]) - 0.341 * x[0] + 0.9404 * x[1] * x[2] - 0.3877 * \
                        x[1] * sympy.cos(x[3]) + 0.3872 * x[2] * sympy.cos(x[0]) - 0.6938 * x[2] - 0.1502 * x[3] + 0.6384 * sympy.sin(
            x[1]) - 0.4404 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.4377


@register_eq_class
class sincosinv_nv4_nt46_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.9948 * x[1] * x[3] + 0.3947 * x[2] * sympy.sin(x[1]) + 0.9735 * x[2] + 0.3526 * x[3] * sympy.sin(x[0]) + 0.8203 * \
                        x[3] - 0.4217 * sympy.sin(x[0]) * sympy.cos(x[2]) + 0.7697 * sympy.cos(x[0]) - 0.1809 * sympy.cos(
            x[1]) + 0.8659 - 0.5202 * sympy.sin(x[2]) / x[3] - 0.5927 * x[1] / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8143 * x[0] * x[2] + 0.0535 * x[0] * sympy.sin(x[3]) + 0.5121 * x[0] * sympy.cos(x[1]) + 0.1228 * x[
            2] * sympy.cos(x[3]) + 0.8748 * x[2] + 0.6856 * x[3] * sympy.cos(x[1]) - 0.0869 * sympy.sin(x[0]) - 0.8356 * sympy.sin(
            x[1]) * sympy.cos(x[2]) - 0.4972 + 0.633 / x[3] + 0.1903 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4872 * x[0] * x[1] + 0.8406 * x[0] * x[3] + 0.8626 * x[2] * sympy.sin(x[0]) - 0.8141 * x[2] * sympy.cos(
            x[1]) - 0.6389 * x[2] - 0.1773 * x[3] - 0.4095 * sympy.cos(x[0]) - 0.1721 - 0.0743 * x[3] / x[2] - 0.9859 * sympy.cos(x[3]) / x[
                            1] - 0.5481 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7084 * x[0] * x[1] + 0.2977 * x[0] * x[2] - 0.9769 * x[0] * sympy.sin(x[3]) - 0.0986 * x[2] * x[
            3] - 0.9107 * sympy.sin(x[3]) + 0.3125 * sympy.cos(x[1]) - 0.2841 - 0.1968 * sympy.cos(x[1]) / x[3] + 0.1467 / x[2] + 0.9618 * \
                        x[2] / x[1] + 0.4975 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8954 * x[0] * x[1] - 0.9503 * x[0] - 0.1242 * x[1] * x[2] + 0.6666 * x[2] + 0.8218 * sympy.sin(x[0]) * sympy.cos(
            x[2]) - 0.0379 * sympy.sin(x[1]) + 0.5989 * sympy.sin(x[3]) * sympy.cos(x[0]) + 0.3228 * sympy.cos(
            x[3]) - 0.4124 + 0.3212 * sympy.sin(x[1]) / x[3] + 0.9003 / (x[2] * x[3])


@register_eq_class
class sincosinv_nv4_nt46_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3775 * x[0] * x[1] - 0.7296 * x[0] * x[3] + 0.3842 * x[0] - 0.724 * x[0] / x[2] + 0.2645 * x[1] * x[3] - 0.5005 * \
                        x[1] - 0.4277 * x[2] * sympy.cos(x[3]) + 0.5815 * sympy.cos(x[2]) + 0.1152 - 0.5626 / x[3] + 0.919 * sympy.cos(
            x[1]) / x[2]


@register_eq_class
class sincosinv_nv4_nt46_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3996 * x[0] * x[1] - 0.6741 * x[0] * x[3] + 0.702 * x[0] + 0.9308 * x[1] * sympy.cos(x[2]) + 0.6196 * x[
            3] * sympy.sin(x[1]) - 0.7706 * x[3] + 0.2987 * sympy.sin(x[2]) + 0.1936 * sympy.sin(x[3]) * sympy.cos(
            x[2]) + 0.1008 - 0.6954 * sympy.cos(x[0]) / x[2] - 0.9954 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.7934 * x[0] * sympy.cos(x[1]) - 0.1266 * x[0] * sympy.cos(x[2]) - 0.3157 * x[0] / x[3] + 0.8737 * x[1] * x[
            3] + 0.3707 * x[1] + 0.2198 * x[2] / x[3] - 0.2341 * sympy.cos(x[2]) + 0.6399 - 0.4468 / x[3] + 0.0101 * x[2] / x[1] - 0.9277 / \
                        x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3961 * x[0] * x[1] + 0.4541 * x[0] * sympy.sin(x[3]) - 0.3114 * x[0] * sympy.cos(x[2]) - 0.6778 * x[2] + 0.4466 * \
                        x[3] * sympy.sin(x[2]) - 0.1626 * sympy.cos(x[1]) * sympy.cos(x[3]) + 0.0488 * sympy.cos(x[1]) + 0.0695 * sympy.cos(
            x[3]) + 0.8271 + 0.4507 * x[2] / x[1] + 0.1595 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.9609 * x[0] * x[3] + 0.7513 * x[0] + 0.7354 * x[1] * x[2] + 0.5942 * x[1] * x[3] + 0.0945 * x[2] * x[
            3] + 0.5163 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.3987 * sympy.sin(x[1]) + 0.0753 * sympy.cos(x[2]) + 0.8941 - 0.5563 / x[
                            3] + 0.0322 * sympy.cos(x[0]) / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.5829 * x[0] / x[2] - 0.3507 * x[1] * x[3] - 0.9677 * x[2] * sympy.sin(x[1]) - 0.9248 * x[2] - 0.6021 * x[
            3] * sympy.sin(x[2]) - 0.1927 * x[3] - 0.0087 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.2719 * sympy.cos(x[0]) + 0.9684 - 0.7514 / \
                        x[1] - 0.0727 * x[3] / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6866 * x[0] * x[1] + 0.8003 * x[0] + 0.2113 * x[1] - 0.4232 * x[2] * sympy.sin(x[0]) + 0.983 * x[2] * sympy.sin(
            x[3]) + 0.8045 * x[2] + 0.9657 * x[3] + 0.1183 * sympy.sin(x[1]) * sympy.sin(x[2]) - 0.1055 * sympy.sin(x[3]) * sympy.cos(
            x[0]) - 0.212 + 0.6401 * sympy.sin(x[1]) / x[3]


@register_eq_class
class sincosinv_nv4_nt46_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2947 * x[0] * sympy.sin(x[1]) - 0.0458 * x[0] * sympy.sin(x[2]) - 0.9091 * x[0] + 0.9834 * x[1] * sympy.cos(
            x[3]) - 0.6791 * x[2] * sympy.cos(x[1]) - 0.2106 * x[3] * sympy.sin(x[2]) + 0.6067 * sympy.sin(x[0]) * sympy.cos(
            x[3]) - 0.8392 * sympy.sin(x[1]) + 0.0241 - 0.7407 / x[3] + 0.6056 / x[2]


@register_eq_class
class sincosinv_nv4_nt46_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.1706 * x[0] * x[1] - 0.2747 * x[0] * x[2] - 0.9582 * x[0] * sympy.cos(x[3]) - 0.1499 * x[1] * x[3] - 0.7688 * x[
            1] + 0.2604 * x[2] - 0.2873 * x[3] + 0.5403 * sympy.sin(x[2]) * sympy.cos(x[3]) - 0.0672 + 0.961 * sympy.sin(x[2]) / x[
                            1] - 0.1997 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4887 * x[0] * x[2] - 0.7385 * x[0] * x[3] + 0.4098 * x[1] * x[3] + 0.8942 * x[1] + 0.8493 * x[
            2] + 0.9343 * sympy.cos(x[0]) * sympy.cos(x[1]) - 0.4873 * sympy.cos(x[0]) + 0.8926 * sympy.cos(
            x[3]) - 0.3352 + 0.2894 * sympy.sin(x[2]) / x[3] + 0.7322 * sympy.cos(x[2]) / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5658 * x[0] * x[2] + 0.7047 * x[0] + 0.1724 * x[1] * x[2] + 0.524 * x[1] / x[3] + 0.4566 * x[2] / x[3] + 0.475 * \
                        x[3] * sympy.cos(x[0]) - 0.5521 * sympy.sin(x[2]) + 0.3009 - 0.2386 / x[3] + 0.6295 * sympy.cos(x[0]) / x[
                            1] + 0.0193 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0161 * x[0] * x[1] + 0.6486 * x[0] * x[2] - 0.1044 * x[0] + 0.0299 * x[1] * sympy.sin(x[3]) - 0.2646 * x[
            1] * sympy.cos(x[2]) - 0.9449 * x[2] - 0.0297 * x[3] * sympy.sin(x[0]) + 0.6347 * x[3] * sympy.cos(x[2]) + 0.9107 * sympy.sin(
            x[3]) - 0.5035 * sympy.cos(x[1]) - 0.2394


@register_eq_class
class sincosinv_nv4_nt46_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0379 * x[0] * x[3] - 0.473 * x[1] * sympy.sin(x[3]) + 0.5325 * x[1] + 0.9821 * x[2] * x[3] + 0.4999 * x[
            2] * sympy.sin(x[0]) - 0.414 * x[2] + 0.293 * sympy.sin(x[0]) - 0.1954 * sympy.cos(x[0]) * sympy.cos(x[1]) - 0.1456 * sympy.cos(
            x[3]) - 0.9976 + 0.3773 * sympy.sin(x[2]) / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5831 * x[0] / x[3] - 0.8279 * x[0] / x[1] - 0.5829 * x[2] * x[3] + 0.6772 * x[2] * sympy.sin(x[0]) - 0.8827 * x[
            2] * sympy.cos(x[1]) + 0.1707 * sympy.sin(x[1]) * sympy.cos(x[3]) - 0.4814 * sympy.sin(x[2]) + 0.3904 * sympy.cos(
            x[0]) + 0.8619 * sympy.cos(x[1]) - 0.0263 * sympy.cos(x[3]) + 0.9078


@register_eq_class
class sincosinv_nv4_nt46_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.1845 * x[0] + 0.6429 * x[1] + 0.9877 * x[2] - 0.9856 * sympy.sin(x[3]) - 0.1895 + 0.4738 * sympy.sin(x[0]) / x[
            3] - 0.6877 * sympy.cos(x[1]) / x[3] - 0.2856 * x[3] / x[2] - 0.7607 * sympy.sin(x[1]) / x[2] + 0.5997 * sympy.sin(x[0]) / x[
                            1] - 0.3106 * x[2] / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8223 * x[0] * sympy.sin(x[2]) - 0.8245 * x[0] * sympy.cos(x[1]) - 0.5755 * x[1] - 0.0953 * x[1] / x[3] - 0.7148 * \
                        x[2] * x[3] - 0.0383 * x[3] * sympy.cos(x[0]) - 0.2375 * sympy.sin(x[3]) - 0.2508 + 0.8643 * sympy.cos(x[1]) / x[
                            2] + 0.8827 / x[2] - 0.6075 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.5606 * x[0] + 0.382 * x[1] * x[3] + 0.2782 * x[1] / x[2] + 0.863 * x[2] * x[3] + 0.5985 * x[2] + 0.0279 * x[
            3] * sympy.cos(x[0]) + 0.1757 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.6383 * sympy.sin(x[1]) - 0.2964 - 0.2588 / x[3] - 0.9582 * \
                        x[2] / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.9718 * x[0] * x[1] + 0.0822 * x[0] * x[3] + 0.1061 * x[0] / x[2] - 0.8731 * x[1] * sympy.sin(x[2]) - 0.7374 * x[
            2] * sympy.sin(x[3]) + 0.1245 * x[3] - 0.2283 * sympy.sin(x[0]) - 0.3289 + 0.9806 * sympy.sin(x[1]) / x[3] - 0.4961 / x[
                            2] - 0.2814 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.1931 * x[0] * x[2] - 0.5916 * x[0] * x[3] - 0.4359 * x[1] * sympy.cos(x[0]) + 0.9291 * x[2] / x[
            3] + 0.6206 * sympy.cos(x[0]) + 0.3116 * sympy.cos(x[1]) + 0.0705 - 0.2962 / x[3] + 0.7895 / x[2] - 0.5723 * x[2] / x[
                            1] - 0.1737 * x[3] / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6846 * x[0] - 0.5385 * x[1] * sympy.cos(x[3]) + 0.8629 * x[2] * sympy.sin(x[3]) + 0.6228 * x[2] * sympy.cos(
            x[1]) - 0.6022 * x[3] - 0.2381 * sympy.sin(x[1]) - 0.3248 * sympy.sin(x[2]) - 0.8062 - 0.1114 * x[1] / x[0] - 0.9445 * x[2] / x[
                            0] + 0.0651 * x[3] / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3393 * x[0] * sympy.cos(x[1]) - 0.6681 * x[0] * sympy.cos(x[2]) + 0.0164 * x[0] * sympy.cos(x[3]) - 0.7419 * x[
            0] + 0.6467 * x[2] * sympy.sin(x[3]) - 0.7364 * x[2] + 0.9931 * x[3] + 0.0603 + 0.6414 * sympy.sin(x[2]) / x[
                            1] - 0.4127 * sympy.cos(x[3]) / x[1] + 0.6252 / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.9272 * x[0] * sympy.cos(x[3]) + 0.8567 * x[0] / x[2] + 0.7576 * x[1] * sympy.sin(x[0]) + 0.1538 * x[
            1] * sympy.sin(x[2]) - 0.9271 * x[1] - 0.5784 * x[2] / x[3] - 0.6988 * x[3] - 0.7913 * sympy.cos(x[1]) * sympy.cos(
            x[3]) + 0.9639 - 0.0425 / x[2] - 0.7804 / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2109 * x[0] * x[2] - 0.3446 * x[0] + 0.2412 * x[1] * x[2] - 0.0512 * x[1] * sympy.cos(x[0]) + 0.7984 * x[
            2] + 0.0004 * x[3] * sympy.sin(x[2]) - 0.9162 * x[3] * sympy.cos(x[0]) - 0.9817 * x[3] + 0.9621 * sympy.sin(
            x[1]) - 0.4829 - 0.5179 * x[3] / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.409 * x[0] * x[1] - 0.3351 * x[0] * x[3] - 0.9086 * x[0] + 0.9185 * x[1] * x[2] + 0.3334 * x[
            1] - 0.0919 * sympy.cos(x[2]) * sympy.cos(x[3]) + 0.4162 - 0.2573 * sympy.cos(x[1]) / x[3] - 0.2039 / x[3] + 0.4581 * sympy.sin(
            x[0]) / x[2] - 0.1094 / x[2]


@register_eq_class
class sincosinv_nv4_nt46_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8124 * x[0] * x[2] - 0.5846 * x[1] * sympy.sin(x[2]) - 0.6956 * x[2] * x[3] - 0.1207 * sympy.cos(
            x[0]) * sympy.cos(x[1]) - 0.3657 * sympy.cos(x[0]) * sympy.cos(x[3]) - 0.0453 * sympy.cos(x[0]) + 0.7809 * sympy.cos(
            x[1]) - 0.4657 + 0.1619 / x[3] - 0.7233 / x[2] - 0.2625 * x[3] / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.289 * x[0] - 0.2205 * x[1] * x[3] - 0.9956 * x[2] * sympy.sin(x[3]) - 0.9393 * x[2] + 0.2012 * x[
            3] - 0.0904 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.1126 * sympy.sin(x[0]) * sympy.cos(x[2]) + 0.5887 * sympy.sin(
            x[3]) * sympy.cos(x[0]) - 0.4748 * sympy.cos(x[1]) - 0.3355 - 0.4921 * sympy.cos(x[2]) / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.831 * x[0] + 0.5499 * x[1] * x[2] - 0.9764 * x[1] * x[3] - 0.0547 * x[1] * sympy.sin(x[0]) - 0.8988 * sympy.sin(
            x[0]) * sympy.cos(x[3]) - 0.8145 * sympy.cos(x[1]) + 0.825 * sympy.cos(x[2]) - 0.2047 * sympy.cos(
            x[3]) + 0.5865 - 0.5199 * sympy.sin(x[2]) / x[3] + 0.0114 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv4_nt46_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.306 * x[0] * x[1] + 0.1302 * x[0] + 0.127 * x[1] * x[3] + 0.8444 * x[1] + 0.3456 * x[2] * x[
            3] + 0.1001 + 0.6226 * sympy.sin(x[0]) / x[3] - 0.7249 / x[3] + 0.4468 / x[2] + 0.6934 * x[2] / x[1] + 0.7425 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv4_nt46_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.1459 * x[0] * x[2] - 0.8804 * x[1] * x[2] + 0.1852 * x[1] * sympy.sin(x[0]) - 0.0905 * x[2] * x[3] + 0.9433 * x[
            3] - 0.6897 * sympy.sin(x[0]) - 0.7763 * sympy.cos(x[1]) - 0.5766 - 0.6405 / x[2] + 0.53 / (x[1] * x[3]) - 0.2587 * sympy.cos(
            x[3]) / x[0]


@register_eq_class
class sincosinv_nv4_nt46_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.9611 * x[0] * x[1] + 0.2645 * x[1] * x[2] - 0.0488 * x[2] * sympy.sin(x[0]) + 0.1079 * x[3] - 0.1779 * sympy.sin(
            x[1]) + 0.5591 * sympy.sin(x[2]) * sympy.sin(x[3]) - 0.8467 * sympy.sin(x[2]) - 0.8117 * sympy.cos(x[0]) - 0.7543 * sympy.cos(
            x[1]) * sympy.cos(x[3]) + 0.1393 - 0.5129 * sympy.sin(x[0]) / x[3]


@register_eq_class
class sincosinv_nv4_nt46_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0929 * x[0] - 0.9502 * x[1] * sympy.cos(x[0]) + 0.327 * x[1] - 0.0229 * x[1] / x[2] - 0.6074 * x[2] * sympy.cos(
            x[0]) - 0.0397 * x[3] * sympy.cos(x[2]) - 0.2158 * x[3] - 0.3472 * sympy.sin(x[0]) * sympy.cos(x[3]) + 0.2152 * sympy.sin(
            x[2]) + 0.2605 - 0.4967 * sympy.cos(x[3]) / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0981 * x[0] * x[2] + 0.2815 * x[0] * x[3] + 0.6737 * x[0] * sympy.cos(x[1]) - 0.9701 * x[1] * sympy.sin(
            x[3]) - 0.806 * x[2] * x[3] + 0.2464 * x[2] - 0.6814 * sympy.sin(x[1]) - 0.1977 * sympy.cos(x[0]) - 0.8003 - 0.0435 / x[
                            3] + 0.8952 * x[2] / x[1]


@register_eq_class
class sincosinv_nv4_nt46_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2663 * x[0] * x[2] - 0.886 * x[1] - 0.3725 * x[2] * x[3] + 0.846 * x[2] + 0.3458 * x[3] * sympy.sin(
            x[1]) + 0.3444 * sympy.sin(x[0]) * sympy.sin(x[3]) - 0.4977 * sympy.sin(x[0]) - 0.3663 * sympy.sin(x[3]) + 0.5169 * sympy.cos(
            x[0]) * sympy.cos(x[1]) - 0.4616 - 0.6095 * sympy.cos(x[1]) / x[2]


@register_eq_class
class sincosinv_nv4_nt46_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv4_nt46_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6544 * x[2] * sympy.sin(x[0]) + 0.4121 * x[2] * sympy.sin(x[1]) + 0.8252 * x[2] + 0.6573 * x[3] * sympy.cos(
            x[0]) + 0.8987 * x[3] * sympy.cos(x[1]) + 0.5118 * x[3] + 0.1866 * sympy.sin(x[2]) * sympy.cos(x[3]) + 0.2784 + 0.5141 / x[
                            1] - 0.7678 * sympy.cos(x[1]) / x[0] - 0.4489 / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.4731 * x[0] * x[1] - 0.718 * x[0] - 0.9008 * sympy.cos(x[2]) + 0.6838 - 0.9633 * x[2] / x[1]


@register_eq_class
class sincosinv_nv3_nt22_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6694 * x[0] - 0.9875 * x[1] * sympy.cos(x[0]) - 0.839 * x[2] * sympy.cos(x[0]) - 0.2756 * sympy.cos(x[2]) - 0.8955


@register_eq_class
class sincosinv_nv3_nt22_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.09 * x[0] * sympy.cos(x[1]) - 0.6156 * x[0] / x[2] + 0.6769 * x[2] + 0.7251 * sympy.sin(x[1]) - 0.2127


@register_eq_class
class sincosinv_nv3_nt22_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3186 * x[0] * x[1] - 0.3379 * x[0] + 0.1903 * x[2] + 0.3151 - 0.4833 * sympy.sin(x[1]) / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6337 * x[0] * x[2] + 0.2587 * x[0] - 0.6411 * x[1] + 0.603 * x[2] * sympy.cos(x[1]) - 0.7619


@register_eq_class
class sincosinv_nv3_nt22_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0005 * x[0] * x[2] + 0.5346 * x[0] / x[1] + 0.065 * x[2] - 0.6081 * sympy.sin(x[1]) - 0.3402


@register_eq_class
class sincosinv_nv3_nt22_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.9022 * x[2] * sympy.sin(x[0]) + 0.2754 * sympy.cos(x[1]) - 0.3381 * sympy.cos(x[2]) - 0.358 - 0.4568 * x[1] / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9011 * x[0] * sympy.cos(x[2]) + 0.7954 * x[0] + 0.5627 * x[1] * sympy.sin(x[0]) + 0.3975 * x[1] + 0.4821


@register_eq_class
class sincosinv_nv3_nt22_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7485 * x[0] / x[2] + 0.6692 * x[1] / x[2] - 0.4806 * sympy.sin(x[0]) + 0.2442 * sympy.cos(x[1]) - 0.729


@register_eq_class
class sincosinv_nv3_nt22_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.2018 * x[0] - 0.6162 * x[2] * sympy.cos(x[0]) - 0.1248 * x[2] + 0.4597 + 0.3195 * sympy.sin(x[2]) / x[1]


@register_eq_class
class sincosinv_nv3_nt22_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8278 * x[0] / x[2] + 0.8361 * x[1] - 0.3364 * sympy.sin(x[0]) + 0.2329 - 0.9948 * sympy.sin(x[2]) / x[1]


@register_eq_class
class sincosinv_nv3_nt22_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.3462 * x[0] + 0.0067 * x[1] * x[2] - 0.5528 * sympy.sin(x[0]) * sympy.sin(x[2]) - 0.0606 - 0.8507 / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6784 * x[0] * x[2] - 0.6881 * x[0] + 0.0736 * x[1] * sympy.sin(x[0]) + 0.5985 * x[2] + 0.5391


@register_eq_class
class sincosinv_nv3_nt22_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2502 * x[0] - 0.0372 + 0.7395 / x[2] + 0.4393 * x[2] / x[1] + 0.9225 * sympy.cos(x[1]) / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5816 * x[1] * x[2] + 0.863 * x[2] * sympy.cos(x[0]) - 0.1962 * x[2] - 0.5268 * sympy.sin(x[0]) - 0.6602


@register_eq_class
class sincosinv_nv3_nt22_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.1529 * x[0] * sympy.sin(x[2]) + 0.8207 * x[1] * x[2] - 0.7407 * x[1] + 0.7897 * x[2] - 0.5552


@register_eq_class
class sincosinv_nv3_nt22_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7534 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.9114 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.5426 * sympy.sin(
            x[2]) + 0.576 * sympy.cos(x[0]) + 0.5281


@register_eq_class
class sincosinv_nv3_nt22_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7276 * x[0] * x[2] + 0.0839 * x[0] * sympy.sin(x[1]) + 0.9439 * x[1] + 0.8618 * sympy.sin(x[0]) - 0.7685


@register_eq_class
class sincosinv_nv3_nt22_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5021 * x[0] * sympy.cos(x[2]) + 0.0883 * x[1] * sympy.cos(x[2]) + 0.1078 * x[2] + 0.3108 * sympy.sin(
            x[0]) - 0.0025


@register_eq_class
class sincosinv_nv3_nt22_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8059 * x[0] - 0.3823 * x[0] / x[1] + 0.8989 * x[1] * sympy.sin(x[2]) + 0.2407 * sympy.sin(x[1]) - 0.5734


@register_eq_class
class sincosinv_nv3_nt22_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.7167 * x[0] / x[2] - 0.0632 * x[1] + 0.2746 * x[2] * sympy.cos(x[1]) - 0.7293 + 0.0627 / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.8156 * x[0] * x[1] + 0.5922 * x[0] * sympy.sin(x[2]) + 0.2842 * sympy.sin(x[2]) + 0.9092 * sympy.cos(
            x[1]) + 0.4943


@register_eq_class
class sincosinv_nv3_nt22_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.4717 * x[2] - 0.8981 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.2897 * sympy.cos(
            x[1]) + 0.0718 + 0.1499 * sympy.cos(x[0]) / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.3355 * x[0] * x[2] - 0.8855 * x[0] - 0.1012 * x[1] * sympy.sin(x[0]) - 0.8832 * x[2] - 0.7267


@register_eq_class
class sincosinv_nv3_nt22_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0631 * x[1] - 0.4757 * x[2] - 0.1092 + 0.888 * x[2] / x[1] - 0.8016 * x[2] / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.2746 * x[0] * x[1] - 0.1578 * x[0] - 0.2008 * x[1] * sympy.sin(x[2]) + 0.4407 * x[2] - 0.9655


@register_eq_class
class sincosinv_nv3_nt22_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5666 * x[0] * x[1] + 0.5294 * x[0] - 0.9168 * x[2] * sympy.sin(x[1]) + 0.8367 - 0.7885 / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.0915 * x[2] * sympy.sin(x[0]) - 0.4029 * sympy.sin(x[1]) * sympy.cos(x[2]) + 0.0705 + 0.1593 / x[2] - 0.3128 / x[
            0]


@register_eq_class
class sincosinv_nv3_nt22_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.9717 * x[0] / x[1] - 0.8968 * x[1] - 0.7034 * x[2] * sympy.cos(x[0]) - 0.2461 * sympy.cos(x[2]) - 0.4229


@register_eq_class
class sincosinv_nv3_nt22_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.4529 * x[0] * sympy.cos(x[1]) - 0.0496 * x[0] - 0.1261 * x[1] * x[2] + 0.832 * x[2] - 0.9881


@register_eq_class
class sincosinv_nv3_nt22_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.2384 * x[0] * sympy.sin(x[2]) + 0.4265 * x[0] - 0.3308 * sympy.cos(x[2]) + 0.6222 - 0.3814 * sympy.cos(x[2]) / x[
            1]


@register_eq_class
class sincosinv_nv3_nt22_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.471 * sympy.sin(x[1]) * sympy.cos(x[2]) - 0.0438 * sympy.sin(x[2]) - 0.7955 * sympy.cos(
            x[1]) + 0.8211 + 0.3759 / (x[0] * x[1])


@register_eq_class
class sincosinv_nv3_nt22_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5803 * x[0] / x[2] + 0.0546 * x[2] + 0.8823 * sympy.cos(x[0]) + 0.2353 + 0.2675 * sympy.cos(x[1]) / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6071 * x[1] * x[2] + 0.3788 * sympy.sin(x[0]) + 0.8719 + 0.7567 * sympy.cos(x[0]) / x[2] + 0.2025 / x[1]


@register_eq_class
class sincosinv_nv3_nt22_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.6232 * x[0] / x[2] - 0.7601 * x[2] + 0.4806 * sympy.sin(x[0]) - 0.9833 - 0.7326 * x[2] / x[1]


@register_eq_class
class sincosinv_nv3_nt22_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.2705 * x[0] * x[1] - 0.1976 * x[0] * sympy.sin(x[2]) - 0.0635 * x[1] - 0.253 * x[2] - 0.048


@register_eq_class
class sincosinv_nv3_nt22_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.4125 * x[1] - 0.3342 * x[1] / x[2] + 0.6668 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.0636 * sympy.cos(
            x[2]) - 0.5172


@register_eq_class
class sincosinv_nv3_nt22_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.5249 * x[0] * x[1] + 0.3362 * x[0] + 0.4631 * x[1] * x[2] - 0.8929 * x[1] + 0.992


@register_eq_class
class sincosinv_nv3_nt22_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.0349 * x[0] * x[2] - 0.1877 * x[1] * sympy.sin(x[2]) + 0.8617 * x[1] + 0.545 * sympy.sin(x[2]) + 0.6662


@register_eq_class
class sincosinv_nv3_nt22_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.39 * x[0] / x[1] - 0.2232 * x[1] - 0.5088 * x[2] * sympy.sin(x[1]) + 0.5039 + 0.2385 / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.7661 * x[0] * sympy.cos(x[1]) - 0.458 * x[0] - 0.6815 * x[2] * sympy.cos(x[1]) - 0.1257 + 0.8656 / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6059 * x[0] - 0.7633 * x[1] * sympy.cos(x[2]) + 0.2494 * sympy.sin(x[2]) - 0.3159 - 0.6113 * sympy.cos(x[0]) / x[
            2]


@register_eq_class
class sincosinv_nv3_nt22_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.8641 * x[0] * x[2] + 0.885 * x[2] * sympy.cos(x[1]) - 0.0017 * x[2] - 0.7722 * sympy.cos(x[0]) - 0.7641


@register_eq_class
class sincosinv_nv3_nt22_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.071 * x[0] * x[2] + 0.8982 * x[0] + 0.9415 * x[1] / x[2] - 0.5899 - 0.8433 / x[2]


@register_eq_class
class sincosinv_nv3_nt22_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.3205 * x[0] * sympy.cos(x[1]) + 0.7197 * sympy.sin(x[0]) * sympy.sin(x[2]) + 0.4752 * sympy.sin(
            x[1]) + 0.8174 + 0.4287 / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.6096 * x[0] * x[1] - 0.3284 * x[1] * x[2] - 0.6288 * x[2] - 0.154 * sympy.cos(x[0]) + 0.7472


@register_eq_class
class sincosinv_nv3_nt22_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.0123 * x[2] + 0.361 * sympy.cos(x[0]) - 0.8996 - 0.5054 * sympy.cos(x[1]) / x[2] - 0.5686 * x[1] / x[0]


@register_eq_class
class sincosinv_nv3_nt22_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.033 * x[0] * sympy.cos(x[2]) - 0.0654 * x[1] * sympy.cos(x[0]) + 0.7153 * x[1] + 0.6829 * x[2] - 0.3176


@register_eq_class
class sincosinv_nv3_nt22_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -0.8263 * x[0] + 0.639 * x[1] * sympy.sin(x[2]) - 0.4999 * x[1] * sympy.cos(x[0]) + 0.0083 * x[2] + 0.5796


@register_eq_class
class sincosinv_nv3_nt22_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv3_nt22_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.0324 * x[0] * sympy.sin(x[1]) - 0.0193 * x[0] + 0.8748 * x[2] * sympy.sin(x[1]) + 0.0158 * x[2] + 0.1359


@register_eq_class
class inv_nv4_nt46_prog_46(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3159 * x[0] - 0.5836 * x[0] / x[1] + 0.1432 * x[1] + 0.6298 * x[1] / x[2] - 0.2072 - 0.9315 / x[3] + 0.4862 * x[
            3] / x[2] + 0.899 / x[2] - 0.9998 * x[3] / x[1] + 0.3619 * x[3] / x[0] + 0.6039 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_0(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.8009 * x[0] * x[2] + 0.287 * x[0] * x[3] + 0.5974 * x[0] - 0.3582 + 0.598 / x[3] + 0.7146 / x[2] - 0.7463 / (
                x[2] * x[3]) - 0.3685 * x[3] / x[1] - 0.7113 / x[1] - 0.0028 / (x[1] * x[2]) + 0.6104 * x[1] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_35(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.8075 * x[0] * x[1] - 0.9243 * x[0] * x[2] - 0.6596 * x[0] + 0.8634 * x[1] + 0.5276 * x[2] * x[3] - 0.1524 * x[
            3] + 0.3784 + 0.0149 / x[2] - 0.4958 * x[3] / x[1] - 0.0611 / (x[1] * x[2]) + 0.4754 / (x[0] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_8(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7926 * x[0] + 0.9284 * x[0] / x[2] - 0.5497 * x[0] / x[1] + 0.6305 * x[1] * x[2] - 0.1068 * x[1] / x[
            3] - 0.3143 * x[2] - 0.5154 - 0.4889 / x[3] + 0.6916 * x[3] / x[2] + 0.606 / x[1] + 0.085 * x[3] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_42(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6354 * x[0] * x[2] + 0.0702 * x[0] * x[3] + 0.2983 + 0.9351 / x[3] + 0.1011 / x[2] - 0.7963 / (
                x[2] * x[3]) + 0.5083 / x[1] + 0.408 / (x[1] * x[3]) - 0.3854 / (x[1] * x[2]) + 0.0385 / x[0] + 0.7783 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_33(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.1689 * x[0] - 0.0033 * x[1] * x[3] + 0.977 * x[2] * x[3] - 0.1576 - 0.5576 / x[3] - 0.2833 / x[2] + 0.0394 / x[
            1] - 0.7305 / (x[1] * x[2]) + 0.9509 * x[3] / x[0] + 0.4707 / (x[0] * x[2]) + 0.2824 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_20(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7375 * x[0] * x[1] + 0.7474 * x[0] * x[3] + 0.2656 * x[1] * x[2] - 0.472 * x[1] + 0.0943 * x[
            2] - 0.8573 + 0.4989 / x[3] - 0.1175 / (x[2] * x[3]) + 0.0179 / (x[1] * x[3]) + 0.326 * x[2] / x[0] - 0.4674 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_14(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0392 * x[0] - 0.985 * x[0] / x[2] - 0.2819 * x[1] / x[2] - 0.8738 * x[2] * x[3] - 0.0259 * x[
            2] - 0.9108 + 0.2128 / x[3] + 0.8517 * x[3] / x[1] + 0.2623 / x[1] - 0.8483 / (x[0] * x[3]) - 0.5977 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_31(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6488 * x[0] * x[2] + 0.8432 * x[1] * x[2] - 0.053 * x[1] * x[3] - 0.2717 * x[2] * x[3] - 0.1355 + 0.1292 / x[
            3] - 0.1546 / x[2] - 0.7341 / x[1] - 0.136 * x[3] / x[0] - 0.7318 / x[0] + 0.8905 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_48(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.7063 * x[0] * x[1] + 0.9431 * x[0] * x[2] + 0.1772 * x[0] - 0.9815 * x[0] / x[3] - 0.36 * x[1] * x[2] - 0.7639 * \
                        x[2] * x[3] - 0.6576 * x[2] + 0.5199 + 0.817 / x[3] - 0.5641 / x[1] + 0.5563 / (x[1] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_41(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.7442 * x[0] - 0.3747 * x[0] / x[1] + 0.5366 * x[1] * x[2] - 0.352 * x[1] - 0.8531 * x[2] - 0.0978 * x[2] / x[
            3] - 0.0848 + 0.7206 / x[3] + 0.4682 / (x[1] * x[3]) + 0.2499 * x[3] / x[0] - 0.6061 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_7(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0622 * x[0] + 0.7445 * x[1] * x[3] + 0.7972 * x[1] - 0.6852 * x[1] / x[2] - 0.009 - 0.9344 / x[3] - 0.6603 * x[
            3] / x[2] + 0.2866 / x[2] - 0.1778 * x[2] / x[0] + 0.7024 * x[3] / x[0] - 0.8865 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_37(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2292 * x[0] + 0.8001 * x[0] / x[3] + 0.1056 * x[1] * x[2] + 0.0086 * x[1] * x[3] + 0.2069 * x[1] + 0.0551 * x[
            2] - 0.7624 * x[2] / x[3] - 0.1092 * x[3] + 0.4165 - 0.252 / (x[0] * x[2]) - 0.3389 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_15(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.4253 * x[0] * x[3] + 0.7523 * x[0] - 0.4235 * x[0] / x[1] + 0.8888 * x[1] / x[3] - 0.0395 * x[2] / x[
            3] + 0.3352 * x[3] + 0.9478 - 0.9662 / x[2] + 0.4637 / x[1] + 0.5776 / (x[1] * x[2]) - 0.4609 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_23(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3504 * x[0] * x[1] - 0.0859 * x[1] / x[3] + 0.1884 * x[1] / x[2] + 0.5141 * x[2] - 0.7749 * x[
            3] + 0.2424 + 0.2093 * x[3] / x[2] - 0.5359 / x[1] + 0.8792 * x[3] / x[0] + 0.836 / x[0] + 0.3935 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_30(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.398 * x[0] * x[1] + 0.7412 * x[1] / x[3] + 0.5461 * x[2] / x[3] - 0.7527 - 0.1911 / x[3] - 0.4141 / x[
            2] + 0.2902 / x[1] - 0.1122 / (x[1] * x[2]) - 0.379 * x[2] / x[0] - 0.815 * x[3] / x[0] - 0.5291 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_28(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6398 * x[0] - 0.3261 * x[0] / x[3] + 0.1537 * x[0] / x[2] + 0.8154 * x[1] * x[3] + 0.5313 * x[2] * x[3] - 0.2925 * \
                        x[3] + 0.3168 + 0.3732 / x[2] - 0.9296 / x[1] - 0.5028 / (x[1] * x[2]) + 0.2783 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_17(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0862 * x[0] - 0.2103 * x[0] / x[2] + 0.2244 * x[1] - 0.7379 + 0.3504 / x[3] - 0.2221 * x[3] / x[2] - 0.7666 / x[
            2] + 0.1658 / (x[1] * x[3]) - 0.3871 / (x[1] * x[2]) + 0.697 * x[1] / x[0] - 0.6307 * x[3] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_43(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.7135 * x[0] / x[2] + 0.8319 * x[0] / x[1] - 0.6392 * x[1] / x[3] - 0.1678 * x[2] + 0.6749 * x[
            3] + 0.8948 - 0.2381 / (x[2] * x[3]) - 0.4031 * x[2] / x[1] - 0.872 / x[1] - 0.3 * x[3] / x[0] - 0.0487 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_2(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.7735 * x[0] / x[3] + 0.963 * x[1] - 0.5836 * x[1] / x[2] - 0.2011 * x[2] - 0.6269 + 0.7055 / x[3] + 0.2884 * x[
            3] / x[2] - 0.5314 / (x[1] * x[3]) - 0.7059 * x[1] / x[0] + 0.5314 * x[2] / x[0] - 0.3782 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_4(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2783 * x[1] / x[2] - 0.3383 * x[3] + 0.1816 - 0.6583 * x[3] / x[2] - 0.7207 / x[2] - 0.1798 * x[3] / x[
            1] - 0.8904 / x[1] - 0.277 / x[0] + 0.889 / (x[0] * x[3]) + 0.7294 / (x[0] * x[2]) - 0.2325 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_45(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.9134 * x[1] * x[2] + 0.7246 * x[2] - 0.4547 * x[3] - 0.2683 + 0.3269 / (x[2] * x[3]) + 0.9718 / x[1] - 0.534 / (
                x[1] * x[3]) - 0.8119 * x[1] / x[0] - 0.9962 * x[2] / x[0] + 0.2501 * x[3] / x[0] + 0.7054 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_49(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.8338 * x[1] * x[2] + 0.4445 * x[1] - 0.1796 * x[2] + 0.6478 * x[2] / x[3] + 0.3381 * x[3] + 0.7677 - 0.6407 * x[
            3] / x[1] + 0.494 * x[1] / x[0] + 0.507 * x[3] / x[0] + 0.1332 / x[0] - 0.7941 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_11(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2885 * x[0] * x[2] + 0.5983 * x[0] + 0.4384 * x[1] * x[3] + 0.6851 * x[2] * x[3] - 0.5195 * x[2] + 0.1683 * x[
            3] - 0.875 + 0.6996 * x[2] / x[1] - 0.6558 / x[1] - 0.7914 / (x[0] * x[3]) + 0.3466 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_10(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.8038 * x[0] * x[3] + 0.8226 * x[0] - 0.2749 * x[2] * x[3] + 0.6585 * x[2] - 0.5442 * x[3] - 0.0733 - 0.6039 * x[
            2] / x[1] + 0.1871 / x[1] + 0.2356 / (x[1] * x[3]) - 0.1166 / (x[0] * x[2]) + 0.1701 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_1(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3385 * x[0] * x[1] + 0.934 * x[0] / x[3] - 0.8029 * x[0] / x[2] - 0.0608 - 0.9344 / x[3] - 0.6286 * x[3] / x[
            2] + 0.189 / x[2] + 0.9354 * x[3] / x[1] - 0.5682 / x[1] + 0.0152 / (x[1] * x[2]) + 0.0263 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_40(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3491 * x[0] / x[2] - 0.4658 * x[0] / x[1] + 0.0116 * x[1] - 0.6598 * x[1] / x[3] + 0.2844 * x[2] * x[
            3] - 0.1434 + 0.6125 / x[3] + 0.9825 / x[2] + 0.6821 * x[2] / x[1] + 0.2088 / x[0] - 0.0204 / (x[0] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_29(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.4219 * x[0] * x[2] + 0.5389 * x[0] - 0.9532 * x[0] / x[1] - 0.7822 - 0.4992 / x[3] - 0.8787 / x[2] - 0.7597 / (
                x[2] * x[3]) + 0.5966 * x[2] / x[1] - 0.0139 / x[1] - 0.982 / (x[1] * x[3]) - 0.5748 * x[3] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_22(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.4826 * x[0] * x[2] + 0.6566 * x[0] * x[3] - 0.8747 * x[1] * x[2] - 0.2731 * x[1] / x[3] - 0.7498 * x[
            2] - 0.7269 + 0.8467 / x[3] - 0.1703 / (x[2] * x[3]) + 0.2208 / x[1] - 0.98 * x[1] / x[0] + 0.786 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_27(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.1995 * x[0] * x[3] - 0.4716 * x[0] + 0.9902 * x[0] / x[1] - 0.4066 * x[1] / x[3] - 0.1862 * x[2] + 0.3405 * x[
            2] / x[3] - 0.0392 * x[3] - 0.3597 - 0.6865 * x[2] / x[1] + 0.8229 / x[1] + 0.394 * x[2] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_34(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.5783 * x[1] * x[2] + 0.857 * x[1] + 0.1773 * x[1] / x[3] - 0.9939 * x[2] / x[3] - 0.5906 + 0.3423 / x[
            3] - 0.6864 / x[2] - 0.9506 * x[1] / x[0] - 0.6998 * x[2] / x[0] - 0.1447 / x[0] - 0.113 / (x[0] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_16(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.9403 * x[0] * x[1] - 0.5403 * x[0] * x[3] + 0.593 * x[0] / x[2] - 0.4719 * x[2] + 0.2136 * x[2] / x[
            3] + 0.2594 - 0.526 / x[3] + 0.0685 * x[3] / x[1] - 0.0247 / x[1] + 0.6985 / (x[1] * x[2]) - 0.3602 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_13(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0754 * x[0] * x[1] - 0.2557 * x[0] - 0.355 * x[1] / x[3] + 0.2656 * x[2] / x[3] - 0.9665 + 0.012 / x[
            3] - 0.6611 / x[2] + 0.7867 / x[1] - 0.8095 / (x[1] * x[2]) - 0.407 * x[3] / x[0] - 0.8163 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_47(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2325 * x[0] * x[2] - 0.4584 * x[0] / x[1] - 0.5862 * x[1] + 0.2003 + 0.7317 / x[3] - 0.4847 * x[3] / x[
            2] - 0.4231 / x[2] - 0.624 * x[3] / x[1] + 0.22 / (x[1] * x[2]) + 0.6405 / x[0] - 0.9025 / (x[0] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_36(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0411 * x[0] * x[2] - 0.2308 * x[0] + 0.6227 * x[0] / x[1] + 0.4015 * x[1] - 0.3808 * x[1] / x[3] - 0.2477 * x[1] / \
                        x[2] + 0.0348 * x[2] / x[3] + 0.0733 * x[3] - 0.2331 - 0.7339 / x[2] + 0.3092 * x[3] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_44(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.8855 * x[0] * x[1] - 0.1755 * x[0] / x[2] + 0.2379 * x[1] * x[3] - 0.3168 * x[1] + 0.0566 * x[
            2] - 0.5543 - 0.9934 / x[3] + 0.054 * x[3] / x[2] - 0.4492 * x[2] / x[1] + 0.6326 * x[3] / x[0] - 0.7184 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_6(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.0103 * x[0] / x[3] - 0.9083 * x[1] * x[3] + 0.5175 * x[1] - 0.7413 * x[2] * x[3] + 0.0489 * x[2] - 0.9727 * x[
            3] + 0.1626 + 0.6084 * x[2] / x[1] - 0.647 / x[0] + 0.7501 / (x[0] * x[2]) - 0.1918 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_18(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.6445 * x[0] * x[2] - 0.0018 * x[0] / x[3] - 0.5838 * x[0] / x[1] + 0.4732 * x[1] * x[3] + 0.0314 * x[1] - 0.164 * \
                        x[1] / x[2] + 0.3883 * x[2] + 0.3751 * x[3] + 0.1974 + 0.2444 * x[3] / x[2] - 0.3245 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_3(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3679 * x[0] + 0.5335 * x[0] / x[3] - 0.3324 * x[1] + 0.9133 * x[2] - 0.2094 * x[3] + 0.0986 - 0.8793 * x[3] / x[
            2] + 0.6348 * x[2] / x[1] + 0.7344 / (x[1] * x[3]) + 0.3084 / (x[0] * x[2]) + 0.3413 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_24(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2527 * x[0] * x[3] + 0.3795 * x[0] - 0.2455 * x[1] - 0.9216 * x[1] / x[3] + 0.0979 * x[2] * x[3] - 0.9283 * x[
            2] + 0.4813 * x[3] - 0.1954 + 0.341 / (x[1] * x[2]) + 0.6324 * x[1] / x[0] - 0.7546 * x[2] / x[0]


@register_eq_class
class inv_nv4_nt46_prog_12(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.2836 * x[0] * x[1] - 0.7123 * x[0] * x[2] - 0.5441 * x[0] * x[3] + 0.7953 - 0.0825 / x[3] - 0.0237 / x[
            2] + 0.717 / (x[2] * x[3]) + 0.277 * x[2] / x[1] + 0.3836 / x[1] + 0.9564 / (x[1] * x[3]) + 0.7264 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_25(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.2728 * x[0] / x[3] - 0.4362 * x[0] / x[2] + 0.895 * x[0] / x[1] + 0.4816 * x[2] * x[3] + 0.3638 * x[
            2] + 0.7686 - 0.6625 / x[3] + 0.2898 * x[3] / x[1] + 0.3114 / x[1] - 0.8213 / (x[1] * x[2]) + 0.0911 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_21(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3936 * x[0] - 0.2727 * x[0] / x[1] + 0.9826 * x[1] * x[2] + 0.4998 * x[1] * x[3] + 0.0558 * x[
            3] + 0.9055 + 0.4539 / x[2] - 0.1765 / (x[2] * x[3]) - 0.6105 / x[1] + 0.7785 * x[3] / x[0] + 0.995 / (x[0] * x[2])


@register_eq_class
class inv_nv4_nt46_prog_26(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.5243 * x[0] * x[1] - 0.7378 * x[0] / x[2] + 0.8976 * x[1] * x[2] - 0.4004 * x[2] - 0.3965 + 0.4242 / x[
            3] + 0.2273 * x[3] / x[2] + 0.2024 / x[1] + 0.3158 / (x[1] * x[3]) - 0.8482 / x[0] - 0.5863 / (x[0] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_39(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.3924 * x[0] + 0.2056 * x[0] / x[3] - 0.0819 * x[1] + 0.2833 * x[2] * x[3] - 0.9562 * x[3] - 0.351 + 0.2249 / x[
            2] + 0.9409 * x[2] / x[1] + 0.0292 * x[3] / x[1] - 0.3082 * x[2] / x[0] - 0.2351 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_19(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.3214 * x[0] * x[1] + 0.6948 * x[0] * x[3] - 0.838 * x[1] * x[3] + 0.5588 * x[1] + 0.6546 * x[1] / x[2] + 0.9229 * \
                        x[2] / x[3] + 0.8457 * x[3] - 0.3931 - 0.1491 / x[2] - 0.2128 * x[2] / x[0] - 0.5755 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_38(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -0.8827 * x[0] * x[1] + 0.4024 * x[0] * x[2] + 0.984 * x[0] / x[3] + 0.4057 * x[1] * x[3] - 0.6267 * x[1] - 0.6453 * \
                        x[2] + 0.031 * x[3] + 0.8334 - 0.9313 / (x[2] * x[3]) + 0.7707 / (x[1] * x[2]) + 0.5523 / x[0]


@register_eq_class
class inv_nv4_nt46_prog_9(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.0659 * x[0] * x[2] + 0.2291 * x[0] - 0.1451 * x[1] * x[2] + 0.8005 * x[2] * x[3] + 0.2746 * x[2] + 0.6498 * x[
            3] - 0.8292 - 0.7617 * x[3] / x[1] - 0.5834 / x[1] - 0.2896 * x[3] / x[0] - 0.7056 / (x[0] * x[1])


@register_eq_class
class inv_nv4_nt46_prog_32(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.3049 * x[0] + 0.2395 * x[0] / x[2] + 0.3626 * x[0] / x[1] + 0.5087 * x[1] * x[2] + 0.9311 * x[
            2] + 0.7237 - 0.0018 / x[3] + 0.4854 / (x[2] * x[3]) - 0.5128 / x[1] - 0.4777 / (x[1] * x[3]) + 0.3779 / (x[0] * x[3])


@register_eq_class
class inv_nv4_nt46_prog_5(KnownEquation):
    _eq_name = 'inv_nv4_nt46_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.732 * x[0] * x[2] + 0.5197 * x[0] / x[3] - 0.6554 * x[0] / x[1] - 0.3569 * x[1] / x[2] + 0.2519 * x[2] / x[
            3] - 0.0124 + 0.9614 / x[3] + 0.3701 / x[2] - 0.5063 / x[1] + 0.7426 / (x[1] * x[3]) - 0.0052 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7465 * x[0] * sympy.sin(x[1]) - 0.5408 * x[0] / x[4] + 0.166 * x[1] * x[3] + 0.8077 * x[1] + 0.3634 * x[
            2] * sympy.sin(x[3]) + 0.9867 * x[2] * sympy.cos(x[0]) - 0.8127 * x[3] * x[4] - 0.2136 * x[3] * sympy.cos(x[5]) - 0.0997 * x[
                            3] - 0.2245 * x[4] - 0.5893 * x[5] - 0.1305 * sympy.sin(x[2]) - 0.8948 - 0.1088 * sympy.cos(x[5]) / x[
                            1] + 0.2575 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8621 * x[1] - 0.494 * x[2] * x[3] + 0.373 * x[2] * x[4] + 0.8349 * x[2] * sympy.cos(x[5]) + 0.8578 * x[
            4] * sympy.sin(x[3]) - 0.9529 * x[4] * sympy.cos(x[1]) + 0.538 * x[4] + 0.5359 * x[5] - 0.0218 * sympy.cos(
            x[0]) + 0.9478 * sympy.cos(x[2]) + 0.4828 + 0.9844 / x[3] + 0.6641 * sympy.sin(x[3]) / x[1] + 0.5185 * x[2] / x[
                            0] - 0.3708 * sympy.sin(x[4]) / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3452 * x[0] * x[3] - 0.5636 * x[1] * sympy.cos(x[2]) + 0.9942 * x[1] + 0.6002 * x[2] * x[3] + 0.2587 * x[2] / x[
            5] + 0.4145 * x[3] - 0.9056 * x[4] * x[5] - 0.8174 * x[5] + 0.2955 * sympy.sin(x[0]) + 0.6304 * sympy.cos(
            x[2]) + 0.5962 * sympy.cos(x[4]) - 0.0288 + 0.1233 * sympy.sin(x[2]) / x[4] - 0.9357 * x[3] / x[1] + 0.9477 * sympy.cos(x[2]) / \
                        x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0041 * x[0] + 0.896 * x[0] / x[5] + 0.703 * x[1] + 0.0168 * x[2] - 0.973 * x[3] * sympy.cos(x[2]) - 0.5971 * x[
            4] * sympy.cos(x[5]) - 0.8457 * sympy.sin(x[3]) * sympy.cos(x[0]) - 0.2209 * sympy.sin(x[5]) - 0.2905 * sympy.cos(
            x[4]) - 0.9089 + 0.1067 * sympy.cos(x[1]) / x[4] + 0.0698 / x[3] + 0.0148 * x[5] / x[2] - 0.3003 * x[2] / x[0] - 0.5148 / (
                                x[0] * x[1])


@register_eq_class
class sincosinv_nv6_nt68_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9136 * x[0] * x[1] + 0.1037 * x[1] * x[3] + 0.6592 * x[1] * sympy.cos(x[2]) - 0.0579 * x[2] * sympy.sin(
            x[3]) + 0.8428 * x[3] * sympy.cos(x[0]) - 0.8869 * x[3] + 0.1398 * x[3] / x[4] - 0.6064 * x[4] * x[5] - 0.3668 * x[
                            5] * sympy.sin(x[1]) - 0.709 * x[5] + 0.9548 * sympy.sin(x[4]) - 0.7325 * sympy.cos(x[1]) + 0.7067 * sympy.cos(
            x[2]) - 0.5511 + 0.4911 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4059 * x[0] * x[4] + 0.3326 * x[0] - 0.3754 * x[2] * x[3] + 0.109 * x[2] * x[4] - 0.6046 * x[2] * sympy.cos(
            x[5]) - 0.5377 * x[3] * sympy.cos(x[0]) + 0.0661 * x[3] - 0.2427 * x[4] * sympy.sin(x[5]) + 0.7979 * x[5] * sympy.sin(
            x[1]) + 0.0596 * sympy.sin(x[1]) - 0.5691 * sympy.sin(x[5]) - 0.8759 * sympy.cos(x[1]) * sympy.cos(x[3]) - 0.2406 * sympy.cos(
            x[2]) - 0.8775 * sympy.cos(x[4]) + 0.8925


@register_eq_class
class sincosinv_nv6_nt68_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8043 * x[0] * x[4] + 0.5975 * x[0] + 0.9354 * x[1] * x[3] - 0.209 * x[1] * x[5] + 0.6394 * x[1] - 0.7544 * x[
            2] + 0.1502 * x[3] + 0.3818 * x[4] + 0.3482 * x[5] - 0.4052 * sympy.sin(x[3]) * sympy.sin(x[4]) - 0.9999 + 0.4825 * sympy.sin(
            x[1]) / x[2] - 0.0146 * sympy.cos(x[0]) / x[2] - 0.8506 * sympy.sin(x[3]) / x[0] + 0.8822 * sympy.cos(x[1]) / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0498 * x[0] - 0.6361 * x[0] / x[3] + 0.6009 * x[1] * x[5] - 0.5285 * x[1] * sympy.sin(x[4]) - 0.9382 * x[
            2] + 0.0438 * x[3] * x[4] + 0.7759 * x[3] - 0.9992 * x[4] * sympy.sin(x[5]) + 0.0365 * x[5] * sympy.sin(
            x[0]) + 0.6571 * sympy.sin(x[1]) + 0.8186 * sympy.sin(x[4]) * sympy.cos(x[2]) + 0.4705 * sympy.sin(x[4]) - 0.8426 + 0.0077 / x[
                            5] + 0.1031 * sympy.sin(x[0]) / x[4]


@register_eq_class
class sincosinv_nv6_nt68_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1063 * x[0] * sympy.cos(x[5]) + 0.7156 * x[0] + 0.5243 * x[1] * sympy.sin(x[5]) - 0.4936 * x[2] * x[4] - 0.2427 * \
                        x[2] + 0.5915 * x[3] * sympy.cos(x[0]) + 0.1038 * x[4] * sympy.sin(x[1]) + 0.5992 * x[4] - 0.7128 * x[
                            5] * sympy.cos(x[2]) - 0.2652 * x[5] - 0.0159 * sympy.sin(x[1]) + 0.2694 * sympy.sin(x[4]) * sympy.cos(
            x[0]) - 0.8151 - 0.5512 * sympy.cos(x[5]) / x[4] + 0.6473 / x[3]


@register_eq_class
class sincosinv_nv6_nt68_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.63 * x[0] - 0.0144 * x[1] * sympy.sin(x[2]) - 0.7673 * x[1] - 0.3158 * x[2] * x[5] - 0.0062 * x[2] + 0.0338 * x[
            3] * sympy.sin(x[1]) - 0.7765 * x[3] + 0.2417 * x[4] * sympy.sin(x[5]) - 0.778 * x[4] * sympy.cos(x[1]) + 0.0199 * x[
                            5] - 0.8875 * sympy.sin(x[4]) + 0.5893 * sympy.cos(x[1]) * sympy.cos(x[5]) + 0.1279 + 0.9673 / (
                                x[2] * x[3]) - 0.8229 * x[4] / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3315 * x[0] * x[3] - 0.0224 * x[1] / x[3] - 0.3835 * x[3] * sympy.sin(x[4]) - 0.0739 * x[3] - 0.7084 * x[4] * x[
            5] - 0.6403 * x[5] * sympy.sin(x[0]) - 0.21 * x[5] - 0.3609 * sympy.sin(x[1]) - 0.2896 * sympy.sin(x[2]) * sympy.sin(
            x[5]) - 0.8034 * sympy.sin(x[2]) + 0.5134 * sympy.sin(x[4]) * sympy.cos(x[1]) + 0.6532 * sympy.cos(x[0]) - 0.6544 * sympy.cos(
            x[4]) + 0.3506 - 0.3324 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv6_nt68_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0054 * x[0] * sympy.sin(x[2]) - 0.4446 * x[0] - 0.7156 * x[1] * x[2] + 0.31 * x[1] - 0.0259 * x[2] * x[
            3] + 0.358 * x[2] + 0.0007 * x[2] / x[5] - 0.5845 * x[4] * sympy.cos(x[1]) + 0.4909 * x[4] - 0.933 * x[5] * sympy.sin(
            x[0]) - 0.261 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.9883 * sympy.cos(x[3]) + 0.3888 * sympy.cos(
            x[5]) - 0.9759 + 0.0917 * sympy.sin(x[4]) / x[5]


@register_eq_class
class sincosinv_nv6_nt68_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0273 * x[0] / x[5] - 0.9897 * x[0] / x[4] + 0.6573 * x[1] + 0.2294 * x[1] / x[3] - 0.0005 * x[2] * x[3] - 0.0033 * \
                        x[2] * x[4] + 0.5583 * x[3] * x[5] - 0.9106 * x[5] + 0.5337 * sympy.sin(x[0]) * sympy.sin(
            x[3]) + 0.4339 * sympy.sin(x[3]) * sympy.sin(x[4]) + 0.9119 * sympy.sin(x[3]) - 0.8501 * sympy.sin(x[4]) + 0.198 * sympy.cos(
            x[2]) - 0.7581 - 0.6629 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.352 * x[0] * x[3] + 0.7723 * x[0] * sympy.cos(x[2]) + 0.1821 * x[0] - 0.0142 * x[0] / x[1] + 0.607 * x[1] * x[
            3] - 0.1781 * x[1] * sympy.cos(x[5]) + 0.4545 * x[1] - 0.5578 * x[2] * x[3] - 0.4195 * x[2] + 0.8011 * x[3] - 0.3064 * x[
                            4] * sympy.cos(x[3]) - 0.5462 * x[5] - 0.1954 * sympy.cos(x[4]) + 0.4997 - 0.349 * x[5] / x[4]


@register_eq_class
class sincosinv_nv6_nt68_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4366 * x[0] * x[2] - 0.847 * x[0] - 0.0995 * x[1] * x[3] - 0.138 * x[1] * x[4] - 0.4372 * x[1] - 0.0608 * x[
            2] + 0.1315 * x[4] * x[5] - 0.0357 * x[5] - 0.0413 * sympy.sin(x[4]) + 0.9622 * sympy.cos(x[0]) * sympy.cos(
            x[4]) - 0.003 * sympy.cos(x[3]) + 0.2048 + 0.1885 * sympy.sin(x[2]) / x[5] - 0.4566 * sympy.sin(x[2]) / x[
                            4] + 0.8254 * sympy.sin(x[3]) / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8643 * x[0] * x[1] - 0.5222 * x[0] / x[3] + 0.0876 * x[1] + 0.5756 * x[2] * sympy.cos(x[0]) + 0.7278 * x[
            2] + 0.819 * x[4] * sympy.cos(x[2]) + 0.5714 * x[4] * sympy.cos(x[3]) - 0.1067 * x[4] + 0.3411 * x[5] - 0.3365 * sympy.sin(
            x[0]) - 0.1206 - 0.7276 * sympy.sin(x[0]) / x[5] + 0.3077 / x[3] - 0.8938 * sympy.cos(x[3]) / x[1] - 0.5221 * x[4] / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1831 * x[0] * sympy.cos(x[5]) - 0.7734 * x[0] / x[3] - 0.533 * x[1] * x[4] + 0.452 * x[1] - 0.5458 * x[1] / x[
            3] - 0.1662 * x[2] * x[3] + 0.9142 * x[4] * sympy.sin(x[3]) - 0.8673 * x[4] - 0.8521 * x[5] * sympy.cos(x[4]) - 0.1284 * x[
                            5] - 0.9902 * sympy.sin(x[3]) - 0.3226 * sympy.cos(x[0]) - 0.5875 - 0.8761 / x[2] + 0.6158 * x[1] / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7145 * x[0] * sympy.sin(x[1]) + 0.9085 * x[1] * sympy.sin(x[4]) - 0.8709 * x[2] * x[4] + 0.3523 * x[2] - 0.3181 * \
                        x[3] * x[5] - 0.9314 * x[3] * sympy.sin(x[4]) - 0.257 * x[3] * sympy.cos(x[0]) + 0.9531 * x[3] * sympy.cos(
            x[1]) + 0.3655 * x[4] + 0.5277 * x[5] * sympy.cos(x[1]) + 0.2283 * sympy.cos(x[0]) + 0.9431 * sympy.cos(
            x[1]) - 0.0645 * sympy.cos(x[5]) - 0.1147 + 0.5761 / x[3]


@register_eq_class
class sincosinv_nv6_nt68_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0345 * x[0] * sympy.sin(x[3]) - 0.0641 * x[0] * sympy.sin(x[4]) + 0.8901 * x[1] * x[5] + 0.613 * x[1] * sympy.sin(
            x[4]) + 0.8822 * x[2] * sympy.sin(x[3]) + 0.0302 * x[2] / x[5] + 0.0557 * x[3] * sympy.cos(x[1]) + 0.4625 * x[3] - 0.5696 * x[
                            4] + 0.1001 * sympy.sin(x[2]) + 0.4377 * sympy.sin(x[5]) - 0.6907 * sympy.cos(x[0]) - 0.3174 * sympy.cos(
            x[1]) + 0.693 - 0.1938 * x[5] / x[3]


@register_eq_class
class sincosinv_nv6_nt68_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0108 * x[0] + 0.5651 * x[1] * x[2] - 0.0166 * x[1] * x[5] + 0.1424 * x[1] - 0.4995 * x[3] * sympy.sin(
            x[5]) - 0.9223 * x[3] * sympy.cos(x[1]) - 0.8003 * x[3] * sympy.cos(x[4]) - 0.1394 * x[5] * sympy.sin(x[4]) + 0.5594 * x[
                            5] + 0.1777 * sympy.sin(x[3]) - 0.0429 * sympy.sin(x[4]) - 0.0759 * sympy.cos(
            x[2]) + 0.761 - 0.2796 * sympy.sin(x[4]) / x[1] + 0.3348 * sympy.cos(x[3]) / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1173 * x[0] * x[2] + 0.7866 * x[0] * x[4] - 0.4052 * x[0] - 0.3495 * x[1] * sympy.sin(x[4]) + 0.6237 * x[
            1] * sympy.cos(x[0]) - 0.2192 * x[1] + 0.6803 * x[2] - 0.4123 * x[4] * sympy.sin(x[3]) + 0.076 * x[5] * sympy.cos(
            x[2]) + 0.0967 * x[5] + 0.7369 * sympy.sin(x[3]) * sympy.cos(x[1]) + 0.9047 * sympy.sin(x[5]) * sympy.cos(
            x[1]) - 0.5165 - 0.8407 / x[4] - 0.9091 / x[3]


@register_eq_class
class sincosinv_nv6_nt68_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9746 * x[0] * sympy.cos(x[1]) - 0.4334 * x[0] * sympy.cos(x[4]) - 0.6701 * x[0] - 0.4099 * x[1] * x[2] + 0.3309 * \
                        x[1] - 0.7157 * x[2] * x[5] - 0.794 * x[4] - 0.5362 * sympy.sin(x[1]) * sympy.sin(x[5]) + 0.4518 * sympy.sin(
            x[2]) + 0.4259 * sympy.sin(x[3]) - 0.7377 * sympy.sin(x[5]) * sympy.cos(x[3]) - 0.1846 * sympy.sin(
            x[5]) - 0.0694 + 0.9931 * sympy.cos(x[0]) / x[3] - 0.205 * sympy.sin(x[4]) / x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2189 * x[0] * x[3] - 0.0322 * x[0] * sympy.sin(x[2]) - 0.0542 * x[0] * sympy.cos(x[1]) - 0.4996 * x[1] * x[
            4] + 0.6854 * x[1] * x[5] - 0.1495 * x[1] + 0.1598 * x[2] * sympy.sin(x[3]) - 0.8116 * x[2] - 0.9731 * x[3] + 0.399 * sympy.sin(
            x[4]) - 0.697 * sympy.cos(x[5]) + 0.0198 - 0.9825 * sympy.sin(x[5]) / x[3] + 0.2422 * sympy.sin(x[5]) / x[2] + 0.019 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9007 * x[0] * x[4] + 0.1817 * x[0] * sympy.cos(x[3]) - 0.823 * x[0] + 0.3951 * x[1] * sympy.sin(x[0]) - 0.267 * \
                        x[1] * sympy.sin(x[2]) - 0.4703 * x[1] + 0.5016 * x[2] * sympy.sin(x[0]) + 0.4016 * x[2] + 0.0238 * x[
                            4] - 0.395 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.1276 * sympy.sin(x[4]) * sympy.cos(
            x[2]) - 0.6281 * sympy.cos(x[3]) - 0.818 * sympy.cos(x[5]) + 0.3467 - 0.1821 * x[5] / x[4]


@register_eq_class
class sincosinv_nv6_nt68_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8946 * x[0] * x[4] + 0.5152 * x[0] + 0.7558 * x[2] / x[5] - 0.2484 * x[3] * x[4] + 0.225 * x[4] * sympy.cos(
            x[5]) + 0.6966 * x[5] - 0.1932 * sympy.sin(x[1]) * sympy.sin(x[3]) - 0.2585 * sympy.sin(x[1]) * sympy.cos(
            x[4]) + 0.2211 * sympy.sin(x[1]) + 0.2693 * sympy.sin(x[4]) - 0.428 * sympy.cos(x[3]) * sympy.cos(x[5]) + 0.4648 * sympy.cos(
            x[3]) - 0.1699 + 0.0702 * x[4] / x[2] - 0.0776 / x[2]


@register_eq_class
class sincosinv_nv6_nt68_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8624 * x[0] * sympy.cos(x[1]) + 0.308 * x[0] + 0.8727 * x[0] / x[3] + 0.6214 * x[1] + 0.2402 * x[2] * x[
            3] - 0.6441 * x[2] * x[4] + 0.297 * x[2] + 0.002 * x[3] - 0.8112 * x[4] * x[5] + 0.5007 * x[4] * sympy.sin(x[1]) - 0.7944 * x[
                            4] + 0.582 * x[5] + 0.56 * sympy.sin(x[2]) * sympy.cos(x[5]) - 0.9388 - 0.5054 * x[2] / x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5438 * x[0] * x[3] - 0.1937 * x[0] * x[4] + 0.8463 * x[0] - 0.1052 * x[1] * x[3] - 0.6285 * x[2] - 0.6677 * x[
            3] - 0.6066 * x[5] + 0.2411 * sympy.sin(x[1]) * sympy.sin(x[5]) + 0.4395 * sympy.sin(x[1]) + 0.0261 * sympy.sin(
            x[2]) * sympy.cos(x[5]) - 0.3327 * sympy.sin(x[4]) - 0.6811 + 0.364 * sympy.cos(x[0]) / x[5] - 0.8574 * x[1] / x[0] - 0.5385 / (
                                x[0] * x[2])


@register_eq_class
class sincosinv_nv6_nt68_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5572 * x[0] * x[2] - 0.5325 * x[0] * sympy.sin(x[5]) - 0.5437 * x[0] - 0.0411 * x[0] / x[3] - 0.2289 * x[1] * x[
            5] - 0.2565 * x[1] + 0.6852 * x[2] * sympy.sin(x[1]) + 0.7447 * x[2] + 0.1638 * x[4] + 0.3704 * sympy.sin(
            x[3]) - 0.7459 * sympy.sin(x[5]) * sympy.cos(x[4]) + 0.2362 * sympy.sin(x[5]) - 0.2618 * sympy.cos(x[1]) * sympy.cos(
            x[3]) - 0.0573 - 0.4228 / (x[3] * x[5])


@register_eq_class
class sincosinv_nv6_nt68_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4731 * x[1] * x[5] - 0.1847 * x[1] - 0.7132 * x[1] / x[4] - 0.7849 * x[2] * x[5] - 0.8725 * x[2] * sympy.sin(
            x[0]) + 0.2748 * x[3] * x[5] + 0.9961 * sympy.sin(x[0]) + 0.5433 * sympy.sin(x[2]) + 0.7041 * sympy.sin(
            x[4]) + 0.1876 * sympy.sin(x[5]) - 0.5382 * sympy.cos(x[0]) * sympy.cos(x[3]) + 0.8776 * sympy.cos(x[3]) + 0.4808 + 0.7773 * x[
                            3] / x[2] + 0.4744 * x[2] / x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2232 * x[0] * x[5] + 0.7867 * x[1] + 0.4263 * x[3] - 0.1935 * x[4] + 0.4318 * x[5] * sympy.sin(
            x[3]) - 0.8203 * sympy.sin(x[0]) + 0.9005 * sympy.cos(x[2]) - 0.6242 + 0.4853 * sympy.cos(x[2]) / x[5] + 0.2617 / x[
                            5] - 0.2118 * sympy.sin(x[5]) / x[4] + 0.2801 * sympy.cos(x[3]) / x[2] - 0.1439 * x[2] / x[
                            1] + 0.5642 * sympy.sin(x[4]) / x[1] + 0.7572 * sympy.cos(x[4]) / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.386 * x[0] * sympy.sin(x[2]) + 0.1726 * x[0] - 0.0039 * x[0] / x[5] + 0.3491 * x[1] * sympy.sin(x[0]) - 0.834 * \
                        x[1] * sympy.cos(x[2]) + 0.7613 * x[1] - 0.9847 * x[1] / x[3] - 0.3758 * x[2] * x[5] - 0.5082 * x[3] * sympy.sin(
            x[4]) + 0.421 * x[4] * sympy.cos(x[1]) - 0.399 * x[4] + 0.5405 * x[5] - 0.9091 * sympy.sin(x[3]) + 0.8504 - 0.6434 / x[2]


@register_eq_class
class sincosinv_nv6_nt68_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3067 * x[0] * sympy.cos(x[1]) + 0.334 * x[0] / x[3] - 0.0608 * x[1] * sympy.sin(x[3]) - 0.803 * x[2] + 0.63 * x[
            2] / x[5] + 0.6891 * x[3] + 0.3306 * x[4] * x[5] - 0.4746 * x[5] + 0.2095 * sympy.sin(x[0]) + 0.2214 * sympy.sin(
            x[1]) * sympy.sin(x[2]) + 0.9814 * sympy.sin(x[4]) + 0.0737 + 0.1333 * sympy.sin(x[1]) / x[4] + 0.1328 * x[3] / x[2] + 0.6436 / \
                        x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.468 * x[0] * sympy.sin(x[3]) + 0.5313 * x[1] * sympy.cos(x[5]) - 0.6164 * x[1] + 0.198 * x[2] * x[4] + 0.1175 * \
                        x[4] * sympy.sin(x[5]) - 0.4843 * x[4] * sympy.cos(x[1]) + 0.0603 * sympy.sin(x[0]) * sympy.cos(
            x[1]) + 0.882 * sympy.sin(x[0]) * sympy.cos(x[2]) + 0.5322 * sympy.cos(x[2]) + 0.7376 * sympy.cos(x[4]) - 0.6273 * sympy.cos(
            x[5]) - 0.9245 + 0.559 / x[3] + 0.6755 * x[5] / x[2] + 0.9864 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3386 * x[0] * x[4] + 0.7638 * x[0] * sympy.sin(x[2]) - 0.5427 * x[0] * sympy.cos(x[1]) - 0.5585 * x[0] - 0.2994 * \
                        x[1] * sympy.sin(x[5]) - 0.6712 * x[1] * sympy.cos(x[3]) + 0.8855 * x[2] * x[4] + 0.2112 * sympy.sin(
            x[1]) + 0.0057 * sympy.cos(x[5]) - 0.8858 - 0.6359 / x[4] - 0.7383 / x[3] - 0.2421 * sympy.sin(x[1]) / x[2] - 0.4808 / x[
                            2] - 0.7396 / (x[2] * x[5])


@register_eq_class
class sincosinv_nv6_nt68_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2423 * x[0] / x[3] - 0.1149 * x[2] + 0.165 * x[3] * x[4] + 0.4043 * x[3] * x[5] + 0.5914 * x[3] * sympy.cos(
            x[2]) - 0.9921 * x[4] * x[5] + 0.1486 * x[5] + 0.942 * sympy.sin(x[0]) * sympy.sin(x[5]) - 0.5176 * sympy.sin(
            x[0]) - 0.284 * sympy.sin(x[1]) + 0.697 * sympy.cos(x[3]) - 0.0413 - 0.4617 * sympy.sin(x[1]) / x[5] + 0.2576 * sympy.sin(
            x[2]) / x[5] - 0.7757 / x[4]


@register_eq_class
class sincosinv_nv6_nt68_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5602 * x[0] * x[5] - 0.615 * x[0] * sympy.sin(x[1]) - 0.3622 * x[0] * sympy.cos(x[2]) + 0.494 * x[0] + 0.9467 * \
                        x[3] * x[4] + 0.7877 * x[4] + 0.7972 * x[5] - 0.3837 * sympy.sin(x[1]) + 0.2172 * sympy.cos(x[0]) * sympy.cos(
            x[3]) - 0.1667 * sympy.cos(x[3]) - 0.0566 - 0.7662 * x[5] / x[4] - 0.7008 * x[5] / x[3] - 0.5115 / x[2] - 0.2946 * sympy.cos(
            x[5]) / x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9479 * x[0] * x[4] + 0.1945 * x[0] + 0.2748 * x[0] / x[2] + 0.8618 * x[1] * x[5] + 0.7415 * x[1] / x[4] + 0.1396 * \
                        x[2] * sympy.sin(x[4]) - 0.2955 * x[2] * sympy.cos(x[5]) + 0.3702 * x[2] - 0.2809 * x[4] * x[5] - 0.0592 * x[
                            4] - 0.5501 * x[5] + 0.1767 * sympy.sin(x[1]) + 0.5543 * sympy.sin(x[3]) - 0.9509 - 0.9084 * x[4] / x[3]


@register_eq_class
class sincosinv_nv6_nt68_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2059 * x[0] - 0.9968 * x[1] / x[2] + 0.9717 * x[2] - 0.5877 * x[3] * sympy.sin(x[0]) + 0.9357 * x[3] + 0.3287 * \
                        x[5] * sympy.sin(x[1]) - 0.9597 * x[5] - 0.6586 * sympy.sin(x[1]) * sympy.cos(x[4]) - 0.0768 * sympy.sin(
            x[1]) - 0.9381 * sympy.sin(x[4]) - 0.6152 * sympy.cos(x[0]) * sympy.cos(x[1]) - 0.9253 * sympy.cos(x[2]) * sympy.cos(
            x[3]) - 0.1442 * sympy.cos(x[2]) * sympy.cos(x[5]) - 0.0553 * sympy.cos(x[3]) * sympy.cos(x[5]) - 0.3134


@register_eq_class
class sincosinv_nv6_nt68_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6135 * x[0] / x[1] + 0.0905 * x[1] * x[5] - 0.4305 * x[1] - 0.0276 * x[2] * sympy.sin(x[4]) - 0.6855 * x[
            2] - 0.097 * x[3] * x[4] - 0.9496 * x[3] * sympy.sin(x[0]) + 0.7223 * sympy.sin(x[1]) * sympy.cos(x[3]) + 0.7398 * sympy.sin(
            x[3]) - 0.5802 * sympy.cos(x[0]) - 0.9212 * sympy.cos(x[4]) - 0.2588 + 0.6727 / x[5] - 0.3511 * sympy.cos(x[2]) / x[
                            3] - 0.3623 / (x[1] * x[4])


@register_eq_class
class sincosinv_nv6_nt68_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.3315 * x[0] * sympy.sin(x[4]) - 0.695 * x[0] * sympy.cos(x[5]) - 0.0747 * x[1] + 0.2818 * x[1] / x[5] - 0.9185 * \
                        x[1] / x[2] + 0.6057 * x[2] - 0.0627 * x[3] + 0.8969 * x[4] * sympy.sin(x[3]) + 0.3206 * x[5] * sympy.sin(
            x[4]) + 0.9798 * x[5] * sympy.cos(x[2]) - 0.9972 * sympy.sin(x[2]) * sympy.cos(x[3]) - 0.1989 * sympy.sin(
            x[4]) + 0.0064 * sympy.sin(x[5]) + 0.3388 - 0.6935 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1132 * x[0] * sympy.cos(x[1]) + 0.1613 * x[2] * sympy.cos(x[1]) - 0.4923 * x[2] * sympy.cos(x[3]) - 0.6485 * x[
            2] + 0.0493 * x[4] + 0.22 * x[5] * sympy.cos(x[0]) - 0.9008 * sympy.sin(x[0]) * sympy.cos(x[2]) - 0.3572 * sympy.sin(
            x[1]) - 0.1323 * sympy.cos(x[4]) * sympy.cos(x[5]) + 0.9127 - 0.2167 / x[5] - 0.5088 / x[3] + 0.5074 * sympy.sin(x[4]) / x[
                            2] + 0.9884 * sympy.sin(x[4]) / x[0] + 0.0077 / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9208 * x[0] * sympy.sin(x[3]) + 0.648 * x[0] + 0.3389 * x[1] / x[3] - 0.2778 * x[2] * x[3] + 0.9803 * x[2] / x[
            5] - 0.6503 * x[3] - 0.6431 * x[4] * sympy.sin(x[0]) - 0.1158 * x[4] + 0.8091 * x[5] - 0.9915 * sympy.sin(x[0]) * sympy.cos(
            x[5]) - 0.4371 * sympy.sin(x[1]) + 0.6932 + 0.4485 / x[2] + 0.4404 * sympy.sin(x[2]) / x[1] + 0.4813 * x[2] / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7247 * x[0] * sympy.sin(x[4]) - 0.1045 * x[0] - 0.1967 * x[1] * x[4] + 0.7378 * x[2] * sympy.cos(x[4]) + 0.4684 * \
                        x[2] + 0.5734 * x[3] * x[4] - 0.7243 * x[4] + 0.6531 * x[5] + 0.115 * sympy.cos(x[1]) * sympy.cos(
            x[3]) - 0.8588 * sympy.cos(x[1]) - 0.9844 * sympy.cos(x[3]) + 0.0085 * sympy.cos(x[4]) * sympy.cos(
            x[5]) + 0.2254 + 0.8783 * sympy.sin(x[5]) / x[3] + 0.2499 * x[5] / x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9847 * x[1] * x[2] - 0.8099 * x[1] * sympy.cos(x[5]) + 0.6727 * x[1] - 0.3178 * x[3] * sympy.cos(x[0]) - 0.2721 * \
                        x[3] + 0.7038 * x[4] * sympy.sin(x[2]) - 0.7332 * x[5] * sympy.sin(x[4]) + 0.2075 * x[5] - 0.2527 * sympy.cos(
            x[0]) - 0.1597 - 0.2582 * sympy.sin(x[2]) / x[5] + 0.5446 / x[4] + 0.2774 * sympy.cos(x[5]) / x[3] - 0.1504 / x[2] - 0.4512 * x[
                            3] / x[1]


@register_eq_class
class sincosinv_nv6_nt68_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0698 * x[1] * sympy.sin(x[4]) - 0.3692 * x[3] * x[4] - 0.2569 * x[3] + 0.732 * x[4] - 0.851 * x[5] * sympy.sin(
            x[4]) + 0.3903 * sympy.sin(x[0]) - 0.62 * sympy.sin(x[1]) - 0.0312 * sympy.sin(x[2]) * sympy.sin(x[3]) - 0.2198 * sympy.sin(
            x[2]) * sympy.sin(x[5]) + 0.7185 * sympy.sin(x[3]) * sympy.cos(x[5]) + 0.9675 * sympy.cos(x[2]) + 0.0712 * sympy.cos(
            x[5]) - 0.4255 + 0.6542 * sympy.sin(x[2]) / x[1] - 0.0718 / (x[0] * x[2])


@register_eq_class
class sincosinv_nv6_nt68_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9269 * x[0] * x[4] - 0.6393 * x[0] - 0.7046 * x[0] / x[3] + 0.894 * x[1] + 0.8519 * x[2] * x[3] + 0.5938 * x[
            2] + 0.0202 * x[3] * sympy.sin(x[4]) - 0.2642 * x[4] - 0.6233 * x[5] * sympy.cos(x[1]) + 0.2408 * sympy.sin(
            x[3]) - 0.7808 * sympy.cos(x[4]) * sympy.cos(x[5]) - 0.3065 * sympy.cos(x[5]) + 0.4971 + 0.9087 * sympy.sin(x[1]) / x[
                            0] - 0.3764 * sympy.sin(x[2]) / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5649 * x[0] * sympy.sin(x[1]) - 0.3305 * x[0] * sympy.sin(x[4]) - 0.4424 * x[0] + 0.1906 * x[1] + 0.7172 * x[
            2] * sympy.sin(x[5]) + 0.9694 * x[2] - 0.7068 * x[3] + 0.4556 * x[4] * x[5] + 0.8096 * x[4] - 0.5497 * x[
                            5] - 0.1761 - 0.7262 * sympy.sin(x[1]) / x[5] - 0.9237 * sympy.cos(x[1]) / x[4] + 0.583 * sympy.cos(x[2]) / x[
                            1] - 0.0972 * x[2] / x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4844 * x[0] * x[1] - 0.9092 * x[0] - 0.5001 * x[1] * sympy.sin(x[5]) + 0.9148 * x[1] + 0.9926 * x[4] * sympy.sin(
            x[5]) - 0.3356 * x[4] + 0.5281 * x[5] * sympy.sin(x[0]) - 0.8672 * x[5] * sympy.sin(x[2]) - 0.2842 * x[5] - 0.5869 * sympy.sin(
            x[0]) * sympy.cos(x[4]) - 0.226 * sympy.sin(x[3]) + 0.0459 * sympy.sin(x[4]) * sympy.cos(x[1]) - 0.5314 * sympy.cos(
            x[2]) - 0.5096 + 0.0618 * x[4] / x[2]


@register_eq_class
class sincosinv_nv6_nt68_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.407 * x[0] + 0.1931 * x[0] / x[4] + 0.7974 * x[1] + 0.3679 * x[2] + 0.931 * x[2] / x[3] - 0.8067 * x[3] - 0.0105 * \
                        x[4] * sympy.sin(x[1]) - 0.8748 * x[5] * sympy.sin(x[1]) - 0.2458 * x[5] - 0.9641 * sympy.sin(x[3]) * sympy.cos(
            x[4]) + 0.4405 * sympy.cos(x[4]) + 0.0707 + 0.7679 * sympy.sin(x[2]) / x[4] - 0.8553 * sympy.cos(x[0]) / x[2] - 0.0567 * x[5] / \
                        x[0]


@register_eq_class
class sincosinv_nv6_nt68_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv6_nt68_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9965 * x[0] * sympy.cos(x[5]) - 0.8465 * x[0] / x[1] - 0.2624 * x[1] / x[4] - 0.2185 * x[5] * sympy.cos(
            x[2]) - 0.3176 * x[5] - 0.9194 * sympy.sin(x[0]) * sympy.sin(x[3]) + 0.2616 * sympy.sin(x[0]) - 0.916 * sympy.sin(
            x[1]) - 0.9808 * sympy.sin(x[2]) - 0.9171 * sympy.sin(x[4]) + 0.5176 * sympy.cos(x[1]) * sympy.cos(x[5]) + 0.1839 + 0.2956 / x[
                            3] + 0.9446 * x[4] / x[2] - 0.8036 / (x[1] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_46(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0326 * x[0] / x[4] + 0.2109 * x[1] * x[3] + 0.0217 * x[2] * x[4] - 0.3365 * x[2] - 0.5747 * x[3] - 0.9017 * x[
            4] + 0.601 * x[5] + 0.5539 - 0.8628 / (x[2] * x[5]) + 0.6309 * x[4] / x[1] - 0.488 * x[5] / x[1] + 0.2961 / x[1] - 0.5877 / (
                                x[1] * x[2]) + 0.7263 * x[1] / x[0] + 0.5832 * x[2] / x[0] - 0.6562 * x[5] / x[0] - 0.962 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_0(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.9233 * x[0] / x[2] + 0.4064 * x[1] * x[2] + 0.2868 * x[1] * x[4] + 0.4431 * x[1] + 0.5506 * x[2] - 0.2554 * x[
            2] / x[5] - 0.6028 * x[3] - 0.9684 * x[4] * x[5] + 0.2101 * x[4] + 0.6706 - 0.1312 / x[5] + 0.4409 * x[4] / x[3] + 0.8088 / (
                                x[3] * x[5]) - 0.5001 * x[3] / x[1] + 0.2705 * x[1] / x[0] + 0.8766 / x[0] - 0.602 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_35(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8396 * x[0] * x[3] - 0.6742 * x[0] / x[5] + 0.8945 * x[1] * x[4] + 0.5639 * x[3] - 0.5199 * x[3] / x[5] + 0.4565 * \
                        x[3] / x[4] + 0.0011 * x[4] - 0.1753 * x[5] + 0.9407 - 0.1151 * x[5] / x[4] + 0.4368 * x[4] / x[2] - 0.1188 / x[
                            2] + 0.6228 / (x[2] * x[3]) + 0.5373 * x[2] / x[1] - 0.8312 / x[1] + 0.271 / (x[1] * x[3]) - 0.5248 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_8(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4644 * x[0] * x[4] + 0.9301 * x[0] * x[5] + 0.2891 * x[0] / x[3] - 0.2987 * x[1] * x[4] + 0.2448 * x[1] - 0.2437 * \
                        x[1] / x[5] + 0.2527 * x[2] * x[5] - 0.9279 * x[3] - 0.6855 * x[4] / x[5] + 0.4648 * x[5] - 0.7085 - 0.4835 / x[
                            4] + 0.1391 * x[3] / x[2] - 0.7024 / x[2] + 0.3655 * x[2] / x[1] + 0.1227 / x[0] - 0.0974 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_42(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1968 * x[0] - 0.7978 * x[0] / x[5] + 0.0821 * x[0] / x[4] - 0.6053 * x[0] / x[2] + 0.7217 * x[2] * x[3] - 0.8129 * \
                        x[2] / x[5] + 0.6996 * x[3] + 0.1099 + 0.0533 / x[5] - 0.6822 * x[5] / x[4] + 0.249 / x[4] + 0.811 * x[5] / x[
                            3] + 0.2034 * x[4] / x[2] - 0.9298 / x[2] - 0.6912 * x[4] / x[1] + 0.1159 * x[5] / x[1] - 0.6477 / x[1]


@register_eq_class
class inv_nv6_nt610_prog_33(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1316 * x[0] / x[5] + 0.3631 * x[1] + 0.1965 * x[1] / x[5] + 0.7685 * x[1] / x[2] + 0.9412 * x[2] * x[
            3] - 0.8569 * x[2] * x[4] + 0.5419 * x[2] - 0.2007 * x[3] / x[4] + 0.8452 * x[4] - 0.4154 - 0.3089 / x[5] - 0.9906 / x[
                            3] - 0.4448 / (x[3] * x[5]) + 0.7994 * x[5] / x[2] + 0.7919 * x[2] / x[0] + 0.7158 / x[0] + 0.2582 / (
                                x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_20(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8971 * x[0] * x[2] + 0.2184 * x[0] + 0.1696 * x[0] / x[3] - 0.4916 * x[0] / x[1] + 0.5153 * x[1] + 0.7182 * x[1] / \
                        x[4] + 0.3065 * x[1] / x[3] + 0.8985 * x[2] - 0.5563 * x[3] / x[4] + 0.0864 * x[4] + 0.9885 * x[4] / x[5] + 0.0675 * \
                        x[5] + 0.9386 + 0.1348 / x[3] + 0.6002 * x[4] / x[2] - 0.5415 / (x[2] * x[3]) + 0.1727 / (x[1] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_14(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.3205 * x[0] * x[1] - 0.7821 * x[0] * x[3] - 0.0149 * x[1] - 0.697 * x[2] / x[4] - 0.1096 * x[3] - 0.6498 * x[3] / \
                        x[5] - 0.3135 * x[5] - 0.884 - 0.7053 / x[4] + 0.2854 / (x[4] * x[5]) - 0.9222 * x[5] / x[2] + 0.9716 / x[
                            2] + 0.7092 / (x[2] * x[3]) - 0.5722 * x[3] / x[1] + 0.1841 * x[4] / x[1] + 0.4315 * x[4] / x[0] - 0.8026 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_31(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7813 * x[0] * x[3] + 0.6586 * x[0] / x[5] + 0.8598 * x[1] * x[2] + 0.5728 * x[1] * x[5] + 0.1 * x[2] * x[
            4] + 0.8286 * x[2] + 0.8543 * x[3] * x[5] - 0.0067 * x[4] + 0.4231 * x[5] - 0.3637 + 0.2201 / x[3] + 0.4297 / (
                                x[2] * x[5]) + 0.1509 / x[1] + 0.1596 * x[1] / x[0] + 0.6201 * x[2] / x[0] + 0.077 * x[4] / x[
                            0] + 0.7981 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_48(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6176 * x[0] * x[1] - 0.8508 * x[0] * x[2] + 0.0602 * x[0] * x[4] + 0.6048 * x[1] / x[4] - 0.3957 * x[2] + 0.1871 * \
                        x[3] * x[4] + 0.2694 * x[3] * x[5] - 0.9884 * x[3] + 0.0661 * x[5] + 0.8215 - 0.9522 / x[4] - 0.47 / (
                                x[2] * x[3]) - 0.2535 * x[2] / x[1] + 0.0308 * x[5] / x[1] + 0.4147 / x[1] - 0.1194 / x[0] + 0.7972 / (
                                x[0] * x[5])


@register_eq_class
class inv_nv6_nt610_prog_41(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.2559 * x[0] * x[3] - 0.8464 * x[0] * x[5] + 0.3876 * x[0] / x[1] + 0.1437 * x[1] / x[2] - 0.981 * x[2] / x[
            5] + 0.045 * x[3] * x[4] + 0.5674 * x[3] + 0.0825 * x[4] - 0.5051 - 0.0584 / x[5] + 0.7723 * x[5] / x[4] + 0.3609 / x[
                            2] - 0.8001 * x[5] / x[1] + 0.6731 / x[1] + 0.9285 / (x[1] * x[4]) - 0.7567 * x[4] / x[0] + 0.6423 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_7(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1351 * x[0] + 0.6349 * x[1] * x[2] + 0.9516 * x[1] / x[3] - 0.4203 * x[2] / x[5] + 0.0587 * x[3] / x[
            4] + 0.3751 * x[4] / x[5] - 0.9935 * x[5] - 0.909 + 0.9563 / x[4] + 0.7759 / x[3] + 0.8765 / x[2] - 0.105 * x[4] / x[
                            1] - 0.8137 * x[5] / x[1] + 0.0972 / x[1] + 0.4961 * x[2] / x[0] + 0.4668 * x[3] / x[0] - 0.4218 * x[4] / x[0]


@register_eq_class
class inv_nv6_nt610_prog_37(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.258 * x[0] * x[1] - 0.8526 * x[0] + 0.4047 * x[1] * x[5] - 0.1562 * x[1] - 0.2548 * x[5] + 0.9908 + 0.4484 * x[
            5] / x[4] + 0.7758 / x[4] - 0.0276 * x[5] / x[3] + 0.0828 / x[3] + 0.7679 / (x[3] * x[4]) - 0.2704 * x[5] / x[2] + 0.7826 / x[
                            2] - 0.7216 / (x[2] * x[4]) + 0.9018 * x[2] / x[1] - 0.5408 * x[5] / x[0] - 0.1609 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_15(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4015 * x[0] * x[2] - 0.319 * x[0] - 0.7498 * x[0] / x[4] - 0.7974 * x[1] + 0.481 * x[1] / x[5] + 0.1587 * x[2] / \
                        x[4] - 0.1027 * x[3] / x[5] + 0.9223 * x[4] * x[5] + 0.5545 * x[4] + 0.0096 - 0.7712 / x[5] - 0.8625 / x[
                            3] - 0.071 * x[3] / x[2] - 0.7431 / x[2] + 0.8513 / (x[1] * x[3]) + 0.5348 / (x[1] * x[2]) + 0.7144 * x[5] / x[
                            0]


@register_eq_class
class inv_nv6_nt610_prog_23(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9694 * x[1] / x[4] - 0.0218 * x[1] / x[3] + 0.3413 * x[2] * x[4] - 0.0438 * x[3] + 0.3586 * x[3] / x[4] - 0.8946 * \
                        x[4] - 0.0548 * x[4] / x[5] - 0.2679 - 0.1717 / x[5] - 0.0592 / x[2] - 0.4166 * x[2] / x[1] - 0.6803 / x[
                            1] + 0.207 / x[0] + 0.8178 / (x[0] * x[5]) + 0.3712 / (x[0] * x[4]) + 0.5057 / (x[0] * x[3]) + 0.6187 / (
                                x[0] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_30(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.6343 * x[0] * x[1] - 0.7946 * x[0] * x[4] - 0.178 * x[2] * x[3] - 0.234 * x[2] / x[5] + 0.2191 * x[3] - 0.3916 * \
                        x[3] / x[4] + 0.265 + 0.2753 / x[5] + 0.7579 / x[4] - 0.5283 / (x[4] * x[5]) - 0.6333 / (x[3] * x[5]) + 0.7129 / x[
                            2] + 0.3621 * x[3] / x[1] - 0.144 / x[1] - 0.8241 * x[3] / x[0] + 0.9735 * x[5] / x[0] - 0.9713 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_28(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7013 * x[0] * x[1] - 0.6533 * x[0] * x[2] + 0.3515 * x[1] / x[5] + 0.7493 * x[2] / x[5] - 0.6116 * x[3] * x[
            4] - 0.4999 * x[3] - 0.907 * x[3] / x[5] - 0.5288 * x[4] + 0.11 + 0.2234 / x[5] - 0.2747 / x[2] - 0.7791 / (
                                x[2] * x[3]) - 0.5526 / x[1] + 0.7469 / x[0] - 0.7139 / (x[0] * x[5]) + 0.2279 / (
                                x[0] * x[4]) - 0.7908 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_17(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8974 * x[0] * x[5] - 0.6836 * x[0] / x[1] - 0.0313 * x[1] * x[2] - 0.5039 * x[1] / x[5] - 0.7142 * x[2] * x[
            3] - 0.828 * x[5] + 0.8976 + 0.3028 / x[4] - 0.6582 * x[4] / x[3] + 0.2148 * x[5] / x[3] - 0.4005 / x[3] + 0.8097 * x[4] / x[
                            2] + 0.5856 / x[2] + 0.3764 * x[4] / x[1] + 0.5254 / x[1] + 0.2003 * x[4] / x[0] - 0.7267 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_43(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.8773 * x[1] / x[3] + 0.6872 * x[2] * x[3] - 0.4517 * x[3] * x[5] - 0.5967 * x[3] - 0.6697 * x[4] + 0.657 * x[4] / \
                        x[5] - 0.159 * x[5] - 0.4895 + 0.4352 * x[4] / x[3] - 0.5154 * x[4] / x[2] + 0.0822 / x[2] - 0.5417 * x[2] / x[
                            1] - 0.3318 * x[4] / x[1] - 0.7325 / x[1] - 0.2532 * x[2] / x[0] + 0.8895 / x[0] + 0.9679 / (x[0] * x[4])


@register_eq_class
class inv_nv6_nt610_prog_2(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5966 * x[0] * x[5] + 0.0918 * x[0] + 0.9383 * x[0] / x[2] + 0.7121 * x[1] * x[4] - 0.6836 * x[1] + 0.8873 * x[2] * \
                        x[4] + 0.2755 * x[2] * x[5] + 0.5951 * x[3] - 0.9736 + 0.2762 / x[5] + 0.4319 / x[4] - 0.0289 / (
                                x[4] * x[5]) - 0.6804 / (x[3] * x[5]) - 0.8935 / x[2] - 0.1278 * x[3] / x[1] + 0.9238 * x[1] / x[
                            0] - 0.9507 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_4(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1522 * x[0] + 0.578 * x[0] / x[5] - 0.233 * x[0] / x[3] + 0.3114 * x[1] * x[4] - 0.5612 * x[2] * x[3] + 0.7767 * \
                        x[2] - 0.5492 * x[3] * x[5] + 0.4085 * x[3] + 0.3261 * x[4] / x[5] - 0.8781 * x[5] + 0.8959 - 0.1089 / x[
                            4] + 0.1049 / (x[3] * x[4]) + 0.5063 * x[5] / x[2] + 0.5695 / x[1] + 0.8021 / (x[1] * x[3]) - 0.6897 * x[2] / x[
                            0]


@register_eq_class
class inv_nv6_nt610_prog_45(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0025 * x[0] - 0.8043 * x[1] * x[4] + 0.472 * x[1] + 0.2334 * x[2] * x[3] - 0.3626 * x[2] * x[5] - 0.9051 * x[2] / \
                        x[4] - 0.7721 * x[3] * x[5] + 0.2913 * x[4] + 0.9294 * x[4] / x[5] - 0.6384 * x[5] + 0.6717 - 0.6302 * x[4] / x[
                            3] - 0.5687 / x[3] + 0.9856 / x[2] - 0.3134 / (x[1] * x[3]) + 0.7096 * x[3] / x[0] + 0.4171 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_49(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1245 * x[0] * x[4] + 0.929 * x[0] / x[5] + 0.6826 * x[1] / x[5] - 0.4161 * x[2] - 0.3648 * x[3] - 0.4397 * x[3] / \
                        x[5] + 0.4904 * x[3] / x[4] + 0.0904 * x[5] + 0.6528 - 0.0134 / x[4] - 0.3699 * x[3] / x[2] + 0.1979 * x[5] / x[
                            2] - 0.5446 * x[3] / x[1] - 0.7038 / x[1] + 0.1668 / (x[1] * x[4]) - 0.4806 / x[0] + 0.6348 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_11(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.4269 * x[0] / x[4] + 0.0311 * x[0] / x[2] + 0.6691 * x[1] / x[5] - 0.6357 * x[1] / x[3] - 0.2225 * x[
            2] - 0.3998 * x[2] / x[4] - 0.3786 * x[2] / x[3] + 0.7164 * x[3] * x[4] + 0.6959 * x[3] - 0.6302 * x[4] + 0.6506 * x[4] / x[
                            5] - 0.2408 - 0.8629 / x[5] + 0.5417 / x[1] - 0.1138 / (x[1] * x[2]) - 0.2094 / x[0] - 0.1404 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_10(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0253 * x[0] + 0.4355 * x[0] / x[2] - 0.234 * x[1] + 0.024 * x[1] / x[5] + 0.1475 * x[1] / x[4] - 0.1032 * x[1] / \
                        x[3] + 0.1913 * x[2] / x[4] + 0.0402 * x[3] - 0.9471 * x[4] + 0.5086 + 0.4308 / x[5] + 0.6246 * x[5] / x[
                            3] + 0.1889 / (x[3] * x[4]) - 0.6831 / x[2] - 0.4659 * x[3] / x[0] + 0.104 / (x[0] * x[5]) - 0.6527 / (
                                x[0] * x[4])


@register_eq_class
class inv_nv6_nt610_prog_1(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.1607 * x[0] - 0.748 * x[0] / x[4] - 0.7417 * x[1] * x[2] - 0.3145 * x[2] * x[5] + 0.0888 * x[3] * x[5] + 0.9916 * \
                        x[3] - 0.7545 + 0.3458 / x[5] - 0.3248 / x[4] + 0.2925 / (x[4] * x[5]) + 0.8508 / (x[3] * x[4]) + 0.7662 * x[4] / x[
                            2] - 0.3269 / x[2] - 0.5308 / x[1] - 0.8652 * x[5] / x[0] - 0.3374 / (x[0] * x[2]) - 0.3326 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_40(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.6506 * x[0] * x[1] - 0.1815 * x[0] * x[5] + 0.6776 * x[0] - 0.8331 * x[1] / x[4] + 0.5 * x[2] * x[3] - 0.9923 * \
                        x[3] * x[4] - 0.7643 * x[3] + 0.9616 * x[4] - 0.6668 * x[5] + 0.274 - 0.6561 * x[5] / x[3] - 0.146 / x[
                            2] - 0.4145 / (x[2] * x[5]) - 0.3671 * x[3] / x[1] - 0.3694 / x[1] - 0.5411 / (x[1] * x[2]) + 0.6231 / (
                                x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_29(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1889 * x[0] * x[2] + 0.4377 * x[0] - 0.9695 * x[1] * x[4] - 0.8981 * x[1] * x[5] - 0.6993 * x[1] + 0.5178 * x[
            1] / x[2] - 0.5684 * x[2] * x[3] + 0.3762 * x[2] * x[4] - 0.8133 * x[2] + 0.8335 * x[2] / x[5] - 0.5001 * x[4] / x[5] + 0.2632 * \
                        x[5] + 0.3904 - 0.8977 / x[4] + 0.2034 / x[3] - 0.8815 * x[1] / x[0] + 0.7453 * x[3] / x[0]


@register_eq_class
class inv_nv6_nt610_prog_22(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7095 * x[0] * x[4] + 0.5402 * x[0] + 0.1919 * x[0] / x[5] - 0.2316 * x[1] * x[4] - 0.7728 * x[1] / x[3] + 0.6547 * \
                        x[3] + 0.8819 * x[4] + 0.5076 * x[4] / x[5] - 0.4334 * x[5] - 0.3142 + 0.347 / (x[3] * x[5]) + 0.8188 / x[
                            2] + 0.3854 / (x[2] * x[4]) - 0.051 * x[5] / x[1] + 0.9892 / x[1] - 0.2101 / (x[0] * x[2]) + 0.184 / (
                                x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_27(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.851 * x[0] + 0.5141 * x[0] / x[5] - 0.8116 * x[0] / x[4] + 0.4055 * x[0] / x[1] - 0.3256 * x[1] * x[5] - 0.7107 * \
                        x[1] - 0.6929 * x[2] + 0.2047 * x[3] - 0.8928 * x[4] * x[5] - 0.7794 * x[4] - 0.1133 * x[5] + 0.234 - 0.9262 / (
                                x[2] * x[5]) + 0.8677 / (x[2] * x[3]) - 0.0571 * x[3] / x[1] - 0.3722 / (x[1] * x[4]) - 0.0622 / (
                                x[1] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_34(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0472 * x[0] * x[2] + 0.3588 * x[0] / x[5] - 0.8449 * x[1] + 0.9461 * x[2] + 0.68 * x[2] / x[5] - 0.8981 * x[2] / \
                        x[3] - 0.4011 * x[3] + 0.5336 * x[4] + 0.9217 * x[5] - 0.8284 + 0.6327 / (x[3] * x[5]) + 0.8799 / (
                                x[3] * x[4]) - 0.4038 * x[4] / x[1] - 0.9774 * x[1] / x[0] + 0.1578 * x[3] / x[0] - 0.1295 / x[
                            0] + 0.4267 / (x[0] * x[4])


@register_eq_class
class inv_nv6_nt610_prog_16(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5299 * x[0] * x[1] - 0.0135 * x[0] * x[3] - 0.13 * x[0] * x[4] + 0.4232 * x[0] + 0.009 * x[0] / x[5] + 0.164 * x[
            1] * x[5] + 0.1897 * x[1] / x[2] - 0.08 * x[2] * x[5] + 0.0586 * x[2] - 0.6597 * x[2] / x[4] + 0.9402 * x[3] - 0.8538 * x[
                            4] + 0.966 - 0.896 / x[5] - 0.4619 / x[1] - 0.344 / (x[1] * x[3]) + 0.3568 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_13(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.7865 * x[0] * x[2] - 0.996 * x[0] * x[5] - 0.9206 * x[0] + 0.9091 * x[0] / x[4] - 0.6637 * x[1] * x[2] + 0.7388 * \
                        x[1] * x[4] - 0.6794 * x[1] / x[5] - 0.3247 * x[2] - 0.0575 * x[2] / x[5] + 0.6551 * x[3] - 0.1051 * x[4] - 0.7505 * \
                        x[5] + 0.0996 + 0.5946 * x[5] / x[4] - 0.2774 * x[4] / x[3] - 0.6743 * x[3] / x[1] - 0.2963 / x[1]


@register_eq_class
class inv_nv6_nt610_prog_47(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1652 * x[0] / x[5] + 0.0164 * x[0] / x[1] - 0.1572 * x[1] / x[3] + 0.9081 * x[2] / x[4] + 0.2027 * x[3] * x[
            4] - 0.9278 * x[3] * x[5] - 0.7255 * x[3] + 0.0602 - 0.202 / x[5] + 0.1706 / x[4] + 0.5734 / x[2] - 0.7314 * x[2] / x[
                            1] - 0.6474 * x[4] / x[1] - 0.1248 / x[1] - 0.6148 * x[4] / x[0] + 0.351 / x[0] - 0.3332 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_36(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.0084 * x[0] * x[4] + 0.8246 * x[1] * x[2] - 0.2996 * x[1] - 0.2557 * x[1] / x[5] - 0.0172 * x[1] / x[
            3] - 0.4841 * x[3] * x[5] + 0.2045 * x[4] * x[5] - 0.8468 * x[4] - 0.2833 + 0.8552 / x[5] + 0.9483 / x[3] - 0.0707 * x[3] / x[
                            2] + 0.4607 * x[5] / x[2] + 0.6289 / x[2] - 0.6057 * x[1] / x[0] + 0.1058 / x[0] - 0.3197 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_44(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.79 * x[0] + 0.856 * x[1] * x[3] - 0.745 * x[2] * x[3] - 0.247 * x[3] * x[5] + 0.1229 * x[3] - 0.7287 * x[
            4] + 0.2792 * x[5] - 0.8878 + 0.711 * x[5] / x[4] + 0.6458 / x[2] - 0.2634 / (x[2] * x[4]) + 0.1271 / x[1] - 0.5423 / (
                                x[1] * x[5]) + 0.4508 / (x[1] * x[2]) - 0.6167 * x[1] / x[0] + 0.2949 * x[2] / x[0] + 0.7838 * x[5] / x[
                            0]


@register_eq_class
class inv_nv6_nt610_prog_6(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1176 * x[0] * x[2] + 0.926 * x[0] * x[3] + 0.885 * x[0] / x[4] - 0.9214 * x[0] / x[1] - 0.0053 * x[1] * x[
            5] + 0.1619 * x[2] * x[5] - 0.8371 * x[3] / x[5] - 0.5624 * x[4] + 0.7853 - 0.9511 / x[5] - 0.4432 / x[3] - 0.6553 / x[
                            2] + 0.5978 * x[2] / x[1] - 0.6571 / x[1] - 0.9807 / (x[1] * x[3]) - 0.9281 / x[0] - 0.8231 / (x[0] * x[5])


@register_eq_class
class inv_nv6_nt610_prog_18(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5962 * x[0] * x[3] - 0.1713 * x[0] * x[5] - 0.0312 * x[1] * x[2] + 0.1727 * x[1] * x[4] - 0.3405 * x[1] * x[
            5] - 0.3028 * x[2] * x[3] + 0.0125 * x[2] + 0.3949 * x[5] + 0.815 - 0.4329 / x[4] + 0.8578 / (x[4] * x[5]) + 0.4306 / x[
                            3] + 0.2093 * x[5] / x[2] + 0.2691 * x[3] / x[1] - 0.9504 / x[1] + 0.6833 / x[0] - 0.1417 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_3(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7043 * x[0] / x[5] + 0.6608 * x[1] * x[3] - 0.8973 * x[1] + 0.5316 * x[1] / x[5] - 0.6252 * x[2] * x[4] + 0.111 * \
                        x[2] - 0.5048 + 0.2223 / x[5] + 0.9879 / x[4] + 0.5609 * x[4] / x[3] - 0.7831 / x[3] + 0.546 / (
                                x[2] * x[5]) - 0.8872 / (x[1] * x[4]) + 0.1416 * x[2] / x[0] + 0.0995 * x[3] / x[0] - 0.5562 * x[4] / x[
                            0] + 0.1731 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_24(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.1742 * x[0] * x[1] - 0.4436 * x[0] * x[4] + 0.3942 * x[0] - 0.6445 * x[1] / x[5] + 0.9189 * x[2] / x[
            4] - 0.6252 * x[5] - 0.2108 + 0.342 / x[4] - 0.853 / (x[4] * x[5]) - 0.7793 * x[4] / x[3] + 0.6068 / x[3] + 0.5814 / (
                                x[3] * x[5]) + 0.7441 * x[3] / x[2] + 0.2849 / x[2] + 0.2671 / x[1] + 0.4076 / (
                                x[1] * x[4]) + 0.9994 / (x[0] * x[5])


@register_eq_class
class inv_nv6_nt610_prog_12(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8601 * x[0] / x[2] - 0.6014 * x[1] + 0.4537 * x[2] / x[3] + 0.1367 * x[3] / x[4] + 0.9627 * x[4] / x[
            5] + 0.1591 - 0.9453 / x[5] + 0.6319 / x[4] - 0.3831 / x[3] - 0.2568 / x[2] + 0.5873 * x[3] / x[1] + 0.541 * x[4] / x[
                            1] - 0.0205 * x[5] / x[1] + 0.0167 * x[1] / x[0] + 0.0664 / x[0] - 0.0122 / (x[0] * x[5]) - 0.3855 / (
                                x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_25(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.8869 * x[0] * x[1] - 0.623 * x[1] * x[2] - 0.2743 * x[1] - 0.5294 * x[1] / x[5] - 0.766 * x[2] + 0.8063 * x[2] / \
                        x[4] + 0.0246 * x[2] / x[3] + 0.957 * x[4] * x[5] + 0.3977 * x[5] - 0.1909 + 0.5122 / x[4] - 0.5655 / x[
                            3] + 0.5151 * x[3] / x[1] - 0.1278 / (x[1] * x[4]) + 0.4322 * x[3] / x[0] - 0.9404 / x[0] + 0.4328 / (
                                x[0] * x[5])


@register_eq_class
class inv_nv6_nt610_prog_21(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.5327 * x[0] / x[3] + 0.5578 * x[1] / x[2] - 0.2492 * x[2] / x[5] - 0.5392 * x[2] / x[4] - 0.6204 * x[3] * x[
            4] + 0.3801 * x[3] * x[5] + 0.22 * x[3] + 0.2175 * x[4] - 0.9517 * x[4] / x[5] + 0.0984 + 0.4319 / x[5] + 0.7942 / x[
                            2] - 0.2808 / (x[2] * x[3]) + 0.1072 / x[1] + 0.4677 / (x[1] * x[4]) - 0.0895 * x[5] / x[0] - 0.1962 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_26(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0433 * x[0] - 0.4763 * x[1] * x[4] - 0.8963 * x[1] / x[5] + 0.8322 * x[2] * x[3] - 0.1256 * x[2] * x[5] + 0.3379 * \
                        x[3] - 0.3752 * x[3] / x[5] + 0.963 * x[4] * x[5] + 0.1421 * x[4] + 0.7691 + 0.674 / x[5] - 0.7885 * x[4] / x[
                            3] - 0.8941 / x[2] + 0.2403 * x[3] / x[1] - 0.8282 / x[1] - 0.4074 * x[2] / x[0] - 0.3438 * x[5] / x[0]


@register_eq_class
class inv_nv6_nt610_prog_39(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.7346 * x[0] * x[1] - 0.88 * x[0] * x[5] + 0.9037 * x[0] + 0.8606 * x[1] * x[3] + 0.7848 * x[2] * x[4] + 0.1729 * \
                        x[2] * x[5] + 0.5629 * x[3] * x[4] + 0.1175 * x[3] + 0.4513 * x[4] / x[5] - 0.3345 * x[5] + 0.8041 + 0.5136 / x[
                            4] - 0.1878 / x[2] - 0.5331 / x[1] - 0.6874 / (x[1] * x[2]) + 0.1249 / (x[0] * x[4]) + 0.6863 / (x[0] * x[3])


@register_eq_class
class inv_nv6_nt610_prog_19(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.9006 * x[0] * x[3] + 0.2616 * x[0] / x[1] + 0.7978 * x[1] * x[3] - 0.2088 * x[1] - 0.1886 * x[1] / x[5] - 0.0475 * \
                        x[2] * x[5] - 0.9058 * x[2] - 0.3299 * x[2] / x[4] + 0.4869 * x[3] - 0.3117 * x[3] / x[4] + 0.2613 - 0.3518 / x[
                            5] - 0.9576 / x[4] + 0.9399 * x[5] / x[3] + 0.8123 * x[3] / x[2] + 0.3965 * x[4] / x[1] - 0.3928 / x[0]


@register_eq_class
class inv_nv6_nt610_prog_38(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.2455 * x[0] + 0.6019 * x[0] / x[4] - 0.9806 * x[1] - 0.7203 * x[2] + 0.6449 * x[2] / x[5] + 0.3007 * x[2] / x[
            4] - 0.4165 * x[4] - 0.1594 * x[5] - 0.076 + 0.6127 * x[5] / x[4] + 0.2369 / x[3] + 0.8816 / (x[3] * x[4]) - 0.6917 * x[3] / x[
                            1] + 0.5334 * x[4] / x[1] - 0.5284 / (x[1] * x[2]) - 0.8842 / (x[0] * x[2]) + 0.2345 / (x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_9(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.5431 * x[1] * x[2] + 0.3766 * x[1] * x[4] - 0.9913 * x[1] * x[5] + 0.3216 * x[1] + 0.058 * x[2] - 0.513 * x[2] / \
                        x[3] + 0.8666 * x[3] - 0.2405 * x[5] - 0.2665 + 0.0238 / x[4] + 0.8379 / (x[3] * x[5]) + 0.0271 * x[4] / x[
                            2] + 0.5198 * x[3] / x[1] + 0.7745 * x[4] / x[0] + 0.615 * x[5] / x[0] + 0.8462 / x[0] + 0.0736 / (x[0] * x[2])


@register_eq_class
class inv_nv6_nt610_prog_32(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.0647 * x[0] * x[3] - 0.6081 * x[0] + 0.6803 * x[0] / x[5] - 0.891 * x[1] * x[4] + 0.0485 * x[1] * x[5] - 0.5461 * \
                        x[2] + 0.8103 * x[3] / x[5] - 0.9579 * x[4] + 0.2184 * x[5] + 0.1085 - 0.4448 / (x[4] * x[5]) + 0.8451 / x[
                            3] - 0.0587 * x[4] / x[2] + 0.4966 / x[1] + 0.6788 / (x[1] * x[3]) + 0.8921 / (x[0] * x[4]) - 0.9371 / (
                                x[0] * x[1])


@register_eq_class
class inv_nv6_nt610_prog_5(KnownEquation):
    _eq_name = 'inv_nv6_nt610_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = 0.4743 * x[0] / x[5] + 0.1469 * x[0] / x[3] - 0.133 * x[0] / x[2] + 0.6947 * x[2] / x[4] - 0.1466 * x[
            4] - 0.456 - 0.2171 / x[5] + 0.4489 / (x[4] * x[5]) + 0.8922 * x[4] / x[3] + 0.6124 / x[3] - 0.1901 * x[5] / x[2] + 0.4871 / x[
                            2] - 0.221 * x[4] / x[1] - 0.6969 / x[1] + 0.9772 / (x[1] * x[3]) - 0.0779 / x[0] + 0.7085 / (x[0] * x[4])


@register_eq_class
class sincosinv_nv2_nt11_prog_46(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8935 * x[1] * sympy.sin(x[0]) + 0.1825 - 0.1662 / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_0(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7272 * sympy.sin(x[0]) * sympy.sin(x[1]) - 0.3866 + 0.183 / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_35(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.253 * x[0] * x[1] + 0.8975 * sympy.sin(x[0]) + 0.81


@register_eq_class
class sincosinv_nv2_nt11_prog_8(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7375 * x[0] + 0.2691 * x[1] * sympy.sin(x[0]) + 0.802


@register_eq_class
class sincosinv_nv2_nt11_prog_42(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1593 * x[0] - 0.1679 * sympy.cos(x[0]) * sympy.cos(x[1]) + 0.5442


@register_eq_class
class sincosinv_nv2_nt11_prog_33(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6728 * x[0] * x[1] + 0.892 - 0.3941 / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_20(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.5435 * x[1] * sympy.sin(x[0]) - 0.6126 + 0.8928 / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_14(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.9245 * x[1] + 0.6416 - 0.7406 * sympy.sin(x[0]) / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_31(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4677 * sympy.sin(x[1]) * sympy.cos(x[0]) - 0.0058 + 0.5676 / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_48(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.4857 * x[1] - 0.3334 + 0.9501 * sympy.sin(x[1]) / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_41(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2621 * x[1] + 0.2443 - 0.9433 * sympy.sin(x[0]) / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_7(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.5944 * x[0] / x[1] - 0.857 + 0.8584 / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_37(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5173 * x[1] + 0.0422 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.0591


@register_eq_class
class sincosinv_nv2_nt11_prog_15(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1759 * x[0] - 0.6243 * x[1] * sympy.sin(x[0]) + 0.8291


@register_eq_class
class sincosinv_nv2_nt11_prog_23(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0423 * x[0] + 0.4525 * x[1] * sympy.cos(x[0]) + 0.0919


@register_eq_class
class sincosinv_nv2_nt11_prog_30(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2041 * x[0] * sympy.cos(x[1]) - 0.9081 * x[1] - 0.3657


@register_eq_class
class sincosinv_nv2_nt11_prog_28(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5312 * x[1] - 0.1434 + 0.8419 * x[1] / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_17(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0771 * x[1] - 0.5019 + 0.3423 * x[1] / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_43(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4118 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.4273 * sympy.cos(x[1]) - 0.7115


@register_eq_class
class sincosinv_nv2_nt11_prog_2(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.2222 * x[0] * sympy.sin(x[1]) - 0.2025 * x[1] + 0.8661


@register_eq_class
class sincosinv_nv2_nt11_prog_4(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7552 * x[0] * sympy.cos(x[1]) - 0.1967 * sympy.cos(x[1]) + 0.7437


@register_eq_class
class sincosinv_nv2_nt11_prog_45(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6033 * x[0] * x[1] + 0.6467 * x[1] + 0.0791


@register_eq_class
class sincosinv_nv2_nt11_prog_49(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.8429 * x[0] * sympy.cos(x[1]) - 0.0598 + 0.2268 / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_11(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.7186 + 0.9131 * sympy.sin(x[0]) / x[1] - 0.8508 / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_10(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.0515 * sympy.cos(x[0]) + 0.9854 - 0.8783 * x[1] / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_1(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.0495 * x[1] * sympy.sin(x[0]) - 0.0589 * sympy.sin(x[1]) + 0.6305


@register_eq_class
class sincosinv_nv2_nt11_prog_40(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7966 * x[1] * sympy.sin(x[0]) + 0.5536 * sympy.sin(x[1]) - 0.4348


@register_eq_class
class sincosinv_nv2_nt11_prog_29(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.169 * x[0] - 0.2029 - 0.5116 * sympy.cos(x[1]) / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_22(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.6738 * sympy.sin(x[0]) * sympy.sin(x[1]) + 0.3399 * sympy.sin(x[0]) - 0.001


@register_eq_class
class sincosinv_nv2_nt11_prog_27(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.9637 * x[1] * sympy.sin(x[0]) + 0.0162 * sympy.sin(x[1]) + 0.2201


@register_eq_class
class sincosinv_nv2_nt11_prog_34(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5842 * x[0] - 0.6229 - 0.119 / (x[0] * x[1])


@register_eq_class
class sincosinv_nv2_nt11_prog_16(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8276 * sympy.sin(x[1]) * sympy.cos(x[0]) + 0.2331 * sympy.cos(x[1]) + 0.0103


@register_eq_class
class sincosinv_nv2_nt11_prog_13(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.0412 * x[1] + 0.8169 - 0.5382 * x[1] / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_47(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5617 * x[0] / x[1] - 0.3393 * x[1] + 0.1479


@register_eq_class
class sincosinv_nv2_nt11_prog_36(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1686 * x[1] - 0.5873 * sympy.cos(x[0]) * sympy.cos(x[1]) - 0.2531


@register_eq_class
class sincosinv_nv2_nt11_prog_44(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.6752 * x[0] * sympy.sin(x[1]) - 0.3434 * sympy.cos(x[0]) + 0.0382


@register_eq_class
class sincosinv_nv2_nt11_prog_6(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.3031 * x[1] - 0.479 + 0.8057 * x[1] / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_18(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1859 * x[1] - 0.1225 + 0.492 * sympy.cos(x[0]) / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_3(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.4555 + 0.8453 / x[0] + 0.5868 / (x[0] * x[1])


@register_eq_class
class sincosinv_nv2_nt11_prog_24(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1757 * x[0] / x[1] + 0.7412 * x[1] - 0.7486


@register_eq_class
class sincosinv_nv2_nt11_prog_12(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.9799 * x[0] * x[1] - 0.0255 * sympy.sin(x[1]) + 0.7027


@register_eq_class
class sincosinv_nv2_nt11_prog_25(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.7405 * sympy.sin(x[0]) * sympy.cos(x[1]) - 0.7603 * sympy.sin(x[1]) - 0.6079


@register_eq_class
class sincosinv_nv2_nt11_prog_21(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.1889 * x[0] * x[1] - 0.4448 * x[1] - 0.8242


@register_eq_class
class sincosinv_nv2_nt11_prog_26(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6118 * x[0] * sympy.sin(x[1]) - 0.6049 * sympy.sin(x[1]) + 0.5233


@register_eq_class
class sincosinv_nv2_nt11_prog_39(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.8404 * x[0] + 0.9871 - 0.1837 * x[1] / x[0]


@register_eq_class
class sincosinv_nv2_nt11_prog_19(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.0182 * x[0] * sympy.sin(x[1]) - 0.9739 * sympy.cos(x[1]) + 0.4031


@register_eq_class
class sincosinv_nv2_nt11_prog_38(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.581 * x[0] + 0.1162 * sympy.sin(x[0]) * sympy.cos(x[1]) + 0.8543


@register_eq_class
class sincosinv_nv2_nt11_prog_9(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.1458 * x[0] * x[1] + 0.1893 - 0.4203 / x[1]


@register_eq_class
class sincosinv_nv2_nt11_prog_32(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -0.5115 * x[0] * sympy.cos(x[1]) + 0.526 * sympy.cos(x[1]) + 0.4929


@register_eq_class
class sincosinv_nv2_nt11_prog_5(KnownEquation):
    _eq_name = 'sincosinv_nv2_nt11_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.6609 * sympy.sin(x[1]) + 0.1161 + 0.5919 * x[1] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_46(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_46'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2778 * x[0] * x[2] - 0.6445 * x[0] / x[3] - 0.4267 * x[2] + 0.9354 * x[4] + 0.3616 - 0.279 / x[3] - 0.3224 * x[
            3] / x[1] - 0.3413 * x[4] / x[1] - 0.4365 / x[1] - 0.3738 * x[1] / x[0] - 0.5848 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_0(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_0'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.1419 * x[0] + 0.8009 * x[0] / x[4] + 0.1442 * x[1] * x[2] - 0.5546 * x[1] * x[4] - 0.8074 * x[1] - 0.4033 * x[
            2] - 0.8592 * x[3] - 0.2413 - 0.779 / x[4] - 0.7686 / (x[2] * x[4]) - 0.1384 / (x[1] * x[3])


@register_eq_class
class inv_nv5_nt55_prog_35(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_35'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2985 * x[0] * x[4] + 0.455 * x[0] / x[3] - 0.9186 * x[2] / x[3] + 0.3769 * x[3] - 0.9037 - 0.8349 / x[
            4] - 0.4316 / x[2] - 0.7751 / x[1] - 0.788 / (x[1] * x[3]) - 0.963 / x[0] + 0.7054 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt55_prog_8(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3375 * x[0] * x[1] + 0.4993 * x[1] / x[2] - 0.5345 * x[2] * x[3] - 0.9494 * x[2] - 0.3293 * x[3] * x[4] - 0.9343 * \
                        x[4] - 0.129 - 0.2363 / x[3] - 0.7257 / x[1] - 0.5754 / x[0] + 0.9282 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt55_prog_42(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_42'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2476 * x[0] + 0.9649 * x[0] / x[1] - 0.809 * x[1] - 0.3533 + 0.0772 / x[4] + 0.5329 / x[3] - 0.4707 / x[
            2] - 0.7145 / (x[2] * x[4]) + 0.3531 / (x[2] * x[3]) - 0.203 / (x[1] * x[4]) + 0.203 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt55_prog_33(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_33'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8863 * x[1] + 0.0913 * x[2] + 0.2675 * x[3] * x[4] - 0.9391 * x[3] + 0.6745 + 0.7729 / x[4] - 0.7483 * x[4] / x[
            2] - 0.928 * x[4] / x[1] - 0.6731 / (x[1] * x[3]) - 0.9348 / x[0] - 0.9517 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt55_prog_20(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.4543 * x[1] / x[3] + 0.7723 * x[1] / x[2] + 0.3699 * x[3] - 0.6082 + 0.9241 / x[4] - 0.9266 / x[2] + 0.9561 / x[
            1] + 0.7691 / (x[1] * x[4]) + 0.4868 * x[3] / x[0] + 0.1839 / x[0] + 0.6486 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt55_prog_14(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9542 * x[1] - 0.5039 * x[2] - 0.0711 * x[3] - 0.4167 * x[3] / x[4] - 0.3424 - 0.1686 / x[4] + 0.9056 * x[2] / x[
            1] - 0.6342 * x[4] / x[1] - 0.2468 * x[2] / x[0] + 0.5419 * x[4] / x[0] - 0.906 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_31(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_31'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9471 * x[0] + 0.4607 * x[0] / x[1] + 0.6007 * x[1] * x[2] - 0.7861 * x[1] + 0.8348 * x[2] - 0.7693 * x[2] / x[
            3] + 0.0965 * x[3] / x[4] - 0.0184 * x[4] - 0.8564 - 0.847 / x[3] + 0.4741 / (x[0] * x[3])


@register_eq_class
class inv_nv5_nt55_prog_48(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_48'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3054 * x[0] * x[3] - 0.3418 * x[1] * x[3] - 0.5501 * x[1] - 0.6555 * x[2] / x[4] + 0.0283 - 0.3899 / x[
            4] + 0.8122 / x[3] - 0.9707 / x[2] - 0.0395 / (x[1] * x[2]) + 0.585 * x[1] / x[0] + 0.4665 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_41(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_41'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2933 * x[0] * x[3] - 0.5585 * x[0] / x[4] - 0.1267 * x[0] / x[1] + 0.3611 * x[1] / x[3] - 0.4327 * x[2] / x[
            3] - 0.0094 - 0.6946 / x[4] + 0.5417 / x[3] - 0.5917 / x[2] - 0.6812 / x[1] - 0.178 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_7(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.7903 * x[0] / x[3] - 0.0082 * x[1] / x[4] + 0.0486 * x[1] / x[3] + 0.7015 * x[2] - 0.1654 - 0.6553 / x[
            4] - 0.619 / x[3] - 0.4094 * x[4] / x[2] - 0.9589 / x[1] + 0.6798 * x[4] / x[0] - 0.0979 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_37(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_37'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9283 * x[1] - 0.7266 * x[1] / x[3] - 0.0159 * x[1] / x[2] - 0.1885 + 0.3776 / x[4] - 0.6004 / x[3] + 0.3525 * x[
            3] / x[2] - 0.8573 / x[2] + 0.7086 * x[4] / x[1] + 0.7511 * x[4] / x[0] - 0.1224 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_15(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8047 * x[0] * x[3] - 0.3848 * x[0] / x[4] - 0.0637 * x[3] + 0.3381 - 0.6503 / x[4] - 0.6206 / x[2] + 0.454 / (
                x[2] * x[3]) - 0.3609 / x[1] + 0.1664 * x[1] / x[0] + 0.9098 / x[0] - 0.966 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt55_prog_23(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.467 * x[0] * x[3] + 0.5862 * x[0] * x[4] - 0.4148 * x[0] + 0.4825 * x[1] + 0.6389 * x[3] + 0.9936 * x[
            4] - 0.0454 - 0.5455 * x[4] / x[2] + 0.5229 / x[2] + 0.8826 * x[2] / x[1] + 0.5793 / (x[1] * x[3])


@register_eq_class
class inv_nv5_nt55_prog_30(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_30'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.5436 * x[2] - 0.9539 * x[4] - 0.6065 + 0.9711 / x[3] - 0.7961 / (x[2] * x[4]) - 0.6856 / (x[2] * x[3]) - 0.1041 / \
                        x[1] - 0.0072 / (x[1] * x[3]) - 0.3382 / (x[1] * x[2]) - 0.4325 / x[0] + 0.8425 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt55_prog_28(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_28'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1312 * x[1] * x[2] + 0.4256 * x[1] * x[3] + 0.8661 * x[1] / x[4] + 0.1846 * x[2] * x[3] - 0.1322 * x[
            3] - 0.03 - 0.0443 / x[4] + 0.8179 / x[2] - 0.68 / x[1] - 0.968 / x[0] + 0.9879 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt55_prog_17(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.8008 * x[0] - 0.0843 * x[2] * x[3] - 0.5817 * x[2] - 0.0005 * x[3] + 0.7016 + 0.4185 / x[4] + 0.3927 * x[4] / x[
            3] + 0.5021 * x[4] / x[2] + 0.6229 / x[1] + 0.3502 * x[2] / x[0] - 0.6593 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_43(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_43'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6683 * x[0] - 0.7117 * x[1] * x[4] + 0.9145 * x[4] - 0.4723 + 0.7839 / x[3] - 0.3797 / (x[3] * x[4]) + 0.1011 / \
                        x[2] + 0.4302 / x[1] - 0.7508 / (x[1] * x[3]) + 0.2319 / (x[1] * x[2]) + 0.5105 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt55_prog_2(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.4553 * x[0] - 0.3973 * x[0] / x[3] + 0.1222 * x[1] + 0.755 * x[1] / x[4] + 0.7739 * x[2] * x[4] - 0.8353 * x[
            2] + 0.6413 * x[3] + 0.3191 - 0.5703 / x[4] - 0.9915 * x[3] / x[1] + 0.946 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_4(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2475 * x[1] * x[2] - 0.5349 * x[1] - 0.3037 * x[1] / x[4] - 0.5804 * x[3] + 0.6302 * x[3] / x[
            4] - 0.1435 - 0.8799 / x[4] - 0.0137 * x[4] / x[2] + 0.4989 / x[2] - 0.8638 * x[4] / x[0] - 0.6226 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_45(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_45'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.219 * x[0] * x[2] + 0.2053 * x[0] / x[4] - 0.4656 * x[1] + 0.2166 * x[1] / x[2] - 0.5991 * x[2] * x[4] - 0.2074 * \
                        x[3] - 0.621 * x[4] - 0.6524 - 0.6109 * x[3] / x[2] - 0.7911 / x[2] + 0.3001 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_49(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_49'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8021 * x[1] * x[2] - 0.7703 * x[1] * x[3] - 0.6782 * x[2] * x[4] - 0.624 - 0.2486 / x[4] - 0.0644 / x[3] - 0.31 * \
                        x[3] / x[2] + 0.4481 / x[2] - 0.282 / x[1] - 0.6671 * x[1] / x[0] + 0.1798 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_11(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.0476 * x[0] * x[4] - 0.654 * x[0] - 0.7251 * x[2] / x[4] + 0.9688 + 0.9413 / x[4] + 0.8108 / x[3] - 0.1931 / x[
            2] + 0.7845 * x[3] / x[1] - 0.6715 / x[1] - 0.1427 / (x[1] * x[4]) + 0.0417 * x[1] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_10(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8748 * x[0] / x[2] - 0.6263 * x[1] - 0.7411 * x[3] * x[4] + 0.7647 * x[3] + 0.9912 * x[4] + 0.0904 - 0.7226 * x[
            3] / x[2] - 0.5335 / x[2] + 0.8137 * x[4] / x[1] - 0.7914 * x[3] / x[0] + 0.3223 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_1(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8758 * x[0] / x[4] + 0.6688 * x[2] + 0.2103 + 0.1075 / x[4] - 0.4062 * x[4] / x[3] - 0.1108 / x[3] - 0.8076 * x[
            4] / x[2] + 0.0037 / x[1] - 0.0259 / (x[1] * x[2]) + 0.1557 * x[1] / x[0] - 0.5229 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_40(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_40'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.3516 * x[0] * x[2] + 0.6874 * x[0] * x[4] + 0.4952 * x[2] - 0.3939 * x[3] + 0.4658 * x[4] - 0.2515 - 0.1351 * x[
            4] / x[2] - 0.5468 * x[2] / x[1] - 0.2806 / x[1] - 0.7157 * x[3] / x[0] + 0.0564 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_29(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_29'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0951 * x[0] * x[1] - 0.584 * x[1] - 0.073 * x[1] / x[2] + 0.214 * x[4] + 0.7092 + 0.2024 / x[3] + 0.3085 / x[
            2] - 0.8023 / (x[2] * x[4]) + 0.9675 / (x[2] * x[3]) - 0.6701 * x[4] / x[1] - 0.5982 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_22(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3965 * x[0] * x[2] - 0.4419 * x[1] * x[2] + 0.1353 * x[1] + 0.6127 * x[2] - 0.1861 * x[3] * x[4] + 0.8772 * x[
            3] - 0.553 - 0.0251 / x[4] - 0.1388 / (x[2] * x[4]) + 0.9753 / (x[1] * x[3]) - 0.0367 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_27(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_27'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6018 * x[0] * x[3] + 0.1774 * x[1] * x[2] - 0.2758 * x[2] / x[4] + 0.4881 - 0.3621 / x[4] - 0.3709 * x[4] / x[
            3] + 0.8323 / x[3] + 0.2181 / x[2] + 0.3457 / (x[2] * x[3]) - 0.9394 / x[1] + 0.5705 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_34(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_34'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.6075 * x[0] * x[4] + 0.1902 * x[1] * x[4] + 0.6296 * x[1] - 0.0017 * x[2] - 0.5417 * x[2] / x[4] + 0.0968 * x[
            3] - 0.0306 * x[3] / x[4] - 0.8363 * x[4] + 0.9271 - 0.9679 * x[3] / x[2] - 0.4506 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_16(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.043 * x[1] / x[4] - 0.1302 * x[1] / x[2] - 0.2519 * x[2] * x[3] - 0.7408 * x[2] + 0.1871 * x[
            4] + 0.0941 - 0.2237 * x[4] / x[3] + 0.1806 / x[3] + 0.669 / x[1] - 0.0932 * x[4] / x[0] - 0.6139 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_13(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.8762 * x[2] - 0.4447 * x[4] + 0.6767 + 0.1371 / x[3] - 0.0381 / (x[2] * x[3]) - 0.5436 / x[1] + 0.6911 / (
                x[1] * x[2]) - 0.4801 * x[3] / x[0] + 0.6615 / x[0] - 0.3918 / (x[0] * x[4]) - 0.2678 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt55_prog_47(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_47'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2734 * x[1] - 0.7884 * x[2] * x[4] - 0.7361 * x[3] + 0.0764 * x[3] / x[4] + 0.7074 * x[4] + 0.5927 - 0.1638 / x[
            2] - 0.131 / (x[2] * x[3]) + 0.0987 / (x[1] * x[3]) + 0.3993 * x[3] / x[0] - 0.2647 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_36(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_36'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1163 * x[0] * x[1] + 0.3316 * x[0] / x[4] + 0.7571 * x[1] * x[2] + 0.0129 * x[1] * x[3] - 0.8961 * x[3] + 0.9709 * \
                        x[4] - 0.6241 + 0.8114 * x[3] / x[2] - 0.3794 / x[2] - 0.1663 / x[1] - 0.8349 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_44(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_44'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6297 * x[0] * x[2] + 0.7324 * x[2] / x[4] + 0.9777 * x[3] * x[4] - 0.6185 - 0.6393 / x[4] - 0.7777 / x[
            3] - 0.8443 / x[2] - 0.2077 / x[1] + 0.782 / (x[1] * x[4]) + 0.9616 * x[1] / x[0] + 0.9833 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_6(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9192 * x[0] * x[1] - 0.7641 * x[0] + 0.8217 * x[0] / x[2] + 0.79 * x[3] / x[4] + 0.7155 - 0.994 / x[4] - 0.9659 / \
                        x[3] + 0.8192 / x[2] + 0.1309 / x[1] + 0.4067 / (x[1] * x[3]) + 0.7228 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_18(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3627 * x[0] + 0.9554 * x[3] + 0.3289 + 0.3158 / x[4] + 0.7928 / (x[3] * x[4]) - 0.5778 * x[4] / x[2] - 0.2238 / \
                        x[2] - 0.6492 * x[2] / x[1] + 0.4876 / x[1] - 0.4694 * x[1] / x[0] + 0.8411 * x[2] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_3(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9951 * x[0] + 0.7511 * x[0] / x[2] + 0.2602 * x[1] * x[2] + 0.8409 * x[1] + 0.8015 * x[2] * x[4] + 0.4112 * x[
            2] + 0.3248 + 0.4334 / x[4] + 0.5427 * x[4] / x[3] + 0.5625 / x[3] - 0.2452 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_24(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.2696 * x[0] * x[1] + 0.5764 * x[0] + 0.9192 * x[1] * x[4] - 0.9814 * x[2] + 0.9314 * x[3] / x[
            4] + 0.5217 - 0.5725 / x[4] - 0.7824 / x[3] + 0.0951 / x[1] - 0.4815 / (x[1] * x[3]) + 0.8108 * x[4] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_12(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0749 * x[1] + 0.0921 * x[1] / x[3] + 0.0849 * x[2] + 0.9846 * x[3] / x[4] - 0.2835 - 0.5366 / x[4] + 0.7622 / x[
            3] - 0.4741 * x[3] / x[2] + 0.1723 / (x[1] * x[2]) + 0.9523 / x[0] - 0.3212 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt55_prog_25(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.1642 * x[0] + 0.0846 * x[1] * x[2] + 0.5891 * x[1] * x[3] + 0.9565 * x[1] / x[4] - 0.5579 * x[
            3] - 0.3422 - 0.1134 / x[4] + 0.0607 * x[4] / x[2] + 0.9295 / x[2] - 0.442 / x[1] + 0.982 / (x[0] * x[4])


@register_eq_class
class inv_nv5_nt55_prog_21(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2921 * x[0] - 0.7801 * x[0] / x[4] + 0.1694 * x[0] / x[2] - 0.3791 * x[1] * x[4] + 0.1353 * x[1] / x[2] + 0.278 * \
                        x[3] - 0.5728 + 0.6843 / x[4] - 0.4585 / x[2] - 0.6216 * x[3] / x[1] + 0.9359 / x[1]


@register_eq_class
class inv_nv5_nt55_prog_26(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_26'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.9854 * x[1] + 0.0688 * x[1] / x[3] - 0.8275 * x[2] * x[3] - 0.3227 * x[3] + 0.0696 * x[4] - 0.08 - 0.5519 / x[
            2] - 0.4625 / (x[2] * x[4]) + 0.5753 / x[0] - 0.5857 / (x[0] * x[4]) - 0.9562 / (x[0] * x[1])


@register_eq_class
class inv_nv5_nt55_prog_39(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_39'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6357 * x[0] + 0.8415 * x[0] / x[1] - 0.2459 * x[2] * x[4] - 0.7074 * x[2] + 0.3406 * x[2] / x[3] - 0.7818 * x[3] * \
                        x[4] + 0.5623 * x[3] - 0.9943 * x[4] + 0.1524 + 0.1937 / x[1] + 0.1786 * x[2] / x[0]


@register_eq_class
class inv_nv5_nt55_prog_19(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.2077 * x[0] * x[2] + 0.2622 * x[0] * x[3] - 0.7096 * x[1] + 0.0403 * x[1] / x[2] - 0.5247 * x[2] * x[3] - 0.6895 * \
                        x[2] + 0.4077 - 0.1518 / x[4] + 0.3159 * x[4] / x[3] - 0.4949 / x[3] - 0.1333 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_38(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_38'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.7873 * x[0] - 0.4578 * x[0] / x[1] - 0.2073 * x[1] * x[3] + 0.4962 * x[1] - 0.3172 * x[2] * x[4] + 0.5488 * x[
            2] + 0.2924 * x[3] - 0.3702 * x[3] / x[4] - 0.5412 + 0.9876 / x[4] - 0.4113 / (x[1] * x[2])


@register_eq_class
class inv_nv5_nt55_prog_9(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.6889 * x[1] - 0.7871 * x[2] + 0.4616 * x[2] / x[4] + 0.0758 * x[3] + 0.9942 * x[4] - 0.6157 - 0.2102 * x[4] / x[
            3] - 0.9478 / (x[1] * x[2]) + 0.1076 * x[3] / x[0] - 0.1196 / x[0] + 0.5692 / (x[0] * x[2])


@register_eq_class
class inv_nv5_nt55_prog_32(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_32'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.0729 * x[0] * x[1] - 0.5399 * x[0] / x[4] + 0.3418 * x[0] / x[3] + 0.8356 * x[3] + 0.8363 * x[
            4] - 0.4993 + 0.2885 / (x[3] * x[4]) + 0.2878 / x[2] - 0.2825 / x[1] - 0.1202 / (x[1] * x[2]) - 0.1922 / x[0]


@register_eq_class
class inv_nv5_nt55_prog_5(KnownEquation):
    _eq_name = 'inv_nv5_nt55_prog_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'inv', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -0.3429 * x[0] + 0.681 * x[0] / x[3] + 0.0557 * x[0] / x[2] - 0.7501 * x[1] - 0.7204 * x[2] * x[
            4] + 0.1794 + 0.2932 / x[4] - 0.4447 / x[3] + 0.4418 / x[2] + 0.9247 * x[2] / x[1] + 0.1915 / (x[0] * x[4])
