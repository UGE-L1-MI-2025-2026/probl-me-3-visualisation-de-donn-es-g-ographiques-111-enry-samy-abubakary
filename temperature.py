import json

def generer_liste():
    with open ("temperature-quotidienne-departementale.json") as fichier:
        liste=json.load(fichier)
        return liste

def generer_couleur(lst):
    liste=[]
    for dico in lst:
        tmp={"nom":dico['departement'],"date":dico["date_obs"],"num":dico["code_insee_departement"]}
        if dico["tmoy"]!=None:
            if dico['tmoy']<=15 and dico['tmoy']>=10:
                tmp["couleur"]="#FFF069"#jaune
            elif dico['tmoy']>=15 and dico['tmoy']<=20:
                tmp["couleur"]="#FA7100"#orange
            elif dico['tmoy']>20:
                tmp["couleur"]="#FA0000"#rouge
            else:
                tmp["couleur"]="#00E1FA"#bleu
        else:
            tmp["couleur"]=None
        
        liste.append(tmp)
    return liste

L=generer_liste()
couleurs=generer_couleur(L)
#print(couleurs)