# OBJ : transformer un texte en la liste de ses mots

def fractionner_en_mots(texte):
    l = []
    mot = ""
    for char in texte:
        if char != ' ':
            mot = mot + char
        else:
            l.append(mot)
            mot = ""
    l.append(mot)
    return l


# OBJ : compter le nombre d'insultes dans un commentaire (version naïve)

def nb_insultes(comment, liste_insultes):
    nb = 0
    l = fractionner_en_mots(comment)
    for mot in l:
        if mot in liste_insultes:
            nb = nb + 1
    return nb


def levenshtein(s, t):
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


print(levenshtein('kittffazeddddfaefaqeen', 'sittifazefzaefzefezngdddd'))
