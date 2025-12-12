

import math

def conv(lon, lat):

    # Si les valeurs ne ressemblent pas à des degrés on convertit pas
    if abs(lon) > 180 or abs(lat) > 90:
        return lon, lat

    # Conversion degrés en Mercator
    R = 6378137

   
    if lat > 85:
        lat = 85
    elif lat < -85:
        lat = -85

    lon_rad = math.radians(lon)
    lat_rad = math.radians(lat)

    x = R * lon_rad
    y = R * math.log(math.tan(math.pi/4 + lat_rad/2))

    return x, y












