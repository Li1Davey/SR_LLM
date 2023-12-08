#!/usr/bin/zsh
set -x
basepath=/home/jiangnan/PycharmProjects/scibench/eureqa
nvar=$1
operators=Feynman
datasource=${operators}_Vars${nvar}




dump_dir=$basepath/result/$datasource/$(date +%F)
if [ ! -d "$dump_dir" ]; then
	echo "create dir: $dump_dir"
	mkdir -p $dump_dir
fi
python3 $basepath/run_feynman_eureqa.py $dump_dir \
	--config_path $basepath/configs/config_${operators}.json \
	--credential_path $basepath/credentials_dec8.json \
    --mc 1 \
	--num_workers 2 \
	--seed_shift 42 \
	--dataset_path $basepath/data/equations_feynman/ \
	--nvars $nvar

