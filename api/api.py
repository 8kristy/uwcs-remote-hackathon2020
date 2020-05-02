import flask
from flask import request

from predict import predict_article

app = flask.Flask(__name__)

@app.route('/', methods = [ 'POST'])
def post():
    if(request.method == 'POST'):
        # this is a very hacky solution but i don't want to fight with js
        # to send me plain text instead of this immutable multi dictionary thing
        # so this is how we get our text
        text = list(request.form.to_dict().keys())[0]
        title_prediction, content_prediction = predict_article(text)
        return str(title_prediction[0]) + str(content_prediction[0])

# for adding div content into the 
@app.route('/popup', methods = [ 'POST'])
def postPopup():
    if(request.method == 'POST'):
        # adds basic html stuff
        html = '<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="style.css"></head><body>'
        # adds the div content, replacing the id and temp symbols
        html = html + list(request.form.to_dict().keys())[0].replace("£", "=").replace("hello_text_id", "popup_text")
        # changes the sizes because they mess up if originals are used
        html = html.replace("2.5vh", "1.5em").replace("5vh", "3em").replace("1.8vh", "1em")[:-45]
        # adds closing basic html tags + div which was cut off when removing button (that's what [:-45] is for)
        html = html + '</div></body></html>'
        # writes new html into the file
        htmlFile = open("../pageTestV4/index.html", "w")
        htmlFile.write(html)
        htmlFile.close()
        return "ok"

app.run()
