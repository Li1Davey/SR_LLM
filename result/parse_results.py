import argparse
import os

import pandas as pd

# from compute_dso_all_metrics import compute_dso_all_metrics, compute_eureqa_all_metrics


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
    # print(val_dict)
    return val_dict


# def parse_gp_file(filename):
#     # print('filename=', filename)
#     inp = open(filename, 'r')
#     l = read_until_line_starts_with(inp, 'final hof')
#     # print('l=', l)
#     rs = []
#     l = read_until_line_starts_with(inp, 'validate r=')
#     while l != "":
#         print('l=', l.strip())
#         tt = l[:-1].split()
#         val_dict = create_all_metrics_dict(inp)
#         rs.append([float(tt[2]), val_dict])
#         l = read_until_line_starts_with(inp, 'validate r=')

#     inp.close()
#     # print(rs)
#     rs.sort(key=lambda x: x[0], reverse=True)  # changes the list in-place (and returns None)
#     # print(rs[0])
#     r = rs[0]
#     return r

def parse_gp_file(filename, verbose=False):
    #print('filename=', filename)
    inp = open(filename, 'r')
    l = read_until_line_starts_with(inp, 'final hof')
    #print('l=', l)
    rs = []
    l = read_until_line_starts_with(inp, 'validate r=')
    while l != "":
        
        tt = l[:-1].split()
        rs.append(-float(tt[2]))
        if verbose:
            print('l=', l.strip())
        l = read_until_line_starts_with(inp, 'validate r=')
    inp.close()
    if verbose: print(f"filename:{filename}, reward:{rs}")
    r = min(rs)
    return r


def parse_dso_file(dso_log_filename, true_program_file, basepath, noise_std=0.1):
    if not os.path.isfile(dso_log_filename):
        print(dso_log_filename, 'does not exist')
    # print(dso_log_filename)
    inp = open(dso_log_filename, 'r')
    l = read_until_line_starts_with(inp, 'Source path______')
    # print(l)
    data_frame_basepath = l.strip().split('/')[-1]
    print(data_frame_basepath)
    csv_expr_dir = os.path.join(basepath, 'scripts/log', data_frame_basepath)

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
    print(true_program_file)
    # return compute_dso_all_metrics(true_program_file, csv_expr_path, testset_size=256, noise_std=noise_std)


def parse_exp_set(file_prefix, metric_name, noise_type, noise_scale, dso_basepath):
    all_dso_r, all_gp_r, all_egp_r = {}, {}, {}
    gp_output_files, egp_output_files={}, {}
    for root, dirs, files in os.walk(file_prefix, topdown=False):
        for name in files:
            if metric_name in name and noise_type in name and noise_scale in name:
                if 'gp' in name and 'egp' not in name:
                    gp_output_files[name.split('.')[0]] = os.path.join(root, name)
                elif 'egp' in name:
                    egp_output_files[name.split('.')[0]] = os.path.join(root, name)
    for prog in gp_output_files:
        try:
            filename=gp_output_files[prog]
            if not os.path.isfile(filename):
                raise FileExistsError(filename, 'does not exists!')
            gp_r = parse_gp_file(filename, verbose=True)
            all_gp_r[prog] = gp_r
            print('gp', gp_r)
        except:
            print(f'cannot parse GP {filename}')
    
    for prog in egp_output_files:
        try:
            filename=egp_output_files[prog]
            print(f"egp file: {filename}")
            if not os.path.isfile(filename):
                raise FileExistsError(filename, 'does not exists!')
            egp_r = parse_gp_file(filename, verbose=False)
            all_egp_r[prog] = egp_r
            print('egp', egp_r)
        except:
            print(f'cannot parse EGP {filename}')

    
    if dso_basepath == None:
        return all_dso_r, all_gp_r, all_egp_r
    
    for baseline_name in ['VPG', 'PQT', 'DSR', 'GPMELD']:
        all_dso_r[baseline_name] = {}
        # for i in range(start, end):
        #     try:
        #         dso_file = file_prefix + str(i) + '.data.metric_inv_nrmse.' + baseline_name + file_suffix
        #         print(dso_file)
        #         dso_r = parse_dso_file(dso_file, true_program_file + str(i) + '.data', dso_basepath, noise_std)
        #         if dso_r != None:
        #             all_dso_r[baseline_name][i] = dso_r
        #             # print('dso', dso_r)
        #     except:
        #         print(i, "cannot process with", baseline_name)
    return all_dso_r, all_gp_r, all_egp_r
    



def pretty_print_dso_family(all_rs):
    for key in ['r2_score','neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse', 'neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
        print('{}, DSR, PQT, VPG, GPMELD'.format(key))
        for idx in range(10):
            print(idx, end=", ")
            for baseline_name in ['DSR', 'PQT', 'VPG', 'GPMELD']:
                if idx in all_rs[baseline_name]:
                    print(all_rs[baseline_name][idx][key], end=", ")
                else:
                    print(",", end=" ")
            print()
        print()


def pretty_print_pair(all_gp_rs, all_egp_rs, metric_name, is_numbered=True):
    # for key in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse', 'neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
        print(f"{metric_name}\n GP, EGP")
        if is_numbered:
            for key in range(10):
                key ='prog_'+str(key)
                if key in all_gp_rs:
                    print(all_gp_rs[key], end=", ")
                else:
                    print(",", end=" ")
                if key in all_egp_rs:
                    print(all_egp_rs[key])
                else:
                    print()
        else:
            for key in all_gp_rs.keys():
                if key in all_gp_rs:
                    print(all_gp_rs[key], end=", ")
                else:
                    print(",", end=" ")
                if key in all_egp_rs:
                    print(all_egp_rs[key])
                else:
                    print()


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
    parser.add_argument('--fp', type=str, required=True)
    parser.add_argument('--metric', type=str, default='neg_mse', required=True)
    parser.add_argument('--dso_basepath', type=str, required=False, default='None')
    parser.add_argument('--noise_type', type=str, required=True, default="None")
    parser.add_argument('--noise_scale', type=str, default='0.0')
    parser.add_argument('--is_numbered', type=int, default=1)
    
    # Parse the argument
    args = parser.parse_args()

    all_dso_r, all_gp_r, all_egp_r = parse_exp_set(args.fp, args.metric, args.noise_type, args.noise_scale, args.dso_basepath)
    print(all_gp_r)
    print(all_egp_r)
    # if len(all_dso_r) != 0:
    #     pretty_print_dso_family(all_dso_r)
    print("GP & EGP")
    if len(all_gp_r) != 0 or len(all_egp_r):
        pretty_print_pair(all_gp_r, all_egp_r, args.metric, is_numbered=args.is_numbered)
