from model.employee_model import Employee
from db.db import db

class Controller:
    
    def create_(self):
        try:
            with db.session.begin():
                db.session.add()
                db.session.commit()    
        except:
            db.session.rollback()
        finally:

            db.session.close()
    
    def read_(self):
        try:
            with db.session.begin():
                 
                 pass   
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def read_all(self):
        try:
            with db.session.begin():
                 pass    
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update_(self):
        try:
            with db.session.begin():
                pass
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete_(self):
        try:
            with db.session.begin():
                db.session.delete()
                db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()