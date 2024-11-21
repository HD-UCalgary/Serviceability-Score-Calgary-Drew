# Serviceability Score - Calgary - Geospatial Data Package
**Author:** Harrison Drew

**Institution:** University of Calgary - Department of Geography

**UCID:** 30115014

**Email:** harrison.drew@ucalgary.ca

# General Information
This geospatial data package was used in the Creating a Serviceability Score project analysis. This project aimed to generate service areas of essential services with ArcGIS, and create a "serviceability score" using cutom weighted Multi-Criteria Decision Analysis (MCDA). Calgary-focussed data was used to provide recommendations focussing on building a more sustainable future for the City of Calgary.
# Data Overview
The data provided consists of "Compiled Maps", "Statistics", and "ArcPy Scripts" folders. The data imported from external sources are listed in the reference table provided in the files.
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
  
-     Intel Core i7-10700k 3.8 GHz or greater
  
-     Nvidia RTX 3060 or greater
  

Ideally, point shapefiles or XY data should exist for the following essential services in a city, called facilities:

    - Bus Stops
    
    - Rail Stations (LRT/Heavy/HSR)
    
    - Grocery Stores (including convienence stores)
    
    - Fire Stations
    
    - Primary Care Facilities
    
    - Elementary Schools
    
    - Junior High Schools
    
    - Senior High Schools
    
# Service_Area_Analysis.py
To run the script:

1. A geodatabase needs to be created under the home (root) project folder with the exact naming called "Facility Database".
   
2. Import the provided Network Geodatabase to the home (root) folder.
   
3. Import all facilities needed to generate service areas as feature classes to the "Facility Database" geodatabase.
   
4. IF choosing a different city or location to perform analysis, the script will need to be tweaked to point towards network datasets of that location. Be sure to keep the transportation modes (and time cutoffs) of roadway networks to be titled to "Driving" and include a turn restriction layer (again, will need to be tweaked in the script), and pathway/pedestrian networks titled "Biking" and "Walking".
   
5. Run the script. After finishing, produced service area layer files can be found under the new "Service Area Layers" folder created in the home (root) project directory.
# MCDA_Analysis.py
To run the script:

1. Run the Service_Area_Analysis.py script as described above.
   
2. Import the MCDA geoprocessing toolbox into ArcGIS Pro
   
3. Follow the parameter instructions:
   
        - Check/Uncheck components of the analysis wanted (note. unchecking early steps on first run will break the script).

        - Set facility names for each category to the proper facility feature class (the same names as used in the Service_Area_Analysis script, for each facility in the Facility Database)
   
        - Set location of city boundary shapefile or feature class.
   
        - Set location of clipped geometry of desired zones of city for final score generation filtering (the project only scores residential and commercial districts of Calgary, for example).
        
5. Run the script. After finishing, scored rasters will be produced under the MCDA Rasters.gdb geodatabase.
   
# Sharing and access information
The code provided, along with the final result figures, graphs, and tables are licensed under a Creative Commons 1.0 Universal License. More information about the full usage rights under this can be found under the license file or tab.
# Sources
Data was derived from the list of open data specified under the reference table.
