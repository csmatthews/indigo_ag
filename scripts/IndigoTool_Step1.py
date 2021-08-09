# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:58:35 2021

@author: cmatthews
"""

import pandas as pd
import geopandas as gpd
from osgeo import ogr
from osgeo import osr
import os

csv = "indigo_case_study_500_random_buyers.csv"
shapefile = "facilities.shp"
crsdriver = "ESRI Shapefile"
# bufdist is in meters
bufdist = 40233.6


### Convert Facilities CSV to SHP
# Read the .csv file using Pandas
facilities_data = pd.read_csv(csv)

# Create GeoPandas GeoDataFrame from the Pandas Dataframe
facilities_gdf = gpd.GeoDataFrame(facilities_data, geometry = gpd.points_from_xy(facilities_data['longitude'],facilities_data['latitude']))

# Set Coordinate System to WGS84 using https://epsg.io/4326
ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

# Export as Shapefile
facilities_gdf.to_file(filename = shapefile, driver = crsdriver, crs=(ESRI_WKT))

# Open Shapefile
gdf = gpd.read_file(shapefile)

# Transform Coordinate System to USA Contiguous Equidistant Conic using https://epsg.io/102005
gdf = gdf.to_crs('esri:102005') 

# Overwrite Shapefile
gdf.to_file(shapefile, driver = crsdriver)

print("Finished Convert Facilities CSV to SHr")



### Buffer Facilities Layer
# Set facilities layer
drv = ogr.GetDriverByName(crsdriver)
dataSet = drv.Open(shapefile)

# Create Output Layer
layer = dataSet.GetLayer(0)
sr = osr.SpatialReference()
sr.SetFromUserInput('esri:102005')
outfile = drv.CreateDataSource("facilities_buf25mi.shp")
outlayer = outfile.CreateLayer("facilities_buf25mi", geom_type=ogr.wkbPolygon, srs=sr)
nameField = ogr.FieldDefn('id', ogr.OFTString)
outlayer.CreateField(nameField)
featureDefn = outlayer.GetLayerDefn()

# Run buffer
for feature in layer:
    ingeom = feature.GetGeometryRef()
    outgeom = ingeom.Centroid().Buffer(bufdist)
    outFeature = ogr.Feature(featureDefn)
    outFeature.SetGeometry(outgeom)
    outFeature.SetField('id', feature.GetField('id'))
    outlayer.CreateFeature(outFeature)
    outFeature = None
 
layer.ResetReading()
outfile = None
print("Buffer Facilities Layer")



### Format CSV files
filesnames = os.listdir(r"C:\Users\cmatthews\Desktop\Indigo\Tool")
filesnames = [f for f in filesnames if ("2020" in f and f.lower().endswith(".csv"))]

for filename in filesnames:   
    df = pd.read_csv(filename)
    df = df.loc[:, ['State ANSI', 'County ANSI','Value']]
    df['State ANSI'] = df['State ANSI'].astype(str)
    df['County ANSI'] = df['County ANSI'].astype(str)
    df['Value'] = df['Value'].replace(',', '', regex=True)
    df['Value'] = df['Value'].astype(int)
    df['County ANSI'] = df['County ANSI'].astype(str).replace('\.0', '', regex=True)
    df['State ANSI'] = df['State ANSI'].apply(lambda x: x.zfill(2))
    df['County ANSI'] = df['County ANSI'].apply(lambda x: x.zfill(3))
    df['geoid'] = df['State ANSI']+df['County ANSI']
    df = df.loc[:, ['geoid','Value']]
    df.to_csv(os.path.splitext(filename)[0][:-4]+"_DF.csv")

print("Finished Format CSV files")


### Run Step 2 "C:\Users\cmatthews\Desktop\Indigo\Tool\IndigoTool_Step2.py"
print("Move onto Run IndigoTool_Step2.py")