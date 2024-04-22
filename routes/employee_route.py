from flask import Blueprint, request, make_response, jsonify
from controllers.employees_controller import Employee_Controller
from forms.employee_form import Employee_Form

employee_bp = Blueprint('employee', __name__)

#---CREATE ROUTE---#

@employee_bp.route('/api/v1/employee/create', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        try:
            form = Employee_Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:object = Employee_Controller()
                response = controller.create_employee(employee_data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}),400
        except Exception as e:
            return make_response(f'Error: {e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@employee_bp.route('/api/v1/employee/read/<id>')
def get_employee(id:int):
    if request.method == 'GET':
        try:
            controller:object = Employee_Controller()
            employee = controller.read_employee(id=id)
            if isinstance(employee, str):
                return employee
            else:
                return make_response(employee, 200)
        except Exception as e:
            return make_response(f'Error: {e}', 400)
    #---END READ  BY ID---#

    #---READ ALL ---#
@employee_bp.route('/api/v1/employee/read/all')
def get_employees():
    if request.method == 'GET':
        try:
            controller:object = Employee_Controller()
            employees = controller.read_employees()
            if isinstance(employees, str):
                return employees
            else:
                return jsonify(employees), 200
        except Exception as e:
            return make_response(f'Error: {e}', 400)

    #---END READ ALL ---#



#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@employee_bp.route('/api/v1/employee/update/<id>',  methods=['PUT'])
def edit_employee(id:int):
    if request.method == 'PUT':
        try:
            data:dict = request.get_json()
            if data:
                controller:object = Employee_Controller()
                response = controller.update_employee(id=id, new_data=data)
                return make_response(f'{response}!', 200)
            else:
                return 'Needed data to update!'
        except Exception as e:
            return make_response(f'Error: {e}', 400)
    

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#

@employee_bp.route('/api/v1/employee/delete/<id>', methods=['DELETE'])
def remove_employee(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Employee_Controller()
            response = controller.delete_employee(id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'Error: {e}', 400)
#---END DELETE ROUTE---#