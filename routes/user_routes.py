from flask import Blueprint, request, make_response, jsonify
from controllers.user_controller import User_Controller
from forms.user_form import User_Form

user_bp:object = Blueprint('user', __name__ )

#---CREATE USER ROUTE---#
@user_bp.route('/api/v1/user/create', methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            form:object = User_Form()
            if form.validate_on_submit():
                data:dict = {key: value for key, value in form.data.items() if key != 'confirm_password'}
                controller:object = User_Controller()
                response:str = controller.create_user(user_data=data)
                return make_response(f'{response}!', status=201)
            else:
                return make_response({'errors': form.errors}, status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)
#---END CREATE USER ROUTE---#

#---READ USER ROUTE---#
    #---Read User by id route
@user_bp.route('/api/v1/user/read/<id>')
def get_user(id:int):
     if request.method == 'GET':   
        try:
            controller:object = User_Controller()
            user:str|dict = controller.read_user(id=id)
            if isinstance(user, str):
                return make_response(f'{user}!', status=404)
            else:
                return make_response(jsonify(user), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
    #---END Read User by id route
    
    #---READ ALL USERS ROUTE---#
@user_bp.route('/api/v1/user/read/all', methods=['GET'])
def get_users():
    if request.method == 'GET':    
        try:
            controller:object = User_Controller()
            users:str|dict = controller.read_users()
            if isinstance(users, str):
                return make_response(users, status=404)
            else:
                return make_response(jsonify(users), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
    #---END READ ALL USERS ROUTE---#

#---END READ USER ROUTE---#

#---UPDATE USER ROUTE--#
@user_bp.route('/api/v1/user/update/<id>', methods=['PUT'])
def edit_user(id:int):
    if request.method == 'PUT':
        try:
            form:object = User_Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:object = User_Controller()
                    response:str = controller.update_user(id=id, new_data=new_data)
                    return make_response(f'{response}!', status=200)
                else:
                    return make_response({'errors': form.errors} , status=400)
            else:
                return make_response('Needed data to update!', status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)
#---UPDATE USER ROUTE---#

#---DELETE USER ROUTE---#
@user_bp.route('/api/v1/user/delete/<id>', methods=['DELETE'])
def remove_user(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = User_Controller()
            response:str = controller.delete_user(id)
            return make_response(f'{response}!', status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
#---END DELETE USER ROUTE---#