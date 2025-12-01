import json

def generer_liste():
    with open ("temperature-quotidienne-departementale.json") as fichier:
        liste=json.load(fichier)
        return liste

def generer_dico(lst):
    dictionnaire={}
    i=0
    for dico in lst:
        tmp={"nom":dico["departement"],"date":dico["date_obs"][0:4],"num_dep":dico["code_insee_departement"]}
        if dico["tmoy"]!=None:
            tmp["couleur"]=generer_couleur(dico["tmoy"])
            if tmp["date"]!="2025":
                print(dico["tmoy"],dico["departement"],tmp["couleur"],tmp["date"])
        else:
            tmp["couleur"]=None
        dictionnaire[str(i)]=tmp
        i+=1
    return dictionnaire

def generer_couleur(nb):
    if nb<=15 and nb>=12:
        return "yellow"   #jaune
    elif nb>=15 and nb<=20:
        return "orange"  #orange
    elif nb>20:
        return "red"  #rouge
    else:
        return "blue"  #bleu

L=generer_liste()
couleurs=generer_dico(L)
"""for elt in couleurs:
    if elt["couleur"]=="#00E1FA":
        print(elt[])"""

"""if nb<=15 and nb>=12:
        return "#FFF069"   #jaune
    elif nb>=15 and nb<=20:
        return "#FA7100"  #orange
    elif nb>20:
        return "#FA0000"  #rouge
    else:
        return "#00E1FA"""