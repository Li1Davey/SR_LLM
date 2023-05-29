#!/bin/bash -l
nvar=3
nt=33
basepath=/depot/yexiang/apps/jiang631/data/xyx_dso/src
datasource=synthetic_nv${nvar}_nt${nt}

for pgn in {18..18};
do
    prog=prog_$pgn.data
    echo "submit $prog"
    sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="nv$nvar-pg$pgn-xyxneg_mse"
#SBATCH --output=log/run_gp_${pgn}_nv${nvar}_metric_xyxneg_mse.out
#SBATCH --constraint=A
#SBATCH --time=10:00:00
#SBATCH --mem=4096

hostname

module load anaconda

python3 $basepath/ctrl_var_gp/try_gp_xyx.py $nvar $basepath/data/$datasource/$prog --expand_gp > $basepath/result/$datasource/$prog.metric_xyxneg_mse.egp.out
EOT
    for metric in neg_mse #neg_nmse neg_rmse inv_mse inv_nmse inv_rmse
    do
        echo "$metric"
        sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="nv$nvar-pg$pgn-$metric"
#SBATCH --output=log/run_gp_${pgn}_nv${nvar}_metric_${metric}.out
#SBATCH --constraint=A
#SBATCH --time=10:00:00
#SBATCH --mem=4096

hostname

module load anaconda

python3 $basepath/ctrl_var_gp_nan/try_gp_xyx.py $nvar $basepath/data/$datasource/$prog $metric > $basepath/result/$datasource/$prog.metric_${metric}.gp.out
python3 $basepath/ctrl_var_gp_nan/try_gp_xyx.py $nvar $basepath/data/$datasource/$prog $metric --expand_gp > $basepath/result/$datasource/$prog.metric_${metric}.egp.out
EOT

    done
done
