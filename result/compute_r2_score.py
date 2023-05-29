import argparse
import os
import pickle
import numpy as np
import feynman
from feynman.datasets.file_util import make_parent_dirs, load_yaml_file
from feynman.datasets import sampling, physic_equations
from feynman.datasets.registry import get_eq_obj
from feynman.datasets.sampling import build_sampling_objs
import argparse
import os

from compute_dso_all_metrics import read_dso_expression, make_regression_metric

import argparse

from sympy.parsing.sympy_parser import parse_expr
import scipy
from sklearn.metrics import r2_score


def read_until_line_starts_with(inp, line):
    l = inp.readline()
    while l != "" and not l.startswith(line):
        l = inp.readline()
    return l


def parse_dso_file(dso_log_filename, X_test, y_true, basepath, noise_std=0.0):
    if not os.path.isfile(dso_log_filename):
        print(dso_log_filename, 'does not exist')
    # print(dso_log_filename)
    inp = open(dso_log_filename, 'r')
    l = read_until_line_starts_with(inp, 'Source path______')
    # print(l)
    data_frame_basepath = l.strip().split('/')[-1]
    print(data_frame_basepath)
    csv_expr_dir = os.path.join(basepath, 'scripts', 'feynman', 'log', data_frame_basepath)

    if not os.path.isdir(csv_expr_dir):
        print(csv_expr_dir, 'does not exists')
        return None
    else:
        print(csv_expr_dir, 'exists')
    csv_expr_path = None
    for root, dirs, files in os.walk(csv_expr_dir):
        for name in files:
            if name.endswith("hof.csv"):
                csv_expr_path = os.path.join(root, name)
                break
    if not os.path.isfile(csv_expr_path):
        print("cannot find hof file")
    print(csv_expr_path)
    y_hat = read_dso_expression(csv_expr_path, X_test)
    print('%' * 30)
    dict_of_rs = {}
    for metric_name in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse']:
        metric_params = (1.0,)
        metric = make_regression_metric(metric_name, *metric_params)
        r = metric(y_true, y_hat, np.var(y_true))
        dict_of_rs[metric_name] = r
        # print('{} {}'.format(metric_name, r))

    for metric_name in ['neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
        metric_params = [1.0, ]
        metric = make_regression_metric(metric_name, *metric_params)
        r = metric(y_true, y_hat)
        dict_of_rs[metric_name] = r
    score = r2_score(y_true, y_hat)
    dict_of_rs['r2_score'] = score
    return dict_of_rs


def parse_exp_set(file_prefix, metric_name, eq_dict, dso_basepath, noise_std, tau=0.99):
    all_dso_r, all_gp_r2_accuracy, all_egp_r2_accuracy = {}, {}, {}

    for baseline_name in ['VPG', 'PQT', 'DSR', 'GPMELD']:
        all_dso_r[baseline_name] = {}
        r2_score_list, correct_flag_list = [], []
        for eqname in eq_dict:
            try:
                X_test, y_true = eq_dict[eqname]
                dso_file = file_prefix + eqname + '.metric_inv_nrmse.' + baseline_name + ".out"
                print(dso_file)
                dict_of_rs = parse_dso_file(dso_file, X_test, y_true, dso_basepath, noise_std)
                if dict_of_rs != None:
                    all_dso_r[baseline_name][eqname] = dict_of_rs
                    # r2_score_list.append(dso_r2_score)
                    # correct_flag_list.append(dso_r2_score > tau)
            except:
                print(eqname, "cannot process with", baseline_name)

    return all_dso_r, all_gp_r2_accuracy, all_egp_r2_accuracy


def pretty_print_dso(all_rs):
    for key in ['r2_score', 'neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse', 'neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
        print('{}, DSR, PQT, VPG, GPMELD'.format(key))
        for eqname in all_rs['DSR']:
            print(eqname, end=", ")
            for baseline_name in ['DSR', 'PQT', 'VPG', 'GPMELD']:
                if eqname in all_rs[baseline_name]:
                    print(all_rs[baseline_name][eqname][key], end=", ")
                else:
                    print(",", end=" ")
            print()
        print()


def load_all_expression_and_generate_Xtest(yaml_path):
    yaml_config = load_yaml_file(yaml_path)
    print(yaml_config)
    eqnames = []
    eq_dict = {}
    for eq_up_name in yaml_config['eqname']:
        dataset_kwargs = dict()
        sampling_objs = build_sampling_objs(dataset_kwargs.pop('sampling_objs')) if 'sampling_objs' in dataset_kwargs else None
        eq_instance = get_eq_obj(eq_up_name, sampling_objs=sampling_objs, **dataset_kwargs)

        # Write out each split
        eq_name = eq_instance.get_eq_name(prefix=None, suffix=None)
        X_test_and_y = eq_instance.create_dataset(sample_size=256, use_control_variable=False)
        X_test = X_test_and_y[:, :-1]
        y_true = X_test_and_y[:, -1]
        eqnames.append(eq_name)
        eq_dict[eq_name] = [X_test, y_true]
    return eq_dict


if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('--fp', type=str, required=True)
    parser.add_argument('--metric', type=str, default='inv_nrmse', required=True)
    parser.add_argument('--yaml_path', type=str, required=True)
    parser.add_argument('--dso_basepath', type=str, required=True, default='None')
    parser.add_argument('--eureqa_path', type=str, required=False, default="None")
    parser.add_argument('--noise_std', type=float, default=0.1)
    #
    # Parse the argument
    args = parser.parse_args()
    eq_dict = load_all_expression_and_generate_Xtest(args.yaml_path)
    all_dso_r, all_gp_r, all_egp_r = parse_exp_set(args.fp, args.metric, eq_dict, args.dso_basepath, args.noise_std)

    if len(all_dso_r) != 0:
        pretty_print_dso(all_dso_r)
    # print("GP & EGP")
    # if len(all_gp_r) != 0 or len(all_egp_r):
    #     pretty_print_pair(all_gp_r, all_egp_r)
