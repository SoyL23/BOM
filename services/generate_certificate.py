from controllers.evaluation_controller import Evaluation_Controller as Controller
from db.db import db
from model.user_model import User
from model.course_model import Course
from model.certificate_model import Certificate
from model.evaluation_model import Evaluation
from model.company_model import Company
from datetime import datetime as dt

class Generate_Certificate():
    def __init__(self, evaluation_id:int) -> None:
        self.__data = self.__get_data(evaluation_id=evaluation_id)
        self.certificate = self.generate_instance(self.__data)
        pass

    def __get_data(self, evaluation_id:int):
        try:
            evaluation = Controller.read_evaluation(id=evaluation_id)
            if evaluation.status != "Approved":
                return None
            with db.session.begin():
                user = db.session.query(User).filter(User.id == evaluation.student_id).first()
                course = db.session.query(Course).filter(Course.id == evaluation.course_id).first()
                company = db.session.query(Company).filter(Company.id == course.company_id).first()

                return {
                    'user': user.to_dict() if user else None,
                    'course': course.to_dict() if course else None,
                    'company': company.to_dict() if company else None
                }
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def generate_instance(self, data):
        date = dt.now().date()  
        status = 'Certified'  
        company_id = data['company']['id']
        course_id = data['course']['id']
        student_id = data['user']['id']
        certificate = Certificate(date=date, status=status, company_id=company_id, course_id=course_id, student_id=student_id)
        return certificate
