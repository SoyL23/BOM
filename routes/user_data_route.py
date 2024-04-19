from flask import Blueprint, request, make_response, jsonify

user_data_bp = Blueprint('', __name__)

#---CREATE ROUTE---#

@user_data_bp.route('/api/v1/user_data/create', methods=['POST'])
def add_data():
    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            return str(e)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@user_data_bp.route('/api/v1/user_data/read/<id>')
def get_data(id:int):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)
    #---END READ  BY ID---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@user_data_bp.route('/api/v1/user_data/update/<id>',  methods=['PUT'])
def edit_data(id:int):
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return str(e)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#

@user_data_bp.route('/api/v1/user_data/delete/<id>', methods=['DELETE'])
def remove_data(id:int):
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return str(e)
#---END DELETE ROUTE---#