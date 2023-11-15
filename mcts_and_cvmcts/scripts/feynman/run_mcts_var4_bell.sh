#!/usr/bin/zsh

basepath=/depot/yexiang/apps/jiang631/data/scibench
py310=/home/jiang631/workspace/miniconda3/envs/py310/bin/python3

thispath=$basepath/mcts_and_cvmcts
data_path=$basepath/data/unencrypted/equations_feynman
opt=L-BFGS-B

noise_type=normal
noise_scale=0.0
metric_name=neg_nmse

for eq_name in FeynmanICh8Eq14.in FeynmanICh13Eq4.in FeynmanICh13Eq12.in FeynmanICh18Eq4.in FeynmanICh18Eq16.in FeynmanICh24Eq6.in FeynmanICh29Eq16.in FeynmanICh32Eq17.in FeynmanICh34Eq8.in FeynmanICh40Eq1.in FeynmanICh43Eq16.in FeynmanICh44Eq4.in FeynmanICh50Eq26.in FeynmanIICh11Eq20.in FeynmanIICh34Eq11.in FeynmanIICh35Eq18.in FeynmanIICh35Eq21.in FeynmanIICh38Eq3.in FeynmanIIICh10Eq19.in FeynmanIIICh14Eq14.in FeynmanIIICh21Eq20.in FeynmanBonus1.in FeynmanBonus3.in FeynmanBonus11.in FeynmanBonus19.in; do
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
