#!/usr/bin/zsh

basepath=/depot/yexiang/apps/jiang631/data/scibench
py310=/home/jiang631/workspace/miniconda3/envs/py310/bin/python3


thispath=$basepath/mcts_and_cvmcts
data_path=$basepath/data/unencrypted/equations_feynman
opt=L-BFGS-B

noise_type=normal
noise_scale=0.0
metric_name=neg_nmse
all_equations=`ls $data_path/Feynman*.in`
for eq_name in $all_equations;
do
    echo "Submitted $eq_name"
    short_name=$(basename "$eq_name")
    trimed_name=${short_name:7:-3}
        dump_dir=$basepath/result/Feynman/$(date +%F)
    if [ ! -d "$dump_dir" ]
    then
        echo "create dir: $dump_dir"
        mkdir -p $dump_dir
        fi
        log_dir=$basepath/log/Feynman/$(date +%F)/
        if [ ! -d "$log_dir" ]
        then
        echo "create dir: $log_dir"
        mkdir -p $log_dir
        fi
    sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
 #!/bin/bash -l

 #SBATCH --job-name="TS$trimed_name"
 #SBATCH --output=$log_dir/${eq_name}.metric_${metric_name}.noise_${noise_type}_${noise_scale}.mcts.out
 #SBATCH --constraint=A
 #SBATCH --time=24:00:00
 #SBATCH --mem=4096MB

hostname

$py310 $thispath/main.py --equation_name $data_path/$eq_name --optimizer $opt\
        		--metric_name $metric_name --noise_type $noise_type --noise_scale $noise_scale \
         > $dump_dir/${short_name}.metric_${metric_name}.noise_${noise_type}${noise_scale}.mcts.out

EOT

done

