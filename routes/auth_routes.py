from flask import Blueprint, request, make_response, session, Response
from controllers.auth_controller import Auth_Controller as Controller
from forms.auth_form import Auth_Form as Form
from flask_jwt_extended import create_access_token


auth_bp:Blueprint = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_bp.route('/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                controller:Controller = Controller()
                response:str|dict = controller.login(data=form.data)
                if isinstance(response, str):
                    return make_response(f'{response}!', 404)
                else:
                    for key, value in response.items():
                        session[key] = value
                    token_data = {'role': response['role'],
                                  'email': response['email'],
                                  'username': response['username']}
                    session['token'] = create_access_token(identity=response['id'],
                                                        additional_claims=token_data)
                    return make_response('Login successful', 200)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response( str(e) , 400)



@auth_bp.route('/logout', methods=['POST'])

def logout_user():
    session.pop('token', None)
    response = Response()
    response.delete_cookie('access_token')
    session.clear()
    return 'Logout Successfully!', 200