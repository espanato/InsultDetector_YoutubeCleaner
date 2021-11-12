def get_video_commetns(service, **kwargs):
    dico = {}

    # request google api
    results = service.commentThreads().list(**kwargs).execute()

    while results:
        # keep comments and authors
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayname']
            # la cle est le pseudo de l'auteur et la cle son commentaire
            dico[author] = comment

            # Check if another page exists
            if 'nextPageToken' in results:
                kwargs['pageToken'] = results['nextPageToken']
                results = service.commentThreads().list(**kwargs).execute()
            else:
                break
        return dico


service = get_authenticated_service("creds.json")
video_id = input("Quel est l'id de la video")
result = get_video_comments(service, part='snippet',
                            videoId=video_id, textFormat='plaintText')
print(result)
