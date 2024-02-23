from config.db import db
from model.estudiante import Estudiante
from model.curso import Curso

class Certificado(db.Model):
    __tablename__ = 'certificados'

    id = db.Column(db.Integer, primary_key=True)
    fecha_emision = db.Column(db.Date)

    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'))
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))