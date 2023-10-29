import numpy as np
import math


def protectDiv(a, b):
    if (type(b) == int or type(b) == float or type(b) == np.float64) and b == 0:
        return a / math.nan
    if (type(b) == np.ndarray) and (0 in b):
        return a / np.where(b == 0, math.nan, b)
    return a / b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def exp(a):
    return np.exp(a)



def power(a, b):
    return a ** b


def sqrt(a):
    return np.sqrt(a)


def sqrd(a):
    return a ** 2


def inv(a):
    return np.array(a).astype(float) ** (-1)


def sin(a):
    return np.sin(a)


def cos(a):
    return np.cos(a)


def tan(a):
    return np.tan(a)


def arccos(a):
    return np.arccos(a)


def arcsin(a):
    return np.arcsin(a)


def arctan(a):
    return np.arctan(a)


def tanh(a):
    return np.tanh(a)


def log(a):
    return np.log(a)


def defaultOps():
    return [protectDiv, add, sub, mult, exp, sqrd, sqrt, inv, "pop", "pop", "pop", "pop", "pop", "pop"]


def allOps():
    return [protectDiv, add, sub, mult, exp, sqrd, sqrt, inv, cos, sin, tan, arccos, arcsin, arctan, tanh, log, "pop", "pop", "pop", "pop",
            "pop", "pop", "pop", "pop", "pop", "pop"]
