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
                dictionnaire[dico["departement"]]=tmp
                i+=1
    return dictionnaire

def generer_couleur(nb):
    if nb<=11 and nb>=8:
        return "#FFF069"   #jaune
    elif nb>=12 and nb<=15:
        return "#FA7100"  #orange
    elif nb>16:
        return "#FA0000"  #rouge
    else:
        return "#00E1FA"  #bleu

dico=generer_dico(generer_liste(),"2025")
print(dico)