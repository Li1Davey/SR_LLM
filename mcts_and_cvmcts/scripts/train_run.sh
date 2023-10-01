#!/usr/bin/zsh
set -x
task=nguyen-8
num_run=10
output_dir=results/
python spl_train.py --task $task --num_run $num_run --output_dir $output_dir
