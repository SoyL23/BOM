from flask import Blueprint, request

company_bp = Blueprint('company', __name__)

#---CREATE ROUTE---#

@company_bp.route('/api/v1/company/create', methods=['POST'])
def add_company():
    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            return str(e)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@company_bp.route('/api/v1/company/read/<id>')
def get_company():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)
    #---END READ  BY ID---#

    #---READ ALL ---#
@company_bp.route('/api/v1/company/read/all')
def get_companies():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)

    #---END READ ALL ---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@company_bp.route('/api/v1/company/update/<id>',  methods=['PUT'])
def edit_company():
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return str(e)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#

@company_bp.route('/api/v1/company/delete/<id>', methods=['DELETE'])
def remove_company():
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return str(e)
#---END DELETE ROUTE---#