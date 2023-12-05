#!/usr/bin/zsh
basepath=/home/jiangnan/PycharmProjects/scibench
py37=/home/jiangnan/anaconda3/envs/py37/bin/python3.7
type=Livermore2
nv=$1
bsl=$2
thispath=$basepath/dso_classic
datapath=$basepath/data/unencrypted/equations_livermore2
opt=L-BFGS-B

noise_type=normal
noise_scale=0.0
#metric_name=neg_nmse
for prog in {1..25}; do
	eq_name=${type}_Vars${nv}_$prog.in
	echo "submit $eq_name"

	dump_dir=$basepath/result/${type}_nv${nv}_nt${nt}/$(date +%F)
	if [ ! -d "$dump_dir" ]; then
		echo "create output dir: $dump_dir"
		mkdir -p $dump_dir
	fi
	log_dir=$basepath/log/$(date +%F)
	if [ ! -d "$log_dir" ]; then
		echo "create dir: $log_dir"
		mkdir -p $log_dir
	fi
	#	for bsl in DSR PQT VPG GPMELD; do
	echo $basepath/dso_classic/config/config_regression_${bsl}.json
	echo $datapath/$eq_name
	echo $dump_dir/${eq_name}.noise_${noise_type}${noise_scale}.opt${opt}.${bsl}
	timeout 12h $py37 $thispath/run.py $basepath/dso_classic/config/config_regression_${bsl}.json --equation_name $datapath/$eq_name \
		--logdir $dump_dir/${eq_name}.noise_${noise_type}${noise_scale}.opt${opt}.${bsl} \
		--noise_type $noise_type --noise_scale $noise_scale >$dump_dir/prog_${prog}.noise_${noise_type}${noise_scale}.opt$opt.${bsl}.out
	#	done
done
