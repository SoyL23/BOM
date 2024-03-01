from flask import session, request, render_template, jsonify, Blueprint, redirect
from datetime import datetime, date
from model.user import User
from forms.auth import AuthForm
from services.generate_token import generate_token
from flask_jwt_extended import create_access_token
auth = Blueprint('auth', __name__)

@auth.route('/api/auth/login', methods=['GET', 'POST'])
def login_user():
    form = AuthForm()
    if request.method == 'GET':
        token = generate_token()
        return jsonify({'token': token})
    else:
        if form.validate_on_submit():

            email:str = str(form.login_user.data)
            password:str = str(form.login_password.data)

            user = User.query.filter_by(email=email).first()

            if user is None:
                return jsonify({'No existe este usuario'})
            else:
                if user.check_password(user.password, password):
                    access_token = create_access_token(identity=user.username)
                    sesion_data = user.to_dict() 
                    for key, value in sesion_data.items():
                        session[key] = value
                    session['access_token'] = access_token
                    return f"{session['access_token']}"
                else:
                    return jsonify({'Contraseña Invalida'})
        else:
            return render_template('login.html', form=form, errors=form.errors)

@auth.route('/api/auth/logout')
def logout_user():
    session.pop('token', None)
    session.clear()
    return redirect('/')
