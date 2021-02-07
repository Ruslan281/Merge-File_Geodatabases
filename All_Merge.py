# -*- #################

# Created by Ruslan Huseynov


import arcpy

import zipfile

import random

import re

import itertools



Gdb_list = []

GDBS = str(arcpy.GetParameterAsText(0))

for h in GDBS.split(";"):

    Gdb_list.append(h)

default_gdb = str(arcpy.GetParameterAsText(1))
    
arcpy.env.scratchWorkspace = "c:/projects/Scratch/scratch.gdb"

arcpy.env.workspace = default_gdb

default_gdb_features = arcpy.ListFeatureClasses()



for fc in default_gdb_features:

    orijinal_name = fc

    replace_name = fc + "_1"

    data_type = "FeatureClass"

    arcpy.Rename_management(orijinal_name, replace_name, data_type)

    


    
arcpy.env.workspace = default_gdb

default_gdb_features_1 = arcpy.ListFeatureClasses()


for m in Gdb_list:

    arcpy.env.workspace = m

    Gdb_list_features = arcpy.ListFeatureClasses()

    

    arcpy.env.scratchWorkspace = "c:/projects/Scratch/scratch.gdb"

    for i in Gdb_list_features :

        for n in default_gdb_features_1 :

            arcpy.env.workspace = default_gdb

            if i[0:3] == n[0:3] and n[0:3] == i[0:3] :
                

                arcpy.env.workspace = default_gdb

                if arcpy.Exists(i + "_merge"):

                    a = i + "_merge"

                    a+="tam"
                    


                    merge= arcpy.Merge_management("{};{}".format(m + "/" + i,default_gdb + "/" + n),default_gdb + "/" + a)

                    arcpy.Delete_management(default_gdb+"/"+n)

                    default_gdb_features_1 = arcpy.ListFeatureClasses()

                    

                else:

                    merge= arcpy.Merge_management("{};{}".format(m + "/" + i,default_gdb + "/" + n),default_gdb + "/" + i + "_merge")


                    arcpy.Delete_management(default_gdb+"/"+n)

                    default_gdb_features_1 = arcpy.ListFeatureClasses()

                    del merge





arcpy.env.workspace = default_gdb

all_new_features_list = arcpy.ListFeatureClasses()


for new_features in all_new_features_list:

    orijinal_name = new_features

    replace_name = orijinal_name.replace("_merge","")

    data_type = "FeatureClass"

    arcpy.Rename_management(orijinal_name, replace_name, data_type)



















            


