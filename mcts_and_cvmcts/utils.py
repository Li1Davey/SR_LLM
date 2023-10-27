import sympy
from sympy.core.numbers import Float, Rational, NegativeOne, Integer
from sympy import simplify, expand, Symbol
from sympy.parsing.sympy_parser import parse_expr


# from py_expression_eval import Parser


def pretty_print_expr(eq) -> str:
    '''
    ask sympy simplify to pretty print the expression.
    '''
    if type(eq) == str:
        eq = parse_expr(eq)
    return str(expand(simplify(eq)))


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


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def create_uniform_generations(n_generations, nvar):
    gens = [0] * nvar
    each_gen = n_generations // nvar
    for it in range(nvar - 1, 0, -1):
        gens[it] = each_gen
        n_generations -= each_gen
    gens[0] = n_generations
    print('generation #:', gens, 'sum=', sum(gens))
    return gens


def expression_to_template(expr) -> str:
    C = Symbol('C')
    all_floats = expr.atoms(Float)
    for fi in all_floats:
        expr = expr.replace(fi, C)
    print(str(expr))



