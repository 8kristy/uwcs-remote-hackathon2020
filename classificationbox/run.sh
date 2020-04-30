#!/bin/bash

python3 dataparser.py

# starts classificationbox
# get the MB KEY here https://machinebox.io/account?utm_source=matblog-fakenews&utm_medium=matblog-fakenews&utm_campaign=matblog-fakenews&utm_term=matblog-fakenews&utm_content=matblog-fakenews

docker run -p 8080:8080 -e MB_KEY="key"-d --name box machinebox/classificationbox & 

# wait for the initial setup, i don't know if there's an option to detect when it's ready so this is the next best thing
sleep 10

# creates a model in classificationbox
curl -X POST -H "Content-Type: application/json" -d @model.json http://localhost:8080/classificationbox/models

# teaches the model
curl -X POST -H "Content-Type: application/json" -d @toTeach.json http://localhost:8080/classificationbox/models/model1/teach-multi



