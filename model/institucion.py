from config.db import db

class Institucion(db.Model):
    __tablename__ = 'instituciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    sitio_web = db.Column(db.String(255))
    correo_electronico = db.Column(db.String(255))

    cursos = db.relationship('Curso', backref='institucion')