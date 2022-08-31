from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base

class LoginModel(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50)) # unique=True ?
    senha = Column(String(50))

    def __init__(
                self,
                usuario=None,
                senha=None
                ):
        self.usuario = usuario
        self.senha = senha
    
    def __repr__(self):
        return f"<Usuaio {self.usuario}>! \n Senha: {self.senha}\n"
