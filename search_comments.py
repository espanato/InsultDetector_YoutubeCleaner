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
        "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs&part=snippet&videoId="+video_id+"&textFormat=plainText")
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))

    for item in dico['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        commentaires_dico[author] = comment
    return commentaires_dico


print(get_video_comments('DHiTuMboqVI'))
