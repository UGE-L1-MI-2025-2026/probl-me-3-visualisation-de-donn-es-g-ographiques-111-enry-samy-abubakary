
import shapefile
from fltk import *

from conversion import conv  
from temperature import *
from ecran_accueil import *

sf = shapefile.Reader("departements-20180101")

L=generer_liste()
shapes_metro = []
for shapeRec, record in zip(sf.shapes(), sf.records()):
    dep_code = str(record[0])  # ex: "75", "29", "974"
    if not dep_code.startswith(("97", "98")):  
        shapes_metro.append((shapeRec,record[1]))

minx = min(min(shp[0].bbox[0], shp[0].bbox[2]) for shp in shapes_metro)
miny = min(min(shp[0].bbox[1], shp[0].bbox[3]) for shp in shapes_metro)
maxx = max(max(shp[0].bbox[0], shp[0].bbox[2]) for shp in shapes_metro)
maxy = max(max(shp[0].bbox[1], shp[0].bbox[3]) for shp in shapes_metro)

# On convertit min/max pour Mercator
minX, minY = conv(minx, miny)
maxX, maxY = conv(maxx, maxy)

width = maxX - minX
height = maxY - minY

window_w = 1200
window_h = 1200
cree_fenetre(window_w, window_h)

scale = min((window_w * 0.8) / width, (window_h * 0.8) / height)

scaled_w = width * scale
scaled_h = height * scale
offset_x = (window_w - scaled_w) / 2
offset_y = (window_h - scaled_h) / 2


zoom = 1.0
decalage_x = 0
decalage_y = 0
pas_decalage = 40

parcours_date = ["2018","2019","2020","2021","2022","2023","2024","2025"]

def dessiner_france(couleurs):
    for shape_rec in shapes_metro:
        pts = shape_rec[0].points
        parts = list(shape_rec[0].parts) + [len(pts)]

        for i in range(len(parts) - 1):
            start = parts[i]
            end = parts[i + 1]
            segment = pts[start:end]

            poly = []
            for x, y in segment:
                # Conversion en  Mercator
                Xm, Ym = conv(x, y)
                
                X = (Xm - minX) * scale * zoom + offset_x + decalage_x
                Y = window_h - ((Ym - minY) * scale * zoom + offset_y + decalage_y)
                poly.append((X, Y))

            if shape_rec[1] in couleurs.keys():
                polygone(poly, remplissage=couleurs[shape_rec[1]]["couleur"])
            else:
                polygone(poly)

def afficher_txt(date,mode):
    texte(10, 10, date , couleur="black", taille=40)
    if mode =='tmax':
        texte(140, 10, "Très chaud" , couleur="#FA0000", taille=20)
        texte(300, 10, "Moyen" , couleur="#00E1FA", taille=20)
        texte(440, 10, "Chaud" , couleur="#FA7100", taille=20)
        texte(550, 10, "Moyen-chaud" , couleur="#FFF069", taille=20)
    if mode =='tmoy':
        texte(140, 10, "Moyenne haute" , couleur="#FA0000", taille=20)
        texte(350, 10, "Moyenne basse" , couleur="#00E1FA", taille=20)
        texte(600, 10, "Moyen-haut" , couleur="#FA7100", taille=20)
        texte(780, 10, "Moyen-bas" , couleur="#FFF069", taille=20)    
    if mode =='tmin':
        texte(140, 10, "Moyen" , couleur="#FA0000", taille=20)
        texte(300, 10, "Très froid" , couleur="#00E1FA", taille=20)
        texte(560, 10, "Moyen-froid" , couleur="#FA7100", taille=20)
        texte(760, 10, "Froid" , couleur="#FFF069", taille=20)  

def appels(date,mode):
    couleurs=generer_dico(L,date,mode)
    afficher_txt(date,mode)
    dessiner_france(couleurs)

def parcours():
    global zoom, decalage_x, decalage_y

    mode=accueil()
    i=0
    date=parcours_date[i]
    appels(date,mode)

    while True:
        ev = attend_ev()
        tev = type_ev(ev)

        if tev=='Touche':
            t = touche(ev)

            if t=='Right':
                i = (i + 1) % len(parcours_date)
                date=parcours_date[i]
                efface_tout()

            if t=='Left':
                i = (i - 1) % len(parcours_date)
                date=parcours_date[i]
                efface_tout()

            
            if t == 'g':
                zoom *= 1.2
                efface_tout()

            if t == 'h':
                zoom /= 1.2
                efface_tout()

            
            if t == 'j':   
                decalage_x += pas_decalage
                efface_tout()

            if t == 'k':   
                decalage_x -= pas_decalage
                efface_tout()

            if t == 'i':   
                decalage_y += pas_decalage
                efface_tout()

            if t == 'n':   
                decalage_y -= pas_decalage
                efface_tout()

        elif tev=='Quitte':
            break

        appels(date,mode)

    ferme_fenetre()

def accueil():
    ecran_accueil()
    while True:
        ev = attend_ev()
        tev = type_ev(ev)

        if tev == "ClicGauche":
            x,y=abscisse(ev),ordonnee(ev)
            if detecter_mode(x,y)!=None:
                efface_tout()
                return detecter_mode(x,y)

        elif tev=="Quitte":
            ferme_fenetre()
            break

parcours()

