#!/bin/bash -l
set -x
basepath=/home/jiang631/data/scibench
#basepath=/home/jiangnan/PycharmProjects/scibench
datasource=Others
dates=2023-06-05
metric=neg_mse
python parse_results.py --fp $basepath/result/$datasource/$dates/ \
--metric $metric \
--dso_basepath $basepath/dso_classic/scripts/ \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 0 \
--true_program_basepath $basepath/data/unencrypted/equations_others/ \
--keyword $1
