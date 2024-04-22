from db.db import Base
from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime as dt

class Evaluation(Base):

    __tablename__ = 'Evaluations'
    
    id = Column(Integer(), primary_key=True, autoincrement=True, name='Evaluation_id')
    date =  Column(DateTime(), default=dt.now(), nullable=False, name='Evaluation_date')
    score = Column(DECIMAL(precision=5, scale=2), nullable=False, name='Evaluation_Score')
    status = Column(Enum('In_progress', 'Approved', 'Reprobate'), nullable=False, name='Evaluation_Status')
    questions = Column(Text(), nullable=False, name='Evaluation_Questions')

    course_id = Column(Integer(), ForeignKey('Courses.Course_id'), nullable=False, name='Course_id')
    course = relationship('Course', backref='evaluations')

    student_id = Column(Integer(), ForeignKey('Users.User_id'), nullable=False, name='Student_id')
    student = relationship('User', backref='evaluations')

    def __init__(self, score:float, status:str, questions:str, course_id:int, student_id:int):
        self.score = score
        self.status = status
        self.questions = questions
        self.course_id = course_id
        self.student_id = student_id

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S'),
            'score': self.score,
            'status': self.status,
            'questions': self.questions,
            'course_id': self.course_id,
            'student_id': self.student_id.to_dict()['full_name']
        }
