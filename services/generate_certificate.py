from controllers.evaluation_controller import Evaluation_Controller
from db.db import db
from models.user_model import User
from models.course_model import Course
from models.certificate_model import Certificate
from models.evaluation_model import Evaluation
from models.company_model import Company
from datetime import datetime as dt

class Generate_Certificate:
    def __init__(self, evaluation_id: int):
        self.certificate = self.__generate_certificate(evaluation_id)

    def __generate_certificate(self, evaluation_id: int):
        try:
            evaluation_controller = Evaluation_Controller()
            evaluation:str|dict = evaluation_controller.read_evaluation(id=evaluation_id)
            if not evaluation or isinstance(evaluation, str):
                return None

            user_id:int = evaluation['student_id']
            course_id:int = evaluation['course_id']

            with db.session.begin():
                user = db.session.query(User).get(user_id)
                course = db.session.query(Course).get(course_id)
                company = db.session.query(Company).get(course.company_id)

                if not all([user, course, company]):
                    return None

                date = dt.now().date()
                status = 'Certified'
                certificate = Certificate(
                    date=date,
                    status=status,
                    company_id=company.id,
                    course_id=course.id,
                    student_id=user.id
                )
                return certificate
        except Exception as e:
            db.session.rollback()
            print(f"Error: {str(e)}")
            return None
        finally:
            db.session.close()