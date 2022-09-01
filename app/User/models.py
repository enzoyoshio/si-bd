from crypt import methods
import email
from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base

class UserModel(Base):
    def __init__(self, id, username, senha, nome, email):
        self.id = id
        self.username = username
        self.senha = senha
        self.email = email
        self.nome = nome

    def __repr__(self):
        return f'<User: {self.username}'


