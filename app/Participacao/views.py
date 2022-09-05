from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Participacao.models import ParticipacaoModel
# from app.Area.schemas import AreaSchema

from sqlalchemy import update, delete

from flask_login import current_user, login_required


def query2json(q):
    data = []
    for el in q:
        d = {}
        d["user_id"] = el.user_id
        d["area_id"] = el.area_id
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
        
        data = ParticipacaoModel.query.filter(ParticipacaoModel.user_id==curr_user.id).all()
        data_json = query2json(data)
        
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
