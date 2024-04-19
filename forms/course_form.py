from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length

class Course_Form(FlaskForm):
    
    class Meta:
        csrf = False    

    name = StringField('Course Name', validators=[
        DataRequired(message='Course name is required.'),
        Length(min=5, max=50, message='Course name must be between 5 and 50 characters.')
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(message='Description is required.'),
        Length(min=5, message='Description must be at least 5 characters.')
    ])
    duration = StringField('Duration', validators=[
        DataRequired(message='Duration is required.'),
        Length(min=5, max=50, message='Duration must be between 5 and 50 characters.')
    ])
    price = DecimalField('Price', validators=[
        DataRequired(message='Price is required.')
    ])
