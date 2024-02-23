from config.db import db
from model.curso_estudiante import CursoEstudiante

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    numero_identificacion = db.Column(db.String(255), unique=True)
    correo_electronico = db.Column(db.String(255))
    telefono = db.Column(db.String(255))
    direccion = db.Column(db.Text)

    cursos_inscritos = db.relationship('CursoEstudiante', backref='estudiante')