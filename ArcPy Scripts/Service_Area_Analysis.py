import arcpy
from arcpy import env
import os

# Read Parameters
roadDataset = arcpy.GetParameterAsText(0)
roadRestrictions = arcpy.GetParameterAsText(1)
pedDataset = arcpy.GetParameterAsText(2)
bikeDataset = arcpy.GetParameterAsText(3)
facilityDatabase = arcpy.GetParameterAsText(4)

# Set Up Processing and Facility Database Directories
env.workspace = facilityDatabase
facility_list = arcpy.ListFeatureClasses()
arcpy.env.parallelProcessingFactor = "100%"

env.workspace = os.getcwd()
if arcpy.Exists(r"Service Area Database.gdb") :
    arcpy.management.Delete("Service Area Database.gdb")

arcpy.management.CreateFileGDB(
    out_folder_path=os.getcwd(),
    out_name="Service Area Database",
    out_version="CURRENT"
)

# Define Transport Modes
transport_mode = ['Walking', 'Biking', 'Driving']

# Outer Facility Processing Loop - Process Service Areas for X Number of Facilities
for facility in facility_list :

    arcpy.env.overwriteOutput = True

    env.workspace = os.getcwd() + r"\Service Area Database.gdb/"

    # Inner Transportation Mode Processing Loop
    for mode in transport_mode :

        # Make the Service Area Layer
        if mode == "Driving":
            net_path = roadDataset
            result_object = arcpy.na.MakeServiceAreaAnalysisLayer(
                network_data_source=net_path,
                layer_name=facility + "_Service_Area_-_" + mode,
                travel_mode=mode,
                travel_direction="TO_FACILITIES",
                cutoffs=[300,600,900],
                time_of_day=None,
                time_zone="LOCAL_TIME_AT_LOCATIONS",
                output_type="POLYGONS",
                polygon_detail="HIGH",
                geometry_at_overlaps="DISSOLVE",
                geometry_at_cutoffs="DISKS",
                polygon_trim_distance="100 Meters",
                exclude_sources_from_polygon_generation=None,
                accumulate_attributes=None,
                ignore_invalid_locations="SKIP"
            )
        else :
            net_path = bikeDataset
            result_object = arcpy.na.MakeServiceAreaAnalysisLayer(
                network_data_source=net_path,
                layer_name=facility + "_Service_Area_-_" + mode,
                travel_mode=mode,
                travel_direction="TO_FACILITIES",
                cutoffs=[5,10,15],
                time_of_day=None,
                time_zone="LOCAL_TIME_AT_LOCATIONS",
                output_type="POLYGONS",
                polygon_detail="HIGH",
                geometry_at_overlaps="DISSOLVE",
                geometry_at_cutoffs="DISKS",
                polygon_trim_distance="100 Meters",
                exclude_sources_from_polygon_generation=None,
                accumulate_attributes=None,
                ignore_invalid_locations="SKIP"
            )
        layer_object = result_object.getOutput(0)
        
        print("Created Service Area Layer " + layer_object.name)

        # Add Facility Locations
        arcpy.na.AddLocations(
            in_network_analysis_layer=layer_object,
            sub_layer="Facilities",
            in_table=facilityDatabase + r"/" + facility,
            field_mappings="Name Name #;CurbApproach # 0;Attr_Travel_Time # 0;Attr_Length # 0;Breaks_Travel_Time # #;Breaks_Length # #",
            search_tolerance="5000 Meters",
            sort_field=None,
            match_type="MATCH_TO_CLOSEST",
            append="CLEAR",
            snap_to_position_along_network="NO_SNAP",
            snap_offset="5 Meters",
            exclude_restricted_elements="EXCLUDE",
            search_query=None,
            allow_auto_relocate="ALLOW"
        )
        print("Added " + facility + " Locations")

        # If Driving, add Restricted Turns
        if mode == "Driving" :
            arcpy.na.AddLocations(
                in_network_analysis_layer=layer_object,
                sub_layer="Line Barriers",
                in_table= roadRestrictions,
                field_mappings="Name # #;BarrierType # 1;Attr_Travel_Time # 1;Attr_Length # 1;Shape_Length Shape_Length #",
                search_tolerance="5000 Meters",
                sort_field=None,
                match_type="MATCH_TO_CLOSEST",
                append="CLEAR",
                snap_to_position_along_network="NO_SNAP",
                snap_offset="5 Meters",
                exclude_restricted_elements="EXCLUDE",
                search_query=None,
                allow_auto_relocate="ALLOW"
            )
            print("Added Driving Restrictions")
        
        # Solve Service Area
        result = arcpy.na.Solve(
            in_network_analysis_layer=layer_object,
            ignore_invalids="SKIP",
            terminate_on_solve_error="TERMINATE",
            simplification_tolerance=None,
            overrides=""            
        )
        print("Solved Service Area Analysis Successfully")

        # Export to Service Area Geodatabase
        
        arcpy.management.SaveToLayerFile(layer_object, os.getcwd() + r"\Service Area Layers/" + facility + r"/" + layer_object.name, "ABSOLUTE")    
                
        print("Export Successful")