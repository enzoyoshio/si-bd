#from crypt import methods
import email
from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base
from flask_login import UserMixin

class UserModel(Base, UserMixin):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    password = Column(String(256))
    email = Column(String(256), unique=True)

    def __init__(self, password= None, nome = None, email = None):
        self.password = password
        self.email = email
        self.nome = nome

    def __repr__(self):
        return f'<User: {self.email}'


