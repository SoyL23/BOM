from model.evaluation_model import Evaluation
from db.db import db

class Evaluation_Controller:
    
    def create_evaluation(self, evaluation_data:dict):
        
        try:
            evaluation:object = Evaluation(**evaluation_data)
            with db.session.begin():
                db.session.add(evaluation)
                db.session.commit()
            return 'Evaluation created successfully.'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()
    
    def read_evaluation(self, id:int):
        try:
            with db.session.begin():
                 evaluation:object = db.session.query(Evaluation).filter(Evaluation.id == id).first()
                 if evaluation:
                     return evaluation.to_dict()
                 else:
                     return 'Evaluation not found'   
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
                    data:dict = {evaluation.id:evaluation.to_dict() for evaluation in evaluations}
                    return data
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def update_evaluation(self, id:int, new_data:dict):
        try:
            with db.session.begin():
                evaluation:object = db.session.query(Evaluation).filter(Evaluation.id == id).first()
                if evaluation:
                    for attribute, data in new_data.items():
                        setattr(evaluation, attribute, data)
                    db.session.commit()
                    return "Evaluation updated successfully."
                else:
                     return 'User not found.'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def delete_evaluation(self, id:int):
        try:
            evaluation:object = db.session.query(Evaluation).filter(Evaluation.id == id).first()
            if evaluation:
                with db.session.begin():
                    db.session.delete(evaluation)
                    db.session.commit()
                    return 'Evaluation deleted successfully.'
            else:
                return "Evaluation not found."
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()