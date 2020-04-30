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

categories = []

# goes through all tests to check the accuracy (current: 75, 45, 59) (done manually for now)
for fileName in os.listdir("tests"):
    with open ("tests/" + fileName, "rt",  encoding='utf8', errors='ignore') as f:
        if ("neutral" in fileName):
            categories.append(0)
        elif ("biased" in fileName):
            categories.append(1)  
        elif ("satire" in fileName):
            categories.append(2)    
        else:
            categories.append(3)      
        parseData(f)

p1, p2, p3 = [], [], []

for title, content in zip(titles, contents):
    # gets all the vectors for the specified article
    hash_vectors, count_vectors, family_count_vectors = getData(title, content)

    # makes a predition on where the article belongs using 3 models
    hash_prediction = hash_model.predict(hash_vectors)
    count_prediction = count_model.predict(count_vectors)
    family_count_prediction = family_count_model.predict(family_count_vectors)
    p1.append(hash_prediction)
    p2.append(count_prediction)
    p3.append(family_count_prediction)

c1, c2, c3 = 0, 0, 0

for i in range(len(categories)):
    l1 = p1[-1]
    l2 = p2[-1]
    l3 = p3[-1]
    if (l1[i] == categories[i]):
        c1 = c1 + 1
    if (l2[i] == categories[i]):
        c2 = c2 + 1
    if (l3[i] == categories[i]):
        c3 = c3 + 1   

print(c1, c2, c3)                 

# 0 2 2 0 0 2 2 0 0 3 0 0 2 2 3 3 2 0 2 3 0 2 2 2 2 2 3 2 0 2 0 2 0 2 2 2 0 0 1 2 2 2 2 0 2 2 2 3 2 1 1 3 2 2 2 1 2 3 1 0 1 3 2
# 2 2 3 3 1 3 0 0 0 1 1 1 2 2 1 1 3 2 0 1 2 2 0 0 2 1 1 0 0 0 2 0 2 3 2 3 0 0 3 2 1 2 2 0 0 2 3 1 1 3 3 1 3 1 3 3 1 1 1 2 3 1 0