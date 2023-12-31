import base64
import numpy as np
import io
from PIL import Image

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array

from flask import Flask, request, jsonify

import os
os.environ['KERAS_BACKEND'] = 'theano'

app = Flask(__name__)

def get_model():
    global model
    model = load_model('dl_model/VGG16_cats_and_dogs_model/model.h5')
    print(" * Model loaded!")

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image

print(" * Loading Keras model...")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224,224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction' : {
            'cat' : prediction[0][0] * 100,
            'dog' : prediction[0][1] * 100
        }
    }

    return jsonify(response)
