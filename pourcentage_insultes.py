from search_comments import *
from contient_insulte import *


def get_video_all_comments_list(video_id, nb=3):
    """OBJ: récupérer la liste des commentaires
    la liste : les valeurs sont les textes des commentaires"""
    commentaires_liste = []
    dico_comments = get_video_comments(video_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        commentaires_liste.append(comment)
    return commentaires_liste


def percent_insultes(video_id):
    """OBJ : récupérer le pourcentage de commentaires insultants
    et le nombre moyen d'insultes par message insultant"""
    l_comm = get_video_all_comments_list(video_id, 100)
    l_insultes = []
    n = 0
    for comm in l_comm:
        nb = nb_insultes(comm)[0]
        if nb >= 1:
            n = n + 1
            l_insultes.append(nb_insultes(comm)[1])
    return n/len(l_comm) * 100, l_insultes


print(percent_insultes("fglVkx5E29U"))
