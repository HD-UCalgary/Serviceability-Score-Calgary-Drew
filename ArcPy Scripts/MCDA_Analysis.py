import arcpy
from arcpy import env
import os
         
arcpy.env.overwriteOutput = True

# Read Parameters

createPoly = arcpy.GetParameterAsText(0)
createRaster = arcpy.GetParameterAsText(1)
createMCDA = arcpy.GetParameterAsText(2)
cityBoundary = arcpy.GetParameterAsText(3)
scoreZones = arcpy.GetParameterAsText(4)
calcTransit = arcpy.GetParameterAsText(5)
calcGrocery = arcpy.GetParameterAsText(6)
calcEmergency = arcpy.GetParameterAsText(7)
calcSchool = arcpy.GetParameterAsText(8)
calcFinal = arcpy.GetParameterAsText(9)
nameBus = arcpy.GetParameterAsText(10)
nameRail = arcpy.GetParameterAsText(11)
nameGrocery = arcpy.GetParameterAsText(12)
nameFire = arcpy.GetParameterAsText(13)
nameCare = arcpy.GetParameterAsText(14)
nameElementary = arcpy.GetParameterAsText(15)
nameJrHigh = arcpy.GetParameterAsText(16)
nameSrHigh = arcpy.GetParameterAsText(17)

# Create Polygon Geodatabase, if not exists

if not arcpy.Exists(os.getcwd() + r"\MCDA Polygons.gdb"):
    arcpy.management.CreateFileGDB(
        out_folder_path=os.getcwd(),
        out_name="MCDA Polygons",
        out_version="CURRENT"
    )

# Create Polygons from Service Area Layers

