#!/bin/bash -l
nvar=6
nt=66
basepath=/depot/yexiang/apps/jiang631/data/xyx_dso/src
datasource=synthetic_nv${nvar}_nt${nt}
metric=neg_nmse
for pgn in {0..10};
do
    prog=prog_$pgn.data
    echo "submit $prog"
    sbatch -A yexiang --nodes=1 --ntasks=1 --cpus-per-task=1 <<EOT
#!/bin/bash -l

#SBATCH --job-name="$nvar-$pgn-$metric"
#SBATCH --output=./log/log_run_gp_${pgn}_nv${nvar}_metric_${metric}.out
#SBATCH --constraint=A
#SBATCH --time=10:00:00
#SBATCH --mem=4096

hostname

module load anaconda


python3 $basepath/ctrl_var_gp_nan/try_gp_xyx.py $nvar $basepath/data/$datasource/$prog $basepath/result/$datasource/$prog.gp $metric > $basepath/result/$datasource/$prog.metric_${metric}.gp.out

python3 $basepath/ctrl_var_gp_nan/try_gp_xyx.py $nvar $basepath/data/$datasource/$prog $basepath/result/$datasource/$prog.egp $metric --expand_gp > $basepath/result/$datasource/$prog.metric_${metric}.egp.out

EOT

done
