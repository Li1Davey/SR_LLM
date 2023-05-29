##!/usr/bin/bash
#nvar=6
#nt=68
#basepath=/home/jiang631/xyx_dso
#datasource=sincosinv_nv${nvar}_nt${nt}
#py3615=/home/jiang631/miniconda3/envs/py3615/bin/python3
#
#
#for metric in inv_nrmse #neg_mse #neg_nmse neg_rmse inv_nrmse
#do
#    for pgn in {10..19};
#    do
#        echo "submit $pgn"
#        dump_dir=$basepath/src/result/$datasource/$(date +%F)
#        if [ ! -d "$dump_dir" ]
#		then
#    		echo "create dir: $dump_dir"
#    		mkdir -p $dump_dir
#		fi
#		for bsl in DSR PQT VPG GPMELD
#		do
#            echo $bsl, $(date +'%R/%m/%d/%Y')
#        	$py3615 -m dso.run $basepath/dso_classic/dataset/$datasource/prog_${pgn}_${bsl}_${metric}.json > $dump_dir/prog_$pgn.data.metric_${metric}.${bsl}.out
#        done
#    done
#done
python3 -m dso.run /home/jiangnan/PycharmProjects/scibench/dso_classic/config/config_regression_GPMELD.json