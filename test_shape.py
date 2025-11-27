import shapefile
from fltk import *


sf = shapefile.Reader("departements-20180101")

cree_fenetre(1200, 1200)


for shape_rec in sf.shapes():
    
    pts = shape_rec.points
    parts = list(shape_rec.parts) + [len(pts)]

    
    for i in range(len(parts) - 1):
        start = parts[i]
        end = parts[i + 1]
        segment = pts[start:end]

        
        poly = []
        for x, y in segment:
            X = x * 20 + 100
            Y = 1200 - (y * 20)
            poly.append((X, Y))

        polygone(poly)

attend_ev()
ferme_fenetre()
