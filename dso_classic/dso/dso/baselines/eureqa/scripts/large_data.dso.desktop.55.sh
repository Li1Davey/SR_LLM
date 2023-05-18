#!/usr/bin/zsh
set -x
basepath=/home/jiang631/data/xyx_dso
nvar=$1
nt=$2
operators=$3
datasource=${operators}_nv${nvar}_nt${nt}


codepath=$basepath/dso_classic/dso/dso/baselines/eureqa

dump_dir=$basepath/result/$datasource/$(date +%F)
if [ ! -d "$dump_dir" ]; then
	echo "create dir: $dump_dir"
	mkdir -p $dump_dir
fi
python3 $codepath/run_eureqa.py $dump_dir \
	--config_path $codepath/config_${operators}.json \
	--credential_path $codepath/credentials.json \
    --mc 1 \
	--num_workers 10 \
	--seed_shift 42 \
	--dataset_path $basepath/dso_classic/dataset/$datasource \
	--nvars $nvar 
