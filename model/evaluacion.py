from config.db import db
from model.curso import Curso
class Evaluacion(db.Model):
    __tablename__ = 'evaluaciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(255))
    fecha = db.Column(db.Date)
    duracion = db.Column(db.Integer)
    calificacion_minima = db.Column(db.Float)

    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))