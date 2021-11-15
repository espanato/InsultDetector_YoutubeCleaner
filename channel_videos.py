import json
import os
from bs4 import BeautifulSoup
import requests
import csv
from search_comments import get_video_statistics

# chercher les commentaires d'une video avec toutes les infos de yt
KEY = "AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs"


# def get_video_viewCount(video_id, nb=1):
#     """Renvoie le nombre de vus d'une vidéo"""
#     requete = requests.get("https://youtube.googleapis.com/youtube/v3/videos?key="+KEY+"&part=statistics&id=" + video_id
#                            + "&textFormat=plainText&order=viewCount&type=video"+"&maxResults="+str(nb))
#     page = requete.content
#     soup = BeautifulSoup(page, features='html.parser')
#     dico = json.loads(str(soup))
#     print(dico)
#     stats = dico['items']['statistics']
#     return({dico['items']['id']: [stats['viewCount', stats['likeCount'], stats['dislikeCount']]]})


def get_channel_videos(channel_id, nb=2):
    """Renvoie un dico contenant les vidéos d'une chaîne"""
    requete = requests.get(
        "https://youtube.googleapis.com/youtube/v3/search?key="+KEY+"&part=snippet&channelId="+channel_id+"&textFormat=plainText&order=viewCount&type=video"+"&maxResults="+str(nb))
    page = requete.content
    soup = BeautifulSoup(page, features='html.parser')
    dico = json.loads(str(soup))
    return(dico)


def presentation_caracteristiques_chaine(channel_id, nb=3):
    """Renvoie un dictionnaire de la forme {'video_id' :  {'title' : ..., 'viewCount' : ..., 'likeCount' : ..., 'dislikeCount' : ...}"""
    dico_videos = get_channel_videos(channel_id, nb)
    D = {}
    for video in dico_videos['items']:
        video_id = video['id']['videoId']
        view, like, dislike = get_video_statistics(video_id)
        D[video_id] = {'title': video['snippet']['title'],
                       'viewCount': view,
                       'likeCount': like,
                       'dislikeCount': dislike}
    return(D)


# print(get_channel_videos("UCUo1RqYV8tGjV38sQ8S5p9A"))
# print(get_video_viewCount("Q0pBzowOKU4"))
# print(presentation_caracteristiques_chaine("UCXwDLMDV86ldKoFVc_g8P0g"))
