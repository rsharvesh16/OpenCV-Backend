# urine-strip-detection-app/backend/app.py
from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

def analyze_urine_strip(image_path):
    image = cv2.imread(image_path)
    strip_height = image.shape[0] // 10
    colors = {}
    labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    for i in range(10):
        strip_region = image[i * strip_height:(i + 1) * strip_height, :]
        avg_color = strip_region.mean(axis=0).mean(axis=0)
        colors[labels[i]] = [int(val) for val in avg_color]
    return colors

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'})

    image_path = 'temp_image.jpg'
    file.save(image_path)
    colors = analyze_urine_strip(image_path)
    print(colors)
    return jsonify(colors)

if __name__ == '__main__':
    app.run(debug=True)