if createPoly:

    # Set Up Service Area Layer Directories
    env.workspace = os.getcwd() + r"\Service Area Layers"
    folder_list = arcpy.ListFiles()


    env.workspace = os.getcwd()

    # Outer Loop - Process Layer Files

    for folder in folder_list :

        arcpy.management.CreateFeatureDataset(        
            out_dataset_path=os.getcwd() + r"\MCDA Polygons.gdb",
            out_name=folder,
            spatial_reference='PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision'
        )

        env.workspace = os.getcwd() + r"\Service Area Layers/" + folder
        layer_list = arcpy.ListFiles()

        # Inner Loop - Read Polygon Types

        for layer in layer_list :
            print("Layer: " + layer)
            print("Folder: " + folder)
            lyrFile = arcpy.mp.LayerFile(os.getcwd() + r"\Service Area Layers/" + folder + r"/" + layer)
            lay_list = lyrFile.listLayers()
            for lay in lay_list :
                if lay.name == "Polygons" :
                    polygons = lay

            # Select Transit Mode, Then Export 5, 10, 15 Minute Polygon Feature Classes

            if "Driving" in layer:
                name = "Driving"
                arcpy.conversion.ExportFeatures(
                in_features=polygons,
                out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_5min",
                where_clause="Name = '0 - 300'",
                use_field_alias_as_name="NOT_USE_ALIAS",
                sort_field=None
                )
                arcpy.conversion.ExportFeatures(
                    in_features=polygons,
                    out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_10min",
                    where_clause="Name = '0 - 600'",
                    use_field_alias_as_name="NOT_USE_ALIAS",
                    sort_field=None
                )
                arcpy.conversion.ExportFeatures(
                    in_features=polygons,
                    out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_15min",
                    where_clause="Name = '0 - 900'",
                    use_field_alias_as_name="NOT_USE_ALIAS",
                    sort_field=None
                )
            elif "Biking" in layer:
                name = "Biking"
                arcpy.conversion.ExportFeatures(
                in_features=polygons,
                out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_5min",
                where_clause="Name = '0 - 5'",
                use_field_alias_as_name="NOT_USE_ALIAS",
                sort_field=None
                )
                arcpy.conversion.ExportFeatures(
                    in_features=polygons,
                    out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_10min",
                    where_clause="Name = '0 - 10'",
                    use_field_alias_as_name="NOT_USE_ALIAS",
                    sort_field=None
                )
                arcpy.conversion.ExportFeatures(
                    in_features=polygons,
                    out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_15min",
                    where_clause="Name = '0 - 15'",
                    use_field_alias_as_name="NOT_USE_ALIAS",
                    sort_field=None
                )
            elif "Walking" in layer:
                name = "Walking"
                arcpy.conversion.ExportFeatures(
                in_features=polygons,
                out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_5min",
                where_clause="Name = '0 - 5'",
                use_field_alias_as_name="NOT_USE_ALIAS",
                sort_field=None
                )
                arcpy.conversion.ExportFeatures(
                    in_features=polygons,
                    out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_10min",
                    where_clause="Name = '0 - 10'",
                    use_field_alias_as_name="NOT_USE_ALIAS",
                    sort_field=None
                )
                arcpy.conversion.ExportFeatures(
                    in_features=polygons,
                    out_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_15min",
                    where_clause="Name = '0 - 15'",
                    use_field_alias_as_name="NOT_USE_ALIAS",
                    sort_field=None
                )
            else:
                name = "_"

            print ("Exported Feature Classes Successfully")
            
            # Empty Feature Class Edge Case Guard

            checker5 =  arcpy.GetCount_management(os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_5min")
            checker10 =  arcpy.GetCount_management(os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_10min")
            checker15 =  arcpy.GetCount_management(os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_15min")
            count5 = int(checker5.getOutput(0))
            count10 = int(checker10.getOutput(0))
            count15 = int(checker15.getOutput(0))

            # Convert to 1m x 1m Raster
            
            with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'):
                if count5 > 0 and not arcpy.Exists(os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"_" + name + r"_5min_Raster"):
                    arcpy.conversion.FeatureToRaster(
                    in_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_5min",
                        field="NAME",
                        out_raster=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"_" + name + r"_5min_Raster",
                        cell_size=1
                    )
                if count10 > 0 and not arcpy.Exists(os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"_" + name + r"_10min_Raster"):
                    arcpy.conversion.FeatureToRaster(
                        in_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_10min",
                        field="NAME",
                        out_raster=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"_" + name + r"_10min_Raster",
                        cell_size=1
                    )
                if count15 > 0 and not arcpy.Exists(os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"_" + name + r"_15min_Raster"):
                    arcpy.conversion.FeatureToRaster(
                        in_features=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"/" + folder + r"_" + name + r"_15min",
                        field="NAME",
                        out_raster=os.getcwd() + r"\MCDA Polygons.gdb/" + folder + r"_" + name + r"_15min_Raster",
                        cell_size=1
                    )

                print ("Exported Rasters Successfully")

        # Convert NoValue Raster to 0
else:
    print ("Skipping Feature Class and Raster Creation")

# Convert Rasters to Scorable Rasters (turn null values into 0's)

if createRaster:
    env.workspace = os.getcwd() + r"\MCDA Polygons.gdb/"
    raster_list = arcpy.ListRasters()

    # Convert Null Points Into 0's and Overwrite

    for raster in raster_list:
        print ("Fixing null values in " + raster)
        raster = raster
        with arcpy.EnvManager(extent='-114.3157895 50.842822 -113.8598987 51.2124253 GEOGCS["WGS84(DD)",DATUM["WGS84",SPHEROID["WGS84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433]]', scratchWorkspace=os.getcwd() + r"\MCDA Polygons.gdb"):
        
            out_raster = arcpy.sa.Con(
                in_conditional_raster=raster,
                in_true_raster_or_constant=0,
                in_false_raster_or_constant=raster,
                where_clause="Value IS NULL"
            )
        out_raster.save(os.getcwd() + r"\MCDA Rasters.gdb/" + raster)
        print ("Successfully assigned 0 values in " + raster)
else:
    print ("Skipping Null Value Raster Cleanup")                

# MCDA Raster Calculations

if createMCDA:
    env.workspace = os.getcwd() + r"\MCDA Rasters.gdb/"


    # Transit - 25%


    if calcTransit:
        
        a = nameBus + "_Walking_5min_Raster"
        b = nameBus + "_Walking_10min_Raster"
        c = nameRail + "_Walking_5min_Raster"
        d = nameRail + "_Walking_10min_Raster"
        e = nameRail + "_Walking_15min_Raster"
        f = nameRail + "_Biking_5min_Raster"
        g = nameRail + "_Biking_10min_Raster"
        h = nameRail + "_Biking_15min_Raster"

        with arcpy.EnvManager(extent='-114.3157895 50.842822 -113.8598987 51.2124253 GEOGCS["WGS84(DD)",DATUM["WGS84",SPHEROID["WGS84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433]]', scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            output_raster = arcpy.ia.RasterCalculator(
                [a, b, c, d, e, f, g, h],
                ["a", "b", "c", "d", "e", "f", "g", "h"],
                expression='((a * 0.7 + b * 0.3) * 0.4) + (((c * 0.4 + d * 0.3 + e * 0.3) * 0.6 + (f * 0.4 + g * 0.3 + h * 0.3) * 0.4) * 0.6)'
            )
            output_raster.save(r"Transit_Scored")

        with arcpy.EnvManager(scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Transit_Scored",
                in_mask_data= cityBoundary,
                extraction_area="INSIDE",
                analysis_extent='685944.282138865 5634462.07307237 722878.297014683 5679469.47188845 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Transit_Scored_City")

        with arcpy.EnvManager(scratchWorkspace= os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Transit_Scored_City",
                in_mask_data= scoreZones,
                extraction_area="INSIDE",
                analysis_extent='687992.438042452 5635247.56222852 722350.465733129 5677753.18487316 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Transit_Scored_Final")
    else:
        print("Skipping Transit MCDA")


    # Grocery - 25%

    
    if calcGrocery:

        a = nameGrocery + "_Walking_5min_Raster"
        b = nameGrocery + "_Walking_10min_Raster"
        c = nameGrocery + "_Walking_15min_Raster"
        d = nameGrocery + "_Biking_5min_Raster"
        e = nameGrocery + "_Biking_10min_Raster"
        f = nameGrocery + "_Biking_15min_Raster"
        g = nameGrocery + "_Driving_5min_Raster"
        h = nameGrocery + "_Driving_10min_Raster"
        i = nameGrocery + "_Driving_10min_Raster"

        with arcpy.EnvManager(extent='-114.3157895 50.842822 -113.8598987 51.2124253 GEOGCS["WGS84(DD)",DATUM["WGS84",SPHEROID["WGS84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433]]', scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            output_raster = arcpy.ia.RasterCalculator(
                [a, b, c, d, e, f, g, h, i],
                ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
                expression='(((a * 0.5) + (b * 0.3) +  (c * 0.2)) * 0.5) + (((d * 0.5) + (e * 0.3) +  (f * 0.2)) * 0.3) + (((g * 0.5) + (h * 0.3) +  (i * 0.2)) * 0.2)'
            )
            output_raster.save(r"Grocery_Scored")

        with arcpy.EnvManager(scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Grocery_Scored",
                in_mask_data= cityBoundary,
                extraction_area="INSIDE",
                analysis_extent='685944.282138865 5634462.07307237 722878.297014683 5679469.47188845 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Grocery_Scored_City")

        with arcpy.EnvManager(scratchWorkspace= os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Grocery_Scored_City",
                in_mask_data= scoreZones,
                extraction_area="INSIDE",
                analysis_extent='687992.438042452 5635247.56222852 722350.465733129 5677753.18487316 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Grocery_Scored_Final")
    else:
        print("Skipping Grocery MCDA")

    # Emergency Services - 25%

    if calcEmergency:

        a = nameFire + "_Driving_5min_Raster"
        b = nameFire + "_Driving_10min_Raster"
        c = nameCare + "_Driving_5min_Raster"
        d = nameCare + "_Driving_10min_Raster"

        with arcpy.EnvManager(extent='-114.3157895 50.842822 -113.8598987 51.2124253 GEOGCS["WGS84(DD)",DATUM["WGS84",SPHEROID["WGS84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433]]', scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            output_raster = arcpy.ia.RasterCalculator(
                [a, b, c, d],
                ["a", "b", "c", "d"],
                expression='(((a * 0.7) + (b * 0.3)) * 0.5) + (((c * 0.7) + (d * 0.3)) * 0.5)'
            )
            output_raster.save(r"Emergency_Scored")

        with arcpy.EnvManager(scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Emergency_Scored",
                in_mask_data=cityBoundary,
                extraction_area="INSIDE",
                analysis_extent='685944.282138865 5634462.07307237 722878.297014683 5679469.47188845 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Emergency_Scored_City")

        with arcpy.EnvManager(scratchWorkspace= os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Emergency_Scored_City",
                in_mask_data=scoreZones,
                extraction_area="INSIDE",
                analysis_extent='687992.438042452 5635247.56222852 722350.465733129 5677753.18487316 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Emergency_Scored_Final")
    else:
        print("Skipping Emergency MCDA")
    

    # Schools - 25%


    if calcSchool:

        a = nameElementary + "_Walking_5min_Raster"
        b = nameElementary + "_Walking_10min_Raster"
        c = nameElementary + "_Walking_15min_Raster"
        d = nameElementary + "_Biking_5min_Raster"
        e = nameElementary + "_Biking_10min_Raster"
        f = nameElementary + "_Biking_15min_Raster"
        g = nameElementary + "_Driving_5min_Raster"
        h = nameElementary + "_Driving_10min_Raster"
        i = nameElementary + "_Driving_10min_Raster"
        aa = nameJrHigh + "_Walking_5min_Raster"
        bb = nameJrHigh + "_Walking_10min_Raster"
        cc = nameJrHigh + "_Walking_15min_Raster"
        dd = nameJrHigh + "_Biking_5min_Raster"
        ee = nameJrHigh + "_Biking_10min_Raster"
        ff = nameJrHigh + "_Biking_15min_Raster"
        gg = nameJrHigh + "_Driving_5min_Raster"
        hh = nameJrHigh + "_Driving_10min_Raster"
        ii = nameJrHigh + "_Driving_10min_Raster"
        aaa = nameSrHigh + "_Walking_5min_Raster"
        bbb = nameSrHigh + "_Walking_10min_Raster"
        ccc = nameSrHigh + "_Walking_15min_Raster"
        ddd = nameSrHigh + "_Biking_5min_Raster"
        eee = nameSrHigh + "_Biking_10min_Raster"
        fff = nameSrHigh + "_Biking_15min_Raster"
        ggg = nameSrHigh + "_Driving_5min_Raster"
        hhh = nameSrHigh + "_Driving_10min_Raster"
        iii = nameSrHigh + "_Driving_10min_Raster"

        with arcpy.EnvManager(extent='-114.3157895 50.842822 -113.8598987 51.2124253 GEOGCS["WGS84(DD)",DATUM["WGS84",SPHEROID["WGS84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433]]', scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            output_raster = arcpy.ia.RasterCalculator(
                [a, b, c, d, e, f, g, h, i, aa, bb, cc, dd, ee, ff, gg, hh, ii, aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii],
                ["a", "b", "c", "d", "e", "f", "g", "h", "i", "aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii"],
                expression='(((((a * 0.5) + (b * 0.3) + (c * 0.2)) * 0.6) + (((d * 0.5) + (e * 0.3) + (f * 0.2)) * 0.3) + (((g * 0.5) + (h * 0.3) + (i * 0.2)) * 0.1)) * 0.33) + (((((aa * 0.5) + (bb * 0.3) + (cc * 0.2)) * 0.6) + (((dd * 0.5) + (ee * 0.3) + (ff * 0.2)) * 0.3) + (((gg * 0.5) + (hh * 0.3) + (ii * 0.2)) * 0.1)) * 0.33) + (((((aaa * 0.5) + (bbb * 0.3) + (ccc * 0.2)) * 0.6) + (((ddd * 0.5) + (eee * 0.3) + (fff * 0.2)) * 0.3) + (((ggg * 0.5) + (hhh * 0.3) + (iii * 0.2)) * 0.1)) * 0.33)'
            )
            output_raster.save(r"School_Scored")

        with arcpy.EnvManager(scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="School_Scored",
                in_mask_data=cityBoundary,
                extraction_area="INSIDE",
                analysis_extent='685944.282138865 5634462.07307237 722878.297014683 5679469.47188845 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"School_Scored_City")

        with arcpy.EnvManager(scratchWorkspace= os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="School_Scored_City",
                in_mask_data=scoreZones,
                extraction_area="INSIDE",
                analysis_extent='687992.438042452 5635247.56222852 722350.465733129 5677753.18487316 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"School_Scored_Final")
    else:
        print("Skipping School MCDA")
        
    
    # Final MCDA - 100%


    if calcFinal:

        a = "Transit_Scored"
        b = "Grocery_Scored"
        c = "Emergency_Scored"
        d = "School_Scored"

        with arcpy.EnvManager(extent='-114.3157895 50.842822 -113.8598987 51.2124253 GEOGCS["WGS84(DD)",DATUM["WGS84",SPHEROID["WGS84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433]]', scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            output_raster = arcpy.ia.RasterCalculator(
                [a, b, c, d],
                ["a", "b", "c", "d"],
                expression='(a * 0.25) + (b * 0.25)) + (c * 0.25)) + (d * 0.25))'
            )
            output_raster.save(r"Final_Scored")

        with arcpy.EnvManager(scratchWorkspace=os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Final_Scored",
                in_mask_data=cityBoundary,
                extraction_area="INSIDE",
                analysis_extent='685944.282138865 5634462.07307237 722878.297014683 5679469.47188845 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Final_Scored_City")

        with arcpy.EnvManager(scratchWorkspace= os.getcwd() + r"\MCDA Rasters.gdb"):
            out_raster = arcpy.sa.ExtractByMask(
                in_raster="Final_Scored_City",
                in_mask_data=scoreZones,
                extraction_area="INSIDE",
                analysis_extent='687992.438042452 5635247.56222852 722350.465733129 5677753.18487316 PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
            )
            out_raster.save(r"Final_Scored_Final")
    else:
        print("Skipping Final MCDA")

else:
    print("Skipping Citywide MCDA Calculations")
