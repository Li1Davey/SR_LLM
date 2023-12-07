#!/usr/bin/zsh
#basepath=/home/jiangnan/PycharmProjects/scibench
basepath=/depot/yexiang/apps/jiang631/data/scibench
#py3615=/home/jiangnan/anaconda3/envs/py3615/bin/python3
py3615=/home/jiang631/workspace/miniconda3/envs/py3615/bin/python3

for pgn in FeynmanICh12Eq1.in FeynmanICh6Eq20.in FeynmanICh10Eq7.in FeynmanICh12Eq4.in FeynmanICh14Eq3.in FeynmanICh12Eq5.in FeynmanICh14Eq4.in FeynmanICh15Eq10.in FeynmanICh16Eq6.in FeynmanICh25Eq13.in FeynmanICh26Eq2.in FeynmanICh32Eq5.in FeynmanICh34Eq10.in FeynmanICh34Eq14.in FeynmanICh38Eq12.in FeynmanICh39Eq10.in FeynmanICh41Eq16.in FeynmanICh43Eq31.in FeynmanICh48Eq2.in FeynmanIICh3Eq24.in FeynmanIICh4Eq23.in FeynmanIICh8Eq7.in FeynmanIICh10Eq9.in FeynmanIICh11Eq28.in FeynmanIICh13Eq17.in FeynmanIICh13Eq23.in FeynmanIICh13Eq34.in FeynmanIICh24Eq17.in FeynmanIICh34Eq29a.in FeynmanIICh38Eq14.in FeynmanIIICh4Eq32.in FeynmanIIICh4Eq33.in FeynmanIIICh7Eq38.in FeynmanIIICh8Eq54.in FeynmanIIICh15Eq14.in FeynmanBonus8.in FeynmanBonus10.in; do
	trimed_name=${pgn:7:-3}
	echo "submit $trimed_name"
	equation_name=$basepath/data/unencrypted/equations_feynman/$pgn
	dump_dir=$basepath/result/Feynman/$(date +%F)
	if [ ! -d "$dump_dir" ]; then
		echo "create output dir: $dump_dir"
		mkdir -p $dump_dir
	fi
	log_dir=$basepath/log/Feynman/$(date +%F)
	if [ ! -d "$log_dir" ]; then
		echo "create dir: $log_dir"
		mkdir -p $log_dir
	fi
	for bsl in DSR PQT VPG GPMELD; do
		echo $bsl, $(date +'%R/%m/%d/%Y')
		sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=8 <<EOT
#!/bin/bash -l

#SBATCH --job-name="$bsl-${trimed_name}"
#SBATCH --output=$log_dir/run_${bsl}_${pgn}.out
#SBATCH --constraint=A
#SBATCH --time=48:00:00
#SBATCH --mem=4096MB

hostname

$py3615 -m dso.run $basepath/dso_classic/config/config_regression_${bsl}.json --equation_name $equation_name --noise_type normal --noise_scale 0.0  > $dump_dir/$pgn.${bsl}.out

EOT
	done
done

#done
