from flask import Blueprint, request, make_response,jsonify
from forms.course_form import Course_Form as Form
from controllers.course_controller import Course_Controller as Controller

course_bp:Blueprint = Blueprint('course', __name__, url_prefix='/api/v1/course')

#---CREATE ROUTE---#

@course_bp.route('/create', methods=['POST'])
def add_course():
    if request.method == 'POST':
        try:
            form:Form = Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:Controller = Controller()
                response:str = controller.create_course(course_data=data)
                return make_response(f'{response}!', 201)
            else:
                return make_response({'errors': form.errors}, 400)
        except Exception as e:
            return make_response(f'{e}', 400)
        
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#

@course_bp.route('/read/<id>')
def get_course(id:int):
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            course:str|dict = controller.read_course(id=id)
            if isinstance(course, str):
                return make_response(f'{course}!' , 404)
            else:
                return make_response(jsonify(course), 200)
        except Exception as e:
            return make_response(f'{e}', 400)
        
    #---END READ BY ID---#

    #---READ ALL---#

@course_bp.route('/read/all')
def get_courses():
    if request.method == 'GET':
        try:
            controller:Controller = Controller()
            courses:str|dict = controller.read_courses()
            if isinstance(courses, str):
                return make_response(f'{courses}!' , 404)
            else:
                return make_response(jsonify(courses), 200)
        except Exception as e:
            return make_response(f'{e}', 400)

    #---END READ ALL ---#

#---END READ ROUTE---#


#---UPDATE ROUTE---#

@course_bp.route('/update/<id>',  methods=['PUT'])
def edit_course(id:int):
    if request.method == 'PUT':
        try:
            form:Form = Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:Controller = Controller()
                    response:str = controller.update_course(id=id, new_data=new_data)
                    return make_response(f'{response}!', 200)
                else:
                    return make_response({'errors': form.errors} , 400)
            else:
                return make_response('Needed data to update', 400)
        except Exception as e:
            return make_response(f'{e}', 400)

#---END UPDATE ROUTE---#


#---DELETE ROUTE---#

@course_bp.route('/delete/<id>', methods=['DELETE'])
def remove_course(id:int):
    if request.method == 'DELETE':
        try:
            controller:Controller = Controller()
            response:str = controller.delete_course(id=id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', 400)
        
#---END DELETE ROUTE---#