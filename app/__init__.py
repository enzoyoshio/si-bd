from flask import Flask 
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager
from app.core.database import db_session 
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, prefix='/api')
CORS(app, resources={r'*': {'origins': '*'}}, supports_credentials=True)

app.secret_key = 'segredoSecretoDoF4s71N0'
login_manager = LoginManager(app)

from app.HelloWorld.views import HelloWorldView
from app.Area.views import AreaView, AreaViewId
from app.User.views import SignupView, UserView, SigninView, SignoutView, UserViewId
from app.Participacao.views import ParticipacaoView

from app.User.models import UserModel

api.add_resource(HelloWorldView, '/hello')

api.add_resource(AreaView, '/areas')
api.add_resource(AreaViewId, '/areas/<area_id>')

api.add_resource(SigninView, '/auth/signin')
api.add_resource(SignupView, '/auth/signup')
api.add_resource(SignoutView, '/auth/signout')
api.add_resource(UserView, '/users')
api.add_resource(UserViewId, '/users/<user_id>')

api.add_resource(ParticipacaoView, '/participacoes')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.filter(UserModel.id==user_id).first()



