from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class AuthForm(FlaskForm):
    
    login_name:object = StringField('login_name',validators=[
        validators.DataRequired(message='Este Campo es Obligatorio'),
        validators.Length(min=7, max=15, message='Debe tener entre 7 y 15 caracteres')
    ])

    login_password:object = PasswordField('login_password',validators=[
        validators.DataRequired(message='Este Campo es Obligatorio'),
        validators.Length(min=8, max=16, message='Debe tener entre 8 y 16 caracteres')
    ])