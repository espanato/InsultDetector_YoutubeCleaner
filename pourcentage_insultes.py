from search_comments import *
from contient_insulte import *


def percent_insultes(video_id):
    """OBJ : récupérer le pourcentage de commentaires insultants
    et la liste des insultes correspondantes dans chaque message"""
    dico_comments = get_all(video_id)
    l_insultes = []
    n = 0
    for comm in dico_comments:
        nb = nb_insultes(dico_comments[comm])[0]
        if nb >= 1:
            n = n + 1
            l_insultes.append(nb_insultes(dico_comments[comm])[1])
    return n/len(dico_comments) * 100, l_insultes


print(percent_insultes("vBFiBT2Z0EM"))
