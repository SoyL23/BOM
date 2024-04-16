from sqlalchemy import Column, Integer, Date, DECIMAL, JSON, ForeignKey
from sqlalchemy.orm import relationship
from db.db import Base

class Sell(Base):

    __tablename__ = 'Sells'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='sell_id')
    date = Column(Date(), name='Sell_date', nullable=False)
    total = Column(DECIMAL(precision=10, scale=2), name='Sell_total', nullable=False)
    client_id = Column(Integer(), ForeignKey('Clients.Client_id'), name='Client_id', nullable=False)
    id_courses = Column(JSON(), name='Id_courses', nullable=False)
    seller_id = Column(Integer(), ForeignKey('Employees.Employee_id'), name='Seller_id', nullable=False)

    courses = relationship('Course', primaryjoin='Sell.id_courses.any_() == Course.id')

    def __init__(self, date, total:float, client_id:int, id_courses:list, seller_id:int):
        self.date = date
        self.total = total
        self.client_id = client_id
        self.id_courses = id_courses
        self.seller_id = seller_id

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'total': float(self.total),
            'client_id': self.client_id,
            'id_courses': self.id_courses,
            'seller_id': self.seller_id
        }
