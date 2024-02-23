from config.db import db
from model.curso import Curso
from model.estudiante import Estudiante

class CursoEstudiante(db.Model):
    __tablename__ = 'cursos_estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    fecha_registro = db.Column(db.Date)
    estado = db.Column(db.String(255))

    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'))
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
