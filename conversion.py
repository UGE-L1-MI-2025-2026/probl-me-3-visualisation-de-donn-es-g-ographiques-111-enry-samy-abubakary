import math


def wsg84_vers_mercator(lon,lat):
    
    
    # Rayon de la Terre en mètres
    R = 6378137.0

    # Conversion des degrés en radians
    lon_rad = math.radians(lon)
    lat_rad = math.radians(lat)
    

    # Calcul des coordonnées Mercator
    x = R * lon_rad
    y = R * math.log(math.tan(math.pi / 4 + lat_rad / 2))

    return (x, y)



import random

Exemple = wsg84_vers_mercator(2.3522, 48.8566)
print(Exemple)
print(random.uniform(-180, 180))
print(random.uniform(-90, 90))