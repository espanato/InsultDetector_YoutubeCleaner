import json
import os
from bs4 import BeautifulSoup
import requests
import csv
from googleapiclient.discovery import build
from requests.api import get

# chercher les commentaires d'une video avec toutes les infos de yt
KEY = "AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs"


def get_video_comments(video_id, nb=3):
    """Renvoie un dictionnaire contenant nb commentaires de la video"""
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key="+KEY+"&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


# print((get_video_comments('6janW0h3cZY', 100))


def get_video_replies(parent_id, nb=3):
    """chercher les réponse d'un commentaire avec toutes les infos de yt"""
    requete = requests.get("https://youtube.googleapis.com/youtube/v3/comments?part=snippet&parentId=" +
                           parent_id+"&textFormat=plainText&key="+KEY+""+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


# print(get_video_replies('UgyXSKR2TSiAgzebL3R4AaABAg'))


def get_video_comments_user_name(video_id, nb=3):
    """ OBJ: renvoie sous forme de dico les commentaires d'une vidéo
le dico: les clés sont les pseudos des utilisateurs, les valeurs sont les textes"""
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)

    for item in dico_comments['items']:
        user_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        commentaires_dico[user_name] = comment

    return commentaires_dico


# print(len(get_video_comments_user_name('vBFiBT2Z0EM', 3)))


def get_video_comments_msg_id(video_id, nb=3):
    """OBJ: idem qu'avant mais cette fois
 le dico: les clés sont les id des commentaires, les valeurs sont les textes"""
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        identifiant = item['id']
        commentaires_dico[identifiant] = comment
    return commentaires_dico


# print(get_video_comments_msg_id('vBFiBT2Z0EM'))


def get_video_comments_words(video_id, liste_de_mots, nb=3):
    """Filtre les commentaires qui possèdent les mots d'une liste de mots"""
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key="+KEY+"&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))

    for mot in liste_de_mots:
        commentaires_dico[mot] = set()

    # la liste des commentaires pour chaque mot, les mots sont les clés de commentaires_dico
    for item in dico['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

        for mot in liste_de_mots:
            if mot in comment:
                commentaires_dico[mot].add(comment)

    # on rajoute une clé 'tout' dont la valeur est l'ensemble des tweets qui contienne tous les mots
    if len(liste_de_mots) > 1:
        commentaires_dico['#tout'] = commentaires_dico[liste_de_mots[0]]
        for i in range(1, len(liste_de_mots)):
            commentaires_dico['#tout'] = commentaires_dico['#tout'].intersection(
                commentaires_dico[liste_de_mots[i]])

    return commentaires_dico


# print(get_video_comments_words(
#    'vBFiBT2Z0EM', ["joue a", "joue", "qu'il", "qu"]))


def get_video_replies_dico(parent_id, nb=3):
    """OBJ: renvoie sous forme de dico les réponses d'un commentaire
le dico: les clés sont les pseudos des utilisateurs, les valeurs sont les textes"""
    reponses_dico = {}
    dico_comments = get_video_replies(parent_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['textDisplay']
        id = item['id']
        reponses_dico[id] = comment
    return reponses_dico


# print(get_video_replies_dico('UgyXSKR2TSiAgzebL3R4AaABAg'))


def get_video_replies_words(parent_id, liste_de_mots, nb=3):
    """OBJ: filtrer les réponses qui possèdent les mots d'une liste de mots"""
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/comments?part=snippet&parentId=" +
        parent_id+"&textFormat=plainText&key="+KEY+""+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))

    for mot in liste_de_mots:
        commentaires_dico[mot] = set()

    # la liste des commentaires pour chaque mot, les mots sont les clés de commentaires_dico
    for item in dico['items']:
        comment = item['snippet']['textDisplay']

        for mot in liste_de_mots:
            if mot in comment:
                commentaires_dico[mot].add(comment)

    # on rajoute une clé 'tout' dont la valeur est l'ensemble des tweets qui contienne tous les mots
    if len(liste_de_mots) > 1:
        commentaires_dico['#tout'] = commentaires_dico[liste_de_mots[0]]
        for i in range(1, len(liste_de_mots)):
            commentaires_dico['#tout'] = commentaires_dico['#tout'].intersection(
                commentaires_dico[liste_de_mots[i]])

    return commentaires_dico


