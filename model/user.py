from datetime import datetime
from werkzeug.security import check_password_hash
from model.role import Role
from model.doc_type import Doc_Type
from config.db import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    document_number = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

    doc_type_id = db.Column(db.Integer, db.ForeignKey('Doc_Type.id'))
    doc_type = db.relationship('Doc_Type', backref='users')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')

    created_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self,first_name:str,last_name:str,document_number:str, email:str, password:str, role_id:int, doc_type_id:int):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.document_number = document_number
        self.email = email
        self.password = password
        self.role_id = role_id
        self.doc_type_id = doc_type_id

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "doc_type": self.document_type,
            "doc_num":self.document_number,
            "email": self.email,
            "role": self.role.to_dict()['role'],
            "created_date": self.created_date
        }
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)