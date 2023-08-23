#!/bin/bash -l
set -x
basepath=/home/jiang631/data/scibench
#basepath=/home/jiangnan/PycharmProjects/scibench
datasource=feynman_vars$1
dates=2023-$2
python parse_randgp_results.py --fp $basepath/result/$datasource/$dates/ \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 0 \
--keyword $3 \



# basepath=/home/jiang631/data/scibench
# #basepath=/home/jiangnan/PycharmProjects/scibench
# datasource=Others
# dates=2023-$2
# python parse_randgp_results.py --fp $basepath/result/$datasource/$dates/ \
# --noise_type normal \
# --noise_scale 0.0 \
# --is_numbered 0 \
# --keyword $3 \
# --max_prog 26
