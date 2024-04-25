from flask import Blueprint, request, make_response, jsonify
from controllers.user_data_controller import User_Data_Controller as Controller
from forms.user_data_form import User_Data_Form as Form

user_data_bp:Blueprint = Blueprint('user_data', __name__, url_prefix='/api/v1/user_data')

#---CREATE ROUTE---#

@user_data_bp.route('/create', methods=['POST'])
def add_data():
    if request.method == 'POST':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:Controller = Controller()
                response:str = controller.create_data(data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}),400
        except Exception as e:
            return make_response(f'{e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@user_data_bp.route('/read/<id>')
def get_data(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
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
@user_data_bp.route('/update/<id>',  methods=['PUT'])
def edit_data(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:Controller = Controller()
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
@user_data_bp.route('/delete/<id>', methods=['DELETE'])
def remove_data(id:int):
    if request.method == 'DELETE':
        try:
            controller:Controller = Controller()
            response:str = controller.delete_data(id=id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END DELETE ROUTE---#