from contextlib import redirect_stderr
from app import app
from app.core.database import init_db
from app.core.database import db_session, engine 
from app.Area.models import AreaModel
from app.Login.models import LoginModel
from flask import (session, request, render_template, redirect, url_for, g)

# from config import config

if __name__ == '__main__':
    # app.config.from_object(config['development'])
    
    # run this if you need to change columns
    # AreaModel.__table__.drop(engine)
    # LoginModel.__table__.drop(engine)
    init_db()
    app.run(debug=True)


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
    
    