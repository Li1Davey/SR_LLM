#!/usr/bin/zsh
set -x
basepath=/home/jiangnan/PycharmProjects/scibench/eureqa
nvar=$1
nt=$2
operators=$3
datasource=${operators}_nv${nvar}_nt${nt}




dump_dir=$basepath/result/$datasource/$(date +%F)
if [ ! -d "$dump_dir" ]; then
	echo "create dir: $dump_dir"
	mkdir -p $dump_dir
fi
python3 $basepath/run_eureqa.py $dump_dir \
	--config_path $basepath/config_${operators}.json \
	--credential_path $basepath/credentials.json \
    --mc 1 \
	--num_workers 10 \
	--seed_shift 42 \
	--dataset_path $basepath/data/equations_trigometric/${datasource}_ \
	--nvars $nvar

