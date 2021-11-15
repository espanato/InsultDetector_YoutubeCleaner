from liste_insulte import insultes,non_insultes



def distance(s, t):
    """
    renvoie la distance d'édition entre les mots s et t : 
    la distance minimale pour passer du mot s au mot t avec des modifications élémentaires
    """
    if s == t:
        return 0
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    v0 = list(range(len(t) + 1))
    v1 = [None] * (len(t) + 1)

    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]



def est_insulte(mot,precision=1):
    """
    renvoie si le mot donné en paramètre est une insulte avec la tolérance précision
    """
    for ins in insultes :
        if distance(mot,ins) <= 1 :
            return not(mot in non_insultes)
    return False


if __name__ == "main":
    print(distance("caaevaevlt","ceavnljabvljahello"))
    est_insulte("salope")








"""
arbre = {}
def ajoute_mot(mot,arbre):
    if len(mot) == 1 :
        arbre[mot[0]] = True
    else :
        ajoute_mot(mot[0:],arbre[mot[0]])

ajoute_mot("connard",arbre)
"""

        