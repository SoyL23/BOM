from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from model.role_model import Role
from model.user_model import User
from model.city_model import City
# from model.doc_type_model import Doc_Type

class User_Data(Base):

    __tablename__ = 'Users_Data'

    id = Column(Integer(), primary_key=True, autoincrement=True, name='Data_id')
    email = Column(String(length=50), nullable=False, unique=True, name='Email_User')
    document_number = Column(String(length=15), nullable=False, name='Document_Number')
    document_type = Column(Enum( 'Cedula_Ciudadanía' , 'Cedula_Extranjería' ,
                                'Pasaporte' , 'NIT', 'PEP' ), nullable=False, name='Document_Type')
    document_city = Column(Integer(), ForeignKey('Cities.City_id'), nullable=False, name='City_Document')
    city_document = relationship(City, backref='documents')

    role_id = Column(Integer(), ForeignKey('Roles.Role_id'), nullable=False, name='role_id')
    role = relationship(Role, back_populates='user_data', uselist=False)

    user_id = Column(Integer(), ForeignKey('Users.User_id'), nullable=False, name='User_id')
    user = relationship(User, backref='data')

    city_id = Column(Integer(), ForeignKey('Cities.City_id'), nullable=False, name='City_id')
    city = relationship(City, backref='Users')

    def __init__(self, email:str, document_number:int):
        self.email = email
        self.document_number = document_number
    
    def to_dict(self):
        return {
            'email': self.email,
            'document_type': self.document_type.to_dict() if self.document_type else None,
            'document_number': self.document_number,
            'role': self.role.to_dict() if self.role else None
        }
