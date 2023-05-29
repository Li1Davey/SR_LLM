#!/usr/bin/zsh
nvar=5
nt=55
basepath=/home/jiang631/xyx_dso
datasource=synthetic_nv${nvar}_nt${nt}
for metric in neg_mse neg_nmse #inv_mse #neg_rmse neg_nmse inv_nrmse inv_nmse inv_nrmse
do
    for pgn in {33..50};
    do
        prog=prog_$pgn.data
        echo "submit $prog"
        dump_dir=$basepath/src/result/$datasource/$(date +%F)
        if [ ! -d "$dump_dir" ]
		then
    		echo "create dir: $dump_dir"
    		mkdir -p $dump_dir
		fi
#		python3 $basepath/src/ctrl_var_gp/try_gp_xyx.py $nvar $basepath/src/data/$datasource/$prog --expand_gp > $dump_dir/$prog.metric_xyx${metric}.egp.out &
        python3 $basepath/src/ctrl_var_gp_nan/try_gp_xyx.py $nvar \
        		$basepath/src/data/$datasource/$prog $metric \
        		 > $dump_dir/$prog.metric_${metric}.gp.out
		python3 $basepath/src/ctrl_var_gp_nan/try_gp_xyx.py $nvar \
		        $basepath/src/data/$datasource/$prog $metric --expand_gp \
		        > $dump_dir/$prog.metric_${metric}.egp.out &
    done
done
