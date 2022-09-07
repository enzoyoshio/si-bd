from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Participacao.models import ParticipacaoModel
from app.Area.models import AreaModel
from app.User.models import UserModel

from sqlalchemy import update, delete

from flask_login import current_user, login_required

from app.Area.views import query2json as queryArea

def query2json(q, u, a):

    dUser = {}
    dArea = {}

    for el in u:
        dUser[el.id] = el
    
    dataArea = queryArea(a, u, q)
    for el in dataArea:
        dArea[el['id']] = el

    data = []
    for el in q:
        d = {}
        d['user'] = {
            "id": dUser[el.user_id].id,
            "nome": dUser[el.user_id].nome,
            "email": dUser[el.user_id].email
        }
        d['area'] = {
            "id": dArea[el.area_id]['id'],
            "user": {
                "id": dUser[el.user_id].id,
                "nome": dUser[el.user_id].nome,
                "email": dUser[el.user_id].email
            },
            "nome": dArea[el.area_id]['nome'],
            "descricao": dArea[el.area_id]['descricao'] ,
            "lotacao_max": dArea[el.area_id]['lotacao_max'] ,
            "horario": {
                "seg_ini": dArea[el.area_id]['horario']['seg_ini'],
                "seg_fim": dArea[el.area_id]['horario']['seg_fim'],
                "ter_ini": dArea[el.area_id]['horario']['ter_ini'],
                "ter_fim": dArea[el.area_id]['horario']['ter_fim'],
                "qua_ini": dArea[el.area_id]['horario']['qua_ini'],
                "qua_fim": dArea[el.area_id]['horario']['qua_fim'],
                "qui_ini": dArea[el.area_id]['horario']['qui_ini'],
                "qui_fim": dArea[el.area_id]['horario']['qui_fim'],
                "sex_ini": dArea[el.area_id]['horario']['sex_ini'],
                "sex_fim": dArea[el.area_id]['horario']['sex_fim'],
                "sab_ini": dArea[el.area_id]['horario']['sab_ini'],
                "sab_fim": dArea[el.area_id]['horario']['sab_fim'],
                "dom_ini": dArea[el.area_id]['horario']['dom_ini'],
                "dom_fim": dArea[el.area_id]['horario']['dom_fim'],
            },
            "modalidade": dArea[el.area_id]['modalidade'],
            "geojson": {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [str(dArea[el.area_id]['geojson']['geometry']['coordinates'][0]), str(dArea[el.area_id]['geojson']['geometry']['coordinates'][0])]
                }
            },
            "lotacao_atual": dArea[el.area_id]['lotacao_atual']

        }
        data.append(d)
    return data

class ParticipacaoView(Resource):
    
    def __init__(self):
        pass

    @login_required
    def get(self):
        curr_user = current_user
        
        data = []
        data_json = []
        
        dataUser = UserModel.query.all()
        dataArea = AreaModel.query.all()
        data = ParticipacaoModel.query.filter(ParticipacaoModel.user_id==curr_user.id).all()
        data_json = query2json(data, dataUser, dataArea)
        
        return json_response(data=data_json, message="Lista de todas as areas cadastradas!", status=200)

    @login_required
    def post(self):
        curr_user = current_user
        data = request.get_json()

        model = ParticipacaoModel(
            user_id=curr_user.id,
            area_id=data['area_id']
        )

        print(model)
        # print(model.latitude, type(model.latitude))

        db_session.add(model)
        db_session.commit()
        
        return json_response(message="Participacao cadastrada com sucesso!", status=200)

    @login_required
    def delete(self):

        data = request.get_json()

        dele = delete(ParticipacaoModel).where(
            (ParticipacaoModel.area_id == data['area_id']) 
            &
            (ParticipacaoModel.user_id == current_user.id))
        db_session.execute(dele)
        db_session.commit()
        
        return json_response(message="area deletada com succeso", status=200)
