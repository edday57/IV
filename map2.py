import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd

from geonamescache import GeonamesCache
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
filename = "pollutiondata2.csv"
shapefile2= "countries.shp"
shapefile= "countries"
colors = 10
cols = ['Country Name', 'Country Code', 'Waste']
title = "Plastics Waste Produced In 2016 (Tons)"
imgfile = 'img/map.png'

gc = GeonamesCache()
iso3_codes = list(gc.get_dataset_by_key(gc.get_countries(), 'iso3').keys())

gdf = gpd.read_file(shapefile2)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')

df = pd.read_csv(filename, usecols=cols)
df.set_index('Country Code', inplace=True)
#df = df.loc[iso3_codes].dropna()
values = df["Waste"]
cm = plt.get_cmap('Greens')
scheme = [cm(i / colors) for i in range(colors)]
bins = np.linspace(values.min(), values.max(), colors)
df['bin'] = np.digitize(values, bins) - 1
print(df.sort_values('bin', ascending=False).head(3))

#mpl.style.use('map')
fig = plt.figure(figsize=(22, 12))

ax = fig.add_subplot(111, facecolor='w', frame_on=False)
fig.suptitle(title, fontsize=30, y=.95)

m = Basemap(lon_0=0, projection='robin')
m.drawmapboundary(color='w')

m.readshapefile(shapefile, 'units', color='#444444', linewidth=.2)
for info, shape in zip(m.units_info, m.units):
    iso3 = info['ADM0_A3']
    if iso3 not in df.index:
        color = '#dddddd'
    else:
        color = scheme[df.loc[iso3]['bin']]

    patches = [Polygon(np.array(shape), True)]
    pc = PatchCollection(patches)
    pc.set_facecolor(color)
    ax.add_collection(pc)

# Cover up Antarctica so legend can be placed over it.
ax.axhspan(0, 1000 * 1800, facecolor='w', edgecolor='w', zorder=2)

# Draw color legend.
ax_legend = fig.add_axes([0.35, 0.14, 0.3, 0.03], zorder=3)
cmap = mpl.colors.ListedColormap(scheme)
print(bins)
cb = mpl.colorbar.ColorbarBase(ax_legend, cmap=cmap, ticks=bins, boundaries=bins, orientation='horizontal')
#cb = mpl.colorbar.ColorbarBase(ax_legend, cmap=cmap, orientation='horizontal')

cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])

# Set the map footer.

plt.savefig(imgfile, bbox_inches='tight', pad_inches=.2)