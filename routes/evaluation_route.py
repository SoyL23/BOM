from flask import Blueprint, request

_bp = Blueprint('', __name__)

#---CREATE ROUTE---#

@_bp.route('/api/v1//create', methods=['POST'])
def add_():
    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            return str(e)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@_bp.route('/api/v1//read/<id>')
def get_():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)
    #---END READ  BY ID---#

    #---READ ALL ---#
@_bp.route('/api/v1//read/all')
def get_companies():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)

    #---END READ ALL ---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@_bp.route('/api/v1//update/<id>',  methods=['PUT'])
def edit_():
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return str(e)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#

@_bp.route('/api/v1//delete/<id>', methods=['DELETE'])
def remove_():
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return str(e)
#---END DELETE ROUTE---#