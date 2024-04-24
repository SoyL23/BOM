from flask import Blueprint, request, make_response, jsonify
from controllers.user_data_controller import User_Data_Controller
from forms.user_data_form import User_Data_Form

user_data_bp:object = Blueprint('user_data', __name__)

#---CREATE ROUTE---#

@user_data_bp.route('/api/v1/user_data/create', methods=['POST'])
def add_data():
    if request.method == 'POST':
        try:
            form:object = User_Data_Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:object = User_Data_Controller()
                response:str = controller.create_data(data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}),400
        except Exception as e:
            return make_response(f'{e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@user_data_bp.route('/api/v1/user_data/read/<id>')
def get_data(id:int):
    if request.method == 'GET':
        try:
            controller:object = User_Data_Controller()
            data:str|dict = controller.read_data(id=id)
            if isinstance(data, str):
                return make_response(f'{data}!', 404)
            else:
                return make_response(jsonify(data), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
    #---END READ  BY ID---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@user_data_bp.route('/api/v1/user_data/update/<id>',  methods=['PUT'])
def edit_data(id:int):
    if request.method == 'PUT':
        try:
            form:object = User_Data_Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:object = User_Data_Controller()
                    response:str = controller.update_data(id=id, new_data=new_data)
                    return make_response(f'{response}', 200)
                else:
                    return make_response({'errors': form.errors} , 400)
            else:
                return make_response('Needed data to update!', 400)
        except Exception as e:
            return make_response(f'{e}', 400)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#
@user_data_bp.route('/api/v1/user_data/delete/<id>', methods=['DELETE'])
def remove_data(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = User_Data_Controller()
            response:str = controller.delete_data(id=id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END DELETE ROUTE---#