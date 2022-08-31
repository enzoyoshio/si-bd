from os import stat
from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse

from app.core.database import db_session
from app.Login.models import LoginModel
from app.Login.schemas import LoginSchema

from sqlalchemy import update, delete

class LoginView(Resource):

    def __init__(self):
        self.teste = ''
    
    def querry2json(self, q):
        data = []
        for el in q:
            d = {}
            d["id"] = el.id
            d["usuario"] = el.usuario
            d["senha"] = el.senha
            data.append(d)
        return data
    
    def get(self):
        data = []
        data_json = []

        return json_response(data=data_json, message = "Lista todos os usuários cadastrados", status = 200)

    def post (self):
        data = request.get_json()

        model = LoginModel(
            usuaio = data["usuaio"],
            senha = data["senha"]
        )

        print(model)
        
        db_session.add(model)
        db_session.commit()

        return json_response(data=data, message = "Usuário cadastrado com sucesso!", status = 200)
    
    def put (self, login_id):
        data = request.get_json()

        up = update(LoginModel).where(LoginModel.id == login_id)
        db_session.execute(up)
        db_session.commit()

        return json_response(message="Usuário atualizado com sucesso", status=200)

