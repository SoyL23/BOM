from flask import Blueprint, request

employee_bp = Blueprint('employee', __name__)

#---CREATE ROUTE---#

@employee_bp.route('/api/v1/employee/create', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        try:
            pass
            
        except Exception as e:
            return f'Error: {str(e)}'
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@employee_bp.route('/api/v1/employee/read/<id>')
def get_employee():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return f'Error: {str(e)}'
    #---END READ  BY ID---#

    #---READ ALL ---#
@employee_bp.route('/api/v1/employee/read/all')
def get_employees():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return f'Error: {str(e)}'

    #---END READ ALL ---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@employee_bp.route('/api/v1/employee/update/<id>',  methods=['PUT'])
def edit_employee():
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return f'Error: {str(e)}'

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#

@employee_bp.route('/api/v1/employee/delete/<id>', methods=['DELETE'])
def remove_employee():
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return f'Error: {str(e)}'
#---END DELETE ROUTE---#