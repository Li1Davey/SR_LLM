import sympy
from sympy import simplify, expand


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
