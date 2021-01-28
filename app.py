import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, jsonify
from werkzeug.utils import secure_filename
import gaussian_smoothing
import sobel

UPLOAD_FOLDER = 'static\\img\\upload-img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        algo = int(request.headers['Algo'])
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            img = ""
            if algo == 1:
                img = gaussian_smoothing.run(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            elif algo == 2:
                img = sobel.run(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            return jsonify({
                "success": True,
                "file_type": filename.split('.')[len(filename.split('.')) - 1],
                "src": img
            })

    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)        