from flask import Blueprint, request, make_response, jsonify
from controllers.employees_controller import Employee_Controller as Controller
from forms.employee_form import Employee_Form as Form

employee_bp:Blueprint = Blueprint('employee', __name__, url_prefix='/api/v1/employee')

#---CREATE ROUTE---#

@employee_bp.route('/create', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:Controller = Controller()
                response:str = controller.create_employee(employee_data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@employee_bp.route('/read/<id>')
def get_employee(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            employee:str|dict = controller.read_employee(id=id)
            if isinstance(employee, str):
                return make_response(f'{employee}!', 404)
            else:
                return make_response(jsonify(employee), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
    #---END READ  BY ID---#

    #---READ ALL ---#
@employee_bp.route('/read/all')
def get_employees():
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            employees:str|dict = controller.read_employees()
            if isinstance(employees, str):
                return make_response(f'{employees}!', 404)
            else:
                return make_response(jsonify(employees), 200)
        except Exception as e:
            return make_response(f'{e}', 400)

    #---END READ ALL ---#



#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@employee_bp.route('/update/<id>',  methods=['PUT'])
def edit_employee(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:Controller = Controller()
                    response:str = controller.update_employee(id=id, new_data=new_data)
                    return make_response(f'{response}!', 200)
                else:
                    return make_response({'errors': form.errors} , 400)
            else:
                return 'Needed data to update!'
        except Exception as e:
            return make_response(f'{e}', 400)
    

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#
@employee_bp.route('/delete/<id>', methods=['DELETE'])
def remove_employee(id:int):
    if request.method == 'DELETE':
        try:
            controller:Controller = Controller()
            response:str = controller.delete_employee(id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END DELETE ROUTE---#