from channel_videos import *
from pourcentage_insultes import *


def most_insulted_video(channel_id, nb=3):
    """Renvoie la vidéo contenant le plus d'insultes parmi les nb plus populaires d'une chaine"""
    dico = get_channel_videos(channel_id, nb=3)
    biggest_percent = 0
    most_insulted_video_Id = ""
    # d = {}
    for i in range(len(dico['items'])):
        video_id = dico['items'][i]['id']['videoId']
        percent, l_insultes = percent_insultes(video_id)
        # d[video_id] = {"percent": percent, "insultes": l_insultes}
        if percent > biggest_percent:
            biggest_percent = percent
            most_insulted_video_Id = video_id
    return most_insulted_video_Id, biggest_percent


# print(most_insulted_video("UCgkhWgBGRp0sdFy2MHDWfSg", 5))
