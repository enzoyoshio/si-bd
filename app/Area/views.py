from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Area.models import AreaModel
from app.Area.schemas import AreaSchema

from sqlalchemy import update, delete

class AreaView(Resource):
    
    def __init__(self):
        self.teste = ''

    def query2json(self, q):
        data = []
        for el in q:
            d = {}
            d["id"] = el.id 
            d["nome"]=el.nome 
            d["descricao"]=el.descricao 
            d["lotacao_max"]=el.lotacao_max 
            d["modalidade"]=el.modalidade
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

    def get(self, area_id):
        data = []
        data_json = []
        # if area_id == 0:
        data = AreaModel.query.all()
        data_json = self.query2json(data)
        # else:
        #     data = AreaModel.query.filter(AreaModel.id == area_id).first()
        #     data_json = self.query2json([data])
        return json_response(data=data_json, message="Lista de todas as areas cadastradas!", status=200)

    def post(self):
        data = request.get_json()

        model = AreaModel(
            nome=data['nome'], 
            descricao=data['descricao'], 
            lotacao_max=data['lotacao_max'], 
            modalidade=data['modalidade'],
            horario_seg=data['horario_seg'],
            horario_ter=data['horario_ter'],
            horario_qua=data['horario_qua'],
            horario_qui=data['horario_qui'],
            horario_sex=data['horario_sex'],
            horario_sab=data['horario_sab'],
            horario_dom=data['horario_dom'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )

        print(model)
        print(model.latitude, type(model.latitude))

        db_session.add(model)
        db_session.commit()
        
        return json_response(data=data, message="area cadastrada com sucesso!", status=200)


    def put(self, area_id):
        data = request.get_json()
 
        up = update(AreaModel).where(AreaModel.id==area_id).values(data)
        db_session.execute(up)
        db_session.commit()
        
        return json_response(message="area atualizada com sucesso!", status=200)
    
    def delete(self, area_id):

        delete = delete(AreaModel).where(AreaModel.id == area_id)
        db_session.execute(delete)
        db_session.commit()
        
        return json_response(message="area deletada com succeso", status=200)