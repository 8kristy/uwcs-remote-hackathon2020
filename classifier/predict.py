import pickle
from vectorize import getData

# loads all the trained models
hash_model = pickle.load(open("hash_model", "rb"))
count_model = pickle.load(open("count_model", "rb"))
family_count_model = pickle.load(open("family_count_model", "rb"))

# placeholder values for testing; will have the input from site later
title = "test"
content = "this is some test content"

# gets all the vectors for the specified article
hash_vectors, count_vectors, family_count_vectors = getData(title, content)

# makes a predition on where the article belongs using 3 models
hash_prediction = hash_model.predict(hash_vectors)
count_prediction = count_model.predict(count_vectors)
family_count_prediction = family_count_model.predict(family_count_vectors)