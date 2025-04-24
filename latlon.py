#See https://stackoverflow.com/questions/36530391/python-matplotlib-surface-plot

import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
import matplotlib.ticker as mticker

fig, ax = plt.subplots(1, 1, figsize=(4, 4), 
                       subplot_kw={'projection': ccrs.Orthographic(central_longitude=-150., central_latitude=45)})

gl = ax.gridlines(draw_labels=False,linewidth=0.5,color='k')

gl.xlocator = cticker.LongitudeLocator(nbins=40)
gl.ylocator = cticker.LatitudeLocator(nbins=20)

plt.title('Latitude-Longitude Grid',fontsize=14)

plt.tight_layout()
plt.savefig('latlon.pdf', bbox_inches='tight')
plt.show()
