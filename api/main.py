from flask import Flask, request, jsonify
from mtexture import searchtexture
from mcolor import searchcolor

app = Flask(__name__)

@app.route("/api/", methods=['GET'])
def main():
    return "<p>Hello, World!</p>"

'''
POST
{
    dataset_folder: string (e.g. C:/User/folderName)
    image: string (e.g. C:/User/image.jpg)
}
'''
@app.route("/api/search_texture", methods=['GET', 'POST'])
def search_texture():
    data = request.get_json()
    if not('dataset_folder' in data and 'image' in data):
        return jsonify({ "error": 'dataset_folder or image is missing', "success": False }), 400
    
    result = searchtexture(data["dataset_folder"], data["image"])
    return jsonify(result)

'''
POST
{
    dataset_folder: string (e.g. C:/User/folderName)
    image: string (e.g. C:/User/image.jpg)
}
'''
@app.route("/api/search_color", methods=['GET', 'POST'])
def search_color():
    data = request.get_json()
    if not('dataset_folder' in data and 'image' in data):
        return jsonify({ "error": 'dataset_folder or image is missing', "success": False }), 400
    
    result = searchcolor(data["image"], data["dataset_folder"])
    return jsonify(result)