from insultes import *
from search_comments import *


def nettoie_mot(mot):
    """enlève les ponctuations résiduelles collées aux mots dans le commentaire"""
    stop_caracteres = {" ","  ",'"',",","?","!",";","-","(",")",":"}
    newmot = mot
    if newmot[0] in stop_caracteres and len(mot)>1 :
        newmot = newmot[1:]
    if newmot[-1] in stop_caracteres and len(mot)>1 :
        newmot = newmot[:-1]
    return newmot


def fractionner_en_mots(texte):
    """OBJ : transformer un texte en la liste de ses mots"""""
    l = texte.split()
    return [nettoie_mot(m) for m in l]


# def nb_insultes(comment, liste_insultes):
#     """OBJ : compter le nombre d'insultes dans un commentaire (version naïve)"""
#     nb = 0
#     l = fractionner_en_mots(comment)
#     for mot in l:
#         if mot in liste_insultes:
#             nb = nb + 1
#     return nb


def nb_insultes(comment, precision=1):
    """OBJ : compter le nombre d'insultes dans un commentaire (version améliorée)"""
    nb = 0
    l_insultes = []
    l = fractionner_en_mots(comment)
    for mot in l:
        if est_insulte(mot.lower(), precision=precision):
            nb = nb + 1
            l_insultes.append(mot.lower())
    return nb, l_insultes

if __name__ == "main":
    #comment = "Sardoche joue avec sa copine on dirait vraiment qu'il est sous exta"
    #print(nb_insultes(comment))

    comm =  get_all_comments("zyFysSUQPxg")
    for key in comm :
        c = comm[key]
        nb, ins = nb_insultes(c)
        if nb >= 1 :
            print("commentaire :")
            print(c)
            print("insultes :")
            for w in ins :
                print(w)
