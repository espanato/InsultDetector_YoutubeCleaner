from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from sklearn.datasets import load_files
import codecs
import pickle


# file0 = codecs.open('C:/Users/Charly Bohard/Documents/PythonScripts/test_with_solutions.csv','r',encoding='utf-8')
# texts= file0.readlines()
# i=1
# for line in texts:
#     line = line.split('"""')
#     print(line)
#     if line[0][0] == '0':
#         file = codecs.open(f'C:/Users/Charly Bohard/Documents/PythonScripts/detecteur_insultes_test/neutre/{i}.txt','w',encoding='utf-8')
#         file.write(line[1])
#     elif line[0][0] == '1':
#         file = codecs.open(f'C:/Users/Charly Bohard/Documents/PythonScripts/detecteur_insultes_test/insultant/{i}.txt','w',encoding='utf-8')
#         file.write(line[1])
#     i+=1

texts_data_train = load_files(
    r"C:/Users/Charly Bohard/Documents/PythonScripts/detecteur_insultes")
X, y = texts_data_train.data, texts_data_train.target

texts_data_test = load_files(
    r"C:/Users/Charly Bohard/Documents/PythonScripts/detecteur_insultes_test")
X_test, y_test = texts_data_test.data, texts_data_test.target

documents = []
documents_test = []


stemmer = WordNetLemmatizer()
stemmer_test = WordNetLemmatizer()

for sen in range(len(X)):
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
    max_features=2000, min_df=2, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()

tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

for sen in range(len(X_test)):
    # Remove all the special characters
    document_test = re.sub(r'\W', ' ', str(X_test[sen]))

    # remove all single characters
    document_test = re.sub(r'\s+[a-zA-Z]\s+', ' ', document_test)

    # Remove single characters from the start
    document_test = re.sub(r'\^[a-zA-Z]\s+', ' ', document_test)

    # Substituting multiple spaces with single space
    document_test = re.sub(r'\s+', ' ', document_test, flags=re.I)

    # Removing prefixed 'b'
    document_test = re.sub(r'^b\s+', '', document_test)

    # Converting to Lowercase
    document_test = document_test.lower()

    # Lemmatization
    document_test = document_test.split()

    document_test = [stemmer_test.lemmatize(word) for word in document_test]
    document_test = ' '.join(document_test)

    documents_test.append(document_test)

vectorizer = CountVectorizer(
    max_features=2000, min_df=2, max_df=0.7, stop_words=stopwords.words('english'))
X_test = vectorizer.fit_transform(documents_test).toarray()

tfidfconverter = TfidfTransformer()
X_test = tfidfconverter.fit_transform(X_test).toarray()

classifier = RandomForestClassifier(n_estimators=2500, random_state=0)
classifier.fit(X, y)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

def opti_hyperpara():
    precision = 0
    n_opti = 0
    for n in range(2000,3401,200):
        classifier = RandomForestClassifier(n_estimators=n, random_state=0)
        classifier.fit(X, y)
        y_pred = classifier.predict(X_test)
        acc = accuracy_score(y_pred,y_test)
        if acc > precision:
            n_opti = n
            precision = acc
        print(n,' : ',acc)
    print(f'Précision de {precision} pour n_estimators = {n_opti}')
