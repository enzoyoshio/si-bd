from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base

class AreaModel(Base):
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50)) # unique=True ?
    descricao = Column(String(400))
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    lotacao_max = Column(Integer, nullable=False)
    modalidade = Column(String(30))
    horario_seg = Column(String(40))
    horario_ter = Column(String(40))
    horario_qua = Column(String(40))
    horario_qui = Column(String(40))
    horario_sex = Column(String(40))
    horario_sab = Column(String(40))
    horario_dom = Column(String(40))

    def __init__(
                self, 
                nome=None, 
                descricao=None, 
                latitude=None,
                longitude=None,
                lotacao_max=None, 
                modalidade=None,
                horario_seg=None,
                horario_ter=None,
                horario_qua=None,
                horario_qui=None,
                horario_sex=None,
                horario_sab=None,
                horario_dom=None
                ):
        self.nome = nome
        self.descricao = descricao
        self.lotacao_max = lotacao_max
        self.modalidade = modalidade
        self.horario_seg = horario_seg
        self.horario_ter = horario_ter
        self.horario_qua = horario_qua
        self.horario_qui = horario_qui
        self.horario_sex = horario_sex
        self.horario_sab = horario_sab
        self.horario_dom = horario_dom
        self.latitude=latitude
        self.longitude=longitude
    
    def __repr__(self):
        return f"<Area {self.nome}!\nDescrição:{self.descricao}\n" + f"Capacidade máxima: {self.lotacao_max}\nModalidade: {self.modalidade}\n" + f"lati: {self.latitude}\nLon: {self.longitude}\n"