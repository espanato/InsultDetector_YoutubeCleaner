## YoutubeCleaner

YoutubeCleaner est un projet créé par des étudiants de CentraleSupélec dans le cadre des Coding Weeks 2021 – 2022 et dans le thème "Détecteur d'insultes".

## Membres

- BLONDEL Hector
- BUI Hugo
- BOHARD Charly
- CERVERA Romain
- ESPANA Tomas
- ROBY Edouard

## Packages nécessaires

tkinter
json
os
csv
codecs
pickle
time
click 
google-auth-oauthlib 
google-auth-httplib2 
google-api-python-client
bs4
requests
pyperclip
dash
nltk
sklearn

## Fonctionnement

Lancer le fichier main.py du dossier src.
La recherche de vidéos peut se faire par URL (url) ou par ID de vidéo (video).

## Usages

Ce projet s’adresse au grand public comme aux professionnels, par exemple :
► Pour de simples utilisateurs de Youtube, à des fins informatives
► Pour des Youtubeurs, afin de mieux connaître leur communauté
► Pour les entreprises désireuses de réaliser un partenariat avec un Youtubeur


## Statut du projet
Le projet est actuellement fonctionnel en tant que MVP (minimum viable product). Une amélioration possible consisterait en le développement de méthodes de machine learning afin d'améliorer la qualité de la détection d'insultes.

## Découpage du projet
Data            _Liste de commentaires pour le machine learning_

    |Commentaires insultants

        |... .txt

    |Commentaires neutres

        |... .txt

Doc         _Documentation_

    |conception.md

    |CW - YoutubeCleaner.pptx

Gui         _Images utilisées pour l'interface graphique_

    |images

        |gitlab-logo.png

        |logo.ico

        |logo.png

        |pc-logo.png

src         _Toues les modules utilisés_

    |channel_videos.py          _Ensemble de fonctions relatives à une chaîne_

    |contient_insultes.py       _Fonction qui permet de déterminer si un commentaire contient des insultes ou non_

    |credentials.py     _Contient la clé pour l'API_

    |Dash.py        _Permet de lancer une page dash pour afficher le graph_

    |fonctions.py           _ensemble de fonctions nécessaires pour la recherche dans l'interface graphique_

    |insultes.py

    |insultes.txt           _Liste de mots considérés comme des insultes_

    |liste_insulte.py

    |main.py      _Fichier permettant de lancer l'interface graphique du programme_

    |ml_comments_train_test.py

    |ml_comments.py

    |ml_set500kpy

    |most_insulted_video.py         _Fonction qui renvoie la vidéo ayant le plus de commentaires insultants parmi les vidéos populaires d'une chaîne_

    |non_insultes.txt           _Liste de mots devant être écartés de la détection d'insultes_

    |pourcentages_insultes.py       _Fonction qui renvoie la proportion de commentaires insultants_

    |search_comments.py         _Ensemble de fonctions utilisant l'API pour récuperer des infos sur des vidéos, chaînes ou commentaires_

    |Set Comments Insultants.py
    
    |setup.py
