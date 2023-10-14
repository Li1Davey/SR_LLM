import sympy
from sympy import simplify, expand
from sympy.parsing.sympy_parser import parse_expr


def pretty_print_expr(eq) -> str:
    if type(eq) == str:
        eq = parse_expr(eq)
    return str(simplify(eq))


def tree_to_eq(prods):
    """
    Convert a parse tree to equation form
    """
    seq = ['f']
    for prod in prods:
        for ix, s in enumerate(seq):
            if s == prod[0]:
                seq = seq[:ix] + list(prod[3:]) + seq[ix + 1:]
                break
    try:
        output = ''.join(seq)
        return output
    except:
        return ''


def create_geometric_generations(n_generations, nvar, ratio=4):
    gens = [0] * nvar
    round = 0
    while n_generations > nvar:
        if round > 10:
            break
        round += 1
        for it in range(nvar - 1, 0, -1):
            temp = n_generations // ratio
            gens[it] += temp
            n_generations -= temp
    # gens[0] = n_generations
    for it in range(0, nvar):
        if gens[it] < 5:
            gens[it] = 5
    gens = gens[::-1]
    print('generation #:', gens, 'sum=', sum(gens))
    return gens


def create_uniform_generations(n_generations, nvar):
    gens = [0] * nvar
    each_gen = n_generations // nvar
    for it in range(nvar - 1, 0, -1):
        gens[it] = each_gen
        n_generations -= each_gen
    gens[0] = n_generations
    print('generation #:', gens, 'sum=', sum(gens))
    return gens
