import re
import string
from nltk.corpus import wordnet
from nltk.corpus import stopwords

# just using input from terminal for now, will change to something else later
title = input()
content = input()

# Removing punctuation from the text, putting it into lowercase and splitting into a list
titleWords = re.sub(r'[^\w\s]','',title.lower()).split()
contentWords = re.sub(r'[^\w\s]','',content.lower()).split()

# Removes stop words from the lists
titleWords = [word for word in titleWords if not word in stopwords.words('english')]
contentWords = [word for word in contentWords if not word in stopwords.words('english')]

synonyms = list()

# Gets all the synonyms for the words from the title
for word in titleWords:
   for syn in wordnet.synsets(word):
         for l in syn.lemmas():
            if (not '_' in l.name() and not l.name().lower() in synonyms):
               synonyms.append(l.name().lower())

keywords = dict()

# Counting how many times a keyword appears in text
# taking into account the synonims for that word
for word in contentWords:
    if (word in titleWords or word in synonyms):
      if (not word in keywords): 
         keywords[word] = 1
      else:
         keywords.update({word: keywords.get(word) + 1})

# Calculating an arbitrary score on how the title and 
# content are related
if (len(keywords) > 0):
   score = int(sum(keywords.values())/len(contentWords) * 1000)
else:
   score = 0   
