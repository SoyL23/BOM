from models.company_model import Company
from db.db import Base
from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
class Course(Base):

    __tablename__ = 'Courses'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Course_id')
    name = Column(String(length=50), nullable=False, name='Course_Name')
    price = Column(DECIMAL(precision=10, scale=2), nullable=False, name='Course_Price')
    description = Column(Text, nullable=True, name='Description_Course')
    duration = Column(String(length=50), nullable=False, name='Course_Description')

    company_id = Column(Integer(), ForeignKey('Companies.Company_id'), nullable=False, name='Company_id')
    courses = relationship(Company, backref='courses')

    
    def __init__(self, name:str, price:float, description:str, duration:str, company_id:int):
        self.name = name
        self.price = price
        self.duration = duration
        self.description = description
        self.company_id = company_id

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'duration': self.duration,
            'description': self.description
        }