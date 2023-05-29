#!/bin/bash -l
nvar=5
nt=55
basepath=/depot/yexiang/apps/jiang631/data/xyx_dso
datasource=synthetic_nv${nvar}_nt${nt}
for metric in neg_mse neg_nmse #inv_mse #neg_rmse neg_nmse inv_nrmse inv_nmse inv_nrmse
do
	for pgn in {0..49};
	do
    	prog=prog_$pgn.data
    	echo "submit $prog"
    	dump_dir=$basepath/src/result/$datasource/$(date +%F)
        if [ ! -d "$dump_dir" ]
		then
    		echo "create dir: $dump_dir"
    		mkdir -p $dump_dir
		fi
		log_dir=log/$(date +%F)
		if [ ! -d "$log_dir" ]
		then
    		echo "create dir: $log_dir"
    		mkdir -p $log_dir
		fi
    sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="gp-$nvar-$pgn-$metric"
#SBATCH --output=$log_dir/run_gp_${pgn}_nv${nvar}_metric_${metric}.out
#SBATCH --constraint=A
#SBATCH --time=48:00:00
#SBATCH --mem=2048MB

hostname

module load anaconda


python3 $basepath/src/ctrl_var_gp_nan/try_gp_xyx.py $nvar \
        		$basepath/src/data/$datasource/$prog $metric \
        		 > $dump_dir/$prog.metric_${metric}.gp.out

EOT

sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="egp-$nvar-$pgn-$metric"
#SBATCH --output=$log_dir/run_egp_${pgn}_nv${nvar}_metric_${metric}.out
#SBATCH --constraint=A
#SBATCH --time=48:00:00
#SBATCH --mem=3072MB

hostname

module load anaconda
python3 $basepath/src/ctrl_var_gp_nan/try_gp_xyx.py $nvar \
		        $basepath/src/data/$datasource/$prog $metric --expand_gp \
		        > $dump_dir/$prog.metric_${metric}.egp.out

EOT

	done
done


