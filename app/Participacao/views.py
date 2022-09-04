from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Participacao.models import ParticipacaoModel
# from app.Area.schemas import AreaSchema

from sqlalchemy import update, delete

def query2json(q):
    pass

class ParticipacaoView(Resource):
    
    def __init__(self):
        pass

    def get(self):
        pass
        
    def post(self):
        pass
        
    def delete(self):
        pass