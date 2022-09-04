from sqlalchemy import Column, Integer, String, Numeric
from app.core.database import Base

from app.Area.models import AreaModel
from app.User.models import UserModel

class ParticipacaoModel(Base):
    __tablename__ = 'participacoes'
    id = Column(Integer, primary_key=True) # do I need this?
    area_id = Column(Integer, ForeignKey("areas.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    def __init__(
                self,
                area_id,
                user_id
                ):
        self.area_id = area_id
        self.user_id = user_id

    def __repr__(self):
        return "isso eh uma participacao"