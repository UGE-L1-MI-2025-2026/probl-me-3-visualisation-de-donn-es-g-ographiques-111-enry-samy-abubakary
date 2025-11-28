import json

def generer_liste():
    with open ("temperature-quotidienne-departementale.json") as fichier:
        liste=json.load(fichier)
        return liste

def generer_dico(lst):
    dictionnaire={}
    for dico in lst:
        tmp={"nom":dico["departement"],"date":dico["date_obs"][0:4]}
        if dico["tmoy"]!=None:
            tmp["couleur"]=generer_couleur(dico["tmoy"])
        else:
            tmp["couleur"]=None
        if dico["code_insee_departement"] in ["01","02","03","04","05","06","07","08","09"]:
            dictionnaire[dico["code_insee_departement"][-1]]=tmp
        else:
            dictionnaire[dico["code_insee_departement"]]=tmp
    return dictionnaire

def generer_couleur(nb):
    if nb<=15 and nb>=10:
        return "#FFF069"   #jaune
    elif nb>=15 and nb<=20:
        return "#FA7100"  #orange
    elif nb>20:
        return "#FA0000"  #rouge
    else:
        return "#00E1FA"  #bleu

L=generer_liste()
couleurs=generer_dico(L)
print(couleurs["1"])
