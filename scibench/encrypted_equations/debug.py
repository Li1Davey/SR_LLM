from encrypt_equations import to_binary_expr_tree
import sympy

x = sympy.symbols("X_0 X_1")
expr = sympy.exp(-(x[0] / x[1]) ** 2 / 2) / (sympy.sqrt(2 * sympy.pi) * x[1])
to_binary_expr_tree(expr)
