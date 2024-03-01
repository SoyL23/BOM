from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, validators


role_options:list = [
    (1, "Administrador"),
    (2, "Operador"),
    (3, "Usuario"),
]
doc_type_options:list = [
    (1, "Cédula de Identidad"),
    (2, "Pasaporte"),
]

class UserForm(FlaskForm):
    first_name:object = StringField('first_name', validators=[
        validators.DataRequired(message='El nombre es obligatorio'),
        validators.Length(min=3, max=50, message='El nombre debe tener entre 3 y 50 caracteres')
    ])

    last_name:object = StringField('last_name', validators=[
        validators.DataRequired(message='El apellido es obligatorio'),
        validators.Length(min=3, max=50, message='El apellido debe tener entre 3 y 50 caracteres')
    ])

    document_number:object = StringField('document_number', validators=[
        validators.DataRequired(message='El número de documento es obligatorio'),
        validators.Length(min=7, max=15, message='El número de documento debe tener entre 7 y 15 caracteres')
    ])

    email:object = StringField('email', validators=[
        validators.DataRequired(message='El correo electrónico es obligatorio'),
        validators.Email(message='Proporciona un correo electrónico válido')
    ])

    password:object = PasswordField('password', validators=[
        validators.DataRequired(message='La contraseña es obligatoria'),
        validators.Length(min=8, max=16, message='La contraseña debe tener entre 8 y 16 caracteres')
    ])

    confirm_password:object = PasswordField('confirm_password', validators=[
        validators.DataRequired(message='Confirma la contraseña'),
        validators.EqualTo('password', message='Las contraseñas no coinciden')
    ])

    role_id:object = SelectField('role_id', validators=[validators.DataRequired()], choices=role_options)
    doc_type_id:object = SelectField('doc_type_id', validators=[validators.DataRequired()], choices=doc_type_options)
