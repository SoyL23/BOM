from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class User_Data_Form(FlaskForm):
    class Meta:
        csrf = False

    email = StringField('Email', validators=[DataRequired(message='Email is required'), Length(max=50, message='Maximum 50 characters')])
    document_number = StringField('Document_Number', validators=[DataRequired(message='Document Number is required')])
    document_type = SelectField('Document_Type', choices=[('Cedula_Ciudadanía', 'Cedula Ciudadanía'), 
                                                          ('Cedula_Extranjería', 'Cedula Extranjería'),
                                                          ('Pasaporte', 'Pasaporte'),
                                                          ('NIT', 'NIT'),
                                                          ('PEP', 'PEP')],
                                validators=[DataRequired(message='Document Type is required')])
    role_id = IntegerField('Role_ID', validators=[DataRequired(message='Role ID is required')])
    user_id = IntegerField('User_ID', validators=[DataRequired(message='User ID is required')])
    city_id = IntegerField('City_ID', validators=[DataRequired(message='City ID is required')])
