#eqname=Debug_9.in
#set -x
#eqname=Debug_9.in
#filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_debug_cvgp/Debug_9.in
#python try_gp_xyx.py --equation_name $filename --metric_name neg_mse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log
#echo '8'
#eqname=Debug_8.in
#filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_debug_cvgp/$eqname
#python try_gp_xyx.py --equation_name $filename --metric_name neg_mse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log
#
#echo 7
#eqname=Debug_7.in
#filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_debug_cvgp/$eqname
#python try_gp_xyx.py --equation_name $filename --metric_name neg_mse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log
#


#echo 7
#eqname=inv_nv3_nt22_prog_1.in
#filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_trigometric/$eqname
#python try_gp_xyx.py --equation_name $filename --metric_name neg_mse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log



#eqname=FeynmanIIICh13Eq18.in
#filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_feynman/$eqname
#python try_gp_xyx.py --equation_name $filename --metric_name neg_mse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log

eqname=FeynmanICh16Eq6.in
filename=/home/jiangnan/PycharmProjects/scibench/data/unencrypted/equations_feynman/$eqname
python try_gp_xyx.py --equation_name $filename --metric_name neg_mse --noise_type normal --noise_scale 0.0 --expand_gp > output/$eqname.egp.log
