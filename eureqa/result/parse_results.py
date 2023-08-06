import argparse
import os
import numpy as np
import pandas as pd
from sympy.parsing.sympy_parser import parse_expr
# from compute_all_metrics import compute_eureqa_all_metrics
from symbolic_data_generator import DataX
from symbolic_equation_evaluator_public import Equation_evaluator

def read_until_line_starts_with(inp, line):
    l = inp.readline()
    while l != "" and not l.startswith(line):
        l = inp.readline()
    return l


def create_all_metrics_dict(inp):
    l = inp.readline()
    # print(l)
    l = inp.readline()
    # print(l)
    val_dict = {}
    while l != "" and not l.startswith("%%%%%"):
        spl = l.split(" ")
        val_dict[spl[0]] = float(spl[1].strip())
        l = inp.readline()
        # print(l)
    print(val_dict)
    return val_dict


def compute_eureqa_all_metrics(equation_filename, noise_type, noise_scale, expr_str, testset_size, metric_name=""):
    data_query_oracle = Equation_evaluator(equation_filename, noise_type, noise_scale, metric_name)
    dataXgen = DataX(data_query_oracle.get_vars_range_and_types())
    nvar = data_query_oracle.get_nvars()

    X_test = dataXgen.randn(testset_size)
    # y_test_noiseless = y_test
    expr_str = expr_str.replace("^", "**")
    print("orig expr string:", expr_str)
    expr = parse_expr(expr_str)
    print('eureqa', expr.expand())
    var_x = expr.free_symbols
    print(var_x)
    y_hat = np.zeros(X_test.shape[0])
    for idx in range(X_test.shape[0]):
        X = X_test[idx, :]
        val_dict = {}
        for x in var_x:
            i = int(x.name[1:]) - 1
            val_dict[x] = X[i]
        y_hat[idx] = expr.evalf(subs=val_dict)
    print('%' * 30)
    dict_of_rs = data_query_oracle(X, y_hat)

    return dict_of_rs

def parse_exp_set(file_prefix, metric_name, noise_type, noise_scale, true_program_basepath, dso_basepath, keyword="Korns"):
    all_dso_r, all_gp_r, all_egp_r = {}, {}, {}
    gp_output_files, egp_output_files = {}, {}
    dso_output_files = {}
    for key in ['VPG', 'PQT', 'DSR', 'GPMELD']:
        dso_output_files[key] = {}
    for root, dirs, files in os.walk(file_prefix, topdown=False):
        for name in files:
            if keyword and  keyword not in name:
                continue
            if metric_name in name and noise_type in name and noise_scale in name:
                if 'gp' in name and 'egp' not in name:
                    gp_output_files[name.split('.')[0]] = os.path.join(root, name)
                elif 'egp' in name:
                    egp_output_files[name.split('.')[0]] = os.path.join(root, name)
            for key in ['VPG', 'PQT', 'DSR', 'GPMELD']:
                dso_output_files[key][name.split('.')[0]] = os.path.join(root, name)




def parse_eureqa_solutions(eureqa_basepath, noise_std):
    df = pd.read_csv(eureqa_basepath)
    all_eureqa_r = {}
    result_dict = {}
    for row in df.iterrows():
        prog = row['benchmark']
        idx = int(prog.split('_')[-1])
        predicted = row['solution']
        result_dict[idx] = predicted
        equreqa_ri = compute_eureqa_all_metrics(prog+'.in', result_dict[idx], testset_size=256,
                                                    noise_std=noise_std)
        all_eureqa_r[idx] = equreqa_ri
        # except:
        #     print(i, "eureqa cannot process")

    return all_eureqa_r

def pretty_print_eureqa(all_eureqa_rs):
    for key in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse', 'neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
        # print('{}\ndata idx, gp, expand_gp, dso'.format(key))
        print(key, ", EUREQA")
        for idx in range(10):
            print(idx, end=", ")
            if idx in all_eureqa_rs:
                print(all_eureqa_rs[idx][key])
            else:
                print()
        print()


if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('--metric', type=str, default='neg_mse')
    parser.add_argument('--noise_type', type=str, default="None")
    parser.add_argument('--noise_scale', type=str, default='0.0')
    parser.add_argument('--eureqa_path', type=str, required=True)

    # Parse the argument
    args = parser.parse_args()
    all_eureqa_r = parse_eureqa_solutions(args.eureqa_path, args.true_program_file)
    pretty_print_eureqa(all_eureqa_r)
