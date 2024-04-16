from sqlalchemy import Column, Integer, Date, JSON, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from db.db import Base

class Shopping(Base):
    
    __tablename__ = 'Shoppings'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Shopping_id')
    date = Column(Date(), nullable=False, name='Shopping_date')
    quantity = Column(Integer(), nullable=False, name='Quantity')
    total = Column(DECIMAL(precision=10, scale=2), nullable=False, name='Total')
    id_courses = Column(JSON(), nullable=False, name='Id_courses')
    client_id = Column(Integer(), ForeignKey('Clients.Client_id'), nullable=False, name='Client_id')

    courses = relationship('Course', primaryjoin='Shopping.id_courses.any_() == Course.id')

    def __init__(self, date, id, id_courses, quantity, total, client_id):
        self.date = date
        self.id = id
        self.id_courses = id_courses
        self.quantity = quantity
        self.total = total
        self.client_id = client_id

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'id_courses': self.id_courses,
            'quantity': self.quantity,
            'total': str(self.total),
            'client_id': self.client_id
        }
