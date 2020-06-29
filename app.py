
import argparse
from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
import os
import glob

app = Flask("Image Classifier Server")
parser = argparse.ArgumentParser()
parser.add_argument("--root_dir", required=True, help="Root Directory of Sample Images")
parser.add_argument("--upload_dir", default='uploads', help="Root Directory of Sample Images")
args = parser.parse_args()

# @app.route('/')
# def home():
#     sample_imgs = glob.glob(os.path.join(args.root_dir, "*.jpg"))
#     return render_template('index.html', img_paths=sample_imgs)

@app.route('/')
def home():
    sample_imgs = os.listdir(args.root_dir)
    return render_template('index.html', names=sample_imgs)

@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(args.root_dir, filename, as_attachment=False)

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['img']
    file.save(os.path.join(args.upload_dir, file.filename))
    return 'testResponse'

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)


# def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--root_dir", required=True, help="Root Directory of Sample Images")
    # args = parser.parse_args()
    # sample_imgs = glob.glob(os.path.join(args.root_dir, "*.jpg"))
