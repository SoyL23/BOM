from config.db import db
class ResultadoEvaluacion(db.Model):
    __tablename__ = 'resultados_evaluaciones'

    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Float)
    respuestas = db.Column(db.json)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'))
    evaluacion_id = db.Column(db.Integer, db.ForeignKey('evaluaciones.id'))