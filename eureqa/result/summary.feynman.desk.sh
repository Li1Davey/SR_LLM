#!/bin/bash -l
set -x
#basepath=/home/jiang631/data/scibench
basepath=/home/jiangnan/PycharmProjects/scibench/eureqa/
type=Feynman
nv=8
datasource=${type}_Vars${nv}
dates=2023-12-11



python parse_results.py --eureqa_path $basepath/result/$datasource/$dates/eureqa_result.csv \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 0