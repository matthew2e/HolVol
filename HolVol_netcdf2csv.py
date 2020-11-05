from netCDF4 import Dataset, num2date
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd


nc     = Dataset('HolVol_volcanic_stratospheric_sulfur_injection_v1.0.nc')
year   = nc.variables['year'][:]
yearCE = nc.variables['yearCE'][:]
month  = nc.variables['month'][:]
day    = nc.variables['day'][:]
lat    = nc.variables['lat'][:]
vssi   = nc.variables['vssi'][:]
hemi   = nc.variables['hemi'][:]
sig    = nc.variables['sigma_vssi'][:]
dur    = nc.variables['duration'][:]
#volc   = nc.variables['volcano'][:]

nc.close()

x=np.vstack((year,yearCE,month,day,lat,vssi,sig,dur,hemi)).T
#x=np.concatenate((year,yearCE,month,day,lat,vssi,sig,dur,hemi))

df = pd.DataFrame(data=x,index=None, columns=['Year','YearCE','Month','Day','Lat','VSSI','Sigma VSSI','Duration','Hemi'])
df.to_csv('HolVol_volcanic_stratospheric_sulfur_injection_v1.0.csv')


