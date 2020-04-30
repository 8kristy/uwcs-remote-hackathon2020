import pickle, os
from classifier.vectorize import getData

def predict_article(article):

    # loads the trained model
    title_model = pickle.load(open("models/title_model", "rb"))
    content_model = pickle.load(open("models/content_model", "rb"))

    # values for prediction from the article
    title = article.split("\n", 1)[0].strip()
    content = article.split("\n", 1)[1].replace("\n", " ")

     # gets the vector for the specified article
    title_vect, content_vect = getData(title, content)
    # makes a predition on where the article belongs using 3 models
    title_prediction = title_model.predict([title_vect])
    content_prediction = content_model.predict([content_vect])

    return title_prediction, content_prediction
                

