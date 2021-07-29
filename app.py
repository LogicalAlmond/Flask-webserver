from flask import Flask
from flask import send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files')
def download_file():
    path = "my_file"
    return send_file(path, as_attachment=True)