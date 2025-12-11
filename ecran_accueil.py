from fltk import *

def ecran_accueil():
    x1,y1,x2,y2=400,350,800,450
    x,y=425,385
    texte(150,50,chaine='Quelles donnees voulez vous afficher ?',taille=40)
    rectangle(x1,y1,x2,y2,remplissage="#C72300")
    texte(x,y,taille=24,chaine="Temperature maximale")
    rectangle(x1,y1+150,x2,y2+150,remplissage="#FF6A00")
    texte(x,y+150,taille=24,chaine="Temperature moyenne")
    rectangle(x1,y1+300,x2,y2+300,remplissage="#FFEE00")
    texte(x,y+300,taille=24,chaine="Temperature minimale")
    mise_a_jour()

def detecter_mode(x,y):
    x1,y1,x2,y2=400,350,800,450
    
    if x>=x1 and x<=x2 and y>=y1 and y<=y2:
        return 'tmax'
    elif x>=x1 and x<=x2 and y>=y1+150 and y<=y2+150:
        return 'tmoy'
    elif x>=x1 and x<=x2 and y>=y1+300 and y<=y2+300:
        return 'tmin'
    else:
        return None
