import arcpy
from arcpy import env
env.workspace = r"(C:\Users\yxiao081\Downloads\Lecture7_Data\Module7_Data\OTTAWA.gdb\OTTAWADATA)"
featureclass_list=arcpy.ListFeatureClasses()
