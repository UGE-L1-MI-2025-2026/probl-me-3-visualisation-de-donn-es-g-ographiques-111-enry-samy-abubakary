import json

def generer_liste():
    with open ("temperature-quotidienne-departementale.json") as fichier:
        liste=json.load(fichier)
        return liste

def generer_dico(lst,annee):
    dictionnaire={}
    i=0
    for dico in lst:
        tmp={"nom":dico["departement"],"date":dico["date_obs"][0:4],"num_dep":dico["code_insee_departement"]}
        if tmp["date"]==annee:
            if dico["tmoy"]==None:
                tmp["couleur"]=None
            else:
                tmp["couleur"]=generer_couleur(dico["tmoy"])
            if tmp["date"]==annee:
                #print(dico["tmoy"],dico["departement"],tmp["couleur"],tmp["date"])
                dictionnaire[str(i)]=tmp
                i+=1
    return dictionnaire

def generer_couleur(nb):
    if nb<=15 and nb>=12:
        return "#FFF069"   #jaune
    elif nb>=15 and nb<=20:
        return "#FA7100"  #orange
    elif nb>20:
        return "#FA0000"  #rouge
    else:
        return "#00E1FA"  #bleu

