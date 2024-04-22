
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.db import Base

class Employee(Base):
    
    __tablename__ = 'Employees'

    id = Column(Integer, primary_key=True, autoincrement=True, name='Employee_id')

    salary = Column(String(length=25), nullable=False, name='Salary_employee')
    start_date = Column(Date(), nullable=False, name='Date_of_hire')
    end_date = Column(Date(), nullable=True, name='Finish_date')

    company_id = Column(Integer(), ForeignKey('Companies.Company_id'), nullable=False, name='Company_id')
    user_id = Column(Integer(), ForeignKey('Users.User_id'), nullable=False, name='User_id')

    company = relationship("Company", back_populates="employees")
    user = relationship("User", backref="employees")

    def __init__(self, company_id:int, user_id:int, salary:str, start_date, end_date):

        self.company_id = company_id
        self.user_id = user_id
        self.salary = salary
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'user_id': self.user_id,
            'salary': self.salary,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d') if self.end_date else None
        }
