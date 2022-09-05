from app import app
from app.core.database import init_db
from app.core.database import db_session
from app.User.models import UserModel
from app.Area.models import AreaModel
from app.core.database import engine

# from config import config

if __name__ == '__main__':
    # app.config.from_object(config['development'])
    
    # run this if you need to change columns
    # AreaModel.__table__.drop(engine)
    # UserModel.__table__.drop(engine)
    init_db()
    app.run(debug=True)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()