import json
import os
from bs4 import BeautifulSoup
import requests
import csv

# chercher les commentaires d'une video avec toutes les infos de yt


def commentformat(item):
    # renvoie un dictionnaire de la forme {id,text,author,likeCount,replyCount}
    identificator = item['id']
    text = item['snippet']['topLevelComment']['snippet']['textDisplay']
    author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
    likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']
    replyCount = item['snippet']['totalReplyCount']
    return {'id': identificator, 'text': text, 'author': author, 'likeCount': likeCount, 'replyCount': replyCount}


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

        comment_words = list(m)
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


