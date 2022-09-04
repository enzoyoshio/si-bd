from flask import Flask 
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.database import db_session 

app = Flask(__name__)
api = Api(app, prefix='/api')

from app.HelloWorld.views import HelloWorldView
from app.Area.views import AreaView, AreaViewId

# @app.route("/")
# def home():
#     return "Hello, si-bd!"

api.add_resource(HelloWorldView, '/hello')
api.add_resource(AreaView, '/areas')
api.add_resource(AreaViewId, '/areas/<area_id>')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()