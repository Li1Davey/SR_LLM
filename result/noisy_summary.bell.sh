#!/bin/bash -l
set -x
basepath=/home/jiang631/data/xyx_dso
operators=inv
noise_std=0.0
datasource=${operators}_nv4_nt46
dates=2023-01-25
metric=neg_mse
python parse_results.py --fp $basepath/result/noisy${noise_std}_$datasource/$dates/prog_ \
--metric $metric \
--true_program_file $basepath/data/$datasource/prog_ \
--dso_basepath $basepath/dso_classic \
--noise_std $noise_std

