from liste_insulte import insultes, non_insultes


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


def est_insulte(mot, precision=1):
    for ins in insultes:
        if distance(mot.lower(), ins) <= 1:
            return not(mot.lower() in non_insultes)
    return False
