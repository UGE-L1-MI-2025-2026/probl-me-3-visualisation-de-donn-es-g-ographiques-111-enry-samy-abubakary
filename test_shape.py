import shapefile
from fltk import *
sf = shapefile.Reader("departements-20180101") #ouverture du fichier shapefile
sf.records()# visualisation de toutes les entrées du fichier


france=[]
for i in range(len(sf.records())):    
    e = sf.shape(i).points
    
    for j in range(len(e)):

        x = e[j][0] *20
        y = e[j][1] *20
        z=(x,y)
        france.append(z)
    


cree_fenetre(1200, 1200)

polygone(france)

attend_ev()
ferme_fenetre()
