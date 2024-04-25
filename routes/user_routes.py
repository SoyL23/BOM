from flask import Blueprint, request, make_response, jsonify
from controllers.user_controller import User_Controller as Controller
from forms.user_form import User_Form as Form

user_bp:Blueprint = Blueprint('user', __name__ , url_prefix='/api/v1/user')

#---CREATE USER ROUTE---#
@user_bp.route('/create', methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                data:dict = {key: value for key, value in form.data.items() if key != 'confirm_password'}
                controller:Controller = Controller()
                response:str = controller.create_user(user_data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END CREATE USER ROUTE---#

#---READ USER ROUTE---#
    #---Read User by id route
@user_bp.route('/read/<id>')
def get_user(id:int):
     if request.method == 'GET':   
        try:
            controller:Controller = Controller()
            user:str|dict = controller.read_user(id=id)
            if isinstance(user, str):
                return make_response(f'{user}!', 404)
            else:
                return make_response(jsonify(user), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
    #---END Read User by id route
    
    #---READ ALL USERS ROUTE---#
@user_bp.route('/read/all', methods=['GET'])
def get_users():
    if request.method == 'GET':    
        try:
            controller:Controller = Controller()
            users:str|dict = controller.read_users()
            if isinstance(users, str):
                return make_response(users, 404)
            else:
                return make_response(jsonify(users), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
    #---END READ ALL USERS ROUTE---#

#---END READ USER ROUTE---#

#---UPDATE USER ROUTE--#
@user_bp.route('/update/<id>', methods=['PUT'])
def edit_user(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:Controller = Controller()
                    response:str = controller.update_user(id=id, new_data=new_data)
                    return make_response(f'{response}!', 200)
                else:
                    return make_response({'errors': form.errors} , 400)
            else:
                return make_response('Needed data to update!', 400)
        except Exception as e:
            return make_response(f'{e}', 400)
#---UPDATE USER ROUTE---#

#---DELETE USER ROUTE---#
@user_bp.route('/delete/<id>', methods=['DELETE'])
def remove_user(id:int):
    if request.method == 'DELETE':
        try:
            controller:Controller = Controller()
            response:str = controller.delete_user(id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END DELETE USER ROUTE---#