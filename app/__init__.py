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
from app.User.views import SigninView, SignupView, SignoutView, UserView, UserViewId

# @app.route("/")
# def home():
#     return "Hello, si-bd!"

api.add_resource(HelloWorldView, '/hello')

api.add_resource(AreaView, '/areas')
api.add_resource(AreaViewId, '/areas/<area_id>')

api.add_resource(SigninView, '/auth/Signin')
api.add_resource(SignupView, '/auth/signup')
api.add_resource(SignoutView, '/auth/Signout')
api.add_resource(UserView, '/users/<user_id>')
api.add_resource(UserViewId, '/users')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

#pro login
app.secret_key = 'segredoSecretoDoF4s71N0'

@app.before_request
def before_request(data):
    g.user = None
    if 'user_id' in session:
        aux = [x for x in data if x.id == session['user_id']] 
        if(len(aux) == 0):
            return 0 #não sei o q retorna então retornei 0
        user = aux[0]
        g.user =user


@app.route('/login', methods = ['GET', 'POST'])
def login(data):
    if request.method == 'POST' :
        session.pop('user_id', None)
        username = request.form['username']
        senha = request.form['senha']

        aux = [x for x in data if x.username == username]
        if(len(aux) == 0):
            return 0 #não sei o q retorna então retornei 0
        user = aux[0]
        if(user and user.senha == senha):
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/pofile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('login.html')