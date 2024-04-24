from flask import Blueprint, request, make_response,jsonify
from forms.course_form import Course_Form
from controllers.course_controller import Course_Controller

course_bp:object = Blueprint('course', __name__)

#---CREATE ROUTE---#

@course_bp.route('/api/v1/course/create', methods=['POST'])
def add_course():
    if request.method == 'POST':
        try:
            form:object = Course_Form()
            if form.validate_on_submit():
                data:dict = form.data
                controller:object = Course_Controller()
                response:str = controller.create_course(course_data=data)
                return make_response(f'{response}!', status=201)
            else:
                return make_response({'errors': form.errors}, status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)
        
#---END CREATE ROUTE---#


#---READ ROUTE---#

    #---READ BY ID---#

@course_bp.route('/api/v1/course/read/<id>')
def get_course(id:int):
    if request.method == 'GET':
        try:
            controller:object = Course_Controller()
            course:str|dict = controller.read_course(id=id)
            if isinstance(course, str):
                return make_response(f'{course}!' , status=404)
            else:
                return make_response(jsonify(course), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)
        
    #---END READ BY ID---#

    #---READ ALL---#

@course_bp.route('/api/v1/course/read/all')
def get_courses():
    if request.method == 'GET':
        try:
            controller:object = Course_Controller()
            courses:str|dict = controller.read_courses()
            if isinstance(courses, str):
                return make_response(f'{courses}!' , status=404)
            else:
                return make_response(jsonify(courses), status=200)
        except Exception as e:
            return make_response(f'{e}', status=400)

    #---END READ ALL ---#

#---END READ ROUTE---#


#---UPDATE ROUTE---#

@course_bp.route('/api/v1/course/update/<id>',  methods=['PUT'])
def edit_course(id:int):
    if request.method == 'PUT':
        try:
            form:object = Course_Form()
            if form.data:
                if form.validate_on_submit():
                    new_data:dict = form.data
                    controller:object = Course_Controller()
                    response:str = controller.update_course(id=id, new_data=new_data)
                    return make_response(f'{response}!', status=200)
                else:
                    return make_response({'errors': form.errors} , status=400)
            else:
                return make_response('Needed data to update', status=400)
        except Exception as e:
            return make_response(f'{e}', status=400)

#---END UPDATE ROUTE---#


#---DELETE ROUTE---#

@course_bp.route('/api/v1/course/delete/<id>', methods=['DELETE'])
def remove_course(id:int):
    if request.method == 'DELETE':
        try:
            controller:object = Course_Controller()
            response:str = controller.delete_course(id=id)
            return make_response(f'{response}!', 200)
        except Exception as e:
            return make_response(f'{e}', status=400)
        
#---END DELETE ROUTE---#