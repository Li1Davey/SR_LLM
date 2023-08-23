#!/bin/bash -l
set -x
basepath=/home/jiang631/data/scibench
#basepath=/home/jiang631/jiang631_scratch/data/scibench
# basepath=/home/jiangnan/PycharmProjects/scibench/
type=$1
nv=$2
nt=$3
datasource=${type}_nv${nv}_nt${nt}
dates=2023-$4
data_folder_name=trigometric

python parse_results.py --fp $basepath/result/$datasource/$dates/ \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 1 \
--keyword $5 \
--dso_basepath $basepath/dso_classic/scripts \
--true_program_basepath $basepath/data/unencrypted/equations_$data_folder_name/${datasource}_prog_



##basepath=/home/jiang631/data/scibench
#basepath=/home/jiangnan/PycharmProjects/scibench/eureqa/
#type=Livermore2
#nv=4
#datasource=${type}_Vars${nv}
#dates=2023-08-08
#metric=neg_mse
#
#
#python parse_results.py --eureqa_path $basepath/result/$datasource/$dates/eureqa_result.csv \
#--metric $metric \
#--noise_type normal \
#--noise_scale 0.0
