from flask import Blueprint, request, make_response, jsonify
from controllers.user_controller import User_Controller
from forms.user_form import User_Form

user_bp = Blueprint('user', __name__ )

#---CREATE USER ROUTE---#

@user_bp.route('/api/v1/user/create', methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            form = User_Form()
            if form.validate_on_submit():
                data:dict = {key: value for key, value in form.data.items() if key != 'confirm_password'}
                controller = User_Controller()
                response = controller.create_user(user_data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}),400
        except Exception as e:
            return make_response(f'Error: {e}', 400)
#---END CREATE USER ROUTE---#



#---READ USER ROUTE---#

    #---Read User by id route
@user_bp.route('/api/v1/user/read/<id>')
def get_user(id:int):
     if request.method == 'GET':   
        try:
            controller:object = User_Controller()
            user = controller.read_user(id=id)
            if isinstance(user, str):
                return user
            else:
                return make_response(user, 200)
        except Exception as e:
            return str(e)
    #---END Read User by id route
    
    #---READ ALL USERS ROUTE---#
@user_bp.route('/api/v1/user/read/all', methods=['GET'])
def get_users():
    if request.method == 'GET':    
        try:
            controller = User_Controller()
            users = controller.read_users()
            if isinstance(users, str):
                return users, 500
            else:
                return jsonify(users), 200
        except Exception as e:
            return str(e)
    #---END READ ALL USERS ROUTE---#


#---END READ USER ROUTE---#



#---UPDATE USER ROUTE--#

@user_bp.route('/api/v1/user/update/<id>', methods=['PUT'])
def edit_user(id:int):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            if data:
                controller:object = User_Controller()
                response:str = controller.update_user(id=id, new_data=data)
                return make_response(f'{response}!', 200)
            else:
                return 'Needed data to update!'
        except Exception as e:
            return make_response(f'Error: {e}', 400)

#---UPDATE USER ROUTE---#



#---DELETE USER ROUTE---#

@user_bp.route('/api/v1/user/delete/<id>', methods=['DELETE'])
def remove_user(id:int):
    if request.method == 'DELETE':
        try:
            controller = User_Controller()
            response = controller.delete_user(id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'Error: {e}', 400)
    
#---END DELETE USER ROUTE---#