from sqlalchemy import Column, Integer, Enum, ForeignKey
from db.db import *
from sqlalchemy.orm import relationship

class Client(Base):
    
    __tablename__ = 'Clients'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Client_id')
    type_client = Column(Enum('Company', 'Person'), nullable=True, name='Type_Client')

    company_id = Column(Integer(), ForeignKey('Companies.Company_id'), nullable=True, name='Company_Client')
    user_id = Column(Integer(), ForeignKey('Users.User_id'), nullable=True, name='User_Client')

    company = relationship("Company", back_populates="clients")
    user = relationship("User", back_populates="clients")

    def __init__(self, type_client:str, id_client:int):
        self.type_client = type_client

        if self.type_client == 'Company':
            self.company_id = id_client
        elif self.type_client == 'Person':
            self.user_id = id_client

    def to_dict(self):
        return {
            'id': self.id,
            'type_client': self.type_client,
            'client_id': self.company_id if  self.company_id else self.user_id
        }