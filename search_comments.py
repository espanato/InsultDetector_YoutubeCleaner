import json
import os
from bs4 import BeautifulSoup
import requests
import csv

# OBJ: renvoie sous forme de dico les commentaires d'une vidéo en particulier
# le dico: les clés sont les pseudos des utilisateurs, les valeurs sont leurs commentaires


def get_video_comments(video_id):
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId=DHiTuMboqVI&textFormat=plainText")
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))

    for item in dico['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        commentaires_dico[author] = comment
    return commentaires_dico


# print(get_video_comments('DHiTuMboqVI'))


# OBJ: filtrer les commentaires qui possèdent une liste de mots
# pour une vidéo, on filtre les commentaires qui incluent les mots dans la liste en argument

def get_video_comments_words(video_id, liste_de_mots):
    commentaires_dico = {}
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId=DHiTuMboqVI&textFormat=plainText")
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))

    # la liste des commentaires pour chaque mot, les mots sont les clés de commentaires_dico
    for item in dico['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        print(type(comment))
        print(comment)

        for mot in liste_de_mots:
            commentaires_dico[mot] = set()
            if mot in comment:
                commentaires_dico[mot].add(comment)

    # on rajoute une clé 'tout' dont la valeur est l'ensemble des tweets qui contienne tous les mots
    if len(liste_de_mots) > 1:
        commentaires_dico['#tout'] = commentaires_dico[liste_de_mots[0]]
        for i in range(1, len(liste_de_mots)):
            commentaires_dico['#tout'] = commentaires_dico['#tout'].intersection(
                commentaires_dico[liste_de_mots[i]])

    return commentaires_dico


print(get_video_comments_words('DHiTuMboqVI', ["trouver"]))
