"""Utility functions used in deep symbolic optimization."""

import collections
import copy
import functools
import numpy as np
import time
from typing import List
import itertools
import copy

# def unique(arr):
#     return list(set(arr))


# this node is used for keep track of variable ordering
class Node(object):
    def __init__(self, prev_vf: List = None, next_vf: List = None, total_vf: List = None):
        """

        Parameters
        ----------
        prev_vf: previous free variables
        next_vf: next free variables
        total_vf: all free variables
        """
        self.prev_vf = prev_vf
        self.next_vf = next_vf
        if not total_vf:
            self.total_vf = copy.copy(self.prev_vf)
            self.total_vf.extend(self.next_vf)
        else:
            self.total_vf = total_vf

    def __eq__(self, other):
        if not other:
            return False
        if self.prev_vf == other.prev_vf and self.next_vf == other.next_vf and self.total_vf == other.total_vf:
            return True
        return False

    def __repr__(self):
        return f"hist={self.prev_vf},next={self.next_vf}->total={self.total_vf}"

    def __hash__(self):
        return hash(f"{self.prev_vf},{self.next_vf}->{self.total_vf}")


def create_node(prev_node, new_vf):
    # if prev_node == another_pool_idx or another_pool_idx.cur[0] in set(one_pool_idx.cur):
    #     return None
    new_total_vf = prev_node.total_vf
    new_total_vf.extend(new_vf)
    # new_pool_idx = tuple(new_pool_idx)
    # if new_pool_idx == one_pool_idx.total_vf or new_pool_idx == another_pool_idx.total_vf:
    #     return None
    return Node(prev_node.total_vf, new_vf, new_total_vf)


def create_geometric_generations(n_generations, nvar):
    gens = [0] * nvar
    for it in range(nvar - 1, 0, -1):
        gens[it] = n_generations // 2
        n_generations -= gens[it]
    gens[0] = n_generations
    for it in range(0, nvar):
        if gens[it] < 50:
            gens[it] = 50
    print('generation #:', gens, 'sum=', sum(gens))
    return gens


def create_uniform_generations(n_generations, nvar):
    gens = [0] * nvar
    each_gen = n_generations // nvar
    for it in range(nvar - 1, 0, -1):
        gens[it] = each_gen
        n_generations -= each_gen
    gens[0] = n_generations
    print('generation #:', gens, 'sum=', sum(gens))
    return gens


def is_float(s):
    """Determine whether the input variable can be cast to float."""
    try:
        float(s)
        return True
    except ValueError:
        return False


# Adapted from: https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python
def is_pareto_efficient(costs):
    """
    Find the pareto-efficient points given an array of costs.

    Parameters
    ----------

    costs : np.ndarray
        Array of shape (n_points, n_costs).

    Returns
    -------

    is_efficient_maek : np.ndarray (dtype:bool)
        Array of which elements in costs are pareto-efficient.
    """

    is_efficient = np.arange(costs.shape[0])
    n_points = costs.shape[0]
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index < len(costs):
        nondominated_point_mask = np.any(costs < costs[next_point_index], axis=1)
        nondominated_point_mask[next_point_index] = True
        is_efficient = is_efficient[nondominated_point_mask]  # Remove dominated points
        costs = costs[nondominated_point_mask]
        next_point_index = np.sum(nondominated_point_mask[:next_point_index]) + 1
    is_efficient_mask = np.zeros(n_points, dtype=bool)
    is_efficient_mask[is_efficient] = True
    return is_efficient_mask


class cached_property(object):
    """
    Decorator used for lazy evaluation of an object attribute. The property
    should be non-mutable, since it replaces itself.
    """

    def __init__(self, getter):
        self.getter = getter

        functools.update_wrapper(self, getter)

    def __get__(self, obj, cls):
        if obj is None:
            return self

        value = self.getter(obj)
        setattr(obj, self.getter.__name__, value)
        return value


def weighted_quantile(values, weights, q):
    """
    Computes the weighted quantile, equivalent to the exact quantile of the
    empirical distribution.

    Given ordered samples x_1 <= ... <= x_n, with corresponding weights w_1,
    ..., w_n, where sum_i(w_i) = 1.0, the weighted quantile is the minimum x_i
    for which the cumulative sum up to x_i is greater than or equal to 1.

    Quantile = min{ x_i | x_1 + ... + x_i >= q }
    """

    sorted_indices = np.argsort(values)
    sorted_weights = weights[sorted_indices]
    sorted_values = values[sorted_indices]
    cum_sorted_weights = np.cumsum(sorted_weights)
    i_quantile = np.argmax(cum_sorted_weights >= q)
    quantile = sorted_values[i_quantile]

    # NOTE: This implementation is equivalent to (but much faster than) the
    # following:
    # from scipy import stats
    # empirical_dist = stats.rv_discrete(name='empirical_dist', values=(values, weights))
    # quantile = empirical_dist.ppf(q)

    return quantile


# Entropy computation in batch
def empirical_entropy(labels):
    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.
    # Compute entropy
    for i in probs:
        ent -= i * np.log(i)

    return ent


def get_duration(start_time):
    return get_human_readable_time(time.time() - start_time)


def get_human_readable_time(s):
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return "{:02d}:{:02d}:{:02d}:{:05.2f}".format(int(d), int(h), int(m), s)


def safe_merge_dicts(base_dict, update_dict):
    """Merges two dictionaries without changing the source dictionaries.

    Parameters
    ----------
        base_dict : dict
            Source dictionary with initial values.
        update_dict : dict
            Dictionary with changed values to update the base dictionary.

    Returns
    -------
        new_dict : dict
            Dictionary containing values from the merged dictionaries.
    """
    if base_dict is None:
        return update_dict
    base_dict = copy.deepcopy(base_dict)
    for key, value in update_dict.items():
        if isinstance(value, collections.Mapping):
            base_dict[key] = safe_merge_dicts(base_dict.get(key, {}), value)
        else:
            base_dict[key] = value
    return base_dict
