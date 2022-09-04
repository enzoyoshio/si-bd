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
    horario_seg_ini = Column(String(40))
    horario_seg_fim = Column(String(40))
    horario_ter_ini = Column(String(40))
    horario_ter_fim = Column(String(40))
    horario_qua_ini = Column(String(40))
    horario_qua_fim = Column(String(40))
    horario_qui_ini = Column(String(40))
    horario_qui_fim = Column(String(40))
    horario_sex_ini = Column(String(40))
    horario_sex_fim = Column(String(40))
    horario_sab_ini = Column(String(40))
    horario_sab_fim = Column(String(40))
    horario_dom_ini = Column(String(40))
    horario_dom_fim = Column(String(40))

    def __init__(
                self, 
                nome=None, 
                descricao=None, 
                latitude=None,
                longitude=None,
                lotacao_max=None, 
                modalidade=None,
                horario_seg_ini=None,
                horario_seg_fim=None,
                horario_ter_ini=None,
                horario_ter_fim=None,
                horario_qua_ini=None,
                horario_qua_fim=None,
                horario_qui_ini=None,
                horario_qui_fim=None,
                horario_sex_ini=None,
                horario_sex_fim=None,
                horario_sab_ini=None,
                horario_sab_fim=None,
                horario_dom_ini=None,
                horario_dom_fim=None
                ):
        self.nome = nome
        self.descricao = descricao
        self.lotacao_max = lotacao_max
        self.modalidade = modalidade
        self.horario_seg_ini=horario_seg_ini
        self.horario_seg_fim=horario_seg_fim
        self.horario_ter_ini=horario_ter_ini
        self.horario_ter_fim=horario_ter_fim
        self.horario_qua_ini=horario_qua_ini
        self.horario_qua_fim=horario_qua_fim
        self.horario_qui_ini=horario_qui_ini
        self.horario_qui_fim=horario_qui_fim
        self.horario_sex_ini=horario_sex_ini
        self.horario_sex_fim=horario_sex_fim
        self.horario_sab_ini=horario_sab_ini
        self.horario_sab_fim=horario_sab_fim
        self.horario_dom_ini=horario_dom_ini
        self.horario_dom_fim=horario_dom_fim
        self.latitude=latitude
        self.longitude=longitude
    
    def __repr__(self):
        return f"<Area {self.nome}!\nDescrição:{self.descricao}\n" + f"Capacidade máxima: {self.lotacao_max}\nModalidade: {self.modalidade}\n" + f"lati: {self.latitude}\nLon: {self.longitude}\n"