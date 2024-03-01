from config.db import db

class Doc_Type(db.Model):

    __tablename__ = 'Doc_Type'

    id = db.Column(db.Integer, primary_key=True)
    type_doc_name = db.Column(db.String(50), nullable=False)
    type_doc_description = db.Column(db.String(255))

    def __init__(self, type_doc_name, type_doc_description):
        self.type_doc_name = type_doc_name
        self.type_doc_description = type_doc_description

    def __repr__(self):
        return f'{self.type_doc_name}'
    
    def to_dict(self):
        return {
            "doc_type": self.type_doc_name,
        }