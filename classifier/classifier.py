from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
from vectorize import getData

import numpy, string, pickle, os


# categories in order to be passed onto training model later
categories = []

# hashes of all articles in the training data to use when classifying
title_hashes = []
content_hashes = []

# gets the vectors and adds them to the list to be trained
def parseData(f, category):
    title_vect, content_vect = getData(f.readline().strip(), ' '.join(f.readlines()[1:]))
    categories.append(category)
    title_hashes.append(title_vect)
    content_hashes.append(content_vect)

# goes through all training data and adds vectors to corresponding lists
# categories: 0 = neutral, 1 = biased, 2 = satire, 3 = fake
# order is a bit off because it makes small difference in accuracy for some reason
for fileName in os.listdir("data/neutral"):
    with open ("data/neutral/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f, 0)

for fileName in os.listdir("data/satire"):
    with open ("data/satire/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f, 2)          

for fileName in os.listdir("data/biased"):
    with open ("data/biased/" + fileName, "rt", encoding='utf8', errors='ignore') as f:
        parseData(f, 1)                            


for fileName in os.listdir("data/fake"):
    with open ("data/fake/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        parseData(f, 3)  
        
# trains a model based on vectors hashed from the content
# uses neural networks
title_model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(300, 150), random_state=1)
title_model.fit(title_hashes, categories)
pickle.dump(title_model, open("title_model", 'wb'))

content_model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(300, 150), random_state=1)
content_model.fit(content_hashes, categories)
pickle.dump(content_model, open("content_model", 'wb'))
