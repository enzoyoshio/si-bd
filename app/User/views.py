from flask_restful import Resource 
from flask import request, jsonify

from app.core.util.response import json_response
from flask_restful import reqparse
from flask_login import login_user, logout_user
from app.core.database import db_session


from app.User.models import UserModel


from sqlalchemy import update, delete

def query2json(q):
    data = []
    for el in q:
        d = {}
        d["id"] = el.id 
        d["nome"]=el.nome 
        d["email"]=el.email 
        d["password"]=el.password
        data.append(d)
    return data

class UserView(Resource):
    def __init__(self):
        pass


    def get(self):
        data = []
        data_json = []
        
        data = UserModel.query.all()
        data_json = query2json(data)
        
        return json_response(data=data_json, message="Lista de todos os Usuários cadastrados!", status=200)

    

class UserViewId(Resource):
    def __init__(self):
        pass


class SigninView(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json()
        user = UserModel.query.filter(UserModel.email == data['email']).first()    
        if user is None:
            return json_response(message="O usuário não existe", status=405)
        if user.password == data['password']:
            login_user(user)
            return json_response(message="Login realizado com sucesso", status=200)
        return json_response(message="Senha incorreta", status=405)

class SignupView(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json()
        
        if data['password'] != data['password_confirm']:
            return json_response(message="A senhas não são iguais!", status=405)

        model = UserModel(
            nome = data['nome'],
            password = data['password'],
            email = data['email'],
        )
        print(">>>>>>>>>>>>>>>>>>")
        print(model)

        db_session.add(model)
        db_session.commit()
        
        return json_response(message="Usuário cadastrado com sucesso com sucesso!", status=200)




class SignoutView(Resource):
    def __init__(self):
        pass
    def post(self):
        data = request.get_json()
        logout_user()
        return json_response(message="Logout realizado com sucesso", status=200)


