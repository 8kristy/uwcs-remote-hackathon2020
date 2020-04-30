import os
from pathlib import Path

# gets all directories
neutral = os.listdir("raw data/neutral")
biased = os.listdir("raw data/biased")
satire = os.listdir("raw data/satire")  

# adds an article to the final document
def toJSON(className, title, content):
    fw.write('{ "class": "' + className + '", "inputs": [{"key": "title", "type": "text", "value": "' + title + '"},{"key": "content", "type": "text", "value": "' + content + '"}]},')

# generates the correct json file
fw = open("toTeach.json", "a")
fw.write('{"examples": [')

# goes through all files in all folders and adds them to the final file
for fileName in neutral:
    with open ("raw data/neutral/" + fileName, "rt") as f:
        toJSON("neutral", f.readline().strip(), ' '.join(f.readlines()[1:]))

for fileName in biased:
    with open ("raw data/biased/" + fileName, "rt") as f:
        toJSON("biased", f.readline().strip(), ' '.join(f.readlines()[1:]))

for fileName in satire:
    with open ("raw data/satire/" + fileName, "rt") as f:
        toJSON("satire", f.readline().strip(), ' '.join(f.readlines()[1:]))                
fw.write('{ "class": "neutral", "inputs": []}')
fw.write('  ]}')        

fw.close()  
