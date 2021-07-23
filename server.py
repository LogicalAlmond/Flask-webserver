from flask import Flask
from flask.templating import render_template

server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html')