from flask import Flask 
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
api = Api(app, prefix='/api')

from app.HelloWorld.views import HelloWorldView

# @app.route("/")
# def home():
#     return "Hello, si-bd!"

api.add_resource(HelloWorldView, '/hello')