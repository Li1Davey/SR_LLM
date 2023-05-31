#!/bin/bash -l

basepath=/depot/yexiang/apps/jiang631/data/xyx_dso

thispath=$basepath/src/ctrl_var_gp_nan

nvar=6
nt=68

#datasource=inv_nv${nvar}_nt${nt}
#datasource=sincos_nv${nvar}_nt${nt}
datasource=inv_nv${nvar}_nt${nt}

for metric in neg_mse  
do
    noise_std=0.1
	for pgn in {0..9};
	do
    	prog=prog_$pgn.data
    	echo "submit $prog"
    	dump_dir=$basepath/result/noisy${noise_std}_$datasource/$(date +%F)
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

#SBATCH --job-name="gp$pgn-$nvar${nt}-InvNoise"
#SBATCH --output=$log_dir/run_gp_${datasource}_${pgn}_nv${nvar}_metric_${metric}.out
#SBATCH --constraint=A
#SBATCH --time=48:00:00
#SBATCH --mem=2048MB

hostname

module load anaconda


python3 $thispath/try_gp_xyx.py $nvar \
        		$basepath/data/$datasource/$prog $metric --noise_std ${noise_std} \
        		 > $dump_dir/$prog.metric_${metric}.gp.out

EOT

sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="egp$pgn-$nvar${nt}-InvNoise"
#SBATCH --output=$log_dir/run_egp_${datasource}__${pgn}_nv${nvar}_metric_${metric}.out
#SBATCH --constraint=A
#SBATCH --time=48:00:00
#SBATCH --mem=3072MB

hostname

module load anaconda

python3 $thispath/try_gp_xyx.py $nvar \
		        $basepath/data/$datasource/$prog $metric --expand_gp --noise_std ${noise_std} \
		        > $dump_dir/$prog.metric_${metric}.egp.out

EOT

	done
done

