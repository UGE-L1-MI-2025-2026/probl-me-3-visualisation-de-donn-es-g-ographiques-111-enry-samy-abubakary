def repartir(a_diviser, nb_parts):
    quotient, reste = divmod(a_diviser, nb_parts)
    repartition = [quotient for _ in range(nb_parts)]
    for i in range(reste):
        repartition[i] += 1
    return repartition

def degrader(couleur_1,couleur_2,nb):
    liste= []
    for i in range(nb):
        ecart=couleur_2[i]-couleur_1[i]
        lst=repartir(ecart,nb)

