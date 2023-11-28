import argparse
import os
from multiprocessing import Process
import sympy
from sympy import Symbol
from sympy.parsing import parse_expr

from sympy2zss_conversion import sympy2zss_module, count_nodes, compute_distance


def get_est_gt_eq_pairs(est_eq_dir_path, est_delim, gt_eq_dir_path, gt_delim):
    est_gt_pair_list = list()
    est_eq_dict = {file_name.split(est_delim)[0]: os.path.join(est_eq_dir_path, file_name)
                   for file_name in os.listdir(est_eq_dir_path) if file_name.endswith('.pkl')}
    for gt_file_name in os.listdir(gt_eq_dir_path):
        if not gt_file_name.endswith('.pkl') or gt_delim not in gt_file_name:
            continue

        gt_file_path = os.path.join(gt_eq_dir_path, gt_file_name)
        gt_key = gt_file_name.split(gt_delim)[0]
        if gt_key in est_eq_dict:
            est_file_path = est_eq_dict.pop(gt_key)
            est_gt_pair_list.append((est_file_path, gt_file_path))
        else:
            est_gt_pair_list.append((None, gt_file_path))
    print(f'{len(est_gt_pair_list)} equation pairs matched')
    return est_gt_pair_list


def load_eq_as_tree(one_equation, prints=True):
    try:
        eq_sympy = parse_expr(one_equation)
        eq_sympy = sympy.sympify(str(eq_sympy))
        eq_sympy = eq_sympy.subs(sympy.pi, sympy.pi.evalf()).evalf().factor().simplify().subs(1.0, 1)
        eq_sympy = sympy.sympify(str(eq_sympy))
    except TypeError as te:
        if prints:
            print(te)
            print(f'[{one_equation}]')
        return None, None
    except Exception as e:
        if prints:
            print(e)
            print(f'[{one_equation}]')
        return None, None

    if prints:
        print(f'[{one_equation}]')
        print(f'Eq.: {eq_sympy}')
    return sympy2zss_module(eq_sympy), eq_sympy


def compare_equation(est_eq_file_path, gt_eq_file_path, normalizes, prints=True, returns_eqs=False):
    gt_eq_tree, gt_eq = load_eq_as_tree(gt_eq_file_path, prints=prints)
    if est_eq_file_path is not None:
        p = Process(target=load_eq_as_tree, args=[est_eq_file_path, False])
        p.start()
        p.join(timeout=120)
        p.terminate()
        if p.exitcode is None:
            print(f'Failed to load `{est_eq_file_path}`')
            edit_dist = 1 if normalizes else count_nodes(gt_eq_tree)
            est_eq = None
        else:
            est_eq_tree, est_eq = load_eq_as_tree(est_eq_file_path, prints=prints)
            if est_eq_tree is not None:
                edit_dist = compute_distance(est_eq_tree, gt_eq_tree, normalizes)
            else:
                edit_dist = 1 if normalizes else count_nodes(gt_eq_tree)
    else:
        est_eq = None
        edit_dist = 1 if normalizes else count_nodes(gt_eq_tree)
    if prints:
        edit_dist2print = str(edit_dist) if edit_dist is not None else 'N/A'
        print(f'Edit distance: {edit_dist2print}\n')
    if returns_eqs:
        num_gt_nodes = count_nodes(gt_eq_tree)
        return edit_dist, num_gt_nodes, est_eq, gt_eq
    return edit_dist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Equation comparator')
    parser.add_argument('--est', required=True, help='file/dir path for pickled, estimated equation(s)')
    parser.add_argument('--gt', required=True, help='file/dir path for pickled, ground-truth equation(s)')
    parser.add_argument('-normalize', action='store_true', help='normalize distance by ground-truth equation')

    args = parser.parse_args()
    est_path = os.path.expanduser(args.est)
    gt_path = os.path.expanduser(args.gt)
    if os.path.isfile(est_path) and os.path.isfile(gt_path):
        compare_equation(est_path, args.gt, args.normalize)
    else:
        raise ValueError('--est and --gt should be either both file paths or both dir paths')
