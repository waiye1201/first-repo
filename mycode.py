import arcpy
from arcpy import env

import my_function_module

env.workspace = r"(C:\Users\yxiao081\Downloads\Lecture7_Data\Module7_Data\OTTAWA.gdb\OTTAWADATA)"
featureclass_list=arcpy.ListFeatureClasses()
for fc in featureclass_list:
    print(my_function_module.get_number_fields(fc))