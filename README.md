## YoutubeCleaner

YoutubeCleaner is a project created by CentraleSupélec students in the framework of the Coding Weeks 2021 - 2022 and in the theme "Insult detector".

## Members

- BLONDEL Hector
- BUI Hugo
- BOHARD Charly
- CERVERA Romain
- ESPANA Tomas
- ROBY Edouard

## Libraries

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

## How does it work.

Lancer le fichier main.py du dossier src.
La recherche de vidéos peut se faire par URL (url) ou par ID de vidéo (video). ATTENTION : une demande de credentials (clés d'API) doit être faite avant de pouvoir utiliser le produit (il faut alors créer un fichier credentials dans src et les mettre dedans).

## Usages

Ce projet s’adresse au grand public comme aux professionnels, par exemple :
► Pour de simples utilisateurs de Youtube, à des fins informatives
► Pour des Youtubeurs, afin de mieux connaître leur communauté
► Pour les entreprises désireuses de réaliser un partenariat avec un Youtubeur

## Statut du projet
Le projet est actuellement fonctionnel en tant que MVP (minimum viable product). Une amélioration possible consisterait en le développement de méthodes de machine learning afin d'améliorer la qualité de la détection d'insultes.

## Découpage du projet
**Data** ### _Liste de commentaires pour le machine learning_

___|****Commentaires insultants**

______|... **.txt**

___|**Commentaires neutres**

______|... **.txt**

**Doc** ###  _Documentation_

___|**conception.md**

___|**CW - YoutubeCleaner.pptx**

**Gui** ###        _Images utilisées pour l'interface graphique_

___|**images**

______|**gitlab-logo.png**

______|**logo.ico**

______|**logo.png**

______|**pc-logo.png**

**src**    ###    _Tous les modules utilisés_

___|**channel_videos.py**       ###   _Ensemble de fonctions relatives à une chaîne_

___|**contient_insultes.py**    ###   _Fonction qui permet de déterminer si un commentaire contient des insultes ou non_

___|**credentials.py**  ###   _Contient la clé pour l'API_

___|**Dash.py**   ###     _Permet de lancer une page dash pour afficher le graph_

___|**fonctions.py** ### _ensemble de fonctions nécessaires pour la recherche dans l'interface graphique_

___|**insultes.py**

___|**insultes.txt**       ###   _Liste de mots considérés comme des insultes_

___|**liste_insulte.py**

___|**main.py**  ###    _Fichier permettant de lancer l'interface graphique du programme_

___|**ml_finale.py** ###  _Décommenter la ligne 151 pour obtenir le résultat donné par la ml_

___|**ml_comments_train_test.py**

___|**ml_comments.py**

___|**ml_set500kpy**

___|**most_insulted_video.py**   ###     _Fonction qui renvoie la vidéo ayant le plus de commentaires insultants parmi les vidéos populaires d'une chaîne_

___|**non_insultes.txt**     ###      _Liste de mots devant être écartés de la détection d'insultes_

___|**pourcentages_insultes**.py  ### _Fonction qui renvoie la proportion de commentaires insultants_

___|**search_comments.py**     ###    _Ensemble de fonctions utilisant l'API pour récuperer des infos sur des vidéos, chaînes ou commentaires_

___|**Set Comments Insultants.py**

___|**setup.py**
