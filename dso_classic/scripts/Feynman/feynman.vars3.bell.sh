#!/usr/bin/zsh
#basepath=/home/jiangnan/PycharmProjects/scibench
basepath=/depot/yexiang/apps/jiang631/data/scibench
#py3615=/home/jiangnan/anaconda3/envs/py3615/bin/python3
py3615=/home/jiang631/workspace/miniconda3/envs/py3615/bin/python3

for pgn in FeynmanICh6Eq20b.in FeynmanICh12Eq2.in FeynmanICh15Eq3t.in FeynmanICh15Eq3x.in FeynmanBonus20.in FeynmanICh18Eq12.in FeynmanICh27Eq6.in FeynmanICh30Eq3.in FeynmanICh30Eq5.in FeynmanICh37Eq4.in FeynmanICh39Eq11.in FeynmanICh39Eq22.in FeynmanICh43Eq43.in FeynmanICh47Eq23.in FeynmanIICh6Eq11.in FeynmanIICh6Eq15b.in FeynmanIICh11Eq27.in FeynmanIICh15Eq4.in FeynmanIICh15Eq5.in FeynmanIICh21Eq32.in FeynmanIICh34Eq2a.in FeynmanIICh34Eq2.in FeynmanIICh34Eq29b.in FeynmanIICh37Eq1.in FeynmanIIICh13Eq18.in FeynmanIIICh15Eq12.in FeynmanIIICh15Eq27.in FeynmanIIICh17Eq37.in FeynmanIIICh19Eq51.in FeynmanBonus5.in FeynmanBonus7.in FeynmanBonus9.in FeynmanBonus15.in FeynmanBonus18.in; do
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
