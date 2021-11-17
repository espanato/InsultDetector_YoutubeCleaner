from search_comments import *
from contient_insulte import *


def get_all_list(video_id):
    """OBJ: récupérer la liste de tous les commentaires
    la liste : les valeurs sont les textes des commentaires"""
    commentaires_liste = []
    dico_comments = get_all(video_id)
    for text in dico_comments.values():
        commentaires_liste.append(text)
    return commentaires_liste

# print(get_all_list("vBFiBT2Z0EM"))


def percent_insultes(video_id):
    """OBJ : récupérer le pourcentage de commentaires insultants
    et la liste des insultes correspondantes dans chaque message"""
    l_comm = get_all_list(video_id)
    l_insultes = []
    n = 0
    for comm in l_comm:
        nb = nb_insultes(comm)[0]
        if nb >= 1:
            n = n + 1
            l_insultes.append(nb_insultes(comm)[1])
    return n/len(l_comm) * 100, l_insultes


# print(percent_insultes("vBFiBT2Z0EM"))
