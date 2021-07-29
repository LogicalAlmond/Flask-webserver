from flask import Flask
from flask import send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Downloads work, but need to read up on multiple files since this function is specified for one file
@app.route('/download')
def download_file():
    path = 'files/file1.txt'
    return send_file(path, as_attachment=True)