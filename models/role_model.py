from db.db import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

class Role(Base):
    
    __tablename__ = 'Roles'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Role_id')
    name = Column(String(length=50), nullable=False, name='Role_name')
    description = Column(Text(), nullable=False, name='Role_description')
    functions = Column(Text(), nullable=True, name='Role_functions')
    user_data = relationship('User_Data', back_populates='role',  lazy='dynamic')

    def __init__(self, name:str, description:str, functions:str):
        self.name = name
        self.description = description
        self.functions = functions

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'functions': self.functions
        }