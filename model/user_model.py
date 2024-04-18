from datetime import datetime
from db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ ='Users'
    
    id = Column(Integer, primary_key=True,autoincrement=True, name='User_id')
    first_name = Column(String(length=25), nullable=False, name='First_name')
    last_name = Column(String(length=25), nullable=False, name='Last_name')
    username = Column(String(length=15), unique=True, 
                    nullable=False, name='Username')
    password = Column(String(length=266), nullable=False, name='Password')
    birthdate = Column(Date(), nullable=False, name='Birthdate')
    created_ad = Column(DateTime(), default=datetime.now(),
                        nullable=False, name='Register_date')
    
    def __init__(self, first_name:str, last_name:str, username:str, password:str, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password =  password
        self.birthdate = birthdate
        
    def to_dict(self):
        return {
            'id': self.id,
            'full_name':f'{self.first_name} {self.last_name}',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'birthdate': self.birthdate,
            'created_ad': self.created_ad,
            'data': self.data.to_dict() if self.data else None
        }