def get_video_statistics(video_id):
    """ renvoie views, likes, dislikes pour une vidéo donnée"""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = build('youtube', "v3", developerKey=KEY)
    request = youtube.videos().list(part="statistics", id=video_id).execute()
    views = int(request['items'][0]['statistics']['viewCount'])
    likes = int(request['items'][0]['statistics']['likeCount'])
    dislikes = int(request['items'][0]['statistics']['dislikeCount'])
    return views, likes, dislikes


# print(get_video_replies_words('UgyXSKR2TSiAgzebL3R4AaABAg',
#      ['bac+3', 'bac + 3', 'imbecile', 'imbécile']))


def get_comments_page_token(video_id, page_token=''):
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key="+KEY+"&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults=100"+"&pageToken="+page_token)
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico_comments = json.loads(str(soup))
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        identifiant = item['id']
        commentaires_dico[identifiant] = comment
    return commentaires_dico


def get_video_comments_page_token(video_id, page_token=''):
    """Renvoie un dictionnaire contenant nb commentaires de la video"""
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key="+KEY+"&part=snippet&videoId="+video_id+"&textFormat=plainText&maxResults=100"+"&pageToken="+page_token)
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


def get_all_comments(video_id):
    dico = get_video_comments(video_id, 100)
    commentaires_dico = get_video_comments_msg_id(
        video_id, 100)
    while 'nextPageToken' in dico:
        page_token = dico['nextPageToken']
        new_dico = get_comments_page_token(video_id, page_token)
        commentaires_dico.update(new_dico)
        dico = get_video_comments_page_token(video_id, page_token)

    return commentaires_dico


# print(get_all_comments('DHiTuMboqVI'))
# print(get_all_comments('DHiTuMboqVI'))
# print(len(get_all_comments('__HigGObD8U')))

def get_video_replies_page_token(parent_id, page_token):
    """chercher les réponse d'un commentaire avec toutes les infos de yt"""
    requete = requests.get("https://youtube.googleapis.com/youtube/v3/comments?part=snippet&parentId=" +
                           parent_id+"&textFormat=plainText&key="+KEY+""+"&maxResults=100&pageToken="+page_token)
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


def get_video_replies_dico_page_token(parent_id, page_token):
    """OBJ: renvoie sous forme de dico les réponses d'un commentaire
le dico: les clés sont les pseudos des utilisateurs, les valeurs sont les textes"""
    reponses_dico = {}
    dico_comments = get_video_replies_page_token(parent_id, page_token)
    for item in dico_comments['items']:
        comment = item['snippet']['textDisplay']
        id = item['id']
        reponses_dico[id] = comment
    return reponses_dico


def get_all_replies(parent_id):
    dico = get_video_replies(parent_id, 100)
    commentaires_dico = get_video_replies_dico(parent_id, 100)
    while 'nextPageToken' in dico:
        page_token = dico['nextPageToken']
        new_dico = get_video_replies_dico_page_token(video_id, page_token)
        commentaires_dico.update(new_dico)
        dico = get_video_replies_page_token(video_id, page_token)

    return commentaires_dico


def get_all(video_id):
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, 100)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        identifiant = item['id']
        commentaires_dico[identifiant] = comment
        if item['snippet']['totalReplyCount'] > 0:
            dico_replies = get_all_replies(item['id'])
            commentaires_dico.update(dico_replies)

    while 'nextPageToken' in dico_comments:
        page_token = dico_comments['nextPageToken']
        dico_comments = get_video_comments_page_token(video_id, page_token)
        for item in dico_comments['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            identifiant = item['id']
            commentaires_dico[identifiant] = comment
            if item['snippet']['totalReplyCount'] > 0:
                dico_replies = get_all_replies(item['id'])
                commentaires_dico.update(dico_replies)
    return commentaires_dico


# print(len(get_all('th5_9woFJmk')))


def collect_comments_and_replies(video_id, nb):
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        identifiant = item['id']
        commentaires_dico[identifiant] = comment
        if item['snippet']['totalReplyCount'] > 0:
            dico_replies = get_video_replies_dico(item['id'], 100)
            commentaires_dico.update(dico_replies)

    return commentaires_dico


#print(collect_comments_and_replies('vBFiBT2Z0EM', 5))


def dico_en_3(id1, id2, id3, nb):
    return collect_comments_and_replies(id1, nb), collect_comments_and_replies(id2, nb), collect_comments_and_replies(id3, nb)


# print(dico_en_3('vBFiBT2Z0EM', 'vBFiBT2Z0EM', 'vBFiBT2Z0EM', 5))
