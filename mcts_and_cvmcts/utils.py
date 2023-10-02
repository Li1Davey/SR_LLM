import sympy
from sympy import simplify, expand
import functools

def simplify_eq(eq: sympy.Expr) -> str:
    return str(expand(simplify(eq)))


def tree_to_eq(prods):
    """
    Convert a parse tree to equation form
    """
    seq = ['f']
    for prod in prods:
        if str(prod[0]) == 'Nothing':
            break
        for ix, s in enumerate(seq):
            if s == prod[0]:
                seq = seq[:ix] + list(prod[3:]) + seq[ix + 1:]
                break
    try:
        return ''.join(seq)
    except:
        return ''


class cached_property(object):
    """
    Decorator used for lazy evaluation of an object attribute. The property
    should be non-mutable, since it replaces itself.
    """

    def __init__(self, getter):
        self.getter = getter

        functools.update_wrapper(self, getter)

    def __get__(self, obj, cls):
        if obj is None:
            return self

        value = self.getter(obj)
        setattr(obj, self.getter.__name__, value)
        return value