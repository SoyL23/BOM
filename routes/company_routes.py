from flask import Blueprint, request, make_response, jsonify
from forms.company_form import Company_Form
from controllers.company_controller import Company_Controller

company_bp:object = Blueprint('company', __name__)

#---CREATE ROUTE---#
@company_bp.route('/api/v1/company/create', methods=['POST'])
def add_company():
    if request.method == 'POST':
        try:
            form:object = Company_Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:object = Company_Controller()
                response = controller.create_company(company_data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#
@company_bp.route('/api/v1/company/read/<id>')
def get_company(id:int):
    if request.method == 'GET':
        try:
            controller:object = Company_Controller()
            company:str|dict = controller.read_company(id=id)
            if isinstance(company, str):
                return make_response(f'{company}' , 404)
            else:
                return make_response(jsonify(company), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
    #---END READ  BY ID---#

    #---READ ALL ---#
@company_bp.route('/api/v1/company/read/all')
def get_companies():
    if request.method == 'GET':
        try:
            controller:object = Company_Controller()
            companies:str|dict = controller.read_companies()
            if isinstance(companies, str):
                return make_response(f'{companies}!' , 404)
            else:
                return make_response(jsonify(companies), 200)
        except Exception as e:
            return make_response(f'{e}', 400)

    #---END READ ALL ---#

#---END READ  ROUTE---#

#---UPDATE  ROUTE---#
@company_bp.route('/api/v1/company/update/<id>',  methods=['PUT'])
def edit_company(id:int):
    if request.method == 'PUT':
        try:
            form:object = Company_Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:object = Company_Controller()
                    response:str = controller.update_company(id=id, new_data=new_data)
                    return make_response(f'{response}!', 200)
            else:
                return make_response('Need data to update', 400)
        except Exception as e:
            return make_response(f'{e}', 400)

#---END UPDATE ROUTE---#

#---DELETE  ROUTE---#
@company_bp.route('/api/v1/company/delete/<id>', methods=['DELETE'])
def remove_company(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Company_Controller()
            response:str = controller.delete_company(id=id)
            return make_response(f'{response}!', 200)
        except Exception as e:    
            return make_response(f'{e}', 400)
#---END DELETE ROUTE---#