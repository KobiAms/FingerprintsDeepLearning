from flask import Flask, jsonify, request, make_response
from flask_cors import CORS 
import json
import sys

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
    if request.method == 'POST':
        response_data = {
            'img1' : 'Male',
            'img2' : 'Female'
        }
    
    response = make_response(json.dumps(response_data))
    response.headers['Content-Type'] = 'application/json'

    print(request.headers.get('Content-Length', 0))
    print('request detected', file=sys.stderr)
    print('request data', request.data, file=sys.stderr)

    return response

if __name__ == "__main__":
    app.run(host="10.0.0.10", port="5000", debug=True)