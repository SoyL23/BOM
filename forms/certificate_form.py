from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SelectField, IntegerField
from wtforms.validators import DataRequired

class Certificate_Form(FlaskForm):
    class Meta:
        csrf = False

    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired(message='Date is required')])
    status_choices = [('Certified', 'Certified'), ('In_Progress', 'In Progress'), ('No_pay', 'No Pay')]
    status = SelectField('Status', choices=status_choices, validators=[DataRequired(message='Status is required')])
    company_id = IntegerField('Company_ID', validators=[DataRequired(message='Company ID is required')])
    course_id = IntegerField('Course_ID', validators=[DataRequired(message='Course ID is required')])
    student_id = IntegerField('Student_ID', validators=[DataRequired(message='Student ID is required')])
