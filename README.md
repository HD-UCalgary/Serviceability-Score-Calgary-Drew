# Serviceability Score - Calgary - Geospatial Data Package
**Author:** Harrison Drew

**Institution:** University of Calgary - Department of Geography

**Undergraduate Course Name:** GEOG 587 - Geospatial Project Management

**UCID:** 30115014

**Email:** harrison.drew@ucalgary.ca

# General Information
This geospatial data package was used in the Creating a Serviceability Score project analysis. This project aimed to generate service areas of essential services with ArcGIS, and create a "serviceability score" using cutom weighted Multi-Criteria Decision Analysis (MCDA). Calgary-focussed data was used to provide recommendations focussing on building a more sustainable future for the City of Calgary.
# Data Overview
The data provided consists of "Compiled Maps", "Statistics", and "ArcPy Scripts" folders. The data imported from external sources are listed in the reference table provided in the files. The project .zip file contains  compiled city-wide rasters as an example of generated serviceability results from service areas and scoring in Calgary.
**Network Geodatabase.gdb**
Produced network analysis layers for driving, biking, and walking transportation modes, containing Calgary's known roadways and pathways. 
**Compiled Maps** - Consists of Calgary-based maps of the final generated service areas of each essential service and useful transport method, and final generated score maps from the MCDA script.

**Statistics** - Graphs and Tables (.csv files) are provided from analyzing the statistics produced from the MCDA script for serviceability scoring in Calgary.

**ArcPy Scripts** - Two ArcPy python files that automate the proceedures of service area creation from ESRI's ArcGIS Pro Geoprocessing Toolbox, and performing the MCDA, with custom assigned weightings. Along with this, a custom toolbox for the MCDA to be run through ArcGIS Pro with custom options is provided.
# Code Compiling and Setup
The ArcPy Scripts folder needs to be downloaded and extracted to the home (root) folder of an ArcGIS geospatial project. Scripts need to remain under the same functioning folder to function correctly.

Recommended System Requirements:

-     At least 16GB RAM
  
-     ~125GB disk space allocated for ArcGIS project
  
-     Intel Core i7-10700k 3.8 GHz or greater processor
  
-     Nvidia GeForce RTX 3060 or greater video card
  

Ideally, point shapefiles or XY data should exist for the following essential services in a city, called facilities:

    - Bus Stops
    
    - Rail Stations (LRT/Heavy/HSR)
    
    - Grocery Stores (including convienence stores)
    
    - Fire Stations
    
    - Primary Care Facilities
    
    - Elementary Schools
    
    - Junior High Schools
    
    - Senior High Schools

Feature classes or polygon shapefiles are needed for the following boundaries:

    - City Limits/Boundary of area to analyze

    - Districts or zones where final scores should be calculated and filtered to. For example, all residential zones of a city.
# Service_Area_Analysis.py
To run the script:

1. Acquire vehicle (driving), pedestrian, and biking network datasets. IF choosing a different city or location to perform analysis, be sure to keep the transportation modes (and time cutoffs) of roadway networks to be titled to "Driving" and include a turn restriction feature class or shapefile, and pathway/pedestrian networks titled "Biking" and "Walking".
   
2. Import all facilities needed to generate service areas as feature classes to your chosen Facility geodatabase.

3. Import the MCDA geoprocessing toolbox into ArcGIS Pro
   
4. Follow the parameter instructions when running the script:

       - Set driving, pedestrian, and biking network locations to their appropiate network datasets.

       - Set road restrictions to the feature class or shapefile containing the road turn restrictions.

       - Set the Facility Database to the appropiate Geodatabase containing the facilities to calculate service areas for.
   
5. Run the script. After finishing, produced service area layer files can be found under the new "Service Area Layers" folder created in the home (root) project directory.
# MCDA_Analysis.py
To run the script:

1. Run the Service_Area_Analysis.py script as described above.
   
2. Import the MCDA geoprocessing toolbox into ArcGIS Pro
   
3. Follow the parameter instructions when running the script:
   
        - Check/Uncheck components of the analysis wanted (note. unchecking early steps on first run will break the script).

        - Set facility names for each category to the proper facility feature class (the same names as used in the Service_Area_Analysis script, for each facility in the Facility Database)
   
        - Set location of city boundary shapefile or feature class.
   
        - Set location of clipped geometry of desired zones of city for final score generation filtering (the project only scores residential and commercial districts of Calgary, for example).
        
4. Run the script. After finishing, scored rasters will be produced under the MCDA Rasters.gdb geodatabase.
   
# Sharing and access information
The code provided, along with the final result figures, graphs, and tables are licensed under a Creative Commons 1.0 Universal License. More information about the full usage rights under this can be found under the license file or tab.
# Sources
Data was derived from the list of open data specified under the reference table.
