import pickle, os
from vectorize import getData

# loads all the trained models
hash_model = pickle.load(open("hash_model", "rb"))
count_model = pickle.load(open("count_model", "rb"))
family_count_model = pickle.load(open("family_count_model", "rb"))

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
    # gets all the vectors for the specified article
    hash_vectors, count_vectors, family_count_vectors = getData(title, content)

    # makes a predition on where the article belongs using 3 models
    hash_prediction = hash_model.predict(hash_vectors)
    count_prediction = count_model.predict(count_vectors)
    family_count_prediction = family_count_model.predict(family_count_vectors)
