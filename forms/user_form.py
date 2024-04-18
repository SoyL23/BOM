from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField, validators
from wtforms.validators import DataRequired, Length, EqualTo

class User_Form(FlaskForm):
    class Meta:
        csrf = False

    first_name = StringField('first_name', validators=[DataRequired(message='Nombre es Requerido'),
                                                Length(min=3,max=25,message='')])
    last_name = StringField('last_name', validators=[DataRequired(message='Apellido es Requerido'),
                                               Length(min=3,max=25,message='')])
    username = StringField('username', validators=[DataRequired(message='Username es Requerido'),
                                                        Length(min=4,max=15,message='')])
    password = PasswordField('password',validators=[DataRequired(message='Contraseña es Requerido'),
                                                Length(min=8,max=16,message='')])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(message='Confirmar Contraseña es Requerido'),
                                                        Length(min=8,max=16,message='')])
    birthdate = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired(message='Fecha de Nacimiento es Requerido')])
