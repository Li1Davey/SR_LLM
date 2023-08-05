from symbolic_equation_evaluator_public import decrypt_equation
import numpy as np

if __name__ == '__main__':
    basepath="/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_trigometric/inv_nv8_nt812_prog_{}.in"
    for prog in range(10):
        filename=basepath.format(prog)
    one_eq = decrypt_equation(filename)
    batchsize = 256
    n_input = one_eq['num_vars']
    X = np.random.rand(batchsize, n_input) * 9.5 + 0.5
    print(one_eq['eq_expression'].execute(X))
