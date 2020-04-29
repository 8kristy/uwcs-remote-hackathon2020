from sklearn import model_selection,  svm
from sklearn import decomposition, ensemble

import numpy, string

import pickle
import os

from vectorize import getData

# lists used by svm when training the model based on different criteria
categories, hashes, counts, word_family_counts = [], [], [], []

# gets the vectors and adds them to the lists to be trained
def parseData(f, category):
    hash_vect, count, word_family_count = getData(f.readline().strip(), ' '.join(f.readlines()[1:]))
    categories.append(category)
    hashes.append(hash_vect)
    counts.append(count)
    word_family_counts.append(word_family_count)

# goes through all training data and adds vectors to corresponding lists
# categories: 0 = neutral, 1 = biased, 2 = satire, 3 = fake
# TODO: mess around with order of adding stuff in hopes of improving accuracy (worked once, will try again)
for fileName in os.listdir("data/neutral"):
    with open ("data/neutral/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f, 0)

for fileName in os.listdir("data/satire"):
    with open ("data/satire/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f, 2)

for fileName in os.listdir("data/fake"):
    with open ("data/fake/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f, 3)   


for fileName in os.listdir("data/biased"):
    with open ("data/biased/" + fileName, "rt", encoding='utf8', errors='ignore') as f:
        parseData(f, 1)             

# trains a model based on vectors hashed from the content
hash_model = svm.SVC()
hash_model.fit(hashes[0], categories)
pickle.dump(hash_model, open("hash_model", 'wb'))

# trains a second model with arrays of various counts (word count, punctuation count, etc.)
count_model = svm.SVC()
count_model.fit(counts[0], categories)
pickle.dump(count_model, open("count_model", 'wb'))

# trains a third model with arrays of word family counts (nouns, verbs, pronouns, adjectives, adverbs)
family_count_model = svm.SVC()
family_count_model.fit(word_family_counts[0], categories)
pickle.dump(family_count_model, open("family_count_model", 'wb'))