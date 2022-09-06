from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Area.models import AreaModel
from app.User.models import UserModel
# from app.Area.schemas import AreaSchema

from flask_login import current_user, login_required

from sqlalchemy import update, delete

def query2json(q, u):
    dUser = {}
    for el in u:
        dUser[el.id] = el
    data = []
    for el in q:
        d = {}
        d["id"] = el.id 
        d["user"] = {
            "id": dUser[el.user_id].id,
            "nome": dUser[el.user_id].nome,
            "email": dUser[el.user_id].email
        }
        d["nome"]=el.nome 
        d["descricao"]=el.descricao 
        d["lotacao_max"]=el.lotacao_max 
        d["horario"] = {
            "seg_ini": el.horario_seg_ini,
            "seg_fim": el.horario_seg_fim,
            "ter_ini": el.horario_ter_ini,
            "ter_fim": el.horario_ter_fim,
            "qua_ini": el.horario_qua_ini,
            "qua_fim": el.horario_qua_fim,
            "qui_ini": el.horario_qui_ini,
            "qui_fim": el.horario_qui_fim,
            "sex_ini": el.horario_sex_ini,
            "sex_fim": el.horario_sex_fim,
            "sab_ini": el.horario_sab_ini,
            "sab_fim": el.horario_sab_fim,
            "dom_ini": el.horario_dom_ini,
            "dom_fim": el.horario_dom_fim,
        }
        d["modalidade"]=el.modalidade
        d["geojson"] = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [str(el.longitude), str(el.latitude)]
            }
        }
        data.append(d)
    return data

class AreaView(Resource):
    
    def __init__(self):
        pass

    @login_required
    def get(self):
        curr_user = current_user

        print(">>>>>>>>>>>>>>>>")
        print(curr_user.id)
        data = []
        data_json = []
        
        dataUser = UserModel.query.all()
        data = AreaModel.query.all()
        data_json = query2json(data, dataUser)
        
        return json_response(data=data_json, message="Lista de todas as areas cadastradas!", status=200)

    @login_required
    def post(self):
        curr_user = current_user
        data = request.get_json()

        model = AreaModel(
            nome=data['nome'], 
            descricao=data['descricao'], 
            lotacao_max=data['lotacao_max'], 
            modalidade=data['modalidade'],
            horario_seg_ini=data['horario']['seg_inicio'],
            horario_seg_fim=data['horario']['seg_fim'],
            horario_ter_ini=data['horario']['ter_inicio'],
            horario_ter_fim=data['horario']['ter_fim'],
            horario_qua_ini=data['horario']['qua_inicio'],
            horario_qua_fim=data['horario']['qua_fim'],
            horario_qui_ini=data['horario']['qui_inicio'],
            horario_qui_fim=data['horario']['qui_fim'],
            horario_sex_ini=data['horario']['sex_inicio'],
            horario_sex_fim=data['horario']['sex_fim'],
            horario_sab_ini=data['horario']['sab_inicio'],
            horario_sab_fim=data['horario']['sab_fim'],
            horario_dom_ini=data['horario']['dom_inicio'],
            horario_dom_fim=data['horario']['dom_fim'],
            latitude=data['lat'],
            longitude=data['long'],
            user_id=curr_user.id
        )

        print(model)
        # print(model.latitude, type(model.latitude))

        db_session.add(model)
        db_session.commit()
        
        return json_response(message="area cadastrada com sucesso!", status=200)

        def put(self):
            return json_response(message="metodo nao permitido.", status=405)

        def delete(self):
            return json_response(message="metodo nao permitido.", status=405)

class AreaViewId(Resource):

    def __init__(self):
        pass

    def get(self, area_id):
        data = []
        data_json = []
        # if area_id == 0:
        # data = AreaModel.query.all()
        # data_json = query2json(data)
        # else:
        data = AreaModel.query.filter(AreaModel.id == area_id).first()
        if(data == None): 
            return json_response(message="id nao encontrado", status=404) 
        data_json = query2json([data])
        return json_response(data=data_json, message="Lista de todas as areas cadastradas!", status=200)

    def post(self, area_id):
        return json_response(message="metodo nao permitido.", status=405)

    def put(self, area_id):
        data = request.get_json()
 
        up = update(AreaModel).where(AreaModel.id==area_id).values(data)
        db_session.execute(up)
        db_session.commit()
        
        return json_response(message="area atualizada com sucesso!", status=200)
    
    def delete(self, area_id):

        dele = delete(AreaModel).where(AreaModel.id == area_id)
        db_session.execute(dele)
        db_session.commit()
        
        return json_response(message="area deletada com succeso", status=200)

class UserAreaView(Resource):

    def __init__(self):
        pass

    @login_required
    def get(self):
        curr_user = current_user

        print(">>>>>>>>>>>>>>>>")
        print(curr_user.id)
        data = []
        data_json = []
        
        dataUser = UserModel.query.all()
        data = AreaModel.query.filter(AreaModel.user_id == curr_user.id).all()
        data_json = query2json(data, dataUser)
        
        return json_response(data=data_json, message="Lista de todas as areas cadastradas!", status=200)


# { 
#     "user_id": 1,
#     "nome": "area teste", 
#     "descricao": "desc teste", 
#     "lotacao_max": 100, 
#     "horario": {
#         "seg_ini": "12:00",
#         "seg_fim": "12:00",
#         "ter_ini": "12:00",
#         "ter_fim": "12:00",
#         "qua_ini": "12:00",
#         "qua_fim": "12:00",
#         "qui_ini": "12:00",
#         "qui_fim": "12:00",
#         "sex_ini": "12:00",
#         "sex_fim": "12:00",
#         "sab_ini": "12:00",
#         "sab_fim": "12:00",
#         "dom_ini": "12:00",
#         "dom_fim": "12:00"
#     },
#     "modalidade": "horta",
#     "geojson": {
#         "type": "Feature",
#         "Geometry": {
#             "type": "Point",
#             "coordinates": [10.92175, 97.328475]
#         }
#     }
# }