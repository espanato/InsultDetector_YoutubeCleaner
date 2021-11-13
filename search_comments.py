import json
import os
from bs4 import BeautifulSoup
import requests
import csv


# OBJ: renvoie sous forme de dico les commentaires d'une vidéo en particulier
# le dico: les clés sont les pseudos des utilisateurs, les valeurs sont leurs commentaires

def get_video_comments(video_id, nb=3):
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId="+video_id+"&textFormat=plainText"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


def get_video_comments_info(video_id, nb=3):
    commentaires_dico = {}
    dico_comments = get_video_comments(video_id, nb)
    for item in dico_comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        commentaires_dico[author] = comment
    return commentaires_dico


print(get_video_comments_info('vBFiBT2Z0EM', 3))
