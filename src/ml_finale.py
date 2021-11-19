from search_comments import get_all
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
import pandas
import numpy as np
import time
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import json
import os
from bs4 import BeautifulSoup
import requests
import csv
from googleapiclient.discovery import build
from requests.api import get


def enregistrer_ml():
    data = pd.read_csv(
        'C:/Users/etoma/OneDrive/Documents/jigsaw-toxic-comment-classification-challenge-bis/train.csv')

    data["insult"][data["threat"] == 1] = 1
    data["insult"][data["toxic"] == 1] = 1
    data["insult"][data["severe_toxic"] == 1] = 1
    data["insult"][data["obscene"] == 1] = 1
    data["insult"][data["identity_hate"] == 1] = 1

    X, y = data["comment_text"], data['insult']

    documents = []

    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(X[sen]))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)

        documents.append(document)

    vectorizer = CountVectorizer(
        max_features=2000, min_df=0, max_df=0.7, stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform(documents).toarray()

    tfidfconverter = TfidfTransformer()
    X = tfidfconverter.fit_transform(X).toarray()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    classifier = RandomForestClassifier(n_estimators=100)
    classifier.fit(X_train, y_train)
    pickle.dump(classifier, open(
        'C:/Users/etoma/OneDrive/Bureau/insultedetector_s2_YouTubeCleaner/src/ml.sav', 'wb'))


# enregistrer_ml()
# la ml a été enregistrée dans ml.sav

####################################################################################################################################################


def get_props(video_id):
    classifier = pickle.load(open(
        'C:/Users/etoma/OneDrive/Bureau/insultedetector_s2_YouTubeCleaner/src/ml.sav', 'rb'))  # on ouvre la ml
    commentaires_dico = get_all(video_id)
    nb_commentaires = len(commentaires_dico)
    liste_panda = [commentaires_dico[elt] for elt in commentaires_dico]
    X = pd.Series(liste_panda)

    documents = []

    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(X[sen]))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)

        documents.append(document)

    vectorizer = CountVectorizer(
        max_features=2000, min_df=0, max_df=0.7, stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform(documents).toarray()

    tfidfconverter = TfidfTransformer()
    X = tfidfconverter.fit_transform(X).toarray()

    liste = classifier.predict(X)

    nb_insultes = 0
    nb_neutre = 0
    for i in range(len(liste)):
        if liste[i] == 0:
            nb_neutre += 1
        if liste[i] == 1:
            nb_insultes += 1

    print("pourcentage d'insultes identifiées:",
          (nb_insultes/nb_commentaires)*100)
    print("pourcentage de messages neutres identifiés:",
          (nb_neutre/nb_commentaires)*100)


# print(get_props('th5_9woFJmk'))
