import numpy as np
from itertools import combinations
from math import comb
from numpy.linalg import inv
np.set_printoptions(linewidth=np.inf)

def f(N,m,L):
    return L**2*(N-2*m+L) + (m-L)**2


# @click.command()
# @click.option('--N', default=4, help='N')
# @click.option('--M', default=2, help='M')
def compute_convariance_matrix(N, M):
    print(f"the input values: N={N}, M={M}")
    C=np.zeros((comb(N,M), comb(N,M)), dtype=int)
    def compute_L(idx1, idx2):
        return len(set(idx1).intersection(set(idx2)))
        
    print("matrix C is")
    for ci, i in enumerate(combinations(range(N),M)):
        for cj, j in enumerate(combinations(range(N),M)):
            C[ci,cj]=f(N,M, compute_L(i,j))
        print(C[ci,:])
        
    # print("matrix C is\n",C)


    print("matrix of C^-1 is\n",)
    invC= inv(C)
    for i in range(invC.shape[0]):
        # for j in range(invC.shape[1]):
        print(invC[i,:])
        # print()
 
if __name__ == '__main__':
    compute_convariance_matrix(N=4,M=2)
    compute_convariance_matrix(N=5,M=2)
    compute_convariance_matrix(N=6,M=2)
    compute_convariance_matrix(N=6,M=3)
    compute_convariance_matrix(N=7,M=2)
    compute_convariance_matrix(N=7,M=3)