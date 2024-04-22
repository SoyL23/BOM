from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class Evaluation_Form(FlaskForm):
    class Meta:
        csrf = False
    score = DecimalField('Score', 
                        validators=[DataRequired(message='Score is required')])
    status = SelectField('Status', 
                        choices=[('In_progress', 'In Progress'), ('Approved', 'Approved'), ('Reprobate', 'Reprobate')],
                        validators=[DataRequired(message='Status is required')])
    questions = TextAreaField('Questions', 
                            validators=[DataRequired(message='Questions are required')])
    course_id = IntegerField('Course_ID',
                            validators=[DataRequired(message='Course ID is required')])
    student_id = IntegerField('Student_ID',
                            validators=[DataRequired(message='Student ID is required')])
