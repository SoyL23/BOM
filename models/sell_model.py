from sqlalchemy import Table, Column, Integer, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from db.db import Base

association_table = Table('Sells_Courses', Base.metadata,
    Column('sell_id', Integer, ForeignKey('Sells.sell_id')),
    Column('course_id', Integer, ForeignKey('Courses.Course_id'))
)

class Sell(Base):

    __tablename__ = 'Sells'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='sell_id')
    date = Column(Date(), name='Sell_date', nullable=False)
    total = Column(DECIMAL(precision=10, scale=2), name='Sell_total', nullable=False)
    client_id = Column(Integer(), ForeignKey('Clients.Client_id'), name='Client_id', nullable=False)
    seller_id = Column(Integer(), ForeignKey('Employees.Employee_id'), name='Seller_id', nullable=False)

    courses = relationship('Course', secondary=association_table, backref='sells')

    def __init__(self, date, total: float, client_id: int, seller_id: int):
        self.date = date
        self.total = total
        self.client_id = client_id
        self.seller_id = seller_id

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'total': float(self.total),
            'client_id': self.client_id,
            'seller_id': self.seller_id
        }
