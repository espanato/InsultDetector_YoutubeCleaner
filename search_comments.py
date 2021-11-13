import json
import os
from bs4 import BeautifulSoup
import requests
import csv
from api import get_authenticated_service


# OBJ: renvoie sous forme de dico les commentaires d'une vidéo en particulier
# le dico: les clés sont les pseudos des utilisateurs, les valeurs sont leurs commentaires

"""
def get_video_comments(service, **kwargs):
    dico = {}

    # request google api
    results = service.commentThreads().list(**kwargs).execute()

    while results:
        # keep comments and authors
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            dico[author] = comment

            # Check if another page exists
            if 'nextPageToken' in results:
                kwargs['pageToken'] = results['nextPageToken']
                results = service.commentThreads().list(**kwargs).execute()
            else:
                break
        return dico"""


# service = get_authenticated_service("credentials.json")
# video_id = input("Quel est l'id de la video")
# result = get_video_comments(
#    service,  part='snippet', videoId=video_id, textFormat='plainText')
# print(result)
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


print(get_video_comments('DHiTuMboqVI'))
