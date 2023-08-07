#!/bin/bash -l
set -x
#basepath=/home/jiang631/data/scibench
basepath=/home/jiangnan/PycharmProjects/scibench/
type=$1
nv=$2
nt=$3
datasource=${type}_nv${nv}_nt${nt}
dates=2023-07-27
metric=neg_mse
#python parse_results.py --fp $basepath/result/$datasource/$dates/ \
#--metric $metric \
#--dso_basepath $basepath/dso_classic \
#--noise_type normal \
#--noise_scale 0.0 \
#--is_numbered 1



python parse_randgp_results.py --fp $basepath/result/$datasource/$dates/ \
--metric $metric \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 1
