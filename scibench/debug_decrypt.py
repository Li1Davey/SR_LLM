from symbolic_equation_evaluator_public import decrypt_equation
import numpy as np

if __name__ == '__main__':
    one_eq = decrypt_equation(
        '/home/jiangnan/PycharmProjects/scibench/scibench/encrypted_equations/equations_trigometric/22166152459110949461061628456554646.unencypt.in')
    batchsize = 256
    n_input = one_eq['num_vars']
    X = np.random.rand(batchsize, n_input) * 9.5 + 0.5
    print(one_eq['eq_expression'].execute(X))
