# Geo Data Scientist Case Study

This repository contains the Indigo Ag Code challenge for Christian Matthews

The objective of this respository is to automate the prioritization of of buyer locations using CSVs of county level USDA/NASS data.

# Preparation
1. Download data from https://quickstats.nass.usda.gov/.
   *For this example I downloaded 2020 CORN, GRAIN - PRODUCTION, MEASURED IN BU and 2020 SOYBEANS - PRODUCTION, MEASURED IN BU
2. Download and install the following:
   *Anaconda - https://www.anaconda.com/products/individual
   *OSGEO4W - https://www.osgeo.org/projects/osgeo4w/
*PostgreSQL AND PostGIS - https://www.postgresql.org/download/
*Modules: GeoPandas, psycopg2
3. Download all of the files in the Scripts[Scripts] folder.
4. Download the 2020 Census Shapefile[https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=Counties+%28and+equivalent%29]
5. House the raw CSVs, Scripts, and 2020 Census Shapefile in the same folder

# Processing
1. Rename the CSVs to something that makes sense with "2020" in the name
*For this example I used CornGrain_2020_raw.csv and Soybean_2020_raw.csv
2. IndigoTool_Step1.py
*Open the .py file and set any of the first variables to change your input csv and buffer distance
*Run this file
3. IndigoTool_Step2.py
*Using the command line run each line individually
4. IndigoTool_Step3.py
*Run this file
5. IndigoTool_Step4.py
*Copy this code and run in the QGIS Python Module
6. IndigoTool_Step5.py
*Run this file
7. IndigoTool_Step2.py
*Using the command line run the line individually


# Visualization
  A Carto visualization of the final data can be found in the Facilities 2020 Map[https://oijgea98j4.carto.com/builder/e66df8a7-b1ba-40ed-b98b-1bb49f37d3a1/embed]
