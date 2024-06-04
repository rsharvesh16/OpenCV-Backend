from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def analyze_urine_strip(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Assume the strips are in a vertical orientation, and there's 10 strips
    # This is a simplified assumption; proper strip detection logic should be more robust.
    strip_height = image.shape[0] // 10
    
    colors = {}
    labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    
    for i in range(10):
        strip_region = image[i * strip_height:(i + 1) * strip_height, :]
        avg_color = strip_region.mean(axis=0).mean(axis=0)
        # Convert average color values to list of integers
        colors[labels[i]] = [int(val) for val in avg_color]
    
    return colors




@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'})

    # Save the image temporarily
    image_path = 'temp_image.jpg'
    file.save(image_path)

    # Analyze the urine strip image
    colors = analyze_urine_strip(image_path)

    # Remove the temporary image
    # import os
    # os.remove(image_path)

    return jsonify(colors)

if __name__ == '__main__':
    app.run(debug=True)
