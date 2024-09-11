"""
Automated python script for poles and lines
"""
import geopandas as gpd
from shapely.geometry import LineString, Point
import os
import pandas as pd

#get current working directory
cwd = os.getcwd()

#create output directory if not exist
if not os.path.exists(f"{cwd}/output/"):
    os.makedirs(f"{cwd}/output/")

#read poles and lines layers
poles = gpd.read_file(f'{cwd}/data/input_data.gpkg', layer= 'poles')
lines = gpd.read_file(f'{cwd}/data/input_data.gpkg', layer= 'lines')

###Stage 1 snap spans to nearest poles and add Point A Point B columns
print('Snapping lines')
for index, line in lines.iterrows():
    
    line_coords = list(line.geometry.coords)
    
    #find nearest pole for endpoint A
    end_point_1 = Point(line.geometry.coords[0]) #line endpoint A
    nearest_pole_id_1 = poles.distance(end_point_1).idxmin() #nearest pole id to point A
    nearest_pole_1 = poles.loc[nearest_pole_id_1] #nearest pole
    lines.at[index, 'Point A'] = nearest_pole_1['poleID']
    line_coords[0] = nearest_pole_1.geometry.coords[0]
    
    #find nearest pole for endpoint B
    end_point_2 = Point(line.geometry.coords[-1])
    nearest_pole_id_2 = poles.distance(end_point_2).idxmin() #nearest pole id to point A
    nearest_pole_2 = poles.loc[nearest_pole_id_2] #nearest pole
    lines.at[index, 'Point B'] = nearest_pole_2['poleID']
    line_coords[-1] = nearest_pole_2.geometry.coords[0]
    
    #update line geometry with snapped coordinates
    lines.at[index, "geometry"] = LineString(line_coords)

print("Lines snapped")
    
###Stage 2 populate missing values from the nearest pole (only applicable for poles height)
#lines[lines.isna().any(axis=1)]

poles_nan = poles[poles['height'].isna()] #find nan rows

for index, pole in poles_nan.iterrows():
    
    distances = poles.distance(pole.geometry) #calculate distances to all other poles
    sorted_distances = distances[distances > 0].sort_values() #sort distances and filter out the pole itself
    
    #check the nearest non-NaN pole
    for nearest_pole_id in sorted_distances.index:
        nearest_pole = poles.loc[nearest_pole_id]
        if pd.notna(nearest_pole['height']):
            poles.at[index, "height"] = nearest_pole['height']#assign nearest pole height
            break  #stop once we've assigned the nearest valid height

#save output files
print("Writing output")

try:
    lines.to_file(f"{cwd}/output/spans.geojson")
    poles.to_file(f"{cwd}/output/poles.geojson")
except Exception as e:
    print(f"Error saving files: {e}")