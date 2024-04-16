from db.db import Base
from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

class Certificate(Base):
    
    __tablename__ = 'Certificates'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Certificate_id')
    date = Column(Date(), name='Certificate_date')
    status = Column(Enum('Certified','In_Progress', 'No_pay'), nullable=False,  name='Certificate_status')
    company_id = Column(Integer(), ForeignKey('Companies.Company_id'), nullable=False,  name='Company_id')
    course_id = Column(Integer(), ForeignKey('Courses.Course_id'), nullable=False,  name='Course_id')
    student_id = Column(Integer(), ForeignKey('Users.User_id'), nullable=False,  name='Student_id')
    
    def __init__(self, date, status:str, company_id:int, course_id:int, student_id:int):
        self.date = date
        self.status = status
        self.company_id = company_id
        self.course_id = course_id
        self.student_id = student_id

    def to_dict(self):
        return {
            'id': self.id,
            'date': str(self.date),
            'status': self.status,
            'company_id': self.company_id,
            'course_id': self.course_id,
            'student_id': self.student_id
        }