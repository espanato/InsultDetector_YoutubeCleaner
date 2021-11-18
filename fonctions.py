from googleapiclient.discovery import build
KEY = 'AIzaSyAX7dBqLt4ihw9aNtkQZTAKw3mGs9hGRrQ'


def contient_espace(text):
    """Renvoie false s'il n'y a pas d'espace dans le texte"""
    return " " in text


def search_video_channel(word, type_search='video'):
    """renvoie la vidéo ou la chaîne youtube la plus adaptée à la recherche spécifiée dans word
    type_search = 'video' : recherche sur les vidéos
    type_search = 'channel' : recherche sur les chaînes"""
    youtube = build('youtube', "v3", developerKey=KEY)
    if type_search == 'video':
        request = youtube.search().list(part='snippet', type='video',
                                        maxResults=1, q=word).execute()
        if request['items'] != []:
            id_video = request['items'][0]['id']['videoId']
            return id_video
        else:
            return False

    elif type_search == 'channel':
        request = youtube.search().list(part='snippet', type='channel',
                                        maxResults=1, q=word).execute()
        if request['items'] != []:
            id_channel = request['items'][0]['id']['channelId']
            return id_channel
        else:
            return False
    else:
        return False


def reconnait_url(url):
    """Reconnait si url est un lien(ou une id) d'une vidéo ou d'une chaîne.
    Renvoie un tuple (id, type), ou False si le lien est de mauvais format"""
    longueur = len(url)
    if (longueur == 11) and not contient_espace(url):  # id d'une video fait 11 caractères
        return(url, 'video')
    elif (longueur == 24) and not contient_espace(url):  # id d'une chaîne fait 24 caractères
        return(url, 'channel')
    else:
        try:  # on regarde si c'est au moins un lien valide
            if 'watch' in url:  # condition nécessaire pour qu'un lien soit celui d'une vidéo
                reconnait_url(url.split('youtube.com/watch?v=')[1][0:11])
            else:
                reconnait_url(url.split('youtube.com/channel/')[1][0:24])
        except:
            return (False)


def traitement_entree(text, type_entree):
    """ OBJ: Traite les entrées
        RETURN : ID de la vidéo ou chaîne qui match en premier, False s'il n'y a pas de résultat"""
    if type_entree == 'url':
        return reconnait_url(text)
    elif type_entree == 'video':
        return search_video_channel(text, type_search='video')
    else:
        return search_video_channel(text, type_search='channel')


# def reconnait_lien(text):
#     """Fonction qui reconnait si text est un lien(ou une id) d'une vidéo ou d'une chaîne.
#     Renvoie un tuple (id, type)"""
#     longueur = len(text)
#     if longueur > 1:
#         if (longueur == 11) and not contient_espace(text):  # id d'une video fait 11 caractères
#             return(text, 'video')
#         elif (longueur == 24) and not contient_espace(text):  # id d'une chaîne fait 24 caractères
#             return(text, 'channel')
#         else:  # cas où l'utilisateur a rentré le lien complet
#             try:  # on regarde si c'est au moins un lien valide
#                 if 'watch' in text:  # condition nécessaire pour qu'un lien soit celui d'une vidéo
#                     reconnait_lien(text.split('youtube.com/watch?v=')[1][0:11])
#                 else:
#                     reconnait_lien(text.split('youtube.com/channel/')[1][0:24])
#             except:
#                 return (search_video_channel(text, type_search='video'))
