from flask import Blueprint, jsonify  
from flask_restful import Api, Resource 
import requests   

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
app_api2 = Blueprint('api', __name__,
                   url_prefix='/api/chess')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api2)
data = {
        "turn": 0,
        "moves": ["move1", "move2"]
    }
    
class ChessAPI:
    class _GetAll(Resource):
        def get(self):
            return jsonify(data)
    class _putTurn(Resource):
        def put(self):
            data["turn"] += 1
            return jsonify(data)
    class _putMove1(Resource):
        def put(self, move1):
            data["moves"][0] = move1
            return jsonify(data)
    class _putMove2(Resource):
        def put(self, move2):
            data["moves"][1] = move2
            return jsonify(data)


             


    api.add_resource(_GetAll, '/')

    api.add_resource(_putTurn, '/turn/')
    api.add_resource(_putMove1, '/move1/<string:move1>')
    api.add_resource(_putMove2, '/move2/<string:move2>')
        

if __name__ == "__main__": 
    #server = "http://127.0.0.1:5000" #local
    server = 'https://tngc.nighthawkcodescrums.gq' #web
    url = server + "/api/chess/"