## YoutubeCleaner

YoutubeCleaner is a project created by CentraleSupélec students in the framework of the Coding Weeks 2021 - 2022 and in the theme "Insult detector".

## Members

- ESPANA Tomas
- BLONDEL Hector
- BUI Hugo
- BOHARD Charly
- CERVERA Romain
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

## How to make it work

► Write your Youtube API key in credentials.py file in the src folder.  
► Run the main.py file in the src folder.  
► The search for videos can be done by URL (url) or by video ID (video).   

## Applications

This project is aimed at the general public as well as professionals, for example:  
► For simple Youtube users, for informational purposes  
► For Youtubers, to get to know their community better  
► For companies willing to realize a partnership with a Youtuber  

## Project status
The project is currently functional as an MVP (minimum viable product). 

## Architecture of the project 
**Data** ### _Set of comments for the machine learning program_

___|**Commentaires insultants**

______|... **.txt**

___|**Commentaires neutres**

______|... **.txt**

**Doc** ###  _Documentation_

___|**conception.md**

___|**CW - YoutubeCleaner.pptx**

**Gui** ###        _Images used for the graphic interface_

___|**images**

______|**gitlab-logo.png**

______|**logo.ico**

______|**logo.png**

______|**pc-logo.png**

**src**    ###  

___|**channel_videos.py**       ###  _Set of functions related to a channel_

___|**contient_insultes.py**    ###   _Function to determine if a comment contains insults or not_

___|**credentials.py**  ###  _API Key_

___|**Dash.py**   ###     _Allows to launch a dash page to display the graph_

___|**fonctions.py** ### _set of functions needed for searching in the graphical interface_

___|**insultes.py**

___|**insultes.txt**       ###   _List of words considered as insults_

___|**liste_insulte.py**

___|**main.py**  ###    _File to launch the graphic interface of the program_

___|**ml_finale.py** ###  _Uncomment line 151 to obtain the result given by ml_

___|**ml_comments_train_test.py**

___|**ml_comments.py**

___|**ml_set500kpy**

___|**most_insulted_video.py**   ###     _Function that returns the video with the most insulting comments among the popular videos of a channel_

___|**non_insultes.txt**     ###      _List of words to be excluded from insult detection_

___|**pourcentages_insultes**.py  ### _Function that returns the proportion of insulting comments_

___|**search_comments.py**     ###    _Set of functions using the API to retrieve information about videos, channels or comments_

___|**Set Comments Insultants.py**

___|**setup.py**













'''
|_Projet
	|-- configuration.php
	|-- index.php
	|-- /global				-->(template)
	|-- /libs				-->(Facebook,PHPMailer,lib core Guideyou)
	|-- /local				-->(fichier traduction)
	|-- /modules
		|-- /mod_404
			|-- /actions	--> (controleurs)
			|-- /img
			|-- /styles
			|-- /views		--> (views)
			|-- index.php 
		|-- /mod_dashboard
			|-- /actions	--> (controleurs)
			|-- /img
			|-- /styles
			|-- /js
			|-- /views		--> (views)
			|-- index.php 
		|_ /mod_home
			|-- /actions	--> (controleurs)
			|-- /img
			|-- /styles
			|-- /js
			|-- /views		--> (views)
			|-- index.php 
		|_ /mod_user
			|-- /actions	--> (controleurs)
			|-- /img
			|-- /styles
			|-- /js
			|-- /views		--> (views)
			|-- index.php 
		|_ /mod_offer
			|-- /actions	--> (controleurs)
			|-- /img
			|-- /styles
			|-- /js
			|-- /views		--> (views)
			|-- index.php 
	|_ README.md
'''
