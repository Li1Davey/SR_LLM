import os
import time

from ..symbolic_equation_evaluator_public import Equation_evaluator

from ..symbolic_data_generator import *
from sympy import Symbol, lambdify
def to_csv(X, y, filename):
    d = np.concatenate((X, y), axis=1)
    np.random.shuffle(d)
    np.savetxt(filename + ".csv", d, delimiter=",")


var4 = ['FeynmanICh8Eq14', 'FeynmanICh13Eq4', 'FeynmanICh13Eq12', 'FeynmanICh18Eq4', 'FeynmanICh18Eq16', 'FeynmanICh24Eq6',
        'FeynmanICh29Eq16', 'FeynmanICh32Eq17', 'FeynmanICh34Eq8', 'FeynmanICh40Eq1', 'FeynmanICh43Eq16', 'FeynmanICh44Eq4',
        'FeynmanICh50Eq26', 'FeynmanIICh11Eq20', 'FeynmanIICh34Eq11', 'FeynmanIICh35Eq18', 'FeynmanIICh35Eq21', 'FeynmanIICh38Eq3',
        'FeynmanIIICh10Eq19', 'FeynmanIIICh14Eq14', 'FeynmanIIICh21Eq20', 'FeynmanBonus1', 'FeynmanBonus3', 'FeynmanBonus11',
        'FeynmanBonus19', ]
var5 = ['FeynmanICh12Eq11', 'FeynmanIICh2Eq42', 'FeynmanIICh6Eq15a', 'FeynmanIICh11Eq3', 'FeynmanIICh11Eq17', 'FeynmanIICh36Eq38',
        'FeynmanIIICh9Eq52', 'FeynmanBonus12', 'FeynmanBonus13', 'FeynmanBonus14', 'FeynmanBonus16', 'FeynmanBonus4']

if __name__ == '__main__':
    basepath = "/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_feynman/{}.in"
    to_folder = "/home/jiangnan/PycharmProjects/scibench/eureqa/data/equations_feynman/{}"
    for prog in var5:
        filename = basepath.format(prog)
        data_query_oracle = Equation_evaluator(filename, noise_type='normal', noise_scale=0.0, metric_name='neg_mse')
        nvars = data_query_oracle.get_nvars()
        expr=data_query_oracle.expr
        print(expr)
        dataX = DataX(data_query_oracle.get_vars_range_and_types())
        batchsize = 100000

        X = dataX.randn(sample_size=batchsize)
        st = time.time()
        y = data_query_oracle.evaluate(X).reshape(-1, 1)
        used = time.time()-st
        print("Time used by dataOracle", used)
        x=[Symbol(f"x{i}") for i in range(nvars)]
        function =lambdify(x, expr, 'numpy')
        st = time.time()
        y = function(X)
        used = time.time() - st
        print("Time used by dataOracle", used)

        print(X.shape, y.shape)
        filename_csv = to_folder.format(prog)
        to_csv(X, y, filename_csv)
        print(f"{prog} done......")
        # print(one_eq['eq_expression'].execute(X))
