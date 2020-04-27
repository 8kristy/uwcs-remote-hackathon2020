import re
import string

# just using input from terminal for now, will change to something else later
title = input()
content = input()

# TODO: ignore basic words like 'a' 'the' etc.
# Removing punctuation from the text, putting it into lowercase and splitting into a list
title = re.sub(r'[^\w\s]','',title.lower()).split()
content = re.sub(r'[^\w\s]','',content.lower()).split()

keywords = dict()

# Counting how many times a keyword appears in text
# TODO: check for synonims
for word in content:
    if (word in title):
      if (not word in keywords): 
         keywords[word] = 1
      else:
         keywords.update({word: keywords.get(word) + 1})

# Calculating an arbitrary score on how the title and 
# content are related
score = len(content)/sum(keywords.values())

