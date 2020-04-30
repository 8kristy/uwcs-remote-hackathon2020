import pickle, os
from vectorize import getData

# loads the trained model
title_model = pickle.load(open("title_model", "rb"))
content_model = pickle.load(open("content_model", "rb"))


# placeholder values for testing; will have the input from site later
titles, contents = [], []

# going though tests and splitting them into titles and contents
def parseData(f):
    titles.append(f.readline().strip())
    contents.append(' '.join(f.readlines()[1:]))

# goes through all tests to check the accuracy (current: 75, 45, 59) (done manually for now)
for fileName in os.listdir("tests"):
    with open ("tests/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f)    

for title, content in zip(titles, contents):
    # gets the vector for the specified article
    title_vect, content_vect = getData(title, content)
    # makes a predition on where the article belongs using 3 models
    title_prediction = title_model.predict([title_vect])
    content_prediction = content_model.predict([content_vect])
               

