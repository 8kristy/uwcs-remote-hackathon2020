import pickle, os
from sklearn.feature_extraction.text import HashingVectorizer

def predict_article(article):

    # loads the trained model
    title_model = pickle.load(open("models/title_model", "rb"))
    content_model = pickle.load(open("models/content_model", "rb"))

    # values for hashing from the article
    title = article.split("\n", 1)[0].strip()
    content = article.split("\n", 1)[1].replace("\n", " ")

     # gets the vectors for the article
    title_vect = HashingVectorizer(n_features=100).transform([title]).toarray()[0]
    content_vect = HashingVectorizer(n_features=300).transform([content]).toarray()[0]

    # makes a predition on where the article belongs using 2 models
    title_prediction = title_model.predict([title_vect])
    content_prediction = content_model.predict([content_vect])

    return title_prediction, content_prediction
                

