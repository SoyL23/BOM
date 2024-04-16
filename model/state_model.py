from db.db import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class State(Base):

    __tablename__ = 'States'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='State_id')
    name = Column(String(50), nullable=False, name='State_name')
    description = Column(Text(), nullable=False, name='State_description')
    code = Column(String(4), nullable=True, name='State_code')

    country_id = Column(Integer(), ForeignKey('Countries.Country_id'),
                        nullable=False, name='Country_id')
    
    country = relationship("Country", back_populates="states",lazy='dynamic')

    cities = relationship('City', back_populates='state',  lazy='dynamic')

    def __init__(self, name:str, description:str, code:str, country_id:str):
        self.name = name
        self.description = description
        self.code = code
        self.country_id = country_id

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'code': self.code,
            'country': self.country.to_dict()['name']
        }