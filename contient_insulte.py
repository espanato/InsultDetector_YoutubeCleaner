from insultes import *


def fractionner_en_mots(texte):
    """OBJ : transformer un texte en la liste de ses mots"""""
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
