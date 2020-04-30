from sklearn.feature_extraction.text import HashingVectorizer

# all vectors to be returned
hashes = []

# calcualtes all the hashes
def getData(title, content):
    # hashes the content into a 300 feature vector
    hashes.append(HashingVectorizer(n_features=300).transform([content]).toarray()[0])
    return hashes
