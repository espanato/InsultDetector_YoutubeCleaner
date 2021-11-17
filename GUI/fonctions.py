from search_comments import *

def contient_espace(text):
    return " " in text

def reconnait_lien(text):
    """Fonction qui reconnait si text est un lien(ou une id) d'une vidéo ou d'une chaîne.
    Renvoie un tuple (id, type)"""
    longueur = len(text)
    if (longueur == 11) and not contient_espace(text):  # id d'une video fait 11 caractères
        print('video')
        return(text, 'video')
    elif (longueur == 24) and not contient_espace(text):  # id d'une chaîne fait 24 caractères
        print('chaine')
        return(text, 'channel')
    else:  # cas où l'utilisateur a rentré le lien complet
        try:  # on regarde si c'est au moins un lien valide
            if 'watch' in text:  # condition nécessaire pour qu'un lien soit celui d'une vidéo
                reconnait_lien(text.split('youtube.com/watch?v=')[1][0:11])
            else:
                reconnait_lien(text.split('youtube.com/channel/')[1][0:24])
        except:
            return (search_video_channel(text,type_search='video'), 'video')
