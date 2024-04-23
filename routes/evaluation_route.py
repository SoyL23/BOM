from flask import Blueprint, request, make_response, jsonify
from controllers.evaluation_controller import Evaluation_Controller
from forms.evaluation_form import Evaluation_Form

evaluation_bp = Blueprint('evaluation', __name__)

#---CREATE ROUTE---#

@evaluation_bp.route('/api/v1/evaluation/create', methods=['POST'])
def add_evaluation():
    if request.method == 'POST':
        try:
            form = Evaluation_Form()
            if form.validate_on_submit():
                data:dict = {key:value for key, value in form.data.items()}
                controller:object = Evaluation_Controller()
                response = controller.create_evaluation(data)
                return f'{response}!',201
            else:
                return make_response({'errors': form.errors}),400
        except Exception as e:
            return make_response(f'Error: {e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@evaluation_bp.route('/api/v1/evaluation/read/<id>')
def get_evaluation(id:int):
    if request.method == 'GET':
        try:
            controller:object = Evaluation_Controller()
            evaluation = controller.read_evaluation(id=id)
            if isinstance(evaluation, str):
                return evaluation, 404
            else:
                return jsonify(evaluation), 200
        except Exception as e:
            return make_response(f'Error: {e}', 400)
    #---END READ  BY ID---#

    #---READ ALL ---#
@evaluation_bp.route('/api/v1/evaluation/read/all')
def get_evaluations():
    if request.method == 'GET':
        try:
            controller:object = Evaluation_Controller()
            evaluations = controller.read_evaluations()
            if isinstance(evaluations, str):
                return evaluations,404
            else:
                return jsonify(evaluations), 200
        except Exception as e:
            return make_response(f'Error: {e}', 400)

    #---END READ ALL ---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@evaluation_bp.route('/api/v1/evaluation/update/<id>',  methods=['PUT'])
def edit_evaluation():
    if request.method == 'PUT':
        try:
            data:dict = request.get_json()
            if data:
                controller:object = Evaluation_Controller()
                response:str = controller.update_evaluation(id=id, new_data=data)
                return make_response(f'{response}!', 200)
            else:
                return 'Needed data to update!'
        except Exception as e:
            return make_response(f'Error: {e}', 400)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#
@evaluation_bp.route('/api/v1/evaluationdelete/<id>', methods=['DELETE'])
def remove_evaluation(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Evaluation_Controller()
            response = controller.delete_evaluation(id = id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'Error: {e}', 400)
#---END DELETE ROUTE---#
