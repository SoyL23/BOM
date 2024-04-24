from flask import Blueprint, request, make_response, jsonify
from controllers.employees_controller import Employee_Controller
from forms.employee_form import Employee_Form

employee_bp:object = Blueprint('employee', __name__)

#---CREATE ROUTE---#

@employee_bp.route('/api/v1/employee/create', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        try:
            form:object = Employee_Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:object = Employee_Controller()
                response:str = controller.create_employee(employee_data=data)
                return make_response(f'{response}!', status=201)
            else:
                return make_response({'errors': form.errors}, status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@employee_bp.route('/api/v1/employee/read/<id>')
def get_employee(id:int):
    if request.method == 'GET':
        try:
            controller:object = Employee_Controller()
            employee:str|dict = controller.read_employee(id=id)
            if isinstance(employee, str):
                return make_response(f'{employee}!', status=404)
            else:
                return make_response(jsonify(employee), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
    #---END READ  BY ID---#

    #---READ ALL ---#
@employee_bp.route('/api/v1/employee/read/all')
def get_employees():
    if request.method == 'GET':
        try:
            controller:object = Employee_Controller()
            employees:str|dict = controller.read_employees()
            if isinstance(employees, str):
                return make_response(f'{employees}!', status=404)
            else:
                return make_response(jsonify(employees), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)

    #---END READ ALL ---#



#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@employee_bp.route('/api/v1/employee/update/<id>',  methods=['PUT'])
def edit_employee(id:int):
    if request.method == 'PUT':
        try:
            form:object = Employee_Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:object = Employee_Controller()
                    response:str = controller.update_employee(id=id, new_data=new_data)
                    return make_response(f'{response}!', status=200)
                else:
                    return make_response({'errors': form.errors} , status=400)
            else:
                return 'Needed data to update!'
        except Exception as e:
            return make_response(f'{e}', status=400)
    

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#
@employee_bp.route('/api/v1/employee/delete/<id>', methods=['DELETE'])
def remove_employee(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Employee_Controller()
            response:str = controller.delete_employee(id)
            return make_response(f'{response}!', status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
#---END DELETE ROUTE---#