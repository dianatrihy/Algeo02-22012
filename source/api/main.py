from flask import Flask, request, jsonify, render_template, send_file
from mtexture import searchtexture
from mcolor import searchcolor
from directory import get_upload_dir
import base64
import os
from io import BytesIO
import numpy as np

# import requests

app = Flask(__name__)

'''
POST
{
    image: string
}
'''
@app.route("/api/search_texture", methods=['GET', 'POST'])
def search_texture():
    data = request.get_json()
    if not('image' in data):
        return jsonify({ "error": 'dataset_folder or image is missing', "success": False }), 400

    image = base64.b64decode(data['image'])
    result = searchtexture(np.fromstring(image, dtype=np.uint8))
    return jsonify(result)

'''
POST
{
    path_image: string
}
'''
@app.route("/api/search_color", methods=['GET', 'POST'])
def search_color():
    data = request.get_json()
    if not('path_image' in data):
        return jsonify({ "error": 'dataset_folder or image is missing', "success": False }), 400

    image = BytesIO(base64.b64decode(data['path_image']))
    result = searchcolor(image)
    return jsonify(result)

@app.route("/api/upload", methods=['POST'])
def upload():
    UPLOAD_DIRECTORY = get_upload_dir()
    # check folder ada
    if not (os.path.isdir(UPLOAD_DIRECTORY)):
        # buat folder
        os.mkdir(UPLOAD_DIRECTORY)

    data = request.get_json()
    file_content = base64.b64decode(data['content'])
    file = open(UPLOAD_DIRECTORY + '/' + data['name'], 'wb')
    file.write(file_content)
    file.close()

    return jsonify({"success": True})

@app.route("/image", methods=['GET'])
def get_image():
    UPLOAD_DIRECTORY = get_upload_dir()
    filename = request.args.get('name')
    if(filename == None or len(filename) == 0):
        return 'Name is required', 404

    if(not os.path.isfile(UPLOAD_DIRECTORY + '/' + filename)):
        return "File doesn't exist", 404

    return send_file('../' + UPLOAD_DIRECTORY + '/' + filename)