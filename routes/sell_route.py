from flask import Blueprint, request, jsonify, make_response
from controllers.sell_controller import Sell_Controller as Controller

sell_bp:object = Blueprint('', __name__)

@sell_bp.route('/api/v1/sell/create/', methods=['POST'])
def add_(id:int):
    if request.method == 'POST':
        try:
            # data:dict = 
            controller:object = Controller()
            response:str = controller.create_sell()
            return f'{response}!'
        except Exception as e:
            return make_response(f'{e}', status=400)
            

@sell_bp.route('/api/v1/sell/read/<id>', methods=['GET'])
def get_(id:int):
    if request.method == 'GET':
        try:
            controller:object = Controller()
            sell:str|dict = controller.read_sell(id=id)
            if isinstance(sell, str):
                return make_response(f'{sell}!', 404)
            else:
                return make_response(jsonify(sell), 200)
        except Exception as e:
            return make_response(f'{e}', status=400)
            

@sell_bp.route('/api/v1/sell/read/all', methods=['GET'])
def get_(id:int):
    if request.method == 'GET':
        try:
            controller:object = Controller()
            sells:str|dict = controller.read_sell()
            if isinstance(sells, str):
                return make_response(f'{sells}!', 404)
            else:
                return make_response(sells, 200)
        except Exception as e:
            return make_response(f'{e}', status=400)
            

@sell_bp.route('/api/v1/sell/update/<id>', methods=['PUT'])
def edit_(id:int):
    if request.method == 'PUT':
        try:
            new_data = request.get_json()
            controller:object = Controller()
            response = controller.update_sell(id=id, new_data=new_data)
            return f'{response}!'
        except Exception as e:
            return make_response(f'{e}', status=400)
            

@sell_bp.route('/api/v1/sell/delete/<id>', methods=['DELETE'])
def remove_(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Controller()
            response:str = controller.delete_sell(id=id)
            return f'{response}!'
        except Exception as e:
            return make_response(f'{e}', status=400)
            
    