from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import *


class Company(Base):

    __tablename__ = 'Companies'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Company_id')
    name = Column(String(length=25), nullable=False, name='Company_name')
    nit = Column(String(length=25), nullable=False, name='Company_nit')
    email = Column(String(length=25), nullable=False, name='Contact_email')
    phone = Column(String(length=25), nullable=False, name='Phone_number')

    employees = relationship("Employee", back_populates="company")

    def __init__(self, name:str, nit:str, email:str, phone:str):
        self.name = name
        self.nit = nit
        self.email = email
        self.phone = phone
        

    def to_dict(self):
        return{
            'name':f'{self.name}',
            'nit':f'{self.nit}',
            'email':f'{self.email}',
            'phone_number':f'{self.phone}'
        }