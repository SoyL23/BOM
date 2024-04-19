from flask import Blueprint, request
from controllers.evaluation_controller import Evaluation_Controller

evaluation_bp = Blueprint('evaluation', __name__)

#---CREATE ROUTE---#

@evaluation_bp.route('/api/v1/evaluation/create', methods=['POST'])
def add_evaluation():
    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            return str(e)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@evaluation_bp.route('/api/v1/evaluation/read/<id>')
def get_evaluation():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)
    #---END READ  BY ID---#

    #---READ ALL ---#
@evaluation_bp.route('/api/v1/evaluation/read/all')
def get_evaluations():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return str(e)

    #---END READ ALL ---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@evaluation_bp.route('/api/v1/evaluation/update/<id>',  methods=['PUT'])
def edit_evaluation():
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return str(e)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#

@evaluation_bp.route('/api/v1/evaluationdelete/<id>', methods=['DELETE'])
def remove_evaluation():
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return str(e)
#---END DELETE ROUTE---#
