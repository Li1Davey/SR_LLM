#!/usr/bin/zsh
basepath=/home/$USER/PycharmProjects/scibench
py37=/home/$USER/anaconda3/envs/py37/bin/python3.7

type=$1
nv=$1
thispath=$basepath/dso_classic
datapath=$basepath/data/unencrypted/equations_livermore2


noise_type=normal
noise_scale=0.0
type=$1
nv=$2
nt=$3

thispath=$basepath/dso_classic
datapath=$basepath/data/unencrypted/equations_trigonometric
noise_type=normal
noise_scale=0.0

for prog in {0..9}; do
	eq_name=${type}_nv${nv}_nt${nt}_prog_${prog}.in
	echo "submit $eq_name"

	dump_dir=$basepath/result/${type}_nv${nv}_nt${nt}/$(date +%F)
	if [ ! -d "$dump_dir" ]; then
		echo "create output dir: $dump_dir"
		mkdir -p $dump_dir
	fi
	for bsl in DSR PQT VPG; do
		echo "The model configuration file:" $basepath/dso_classic/config/config_regression_${bsl}.json
		echo "The expression:" $datapath/$eq_name
		echo "The output folder:" $dump_dir/${eq_name}.noise_${noise_type}${noise_scale}.${bsl}
		timeout 12h $py37 $thispath/run.py $basepath/dso_classic/config/config_regression_${bsl}.json --equation_name $datapath/$eq_name \
			--logdir $dump_dir/${eq_name}.noise_${noise_type}${noise_scale}.${bsl} \
			--noise_type $noise_type --noise_scale $noise_scale >$dump_dir/prog_${prog}.noise_${noise_type}${noise_scale}.${bsl}.out
	done
done
