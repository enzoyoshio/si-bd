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