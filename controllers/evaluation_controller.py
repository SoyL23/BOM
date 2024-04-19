from model.evaluation_model import Evaluation
from db.db import db

class Evaluation_Controller:
    
    def create_(self, evaluation_data):
        
        try:
            evaluation = Evaluation(**evaluation_data)
            with db.session.begin():
                db.session.add(evaluation)
                db.session.commit()
            return 'Evaluation created successfully.'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()
    
    def read_(self, id:int):
        try:
            with db.session.begin():
                 evaluation = db.session.query(Evaluation).filter(Evaluation.id == id).first()
                 pass   
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def read_evaluations(self):
        try:
            with db.session.begin():
                 evaluations = db.session.query(Evaluation).all()
                 if evaluations:
                    data = {evaluation.id:evaluation.to_dict() for evaluation in evaluations}
                    return data
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def update_evaluation(self, id:int):
        try:
            with db.session.begin():
                evaluation = db.session.query(Evaluation).filter(Evaluation.id == id).first()
                pass
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def delete_evaluation(self, id:int):
        try:
            evaluation = db.session.query(Evaluation).filter(Evaluation.id == id).first()
            with db.session.begin():
                db.session.delete(evaluation)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()