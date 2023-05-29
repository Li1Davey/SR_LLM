#!/usr/bin/zsh
#basepath=/home/jiangnan/PycharmProjects/scibench
basepath=/depot/yexiang/apps/jiang631/data/scibench
py3615=/home/jiangnan/anaconda3/envs/py3615/bin/python3

for pgn in FeynmanBonus10.in FeynmanBonus1.in FeynmanICh10Eq7.in FeynmanICh14Eq4.in FeynmanICh26Eq2.in FeynmanICh34Eq27.in FeynmanICh43Eq31.in FeynmanICh9Eq18.in FeynmanIICh15Eq4.in FeynmanIICh34Eq2a.in FeynmanIICh6Eq11.in FeynmanIIICh15Eq14.in FeynmanBonus11.in FeynmanBonus20.in FeynmanICh11Eq19.in FeynmanICh15Eq10.in FeynmanICh27Eq6.in FeynmanICh34Eq8.in FeynmanICh43Eq43.in FeynmanIICh10Eq9.in FeynmanIICh15Eq5.in FeynmanIICh34Eq2.in FeynmanIICh6Eq15a.in FeynmanIIICh15Eq27.in FeynmanBonus12.in FeynmanBonus2.in FeynmanICh12Eq11.in FeynmanICh15Eq3t.in FeynmanICh29Eq16.in FeynmanICh37Eq4.in FeynmanICh44Eq4.in FeynmanIICh11Eq17.in FeynmanIICh21Eq32.in FeynmanIICh35Eq18.in FeynmanIICh6Eq15b.in FeynmanIIICh17Eq37.in FeynmanBonus13.in FeynmanBonus3.in FeynmanICh12Eq1.in FeynmanICh15Eq3x.in FeynmanICh29Eq4.in FeynmanICh38Eq12.in FeynmanICh47Eq23.in FeynmanIICh11Eq20.in FeynmanIICh24Eq17.in FeynmanIICh35Eq21.in FeynmanIICh8Eq31.in FeynmanIIICh19Eq51.in FeynmanBonus14.in FeynmanBonus4.in FeynmanICh12Eq2.in FeynmanICh16Eq6.in FeynmanICh30Eq3.in FeynmanICh39Eq10.in FeynmanICh48Eq2.in FeynmanIICh11Eq27.in FeynmanIICh27Eq16.in FeynmanIICh36Eq38.in FeynmanIICh8Eq7.in FeynmanIIICh21Eq20.in FeynmanBonus15.in FeynmanBonus5.in FeynmanICh12Eq4.in FeynmanICh18Eq12.in FeynmanICh30Eq5.in FeynmanICh39Eq11.in FeynmanICh50Eq26.in FeynmanIICh11Eq28.in FeynmanIICh27Eq18.in FeynmanIICh37Eq1.in FeynmanIIICh10Eq19.in FeynmanIIICh4Eq32.in FeynmanBonus16.in FeynmanBonus6.in FeynmanICh12Eq5.in FeynmanICh18Eq16.in FeynmanICh32Eq17.in FeynmanICh39Eq22.in FeynmanICh6Eq20a.in FeynmanIICh11Eq3.in FeynmanIICh2Eq42.in FeynmanIICh38Eq14.in FeynmanIIICh12Eq43.in FeynmanIIICh4Eq33.in FeynmanBonus17.in FeynmanBonus7.in FeynmanICh13Eq12.in FeynmanICh18Eq4.in FeynmanICh32Eq5.in FeynmanICh40Eq1.in FeynmanICh6Eq20b.in FeynmanIICh13Eq17.in FeynmanIICh34Eq11.in FeynmanIICh38Eq3.in FeynmanIIICh13Eq18.in FeynmanIIICh7Eq38.in FeynmanBonus18.in FeynmanBonus8.in FeynmanICh13Eq4.in FeynmanICh24Eq6.in FeynmanICh34Eq10.in FeynmanICh41Eq16.in FeynmanICh6Eq20.in FeynmanIICh13Eq23.in FeynmanIICh34Eq29a.in FeynmanIICh3Eq24.in FeynmanIIICh14Eq14.in FeynmanIIICh8Eq54.in FeynmanBonus19.in FeynmanBonus9.in FeynmanICh14Eq3.in FeynmanICh25Eq13.in FeynmanICh34Eq14.in FeynmanICh43Eq16.in FeynmanICh8Eq14.in FeynmanIICh13Eq34.in FeynmanIICh34Eq29b.in FeynmanIICh4Eq23.in FeynmanIIICh15Eq12.in FeynmanIIICh9Eq52.in; do
	echo "submit $pgn"
	equation_name=$basepath/scibench/data/unencrypted/equations_feynman/$pgn
	dump_dir=$basepath/result/Feynman/$(date +%F)
	if [ ! -d "$dump_dir" ]; then
		echo "create output dir: $dump_dir"
		mkdir -p $dump_dir
	fi
	log_dir=$basepath/log/$(date +%F)
	if [ ! -d "$log_dir" ]; then
		echo "create dir: $log_dir"
		mkdir -p $log_dir
	fi
	for bsl in DSR PQT VPG GPMELD; do
		echo $bsl, $(date +'%R/%m/%d/%Y')
		sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=8 <<EOT
#!/bin/bash -l

#SBATCH --job-name="$bsl-${pgn}"
#SBATCH --output=$log_dir/run_${bsl}_${pgn}.out
#SBATCH --constraint=A
#SBATCH --time=48:00:00
#SBATCH --mem=4096MB

hostname

$py3615 -m dso.run $basepath/dso_classic/config/config_regression_${bsl}.json --equation_name equation_name --noise_type normal --noise_scale 0.0  > $dump_dir/$pgn.${bsl}.out

EOT

	done
done

#done
