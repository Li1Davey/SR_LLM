#!/bin/bash -l
set -x

basepath=/home/jiangnan/PycharmProjects/scibench/eureqa/
type=Livermore2
nv=6
datasource=${type}_Vars${nv}
dates=2023-12-08


python parse_results.py --eureqa_path $basepath/result/$datasource/$dates/eureqa_result.csv \
--noise_type normal \
--noise_scale 0.0
