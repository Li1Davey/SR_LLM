#!/usr/bin/zsh

basepath=/depot/yexiang/apps/jiang631/data/scibench
py310=/home/jiang631/workspace/miniconda3/envs/py310/bin/python3

thispath=$basepath/mcts_and_cvmcts
data_path=$basepath/data/unencrypted/equations_feynman
opt=L-BFGS-B

noise_type=normal
noise_scale=0.0
metric_name=neg_nmse
for eq_name in FeynmanICh12Eq11.in FeynmanIICh2Eq42.in FeynmanIICh6Eq15a.in FeynmanIICh11Eq3.in FeynmanIICh11Eq17.in FeynmanIICh36Eq38.in FeynmanIIICh9Eq52.in FeynmanBonus4.in FeynmanBonus12.in FeynmanBonus13.in FeynmanBonus14.in FeynmanBonus16.in; do
	echo "submit $eq_name"
	trimed_name=${eq_name:7:-3}
	dump_dir=$basepath/result/feynman_vars4/$(date +%F)
	if [ ! -d "$dump_dir" ]; then
		echo "create dir: $dump_dir"
		mkdir -p $dump_dir
	fi
	log_dir=$basepath/log/$(date +%F)
	if [ ! -d "$log_dir" ]; then
		echo "create dir: $log_dir"
		mkdir -p $log_dir
	fi
	sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="mtcs_$trimed_name"
#SBATCH --output=$log_dir/${eq_name}.metric_${metric_name}.noise_${noise_type}_${noise_scale}.mcts.out
#SBATCH --constraint=A
#SBATCH --time=12:00:00
#SBATCH --mem=4096MB

hostname

$py310 $thispath/main.py --equation_name $data_path/$eq_name --optimizer $opt
						--metric_name $metric_name --noise_type $noise_type --noise_scale $noise_scale \
         				> $dump_dir/${eq_name}.metric_${metric_name}.noise_${noise_type}${noise_scale}.mcts.out

EOT

done
