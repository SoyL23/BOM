from flask import Blueprint, request, make_response

shopping_bp:object = Blueprint('shopping', __name__)

@shopping_bp.route('/api/v1/shopping/create/', methods=['POST'])
def add_(id:int):
    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', status=400)

@shopping_bp.route('/api/v1/shopping/read/<id>', methods=['GET'])
def get_(id:int):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', status=400)

@shopping_bp.route('/api/v1/shopping/update/<id>', methods=['PUT'])
def edit_(id:int):
    if request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', status=400)

@shopping_bp.route('/api/v1/shopping/delete/<id>', methods=['DELETE'])
def remove_(id:int):
    if request.method == 'DELETE':
        try:
            pass
        except Exception as e:
            return make_response(f'{e}', status=400)
    