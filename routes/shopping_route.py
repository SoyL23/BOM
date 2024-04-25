from flask import Blueprint, request, make_response, jsonify
from controllers.shopping_controller import Shopping_Controller as Controller
from forms.shopping_controller import Shopping_Form as Form

shopping_bp:Blueprint = Blueprint('shopping', __name__, url_prefix='/api/v1/shopping')

@shopping_bp.route('/create', methods=['POST'])
def add_shopping(id:int):
    if request.method == 'POST':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                data:dict = {key:value for key, value in form.data.items()}
                controller:Controller = Controller()
                response:str = controller.create_evaluation(data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)

@shopping_bp.route('/read/<id>', methods=['GET'])
def get_shopping(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            shopping:str|dict = controller.read_shopping(id=id)
            if isinstance(shopping, str):
                return make_response(f'{shopping}', 404)
            else:
                return make_response(jsonify(shopping), 200)
        except Exception as e:
            return make_response(f'{e}', 400)

@shopping_bp.route('/update/<id>', methods=['PUT'])
def edit_shopping(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                new_data:dict = form.data
                controller:Controller = Controller()
                response:str = controller.update_shopping(id=id, new_data=new_data)
                return make_response(f'{response}!', 201)

            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)

@shopping_bp.route('/delete/<id>', methods=['DELETE'])
def remove_shopping(id:int):
    if request.method == 'DELETE':
        try:
            controller:Controller = Controller()
            response:str = controller.delete_shopping(id=id)
            return make_response(f'{response}!', 201)
        except Exception as e:
            return make_response(f'{e}', 400)
    