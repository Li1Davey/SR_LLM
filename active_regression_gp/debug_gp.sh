eqname=Debug_5.in
filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_debug_cvgp/$eqname
python try_gp_xyx.py --equation_name $filename --metric_name neg_nmse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log

python try_gp_xyx.py --equation_name $filename --metric_name neg_nmse --noise_type normal --noise_scale 0.0 > output/$eqname.output.gp.log