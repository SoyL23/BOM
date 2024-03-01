from config.db import db
class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)
    role_description = db.Column(db.String(255))

    def __init__(self, role_name, role_description):
        self.role_name = role_name
        self.role_description = role_description

    def __repr__(self):
        return f'{self.role_name}'
    
    def to_dict(self):
        return {
            "role": self.role_name,
        }