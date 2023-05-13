#!/bin/bash -l

basepath=/home/jiang631/data/scibench
type=$1
nv=$2
nt=$3
datasource=${type}_nv3_nt22
dates=2023-05-12
metric=neg_mse
python parse_results.py --fp $basepath/result/$datasource/$dates/ \
--metric $metric \
--dso_basepath $basepath/dso_classic \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 1