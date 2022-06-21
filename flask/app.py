from flask import Flask, jsonify, request, make_response
from flask_cors import CORS 
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

try:
    # Disable all GPUS
    tf.config.set_visible_devices([], 'GPU')
    visible_devices = tf.config.get_visible_devices()
    for device in visible_devices:
        assert device.device_type != 'GPU'
except:
    # Invalid device or cannot modify virtual devices once initialized.
    pass

genderModel = tf.keras.models.load_model('./models/Gender')
fingerNameModel = tf.keras.models.load_model('./models/FingerName')
shapeModel = tf.keras.models.load_model('./models/Shape')
qualityModel = tf.keras.models.load_model('./models/Quality')


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

@app.route("/", methods=["GET"])
def get_example():
    """GET in server"""
    response = jsonify(message="Simple server is running")
    return response

@app.route("/api/predictImages", methods=["POST"])
def predictImages():
    
    response_data = dict()
    
    mainImage = request.files.get('MainFile', None)
    samePersonFile = request.files.get('SamePersonFile', None)
    
    if mainImage:
        npImg = np.stack((Image.open(mainImage),)*3, axis=-1)
        resized224 = tf.image.resize(npImg, (224, 224))
        resized180 = tf.image.resize(npImg, (180, 180))
        ready224 = np.array([tf.cast(resized224, dtype=tf.uint8)])
        ready180 = np.array([tf.cast(resized180, dtype=tf.uint8)])
        response_data['gender'] = genderModel.predict(ready224).tolist()[0]
        response_data['shape'] = shapeModel.predict(ready224).tolist()[0]
        response_data['fingerName'] = fingerNameModel.predict(ready224).tolist()[0]
        response_data['quality'] = qualityModel.predict(ready180).tolist()[0]
    if mainImage and samePersonFile:
        npMainImage = np.stack((Image.open(mainImage),)*3, axis=-1)
        npSamePerson = np.stack((Image.open(samePersonFile),)*3, axis=-1)
        mainResized = tf.image.resize(npMainImage, (224, 224))
        sameResized = tf.image.resize(npSamePerson, (224, 224))
        stiched = tf.slice(tf.concat([mainResized, sameResized], axis=1), [0, 0, 0], [224, 224*2, 3])
        resized = tf.image.resize(stiched, (224, 224))
        ready = np.array([tf.cast(resized, dtype=tf.uint8)])
        response_data['same'] = genderModel.predict(ready).tolist()[0]

        
    response = make_response(json.dumps(response_data))
    response.headers['Content-Type'] = 'application/json'
    
    print(request.headers.get('Content-Length', 0))

    return response

if __name__ == "__main__":
    app.run(host="10.0.0.10", port="5000", debug=True)