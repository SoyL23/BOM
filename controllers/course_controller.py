from db.db import db
from model.course_model import Course

class Course_Controller():

    def __init__(self):
        pass

    def create_course(self, course_data:dict) -> str:
        try:
            course:object = Course(**course_data)
            with db.session.begin():
                db.session.add(course)
                db.session.commit()
            return 'Course created successfully.'    
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()
        

    def read_course(self, id:int):
        try:
            course:object = db.session.query(Course).filter(Course.id == id).first()
            if course:
                return course.to_dict()
            else:
                return 'Course not found'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def read_courses(self):
        try:
            data:dict = {}
            courses = db.session.query(Course).all()
            if courses:
                for course in courses:
                    data[course.id] = course.to_dict()
                return data
            else:
                return 'Courses not found'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()
        

    def update_course(self, id:int, new_data:dict):
        try:
            course:object = db.session.query(Course).filter(Course.id == id).first()
            if course:
                for attribute, data in new_data.items():
                    if attribute != 'id':
                        setattr(course, attribute, data)
                db.session.commit()
                return "Course updated successfully."
            else:
                return 'Course not Found' 
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def delete_course(self, id:int):
        try:
            course:object = db.session.query(Course).filter(Course.id == id).first()
            if course:
                db.session.delete(course)
                db.session.commit()
                return 'Course deleted successfully'
            else:
                return 'Course not found.'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()
