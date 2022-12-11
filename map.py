import os

import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

filename = "pollutiondata.csv"
shapefile= "countries.shp"
colors = 10
cmap="Blues"
figsize = (16,10)
cols = ['Country Name', 'Country Code', 'Waste']
title = "Plastics Waste Produced In Tons"
imgfile = 'img/map.png'

gdf = gpd.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')
gdf.sample(5)

df = pd.read_csv(filename, usecols=cols)

merged = gdf.merge(df, left_on='ADM0_A3', right_on='Country Code')
merged.describe()
ax = merged.dropna().plot(column="Waste", cmap=cmap, figsize=figsize, scheme='equal_interval', k=colors, legend=True)
merged[merged.isna().any(axis=1)].plot(ax=ax, color='#fafafa', hatch='///')
ax.set_axis_off()
ax.set_xlim([-1.5e7, 1.7e7])
ax.get_legend().set_bbox_to_anchor((.12, .4))
ax.get_figure()
plt.show()