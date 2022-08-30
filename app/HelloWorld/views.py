from flask_restful import Resource 
from flask import request

from app.core.util.response import json_response
from flask_restful import reqparse

class HelloWorldView(Resource):
    
    def __init__(self):
        self.teste = ''
    
    def get(self):
        return json_response(message="Hello, si-bd!", status=200)
