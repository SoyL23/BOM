from flask import Blueprint, request, make_response, jsonify
from services.generate_certificate import Generate_Certificate
from controllers.certificate_controller import Certificate_Controller
from forms.certificate_form import Certificate_Form as Form

certificate_bp = Blueprint('certificate', __name__)

@certificate_bp.route('/api/v1/certificate/create/<evaluation_id>', methods=['POST'])
def add_certificate(evaluation_id:int):
    if request.method == 'POST':
        try:
            certificate:object|None = Generate_Certificate(evaluation_id=evaluation_id).certificate
            if certificate:
                controller:object = Certificate_Controller()
                response:str = controller.create_certificate(certificate=certificate)
                return make_response(f'{response}!', status=200)
            else:
                return make_response('Error Creando Certificado', status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)

@certificate_bp.route('/api/v1/certificate/read/<id>', methods=['GET'])
def get_certificate(id:int):
    if request.method == 'GET':
        try:
            controller:object = Certificate_Controller()
            certificate:str|dict = controller.read_certificate(id=id)
            if isinstance(certificate, str):
                return make_response(f'{certificate}!', status=404)
            else:
                return make_response(jsonify(certificate), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
        
@certificate_bp.route('/api/v1/certificate/read/all', methods=['GET'])
def get_certificates():
    if request.method == 'GET':
        try:
            controller:object = Certificate_Controller()
            certificate:str|dict = controller.read_certificates()
            if isinstance(certificate, str):
                return make_response(f'{certificate}!', status=404)
            else:
                return make_response(jsonify(certificate), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)


@certificate_bp.route('/api/v1/certificate/update/<id>', methods=['PUT'])
def edit_certificate(id:int):
    if request.method == 'PUT':
        try:
            form:object = Form()
            if form.validate_on_submit():
                controller:object = Certificate_Controller()
                response:str = controller.update_certificate(id=id)
                return make_response(f'{response}', status=200)
            else:
                return make_response({'errors': form.errors} , status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)
    pass

@certificate_bp.route('/api/v1/certificate/delete/<id>', methods=['DELETE'])
def remove_certificate(id:int):
    id=0
    return f'Que tas haciendo valemia? xd'
    


