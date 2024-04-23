from db.db import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.state_model import State

class City(Base):

    __tablename__ = 'Cities'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='City_id')
    name = Column(String(length=50), nullable=False, name='City_name')
    description = Column(Text(), nullable=False, name='City_description')
    code = Column(String(length=4), nullable=True, name='City_code')

    state_id = Column(Integer(), ForeignKey('States.State_id'), nullable=False, name='State_id')
    state = relationship(State, back_populates='cities', uselist=False)

    def __init__(self, name:str, description:str, code:str, state_id:int):
        self.name = name
        self.description = description
        self.code = code
        self.state_id = state_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'code': self.code,
            'state': self.state.to_dict()['name']
        }

    
    