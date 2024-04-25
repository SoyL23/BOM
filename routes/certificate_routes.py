from flask import Blueprint, request, make_response, jsonify
from services.generate_certificate import Generate_Certificate
from controllers.certificate_controller import Certificate_Controller as Controller
from forms.certificate_form import Certificate_Form as Form

certificate_bp:Blueprint = Blueprint('certificate', __name__, url_prefix='/api/v1/certificate')

@certificate_bp.route('/create/<evaluation_id>', methods=['POST'])
def add_certificate(evaluation_id:int):
    if request.method == 'POST':
        try:
            certificate:object|None = Generate_Certificate(evaluation_id=evaluation_id).certificate
            if certificate:
                controller:Controller = Controller()
                response:str = controller.create_certificate(certificate=certificate)
                return make_response(f'{response}!', 200)
            else:
                return make_response('Error Creando Certificado', 400)
        except Exception as e:
            return make_response(f'{e}', 400)

@certificate_bp.route('/read/<id>', methods=['GET'])
def get_certificate(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            certificate:str|dict = controller.read_certificate(id=id)
            if isinstance(certificate, str):
                return make_response(f'{certificate}!', 404)
            else:
                return make_response(jsonify(certificate), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
        
@certificate_bp.route('/read/all', methods=['GET'])
def get_certificates():
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            certificates:str|dict = controller.read_certificates()
            if isinstance(certificates, str):
                return make_response(f'{certificates}!', 404)
            else:
                return make_response(jsonify(certificates), 200)
        except Exception as e:
            return make_response(f'{e}', 400)


@certificate_bp.route('/update/<id>', methods=['PUT'])
def edit_certificate(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                controller:Controller = Controller()
                response:str = controller.update_certificate(id=id, new_data=form.data)
                return make_response(f'{response}', 200)
            else:
                return make_response({'errors': form.errors} , 400)
        except Exception as e:
            return make_response(f'{e}', 400)
    pass

@certificate_bp.route('/delete/<id>', methods=['DELETE'])
def remove_certificate(id:int):
    id=0
    return f'Que tas haciendo valemia? xd'
    


