from flask import render_template, request, jsonify, json
from app import app
from PIL import Image
from io import BytesIO
import base64
import numpy as np
from App.predict import predict_CNN


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    postImg = BytesIO(base64.urlsafe_b64decode(request.form['img']))
    img = Image.open(postImg).convert('L')
    img.thumbnail((28, 28))
    img = np.array(img, dtype=np.int32)
    prediction = predict_CNN(img)

    return json.dumps(str(prediction))
