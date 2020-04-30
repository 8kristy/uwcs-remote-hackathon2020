from sklearn.feature_extraction.text import HashingVectorizer

# calcualtes all the hashes
def getData(title, content):
     # hashes the title into a 300 feature vector
    titles_hash = HashingVectorizer(n_features=100).transform([title]).toarray()[0]
    # hashes the content into a 300 feature vector
    content_hash = HashingVectorizer(n_features=300).transform([content]).toarray()[0]
    return titles_hash, content_hash
