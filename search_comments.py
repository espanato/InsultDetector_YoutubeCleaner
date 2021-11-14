import json
import os
from bs4 import BeautifulSoup
import requests
import csv

# OBJ: renvoie sous forme de dico les commentaires d'une vidéo en particulier
# le dico: les clés sont les pseudos des utilisateurs, les valeurs sont leurs commentaires


def nettoyer_mot(mot):
    if mot[-1] == ".":
        newmot = mot[:-1]
    else :
        newmot = mot
    return newmot

def get_video_comments(video_id, nb=3):
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)

def commentformat(item):
    #renvoie un dictionnaire de la forme {id,text,author,likeCount,replyCount}
    identificator = item['id']
    text = item['snippet']['topLevelComment']['snippet']['textDisplay']
    author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
    likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']
    replyCount = item['snippet']['totalReplyCount']
    return  {'id':identificator,'text':text,'author':author,'likeCount':likeCount,'replyCount':replyCount}


def get_video_comments_info(video_id, nb=3):
    #Renvoie une dictionnaire de commentaires
    #chaque clé est l'identifiant d'un commentaire. Le commentaire est représenté par le dico {id,text,author,likeCount,replyCount}

    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)

    for item in dico_comments['items']:
        identificator = item['id']
        commentaires_dico[identificator] = commentformat(item)

    return commentaires_dico


#print(get_video_comments_info('vBFiBT2Z0EM', 3))


# OBJ: filtrer les commentaires qui possèdent une liste de mots
# pour une vidéo, on filtre les commentaires qui incluent les mots dans la liste en argument

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

        comment_words = list(map(nettoyer_mot,comment.split()))
        for mot in liste_de_mots:
            if mot in comment_words:
                commentaires_dico[mot].add(commentformat(item))

    # on rajoute une clé 'tout' dont la valeur est l'ensemble des tweets qui contienne tous les mots
    if len(liste_de_mots) > 1:
        commentaires_dico['#tout'] = commentaires_dico[liste_de_mots[0]]
        for i in range(1, len(liste_de_mots)):
            commentaires_dico['#tout'] = commentaires_dico['#tout'].intersection(
                commentaires_dico[liste_de_mots[i]])

    return commentaires_dico

#print(get_video_comments_words('vBFiBT2Z0EM', ["joue a", "joue", "qu'il", "qu"]))
dico = get_video_comments_words("e424Yz7-8Oo",["water"],nb=6)


