from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from models.role_model import Role
from models.user_model import User
from models.city_model import City

class User_Data(Base):

    __tablename__ = 'Users_Data'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Data_id')
    email = Column(String(length=50), nullable=False, unique=True, name='Email_User')
    document_number = Column(String(length=15), nullable=False, name='Document_Number')
    document_type = Column(Enum( 'Cedula_Ciudadanía' , 'Cedula_Extranjería' ,
                                'Pasaporte' , 'NIT', 'PEP' ), nullable=False, name='Document_Type')
    document_city = Column(Integer(), ForeignKey('Cities.City_id'), nullable=False, name='City_Document')
    city_document = relationship(City, backref='documents', primaryjoin='User_Data.document_city == City.id')

    role_id = Column(Integer(), ForeignKey('Roles.Role_id'), nullable=False, name='role_id')
    role = relationship(Role, back_populates='user_data', uselist=False)

    user_id = Column(Integer(), ForeignKey('Users.User_id'), nullable=False, name='User_id')
    user = relationship(User, backref='data')

    city_id = Column(Integer(), ForeignKey('cities.City_id'), nullable=False, name='City_id')
    city = relationship(City, backref='Users')

    def __init__(self, email:str, document_number:int):
        self.email = email
        self.document_number = document_number
    
    def to_dict(self):
        return {
            'email': self.email,
            'document_type': self.document_type,
            'document_number': self.document_number,
            'role': self.role.to_dict() if self.role else None
        }
