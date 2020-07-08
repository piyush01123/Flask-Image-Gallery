
from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
import os
import glob
import sys

app = Flask("Flask Image Gallery")
IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".gif", ".tiff"]

@app.route('/')
def home():
    root_dir = sys.argv[1]
    image_paths = []
    for root,dirs,files in os.walk(root_dir):
        for file in files:
            if any(file.endswith(ext) for ext in IMAGE_EXTS):
                image_paths.append(os.path.join(root,file).replace('/','__'))
    return render_template('index.html', paths=image_paths)

@app.route('/content/<path:filepath>')
def download_file(filepath):
    dir,filename = os.path.split(filepath.replace('__','/'))
    return send_from_directory(dir, filename, as_attachment=False)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
