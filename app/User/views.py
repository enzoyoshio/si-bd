from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Area.models import AreaModel
from app.Area.schemas import AreaSchema

from sqlalchemy import update, delete

class UserView(Resource):
    def __init__(self):
        self.teste = ''


    def query2json(self, q):
        data = []
        for el in q:
            d = {}
            d["id"] = el.id 
            d["nome"]=el.nome 
            d["usuaio"]=el.usuaio 
            d["email"]=el.email 
            d["senha"]=el.senha
            d["horario_seg"]=el.horario_seg
            d["horario_ter"]=el.horario_ter
            d["horario_qua"]=el.horario_qua
            d["horario_qui"]=el.horario_qui
            d["horario_sex"]=el.horario_sex
            d["horario_sab"]=el.horario_sab
            d["horario_dom"]=el.horario_dom
            d["geojson"] = {
                "type": "Feature",
                "Geometry": {
                    "type": "Point",
                    "coordinates": [str(el.latitude), str(el.longitude)]
                }
            }
            data.append(d)
        return data