from flask import Flask, jsonify, request, make_response, send_from_directory
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
samePersonModel = tf.keras.models.load_model('./models/SamePerson')
fingerNameModel = tf.keras.models.load_model('./models/FingerName')
shapeModel = tf.keras.models.load_model('./models/Shape')
qualityModel = tf.keras.models.load_model('./models/Quality')


app = Flask(__name__, static_folder=os.path.abspath('./static'), static_url_path="")

cors = CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}}, supports_credentials=True)

@app.route("/", methods=["GET"])
def get_example():
    """GET in server"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api/predictImages", methods=["POST"])
def predictImages():
    
    response_data = dict()
    
    mainImage = request.files.get('MainFile', None)
    samePersonImage = request.files.get('SamePersonFile', None)
    
    if mainImage:
        # read file into np array
        npImg = np.array(Image.open(mainImage))
        # fix channel mismatch
        if len(npImg.shape) == 2:
            npImg = np.stack((npImg,)*3, axis=-1)
        elif len(npImg.shape) == 3 and npImg.shape[2] == 4:
            npImg = npImg[:, :, :3]
        
        # resize img to model input layer dimention
        # cast into uint 8
        
        # fingerName, gender, samePerson, shape model
        resized224 = tf.image.resize(npImg, (224, 224))
        cast224 = tf.cast(resized224, dtype=tf.uint8)
        ready224 = np.array([cast224])
        
        # quality model
        resized180 = tf.image.resize(npImg, (180, 180))
        cast180 = tf.cast(resized180, dtype=tf.uint8)
        ready180 = np.array([cast180])
        
        # predict image labels
        response_data['gender'] = genderModel.predict(ready224).tolist()[0]
        response_data['shape'] = shapeModel.predict(ready224).tolist()[0]
        response_data['fingerName'] = fingerNameModel.predict(ready224).tolist()[0]
        response_data['quality'] = qualityModel.predict(ready180).tolist()[0]
        if samePersonImage:
            # read file into np array
            npSamePerson = np.array(Image.open(samePersonImage))
            
            # fix channel mismatch
            if len(npSamePerson.shape) == 2:
                npSamePerson = np.stack((npSamePerson,)*3, axis=-1)
            elif len(npSamePerson.shape) == 3 and npSamePerson.shape[2] == 4:
                npSamePerson = npSamePerson[:, :, :3]
            
            # stiching ing to main img 
            sameResized = tf.image.resize(npSamePerson, (224, 224)) 
            sameCast = tf.cast(sameResized, dtype=tf.uint8)
            sameStiched = tf.slice(tf.concat([cast224, sameCast], axis=1), [0, 0, 0], [224, 448, 3])
            
            # resize to model input layer dim
            sameStichedResized = tf.image.resize(sameStiched, (224, 224))
            sameStichedCast = tf.cast(sameStichedResized, dtype=tf.uint8)
            sameStichedReady = np.array([sameStichedCast])
            
            # predict same person prob
            
            sameRes = samePersonModel.predict(sameStichedReady).tolist()[0]
            sameRes.reverse()
            response_data['same'] = sameRes

        
    response = make_response(json.dumps(response_data))
    response.headers['Content-Type'] = 'application/json'
    

    return response

if __name__ == "__main__":
    app.run(port="5000", debug=True)