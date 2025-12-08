
import math

def conv(lon, lat):
    
    R = 6378137.0
    
    if lat > 85:
        lat = 85
    elif lat < -85:
        lat = -85

    lon_rad = math.radians(lon)
    lat_rad = math.radians(lat)
    
    x = R * lon_rad
    y = R * math.log(math.tan(math.pi / 4 + lat_rad / 2))
    
    return x, y

