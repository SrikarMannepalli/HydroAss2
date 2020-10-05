import pandas as pd
import math
import numpy as np
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
# from IPython.display import display

def q2(df):
    new = df[['State', 'OIP']]
    print(new)

def q1(df):
    df_new = df[['Name', 'lat', 'long', 'WQI', 'WQC']]

    df_final = df_new.groupby('Name').mean().reset_index()
    fig, ax = plt.subplots()
    ind_img = mpimg.imread('./india-rivers-map.jpg')
    plt.imshow(ind_img,extent=[68.7, 96.25, 7.4, 37.6], alpha=0.75)
    longs = [73.65, 81.75, 81.66, 80.61, 73.1333, 72.95]
    lats = [21.916, 17, 17.25, 16.51, 18.4333, 21.283]
    # labels = ["C1", "C2", "C3", "C4", "C3", "C2"]
    scatter = ax.scatter(df["long"], df["lat"])
    legend1 = ax.legend(*scatter.legend_elements(),
                loc="lower left", title="Classes")
    ax.add_artist(legend1)
    plt.show()

# def q1(df):
#     df_new = df[['Name', 'lat', 'long', 'WQI', 'WQC']]

#     df_final = df_new.groupby('Name').mean().reset_index()

#     latitude = 20.5937
#     longitude = 78.9629

#     incidents = folium.map.FeatureGroup()

#     from folium import plugins

#     # let's start with a clean copy of the map of India
#     world_map = folium.Map(location=[latitude, longitude], zoom_start = 4)

#     # instantiate a mark cluster object for the incidents in the dataframe
#     incidents = plugins.MarkerCluster().add_to(world_map)

#     # loop through the dataframe and add each data point to the mark cluster
#     for lat, lng, label1, label2, in zip(df_final.lat, df_final.long, df_final['Name'], df_final['WQI']):
#         temp = 'Station Name: '+label1+' <br>WQI: '+str(round(label2, 2))
#         folium.Marker(
#             location=[lat, lng],
#             icon=None,
#             popup= folium.Popup(temp, max_width=1000),
#         ).add_to(incidents)

#     # display map
#     world_map.save('plot_data.html')

#     # display(world_map)
