from config.db import db
from model.institucion import Institucion
from model.evaluacion import Evaluacion
from model.curso_estudiante import CursoEstudiante

class Curso(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    duracion = db.Column(db.Integer)
    costo = db.Column(db.Float)
    requisitos = db.Column(db.Text)

    institucion_id = db.Column(db.Integer, db.ForeignKey('instituciones.id'))
    evaluaciones = db.relationship('Evaluacion', backref='curso')
    estudiantes_inscritos = db.relationship('CursoEstudiante', backref='curso')