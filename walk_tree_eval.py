import torch
import torch.nn as nn

from diff_ops import *

class WalkTreeEval(nn.Module):
    # in the tree, (0, const_id), (1, inputs_id), (2, operator_str)
    def __init__(self, tree, const_init_val, lap_dx = 1.0, lap_dy = 1.0, \
                 partial_dx = 1.0, partial_dy = 1.0):
        super(WalkTreeEval, self).__init__()
        
        self.tree = tree
        self.consts = nn.Parameter(torch.from_numpy(const_init_val).double())

        self.lap_dx = lap_dx
        self.lap_dy = lap_dy
        self.partial_dx = partial_dx
        self.partial_dy = partial_dy

        self.lap = LaplacianOp()
        self.partial = DifferentialOp()

    def forward(self, inputs):
        eval_result, ip = self.dfs_forward(inputs, 0)
        return eval_result

    def dfs_forward(self, inputs, ip):
        if self.tree[ip][0] == 0:
            # constants
            return self.consts[self.tree[ip][1]], ip+1
        elif self.tree[ip][0] == 1:
            # inputs
            return inputs[self.tree[ip][1]], ip+1
        else:
            # operators
            # print('to process', self.tree[ip])
            assert self.tree[ip][0] == 2
            if self.tree[ip][1] in ['+', '-', '*', '/']:
                # binary operators
                eval_l, ip_l = self.dfs_forward(inputs, ip+1)
                eval_r, ip_r = self.dfs_forward(inputs, ip_l)
                # print('eval_l', eval_l)
                # print('eval_r', eval_r)
                if self.tree[ip][1].startswith('+'):
                    return eval_l + eval_r, ip_r
                elif self.tree[ip][1].startswith('-'):
                    return eval_l - eval_r, ip_r
                elif self.tree[ip][1].startswith('*'):
                    return eval_l * eval_r, ip_r
                elif self.tree[ip][1].startswith('/'):
                    return eval_l / eval_r, ip_r
                else:
                    assert False
            else:
                # singular operators
                eval1, ip1 = self.dfs_forward(inputs, ip+1)
                # print('eval1', eval1)
                if self.tree[ip][1].startswith('dx'):
                    return self.partial(eval1, diffx=True, d=self.partial_dx), ip1
                elif self.tree[ip][1].startswith('dy'):
                    return self.partial(eval1, diffx=False, d=self.partial_dy), ip1 
                elif self.tree[ip][1].startswith('lap'):
                    return self.lap(eval1, dx=self.lap_dx, dy=self.lap_dy), ip1
                elif self.tree[ip][1].startswith('clamp01'):
                    return torch.clamp(eval1, min=0.0, max=1.0), ip1
                else:
                    assert False

