import pickle, os
from vectorize import getData

# loads the trained model
hash_model = pickle.load(open("hash_model", "rb"))

# placeholder values for testing; will have the input from site later
titles, contents = [], []

# going though tests and splitting them into titles and contents
def parseData(f):
    titles.append(f.readline().strip())
    contents.append(' '.join(f.readlines()[1:]))

categories = []

for title, content in zip(titles, contents):
    # gets the vector for the specified article
    hash_vectors = getData(title, content)
    # makes a predition on where the article belongs using 3 models
    hash_prediction = hash_model.predict(hash_vectors)

               

