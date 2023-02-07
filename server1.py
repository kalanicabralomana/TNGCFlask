from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
server1 = Blueprint('balls', __name__,
                   url_prefix='/api/server1')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(server1)

data = []

class ChessAPI:

    class _get(Resource):
        def get(self):
            return "data"

    class _push(Resource):
        def post(self):
            global data
            body = request.get_data(..., True)
            print(body)
            data.append(body)
            return data


             


    api.add_resource(_get, '/')
    api.add_resource(_push, '/post')
        

if __name__ == "__main__": 
    print("LMAO LOOSER!")