from flask import Blueprint, request, make_response
# from controllers.shopping_controller import Shopping_Controller as Controller
from forms.shopping_controller import Shopping_Form as Form

shopping_bp:Blueprint = Blueprint('shopping', __name__, url_prefix='/api/v1/shopping')

@shopping_bp.route('/create/', methods=['POST'])
def add_(id:int):
    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', 400)

@shopping_bp.route('/read/<id>', methods=['GET'])
def get_(id:int):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', 400)

@shopping_bp.route('/update/<id>', methods=['PUT'])
def edit_(id:int):
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', 400)

@shopping_bp.route('/delete/<id>', methods=['DELETE'])
def remove_(id:int):
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', 400)
    