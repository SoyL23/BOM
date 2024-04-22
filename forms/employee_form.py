from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField
from wtforms.validators import DataRequired, NumberRange, Length

class Employee_Form(FlaskForm):
    class Meta:
        csrf = False

    company_id = IntegerField('company_id', validators=[
        DataRequired(message='Company ID is required'),
        NumberRange(min=1, message='Company ID must be a positive integer')
    ])
    user_id = IntegerField('user_id', validators=[
        DataRequired(message='User ID is required'),
        NumberRange(min=1, message='User ID must be a positive integer')
    ])
    salary = StringField('salary', validators=[
        DataRequired(message='Salary is required'),
        Length(min=5, max=25, message='Between 5 and 25 characters')
    ])
    start_date = DateField('start_date', format='%Y-%m-%d', validators=[
        DataRequired(message='Start Date is required')
    ])
    end_date = DateField('end_date', format='%Y-%m-%d', validators=[
        DataRequired(message='End Date is required')
    ])
