import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods = [ 'POST'])
def post():
    if(request.method == 'POST'):
        # this is a very hacky solution but i don't want to fight with js
        # to send me plain text instead of this immutable multi dictionary thing
        # so this is how we get our text
        text = list(request.form.to_dict().keys())[0]
        return text

app.run()
