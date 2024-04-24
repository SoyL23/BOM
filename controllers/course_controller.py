from db.db import db
from models.course_model import Course
from sqlalchemy.exc import SQLAlchemyError
from typing import List

class Course_Controller():

    def __init__(self):
        pass

#---INIT CREATE COURSE CONTROLLER---#
    def create_course(self, course_data:dict) -> str:
        try:
            course:object = Course(**course_data)
            with db.session.begin():
                db.session.add(course)
                db.session.commit()
            return 'Course created successfully.' 
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'   
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END COURSE CONTROLLER---#            

        
#---INIT COURSE CONTROLLER---#
    def read_course(self, id:int) -> str | dict:
        try:
            course:object = db.session.query(Course).get(ident=id)
            if course:
                return course.to_dict()
            else:
                return 'Course not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END COURSE CONTROLLER---#            

#---INIT COURSE CONTROLLER---#
    def read_courses(self) -> str | dict:
        try:
            courses:List[Course] = db.session.query(Course).all()
            if courses:
                data:dict = {course.id:course.to_dict() for course in courses}    
                return data
            else:
                return 'Courses not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END COURSE CONTROLLER---#            
        
#---INIT COURSE CONTROLLER---#
    def update_course(self, id:int, new_data:dict) -> str:
        try:
            course:object = db.session.query(Course).get(ident=id)
            if course:
                for attribute, data in new_data.items():
                    if attribute != 'id':
                        setattr(course, attribute, data)
                db.session.commit()
                return "Course updated successfully."
            else:
                return 'Course not Found' 
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END COURSE CONTROLLER---#

#---INIT COURSE CONTROLLER---#
    def delete_course(self, id:int) -> str:
        try:
            course:object = db.session.query(Course).get(ident=id)
            if course:
                db.session.delete(course)
                db.session.commit()
                return 'Course deleted successfully'
            else:
                return 'Course not found.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END CONTROLLER---#            
