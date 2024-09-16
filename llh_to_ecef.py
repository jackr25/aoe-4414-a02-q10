# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg long_deg hae_km
#  Text explaining script usage
# Parameters:
#  lat_deg: latitude in degrees (lamda)
#  lon_deg: longitude in degrees (phi)
#  hae_km: height above ellipsoid in degrees
#  ...
# Output:
#  outputs radii components for x,y, and z axes in km.
#
# Written by Jack Rathert
# Other contributors: None

# import Python modules

import sys # argv
import math as m

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## shortcut for denominator of common fxns
def calc_denom(ecc,lat_rad):
    return m.sqrt(1-ecc**2 *(m.sin(lat_rad))**2)

# initialize script arguments
lat_rad = float('nan') 
lon_rad = float('nan') 
hae_km = float('nan') 
 

# parse script arguments
if len(sys.argv)==4:
  lat_rad = float(sys.argv[1])*m.pi/180
  lon_rad = float(sys.argv[2])*m.pi/180
  hae_km = float(sys.argv[3])
  ...
else:
  print(\
   'Usage: '\
   'python3 llh_to_ecef.py lat_deg long_deg hae_km'\
  )
  exit()

# write script below this line

denom = calc_denom(E_E, lat_rad)

C_E = R_E_KM/denom
S_E = R_E_KM*(1-E_E**2)/denom

r_x_km = (C_E + hae_km)*m.cos(lat_rad)*m.cos(lon_rad)
r_y_km = (C_E + hae_km)*m.cos(lat_rad)*m.sin(lon_rad)
r_z_km = (S_E + hae_km)*m.sin(lat_rad)

r_km = m.sqrt(r_x_km**2 + r_y_km**2 + r_z_km**2)

print(r_x_km)
print(r_y_km)
print(r_z_km)