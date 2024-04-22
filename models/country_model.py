from db.db import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

class Country(Base):

    __tablename__ = 'Countries'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Country_id')
    name = Column(String(56), nullable=False, name='Country_name')
    description = Column(Text(), nullable=False, name='Country_description')
    code = Column(String(4), nullable=True, name='Country_code')
    states = relationship("State", back_populates="country", uselist=True)

    def __init__(self, name:str, description:str, code:str):
        self.name = name
        self.description = description,
        self.code = code

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'code': self.code,
        }