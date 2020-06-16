#!/usr/bin/env python3
#
#requires patched  gdspy in particular,  xemacs /usr/local/lib/python3.8/dist-packages/gdspy/library.py
#needed changing to allow a hash called 

import gdspy

gds = gdspy.GdsLibrary()  

  


layer_datatype_hash_lookup={}
layer_datatype_hash_lookup[64,20]=(2,0)  #NWELL 64 20		-> (nw)	2
layer_datatype_hash_lookup[65,20]=(3,0)  #DIFF  65 20		-> (od)	3
layer_datatype_hash_lookup[66,20]=(13,0) #POLY  66 20		-> (poly)	13
layer_datatype_hash_lookup[66,44]=(15,0) #CONT  66 44		-> (ct)	15
layer_datatype_hash_lookup[67,20]=(16,0) #LI    67 20		-> (m1)	16
layer_datatype_hash_lookup[67,44]=(17,0) #MCON  67 44		-> (v12)	17
layer_datatype_hash_lookup[68,20]=(18,0) #MET1  68 20		-> (m2)	18
layer_datatype_hash_lookup[68,44]=(27,0) #VIA1  68 44		-> (v23)	27
layer_datatype_hash_lookup[69,20]=(28,0) #MET2  69 20		-> (m3)	28
layer_datatype_hash_lookup[69,44]=(29,0) #VIA2  69 44		-> (v34)	29
layer_datatype_hash_lookup[70,20]=(31,0) #MET3  70 20		-> (m4)	31
layer_datatype_hash_lookup[70,44]=(32,0) #VIA3  70 44		-> (v45)	32
layer_datatype_hash_lookup[71,20]=(33,0) #MET4  71 20		-> (m5)	33
layer_datatype_hash_lookup[71,44]=(39,0) #VIA4  71 44		-> (v56)	39
layer_datatype_hash_lookup[72,20]=(38,0) #MET5  72 20		-> (m6)	38
layer_datatype_hash_lookup[76,20]=(19,0) #GLASS 76 20		-> (pad)	19



gdsfile = gds.read_gds("sky.gds", layers_and_datatypes_to_swap_out=layer_datatype_hash_lookup)

gdsfile.write_gds("la.gds")
