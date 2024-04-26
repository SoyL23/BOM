from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

class Auth_Form(FlaskForm):
    class Meta:
        csrf = False
    
    username = StringField('username', validators=[DataRequired(message='Username is required'),
                                                        Length(min=4,max=15,message='Username does not exist')])
    password = PasswordField('password',validators=[DataRequired(message='Password is required'),
                                                Length(min=8,max=16,message='Between 8 and 16 Characters'),
                                                Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,16}$',
                                                       message='Invalid password rules.')])
    