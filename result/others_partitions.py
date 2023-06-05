from numpy import nan, inf
from parse_results import pretty_print_dso_family

constants = []



output="""neg_nmse GP, EGP
Livermore2_Vars4_6, -1.0002179528287147, 
Livermore2_Vars5_23, -1.045123145327849, -1.0136586025024095
Livermore2_Vars2_6, -0.00012780178505830285, 
Livermore2_Vars7_19, -1.0050928778681876, -1.0022255472302046
GrammarVAE_1, -0.07036424407037153, -0.08469506539551627
Livermore2_Vars7_15, -0.8633456872489578, -1.113303451893163
Livermore2_Vars4_13, -0.027151744508958246, -0.03421994991860975
Livermore2_Vars4_18, nan, nan
Livermore2_Vars4_11, -0.03613393708516457, 
Const_Test_2, -7.095935143156387e-18, -1.6211293767015902e-19
Livermore2_Vars2_20, -1.032986958427975, -1.0252162239659657
Livermore2_Vars5_7, nan, nan
Livermore2_Vars3_19, nan, nan
Livermore2_Vars3_20, -1.351369587405768e-17, 
Livermore2_Vars2_23, nan, nan
Keijzer_12, nan, 
Keijzer_10, -0.0, nan
Livermore2_Vars5_20, -1.0216654939311525, -1.0190013390863781
Livermore2_Vars7_13, nan, nan
Livermore2_Vars4_16, nan, nan
Livermore2_Vars3_2, -1.201522178912673, -0.3236371725190351
Livermore2_Vars6_4, -1.0352879804851405, -1.0319955540431862
Livermore2_Vars5_6, -0.0018805717651952758, 
Livermore2_Vars6_23, nan, 
Livermore2_Vars7_14, -1.2036875759226595, 
Livermore2_Vars4_9, -0.046971784501411304, 
Livermore2_Vars7_12, -0.027460211127382266, 
Livermore2_Vars3_18, -7.930415304463607e-18, -1.8494079368859673e-19
Livermore2_Vars5_9, -0.8679604105392398, 
Livermore2_Vars2_14, -1.0130353632409288, -1.016944947372845
Livermore2_Vars7_16, -0.07050713538103791, 
Livermore2_Vars5_16, -1.0491645767181172, -0.9357006263671154
Livermore2_Vars5_17, -0.10903765976092981, -0.11366865353102122
Livermore2_Vars2_8, nan, 
Livermore2_Vars7_2, nan, nan
Livermore2_Vars7_11, -0.9798940157824313, 
Livermore2_Vars4_15, -0.007848448972654418, 
Livermore2_Vars3_12, -1.1257898938578372, -2.29382277641647e-23
Livermore2_Vars2_25, -4.3262154879103236e-05, 
Livermore2_Vars3_15, -0.15883067355559963, 
Livermore2_Vars6_14, -0.046512350189286025, -0.049791680988905594
Keijzer_8, -0.0, -0.0
Livermore2_Vars2_4, -8.679929833584828e-12, -9.984302729812245e-18
Livermore2_Vars7_17, nan, nan
Livermore2_Vars2_16, nan, nan
Livermore2_Vars6_1, nan, nan
Livermore2_Vars5_8, nan, nan
Livermore2_Vars5_13, nan, nan
Livermore2_Vars4_10, nan, nan
Livermore2_Vars6_21, -0.08871859786431562, 
Livermore2_Vars6_12, -1.0089345393921623, -1.000327104818424
Livermore2_Vars5_22, nan, nan
Livermore2_Vars4_14, -0.07431133207403275, -0.06127155808318271
Livermore2_Vars7_25, -0.48985161666316285, 
Livermore2_Vars6_25, nan, nan
Livermore2_Vars4_23, -0.0634044969838909, 
Livermore2_Vars7_1, -1.0239632312373386, -0.04009088401017743
Koza_3, -6.242987200794048e-08, -0.06774574582302428
Livermore2_Vars2_9, nan, nan
Livermore2_Vars7_20, -0.0, -0.0
Livermore2_Vars6_13, -0.053948698780420724, 
Livermore2_Vars5_4, -3.0500360596570352e-33, 
Livermore2_Vars7_22, nan, nan
Livermore2_Vars4_7, -0.023654631104242207, -0.03294864314580983
Livermore2_Vars5_3, -1.113673062153093, 
Livermore2_Vars7_3, -0.028139489467413417, 
Livermore2_Vars3_24, -3.5912283450480146e-20, -8.647706910716505e-19
Livermore2_Vars5_19, -1.0448421798775236, 
Livermore2_Vars6_17, -1.0099277415968895, -1.0001823564845005
Livermore2_Vars5_15, -0.21471099866670812, 
Livermore2_Vars3_16, -1.0046419635380888, -1.0031376897139008
Livermore2_Vars3_8, nan, nan
Livermore2_Vars3_9, nan, 
Livermore2_Vars6_9, -1.0000192768917202, -1.0000502426468758
Livermore2_Vars6_18, -0.15247304431048347, 
Livermore2_Vars6_24, nan, nan
Livermore2_Vars7_23, -0.08019365013040851, 
Livermore2_Vars7_7, -1.0040231960656254, 
Livermore2_Vars3_7, -0.0023628402128239023, 
Livermore2_Vars7_5, -1.005904197002149, -1.0000964994912884
Keijzer_6, nan, -6.318386530151738e-33
Livermore2_Vars6_6, -1.0151517229138414, -1.021541978200424
Livermore2_Vars2_13, -1.0486028644503431, -0.9478108777041089
Livermore2_Vars3_4, nan, nan
Livermore2_Vars5_12, -0.25116525805012646, -0.03270921977638149
Livermore2_Vars6_11, -0.0013082487915185444, -0.0011713328982481217
Livermore2_Vars3_6, -0.9798163669323653, -1.0049115910284805
Livermore2_Vars3_3, -0.003278440717187432, -0.016526616582590636
Livermore2_Vars5_21, -0.39876626990840053, -0.15735392358295275
Livermore2_Vars6_22, -0.3047513889526416, -0.420158298304414
Livermore2_Vars4_12, -2.955056319556623e-17, -7.806466556098812e-20
Livermore2_Vars2_17, -0.38433982949936735, 
Livermore2_Vars2_7, nan, nan
Keijzer_3, -1.0013554373346296, -1.0018177591304493
Livermore2_Vars2_12, nan, nan
Livermore2_Vars7_10, -0.03847893612576553, 
Livermore2_Vars6_19, nan, nan
Livermore2_Vars5_24, nan, nan
Livermore2_Vars2_15, -9.544014709078632e-22, -0.022347662290038317
Livermore2_Vars4_25, -1.0026149938300561, -0.05172827751126018
Livermore2_Vars3_13, nan, nan
Livermore2_Vars6_7, nan, nan
Livermore2_Vars6_20, -1.0547217586885957, nan
Const_Test_1, -1.4476587294479624e-19, -3.1650844861381538e-21
Livermore2_Vars3_21, nan, nan
Keijzer_7, -0.0, -0.0
Keijzer_2, -1.0803181160317783, -0.622603617732847
Livermore2_Vars6_15, -0.0059126777910570565, -0.006005737910914842
Livermore2_Vars5_10, -1.0127139339731643, -1.0003190665603297
Livermore2_Vars5_11, nan, nan
Livermore2_Vars2_2, nan, nan
Livermore2_Vars4_8, -0.003026552423962214, 
Livermore2_Vars2_24, nan, 
Livermore2_Vars2_10, nan, nan
Koza_2, -0.17312539263817095, nan
Livermore2_Vars5_1, -6.030831427043136e-18, -5.1740356234448425e-18
Livermore2_Vars2_22, -1.0000435580213658, -0.8628533969729545
Livermore2_Vars3_5, -1.0107488312986876, -1.0065978520796661
Livermore2_Vars6_3, nan, nan
Livermore2_Vars6_5, -0.9743226826477123, -0.08923758343110388
Livermore2_Vars5_14, -1.1617294796274786, -0.00028873054490197837
Livermore2_Vars5_18, -0.06435049173102471, -0.5951926242557933
Livermore2_Vars3_10, -1.3934487929906514, 
Livermore2_Vars7_9, nan, nan
Livermore2_Vars2_19, nan, nan
Livermore2_Vars5_5, nan, nan
Livermore2_Vars3_14, -1.058061370208803, -1.0535531244643705
Livermore2_Vars4_3, -1.9686196365730247e-18, -1.2452450032023542e-18
Livermore2_Vars4_19, -1.0582091212614995, 
Livermore2_Vars4_4, nan, 
Livermore2_Vars7_24, nan, nan
Keijzer_1, -1.001979808229091, -1.0000373681496535
Keijzer_5, -1.0642366248693467, nan
Livermore2_Vars7_18, -0.04290540349155146, 
Livermore2_Vars3_22, -0.07526253476107458, 
Livermore2_Vars4_2, -0.9894421522472426, -1.0125960159602545
Livermore2_Vars3_1, -1.0096514877496816, nan"""

def one_partiton(keyword):
    print("\n" + keyword)
    for line in output.split("\n"):
        spl = line.split("\t")
        if len(line) <= 1:
            print(line + '\n')
        elif spl[0] in ['neg_nmse', 'neg_nrmse', 'inv_nrmse', 'inv_nmse', 'neg_mse', 'neg_rmse', 'neglog_mse', 'inv_mse']:
            print(line)
        elif keyword in spl[0]:
            print(line)
    print('-' * 30)


# one_partiton("Livermore2_")
# one_partiton("Neat_")
# one_partiton("Nguyen_")
one_partiton("Korns_")
# one_partiton("Constant_")
# one_partiton("Jin_")
