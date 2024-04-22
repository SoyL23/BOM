from sqlalchemy import Column, Integer, Date, JSON, DECIMAL, ForeignKey, Table
from sqlalchemy.orm import relationship
from db.db import Base

association_table = Table('Shoppings-Courses', Base.metadata,
    Column('shopping_id', Integer, ForeignKey('Shoppings.Shopping_id')),
    Column('course_id', Integer, ForeignKey('Courses.Course_id'))
)

class Shopping(Base):
    
    __tablename__ = 'Shoppings'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Shopping_id')
    date = Column(Date(), nullable=False, name='Shopping_date')
    quantity = Column(Integer(), nullable=False, name='Quantity')
    total = Column(DECIMAL(precision=10, scale=2), nullable=False, name='Total')
    id_courses = Column(JSON(), nullable=False, name='Id_courses')
    client_id = Column(Integer(), ForeignKey('Clients.Client_id'), nullable=False, name='Client_id')

    courses = relationship('Course', secondary=association_table, backref='shoppings')

    def __init__(self, date, id_courses, quantity, total, client_id):
        self.date = date
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
