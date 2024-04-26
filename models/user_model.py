from datetime import datetime
from db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import column_property
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash

class User(Base):

    __tablename__ ='Users'
    
    id = Column(Integer, primary_key=True, autoincrement=True, name='User_id')
    first_name = Column(String(length=25), nullable=False, name='First_name')
    last_name = Column(String(length=25), nullable=False, name='Last_name')
    username = Column(String(length=15), unique=True, nullable=False, name='Username')
    password = Column(String(length=266), nullable=False, name='Password')
    birthdate = Column(Date(), nullable=False, name='Birthdate')
    created_ad = Column(DateTime(), default=datetime.now(), nullable=False, name='Register_date')

    @hybrid_property
    def edad(self):
        return date.today().year - self.birthdate.year - ((date.today(), self.birthdate) < (date.today(), self.birthdate))

    @property
    def data_dict(self):
        return [data.to_dict() for data in self.data] if self.data else None

    def to_dict(self):
        return {
            'id': self.id,
            'full_name': f'{self.first_name} {self.last_name}',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'birthdate': self.birthdate,
            'edad': self.edad,
            'created_ad': self.created_ad,
            'data': self.data_dict
        }
    
    def check_password(self, password:str):
        return check_password_hash(self.password, password)