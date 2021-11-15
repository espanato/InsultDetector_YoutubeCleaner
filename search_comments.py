import json
import os
from bs4 import BeautifulSoup
import requests
import csv

# chercher les commentaires d'une video avec toutes les infos de yt


def get_video_comments(video_id, nb=3):
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


# chercher les réponse d'un commentaire avec toutes les infos de yt
def get_video_replies(parent_id, nb=3):
    requete = requests.get("https://youtube.googleapis.com/youtube/v3/comments?part=snippet&parentId=" +
                           parent_id+"&textFormat=plainText&key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


# print(get_video_replies('UgyXSKR2TSiAgzebL3R4AaABAg'))


# OBJ: renvoie sous forme de dico les commentaires d'une vidéo
# le dico: les clés sont les pseudos des utilisateurs, les valeurs sont les textes

def get_video_comments_user_name(video_id, nb=3):
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        commentaires_dico[author] = comment
    return commentaires_dico


# print(get_video_comments_info('vBFiBT2Z0EM', 3))


# OBJ: idem qu'avant mais cette fois
# le dico: les clés sont les id des commentaires, les valeurs sont les textes

def get_video_comments_msg_id(video_id, nb=3):
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        identifiant = item['id']
        commentaires_dico[identifiant] = item
    return commentaires_dico


# print(get_video_comments_msg_id('vBFiBT2Z0EM'))


# OBJ: filtrer les commentaires qui possèdent les mots d'une liste de mots

def get_video_comments_words(video_id, liste_de_mots, nb=3):
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults="+str(nb))
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


# OBJ: renvoie sous forme de dico les réponses d'un commentaire
# le dico: les clés sont les pseudos des utilisateurs, les valeurs sont les textes

def get_video_replies_dico(parent_id, nb=3):
    reponses_dico = {}
    dico_comments = get_video_replies(parent_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['textDisplay']
        id = item['id']
        reponses_dico[id] = comment
    return reponses_dico


# print(get_video_replies_dico('UgyXSKR2TSiAgzebL3R4AaABAg'))


# OBJ: filtrer les réponses qui possèdent les mots d'une liste de mots

def get_video_replies_words(parent_id, liste_de_mots, nb=3):
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/comments?part=snippet&parentId=" +
        parent_id+"&textFormat=plainText&key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs"+"&maxResults="+str(nb))
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


# print(get_video_replies_words('UgyXSKR2TSiAgzebL3R4AaABAg',
#      ['bac+3', 'bac + 3', 'imbecile', 'imbécile']))
