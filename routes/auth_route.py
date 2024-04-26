from flask import Blueprint, request, make_response, jsonify, session
from controllers.auth_controller import Auth_Controller as Controller
from forms.auth_form import Auth_Form as Form


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
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response( e , 400)
    pass


@auth_bp.route('/logout', methods=['POST'])
def logout_user():
    pass