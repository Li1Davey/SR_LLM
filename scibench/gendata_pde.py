import os

from symbolic_equation_evaluator_public import decrypt_equation, Equation_evaluator
import numpy as np
from symbolic_data_generator import *


def to_csv(X, y, filename):
    d = np.concatenate((X, y), axis=1)
    np.random.shuffle(d)
    np.savetxt(filename + ".csv", d, delimiter=",")


def save_simulated_pde(all_phi, filename):
    print("saving to:", filename)
    np.save(filename, all_phi)


if __name__ == '__main__':
    basepath = "/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_pde/{}.in"
    to_folder = "/home/jiangnan/PycharmProjects/scibench/data/equations_pde/{}"
    for prog in ['SpinodalDecomp64x64', ]:
        filename = basepath.format(prog)
        data_query_oracle = Equation_evaluator(filename, noise_type='normal', noise_scale=0.0, metric_name='neg_mse')
        dataX = DataX(data_query_oracle.get_vars_range_and_types())
        batchsize = 100
        simulated_steps = 2000
        all_y = []
        for bi in range(batchsize):
            print(f'bi={bi}')
            Nx, Ny = data_query_oracle.dim[0]
            c0 = dataX.randn(batchsize).squeeze()
            print(c0.shape)
            y = data_query_oracle.execute_simulate(c0, simulated_steps)
            all_y.append(y)
        output_filename = "_".join([prog, "bs" + str(batchsize), 'steps' + str(simulated_steps)])
        save_simulated_pde(all_y, to_folder.format(output_filename))


