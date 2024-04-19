from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class Company_Form(FlaskForm):
    class Meta:
            csrf = False
            
    name = StringField('Company Name', validators=[
        DataRequired(message='Company name is required.'),
        Length(min=5, max=25, message='Company name must be between 5 and 25 characters.')
    ])
    nit = StringField('NIT', validators=[
        DataRequired(message='NIT is required.'),
        Length(min=5, max=25, message='NIT must be between 5 and 25 characters.')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),
        Length(min=5, max=25, message='Email must be between 5 and 25 characters.')
    ])
    phone = StringField('Phone Number', validators=[
        DataRequired(message='Phone number is required.'),
        Length(min=5, max=25, message='Phone number must be between 5 and 25 characters.')
    ])
