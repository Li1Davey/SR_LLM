#!/bin/bash -l
set -x
#basepath=/home/jiang631/data/scibench
basepath=/home/jiangnan/PycharmProjects/scibench/eureqa/
type=Livermore2
nv=4
datasource=${type}_Vars${nv}
dates=2023-08-08
metric=neg_mse


python parse_results.py --eureqa_path $basepath/result/$datasource/$dates/eureqa_result.csv \
--metric $metric \
--noise_type normal \
--noise_scale 0.0
