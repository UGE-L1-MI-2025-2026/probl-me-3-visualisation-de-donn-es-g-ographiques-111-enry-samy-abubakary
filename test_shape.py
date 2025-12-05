import shapefile
from fltk import *
import conversion
from temperature import *
sf = shapefile.Reader("departements-20180101")


L=generer_liste()
couleurs=generer_dico(L,"2025")
shapes_metro = []
for shapeRec, record in zip(sf.shapes(), sf.records()):
    dep_code = str(record[0])  # ex: "75", "29", "974"
    if not dep_code.startswith(("97", "98")):  
        shapes_metro.append((shapeRec,record[1]))

minx = min(min(shp[0].bbox[0], shp[0].bbox[2]) for shp in shapes_metro)
miny = min(min(shp[0].bbox[1], shp[0].bbox[3]) for shp in shapes_metro)
maxx = max(max(shp[0].bbox[0], shp[0].bbox[2]) for shp in shapes_metro)
maxy = max(max(shp[0].bbox[1], shp[0].bbox[3]) for shp in shapes_metro)

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

parcours_date = ["2018","2019","2020","2021","2022","2023","2024","2025"]
for date in parcours_date:
    couleurs=generer_dico(L,date)
    texte(10, 10, date , couleur="black", taille=40)
    texte(140, 10, "cest chaud" , couleur="#FA0000", taille=20)
    texte(300, 10, "cest froid" , couleur="#00E1FA", taille=20)
    texte(440, 10, "cest chaud mais ca va" , couleur="#FA7100", taille=20)
    texte(740, 10, "cest froid  mais ca va" , couleur="#FFF069", taille=20)
    for shape_rec in shapes_metro:
        pts = shape_rec[0].points
        #print(pts)
        parts = list(shape_rec[0].parts) + [len(pts)]


        for i in range(len(parts) - 1):
            start = parts[i]
            end = parts[i + 1]
            segment = pts[start:end]

            poly = []
            for x, y in segment:
                X = (x - minx) * scale + offset_x
                Y = window_h - ((y - miny) * scale + offset_y)
                poly.append((X, Y))
            if shape_rec[1] in couleurs.keys():
                polygone(poly,remplissage=couleurs[shape_rec[1]]["couleur"])
            
            



    attente(1)
    efface_tout()
ferme_fenetre()
