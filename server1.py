from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   
import json as JSON
import ast

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
server1 = Blueprint('balls', __name__,
                   url_prefix='/api/server1')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(server1)

data = []

class ChessAPI:

    class _get(Resource):
        def get(self):
            return data

    class _push(Resource):
        def post(self):
            global data
            body = request.get_data(..., True)
            print(body)
            data.append(body)
            return data 
    
    class _start(Resource):
        def post(self):
            # request body format : "{'data' : ['uid1' : 1234, 'uid2' : 1234, 'move1' : 'move1', 'move2' : 'move2']}"
            global data
            body = ast.literal_eval(request.get_data(..., True).replace("[", "{").replace("]", "}"))
            data.append(body)
            return data




                


    # class _clear(Resource):


    api.add_resource(_get, '/')
    api.add_resource(_push, '/post')
    api.add_resource(_start, '/start')

if __name__ == "__main__": 
    print("LMAO LOOSER!")