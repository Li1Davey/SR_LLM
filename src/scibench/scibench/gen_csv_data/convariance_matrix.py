import numpy as np
from itertools import combinations
from math import comb
from numpy.linalg import inv

np.set_printoptions(linewidth=np.inf)


def f(N, m, L):
    return L ** 2 * (N - 2 * m + L) + (m - L) ** 2


# @click.command()
# @click.option('--N', default=4, help='N')
# @click.option('--M', default=2, help='M')
def compute_convariance_matrix(N, M, only_diag=False):
    print(f"the input values: N={N}, M={M}")
    C = np.zeros((comb(N, M), comb(N, M)), dtype=int)

    def compute_L(idx1, idx2):
        return len(set(idx1).intersection(set(idx2)))


    print("matrix C is")
    for ci, i in enumerate(combinations(range(N), M)):
        for cj, j in enumerate(combinations(range(N), M)):
            C[ci, cj] = f(N, M, compute_L(i, j))
        if only_diag==False:
            print(C[ci, :])


    # print("matrix C is\n",C)


    invC = inv(C)
    if only_diag==False:
        print("matrix of C^-1 is\n", )
        for i in range(invC.shape[0]):
            print(invC[i, :])
    else:
        print("diagonal value of the matrix:")
        np.set_printoptions(precision=6)
        print("{:.6f}".format( invC.diagonal()[0]),)
        return "{:.6f}".format( invC.diagonal()[0])



if __name__ == '__main__':
    ### for differnet N, fix m, compute diagonal values of convariance matrix.
    ### N must be even number.
    ### need to add x^(1/2), x^(1/3), x^(1/4), x^(1/5)...
    for N in range(4, 100, 2):
        compute_convariance_matrix(N=N, M=2, only_diag=True)
