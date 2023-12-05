#!/bin/bash -l

basepath=/depot/yexiang/apps/jiang631/data/scibench
type=Livermore2
nv=$1

thispath=$basepath/gp_and_cvgp
data_path=$basepath/data/unencrypted/equations_livermore2
py3615=/home/jiang631/workspace/miniconda3/envs/py310/bin/python3

noise_type=normal
noise_scale=0.0
metric_name=neg_nmse
for prog in {1..25};
do
    eq_name=${type}_Vars${nv}_$prog.in
    echo "submit $eq_name"
   	dump_dir=$basepath/result/${type}_Vars${nv}/$(date +%F)
    if [ ! -d "$dump_dir" ]
    then
    	echo "create dir: $dump_dir"
    	mkdir -p $dump_dir
	fi
	log_dir=$basepath/log/$(date +%F)
	if [ ! -d "$log_dir" ]
	then
    	echo "create dir: $log_dir"
    	mkdir -p $log_dir
	fi
    sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="gp_Vars${nv}_$prog"
#SBATCH --output=$log_dir/${eq_name}.metric_${metric_name}.noise_${noise_type}_${noise_scale}.gp.out
#SBATCH --constraint=A
#SBATCH --time=12:00:00
#SBATCH --mem=4GB

$py3 $thispath/main.py --equation_name $data_path/$eq_name \
        		--metric_name $metric_name --noise_type $noise_type --noise_scale $noise_scale \
        		 > $dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}_${noise_scale}.gp.out

EOT

	sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="cvgp_Vars${nv}_$prog"
#SBATCH --output=$log_dir/${eq_name}.metric_${metric_name}.noise_${noise_type}_${noise_scale}.cvgp.out
#SBATCH --constraint=A
#SBATCH --time=12:00:00
#SBATCH --mem=4GB

hostname



$py3 $thispath/main.py --equation_name $data_path/$eq_name --cvgp \
        		--metric_name $metric_name --noise_type $noise_type --noise_scale $noise_scale \
        		 > $dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.cvgp.out

EOT

done

