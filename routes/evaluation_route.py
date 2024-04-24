from flask import Blueprint, request, make_response, jsonify
from controllers.evaluation_controller import Evaluation_Controller
from forms.evaluation_form import Evaluation_Form

evaluation_bp:object = Blueprint('evaluation', __name__)

#---CREATE ROUTE---#

@evaluation_bp.route('/api/v1/evaluation/create', methods=['POST'])
def add_evaluation():
    if request.method == 'POST':
        try:
            form:object = Evaluation_Form()
            if form.validate_on_submit():
                data:dict = {key:value for key, value in form.data.items()}
                controller:object = Evaluation_Controller()
                response:str = controller.create_evaluation(data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@evaluation_bp.route('/api/v1/evaluation/read/<id>')
def get_evaluation(id:int):
    if request.method == 'GET':
        try:
            controller:object = Evaluation_Controller()
            evaluation:str|dict = controller.read_evaluation(id=id)
            if isinstance(evaluation, str):
                return make_response(f'{evaluation}!', 404)
            else:
                return make_response(jsonify(evaluation), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
    #---END READ  BY ID---#

    #---READ ALL ---#
@evaluation_bp.route('/api/v1/evaluation/read/all')
def get_evaluations():
    if request.method == 'GET':
        try:
            controller:object = Evaluation_Controller()
            evaluations:str|dict = controller.read_evaluations()
            if isinstance(evaluations, str):
                return make_response(f'{evaluations}!', 404)
            else:
                return make_response(jsonify(evaluations), 200)
        except Exception as e:
            return make_response(f'{e}', 400)

    #---END READ ALL ---#

#---END READ  ROUTE---#


#---UPDATE  ROUTE---#
@evaluation_bp.route('/api/v1/evaluation/update/<id>',  methods=['PUT'])
def edit_evaluation(id:int):
    if request.method == 'PUT':
        try:
            form:object = Evaluation_Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:object = Evaluation_Controller()
                    response:str = controller.update_evaluation(id=id, new_data=new_data)
                    return make_response(f'{response}!', 200)
                else:
                    return make_response({'errors': form.errors} , 400)
            else:
                return make_response('Needed data to update!', 400)
        except Exception as e:
            return make_response(f'{e}', 400)

#---END UPDATE ROUTE---#


#---DELETE  ROUTE---#
@evaluation_bp.route('/api/v1/evaluation/delete/<id>', methods=['DELETE'])
def remove_evaluation(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Evaluation_Controller()
            response:str = controller.delete_evaluation(id = id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END DELETE ROUTE---#
