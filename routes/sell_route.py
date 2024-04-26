from flask import Blueprint, request, jsonify, make_response
from controllers.sell_controller import Sell_Controller as Controller
from forms.sell_form import Sell_Form as Form
from flask_jwt_extended import jwt_required


sell_bp:Blueprint = Blueprint('Sell', __name__, url_prefix='/api/v1/sell')

@sell_bp.route('/create', methods=['POST'])
def add_sell():
    if request.method == 'POST':
        try:
            form:Form=Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:Controller = Controller()
                response:str = controller.create_sell(data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
            

@sell_bp.route('/read/<id>', methods=['GET'])
def get_sell(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            sell:str|dict = controller.read_sell(id=id)
            if isinstance(sell, str):
                return make_response(f'{sell}!', 404)
            else:
                return make_response(jsonify(sell), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
            

@sell_bp.route('/read/all', methods=['GET'])
def get_sells(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            sells:str|dict = controller.read_sell(id=id)
            if isinstance(sells, str):
                return make_response(f'{sells}!', 404)
            else:
                return make_response(jsonify(sells), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
            

@sell_bp.route('/update/<id>', methods=['PUT'])
def edit_sell(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.validate_on_submit():    
                new_data:dict = request.get_json()
                controller:Controller = Controller()
                response:str = controller.update_sell(id=id, new_data=new_data)
                return make_response(f'{response}!', 200)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
            

@sell_bp.route('/delete/<id>', methods=['DELETE'])
def remove_sell(id:int):
    if request.method == 'DELETE':
        try:
            controller:Controller = Controller()
            response:str = controller.delete_sell(id=id)
            return f'{response}!'
        except Exception as e:
            return make_response(f'{e}', 400)