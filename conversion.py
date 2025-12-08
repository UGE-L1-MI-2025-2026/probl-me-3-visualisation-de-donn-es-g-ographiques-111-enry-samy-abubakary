
import shapefile
from fltk import *
from conversion import conv  

sf = shapefile.Reader("departements-20180101")

shapes_metro = []
for shapeRec, record in zip(sf.shapes(), sf.records()):
    dep_code = str(record[0])
    if not dep_code.startswith(("97", "98")):
        shapes_metro.append(shapeRec)


tous_x = []
tous_y = []

for shp in shapes_metro:
    for lon, lat in shp.points:
        xm, ym = conv(lon, lat)
        tous_x.append(xm)
        tous_y.append(ym)

minx = min(tous_x)
miny = min(tous_y)
maxx = max(tous_x)
maxy = max(tous_y)


width = maxx - minx
height = maxy - miny

window_w = 1000
window_h = 1000
cree_fenetre(window_w, window_h)

scale = min((window_w * 0.8) / width, (window_h * 0.8) / height)

scaled_w = width * scale
scaled_h = height * scale
offset_x = (window_w - scaled_w) / 2
offset_y = (window_h - scaled_h) / 2

for shape_rec in shapes_metro:
    pts = shape_rec.points
    parts = list(shape_rec.parts) + [len(pts)]

    for i in range(len(parts) - 1):
        start = parts[i]
        end = parts[i + 1]
        segment = pts[start:end]

        poly = []
        for lon, lat in segment:
          
        
            xm, ym =conv(lon, lat)
            X = (xm - minx) * scale + offset_x
            Y = window_h - ((ym - miny) * scale + offset_y)
           

            poly.append((X, Y))

        polygone(poly)

attend_ev()
ferme_fenetre()




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


