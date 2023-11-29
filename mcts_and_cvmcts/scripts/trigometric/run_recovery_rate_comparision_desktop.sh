#!/usr/bin/zsh
set -x

basepath=/home/jiangnan/PycharmProjects/scibench
py3=/home/jiangnan/miniconda3/bin/python
nv=$1
nt=$2

thispath=$basepath/mcts_and_cvmcts
data_path=$basepath/data/unencrypted/equations_trigometric
opt=L-BFGS-B

noise_type=normal
noise_scale=0.0
metric_name=neg_mse
for type in inv sincos sincosinv; do
	for prog in {0..9}; do
		eq_name=${type}_nv${nv}_nt${nt}_prog_${prog}.in
		echo "submit $eq_name"
		dump_dir=$basepath/result/${type}_nv${nv}_nt${nt}/$(date +%F)
		if [ ! -d "$dump_dir" ]; then
			echo "create dir: $dump_dir"
			mkdir -p $dump_dir
		fi
		log_dir=$basepath/log/$(date +%F)
		if [ ! -d "$log_dir" ]; then
			echo "create dir: $log_dir"
			mkdir -p $log_dir
		fi
		echo "$dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.opt$opt.out"
		timeout 12h $py3 $thispath/main.py --equation_name $data_path/$eq_name --optimizer $opt --cv_mcts --metric_name 'neg_mse' \
			--noise_type $noise_type --noise_scale $noise_scale >$dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.opt$opt.cv_mcts.out
	done
done

for type in inv sincos sincosinv; do
	for prog in {0..9}; do
		eq_name=${type}_nv${nv}_nt${nt}_prog_${prog}.in
		echo "submit $eq_name"
		dump_dir=$basepath/result/${type}_nv${nv}_nt${nt}/$(date +%F)
		if [ ! -d "$dump_dir" ]; then
			echo "create dir: $dump_dir"
			mkdir -p $dump_dir
		fi
		log_dir=$basepath/log/$(date +%F)
		if [ ! -d "$log_dir" ]; then
			echo "create dir: $log_dir"
			mkdir -p $log_dir
		fi
		echo "$dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.opt$opt.out"
		timeout 12h $py3 $thispath/main.py --equation_name $data_path/$eq_name --optimizer $opt --metric_name 'neg_mse' \
			--noise_type $noise_type --noise_scale $noise_scale >$dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.opt$opt.mcts.out
	done
done
