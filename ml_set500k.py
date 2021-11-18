import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import time
import pickle

data = pd.read_csv(
    'C:/Users/Charly Bohard/Documents/PythonScripts/jigsaw-toxic-comment-classification-challenge/train.csv')
data["insult"][data["threat"] == 1] = 1
data["insult"][data["toxic"] == 1] = 1
data["insult"][data["severe_toxic"] == 1] = 1
data["insult"][data["obscene"] == 1] = 1
data["insult"][data["identity_hate"] == 1] = 1
X, y = data["comment_text"], data['insult']

print(len([i for i in np.array(data.insult) if i == 1]))
'''
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
    max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()

tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

classifier = RandomForestClassifier(n_estimators=100, random_state=None)
classifier.fit(X_train, y_train)

# with open('pickle_model','wb') as file:
#     pickle.dump(classifier,file)
# y_pred = classifier.predict(X_test)


# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(accuracy_score(y_test, y_pred))

# def opti_hyperpara():
#     ti = time.time()
#     precision = 0
#     max_feat_opti = 0
#     for n in range(1, 101, 1000):
#         vectorizer = CountVectorizer(
#             max_features=n, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
#         X = vectorizer.fit_transform(documents).toarray()

#         tfidfconverter = TfidfTransformer()
#         X = tfidfconverter.fit_transform(X).toarray()

#         X_train, X_test, y_train, y_test = train_test_split(
#             X, y, test_size=0.2, random_state=0)

#         classifier = RandomForestClassifier(n_estimators=100, random_state=0)
#         classifier.fit(X_train, y_train)
#         y_pred = classifier.predict(X_test)
#         mat = confusion_matrix(y_test, y_pred)
#         recall = mat[1][1] / (mat[1][0]+mat[1][1])
#         if recall > precision:
#             max_feat_opti = n
#             precision = recall
#         print(n, ' : ', recall)
#         tf = time.time()
#         print(tf-ti)
#     print(f'Précision de {precision} pour max_features = {max_feat_opti}')


# opti_hyperpara()

def detection(text):
    data = pd.DataFrame({
        'text':text
    })
'''