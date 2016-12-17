import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/jonathan/websites/simpleupload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    filedata = request.files['filedata']

    if filedata and allowed_file(filedata.filename):
        filename = secure_filename(filedata.filename)
        filedata.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "thanks for the file!"
    return "invalid filename"

if __name__ == '__main__':
    app.run(debug=True)
