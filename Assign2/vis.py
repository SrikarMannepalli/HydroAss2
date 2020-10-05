import pandas as pd
import math
import numpy as np
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
from IPython.display import display

def q2(df):
    new = df[['State', 'OIP']]
    print(new)


def q1(df):
    print("HI")
    df_new = df[['Name', 'lat', 'long', 'WQI', 'WQC']]

    df_final = df_new.groupby('Name').mean().reset_index()

    latitude = 20.5937
    longitude = 78.9629

    incidents = folium.map.FeatureGroup()

    from folium import plugins

    # let's start with a clean copy of the map of India
    world_map = folium.Map(location=[latitude, longitude], zoom_start = 4)

    # instantiate a mark cluster object for the incidents in the dataframe
    incidents = plugins.MarkerCluster().add_to(world_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label1, label2, in zip(df_final.lat, df_final.long, df_final['Name'], df_final['WQI']):
        temp = 'Station Name: '+label1+' <br>WQI: '+str(round(label2, 2))
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup= folium.Popup(temp, max_width=1000),
        ).add_to(incidents)

    # display map
    display(world_map)
