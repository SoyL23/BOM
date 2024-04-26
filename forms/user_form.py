from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp

class User_Form(FlaskForm):
    class Meta:
        csrf = False

    first_name = StringField('first_name', validators=[DataRequired(message='First Name is required'),
                                                Length(min=3,max=25,message='Between 3 and 25 Characters')])
    last_name = StringField('last_name', validators=[DataRequired(message='Last Name is required'),
                                               Length(min=3,max=25,message='Between 3 and 25 Characters')])
    username = StringField('username', validators=[DataRequired(message='Username is required'),
                                                        Length(min=4,max=15,message='Between 4 and 15 Characters')])
    password = PasswordField('password',validators=[DataRequired(message='Password is required'),
                                                Length(min=8,max=16,message='Between 8 and 16 Characters'),
                                                Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$',
                                                       message='Password must have at least one uppercase letter, one lowercase letter, one number, one special character, and be between 8 and 16 characters long')])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(message='Confirm Password is required'),
                                                        Length(min=8,max=16,message='Between 8 and 16 Characters'),
                                                        EqualTo('password', message='Passwords must match')])
    birthdate = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired(message='Birthdate is required')])
