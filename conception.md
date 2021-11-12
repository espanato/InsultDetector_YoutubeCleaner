Idées : Détecteur d’insultes sur Youtube

MVP : Calculer le ratio like dislike avec les commentaires


Déterminer quels sujets développent le plus la haine sur youtube.
[Classement des chaînes youtubes les plus détestées.]





ETAPES:
      1) Récupérer les commentaires youtube/comprendre le fonctionnement de l’API
Récupérer les commentaires via l’API
Fonction qui stocke les commentaires dans une liste

      2) Déterminer la polarité d’un message 
Trouver le module à utiliser
Fonction qui analyse la polarité du commentaire
Utiliser le pourcentage de dislikes sur un commentaire pour déterminer s’il peut être insultant et s’il demande une vérification plus poussée s’il n’a pas été détecté auparavant.

 
      3) Déterminer à qui s’adresse le message 

Fonction qui détecte les messages envers le youtuber (“tu”,”t’”,pas de pronom..)


      4) Faire un graphique camembert sur Dash
nombre de commentaires insultants/ nombre de commentaires non insultants

Déjà fait (Charly)

      5) faire une fonction qui choisit un sujet (par exemple politique, jeu vidéo) et qui détermine la quantité de like, dislike puis comparer pour différents sujets.



MVP : Pouvoir récupérer les commentaires d’une vidéo et savoir s'il s’agit d’une insulte envers le youtuber  

API : https://developers.google.com/youtube/v3/docs/comments
