import shapefile
from fltk import *

sf = shapefile.Reader("departements-20180101")

shapes_metro = []
for shapeRec, record in zip(sf.shapes(), sf.records()):
    dep_code = str(record[0])
    
    if not dep_code.startswith(("97", "98")):  
        shapes_metro.append(shapeRec)

minx = min(min(shp.bbox[0], shp.bbox[2]) for shp in shapes_metro)
miny = min(min(shp.bbox[1], shp.bbox[3]) for shp in shapes_metro)
maxx = max(max(shp.bbox[0], shp.bbox[2]) for shp in shapes_metro)
maxy = max(max(shp.bbox[1], shp.bbox[3]) for shp in shapes_metro)

width = maxx - minx
height = maxy - miny

window_w = 1200
window_h = 1200
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
        for x, y in segment:
            X = (x - minx) * scale + offset_x
            Y = window_h - ((y - miny) * scale + offset_y)
            poly.append((X, Y))

        polygone(poly)

attend_ev()
ferme_fenetre()
