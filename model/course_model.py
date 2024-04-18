from db.db import Base
from sqlalchemy import Column, Integer, String, Text, DECIMAL

class Course(Base):

    __tablename__ = 'Courses'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Course_id')
    name = Column(String(length=50), nullable=False, name='Course_Name')
    price = Column(DECIMAL(precision=10, scale=2), nullable=False, name='Course_Price')
    description = Column(Text, nullable=True, name='Description_Course')
    duration = Column(String(length=50), nullable=False, name='Course_Description')

    
    def __init__(self, name:str, price:float, description:str, duration:str):
        self.name = name
        self.price = price
        self.duration = duration
        self.description = description

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'duration': self.duration,
            'description': self.description
        }