from search_comments import *
from contient_insulte import *
from langdetect import detect


def percent_insultes(video_id):
    """OBJ : récupérer le pourcentage de commentaires insultants
    et la liste des insultes correspondantes dans chaque message"""
    dico_comments = get_all(video_id)
    l_insultes = []
    n = 0
    for comm in dico_comments:
        try:
            lang = detect(dico_comments[comm])
        except:
            lang = "error"
        if lang == 'fr':
            nb = nb_insultes(dico_comments[comm])[0]
            if nb >= 1:
                n = n + 1
                l_insultes.append(nb_insultes(dico_comments[comm])[1])
        elif lang == 'en':
            pass
        else:  # par défaut on dit que c'est en français
            nb = nb_insultes(dico_comments[comm])[0]
            if nb >= 1:
                n = n + 1
                l_insultes.append(nb_insultes(dico_comments[comm])[1])

    return n/len(dico_comments) * 100, l_insultes


print(percent_insultes("niCMpOkMcWU"))
