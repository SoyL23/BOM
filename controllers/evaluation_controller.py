from models.evaluation_model import Evaluation
from db.db import db
from typing import List
from sqlalchemy.exc import SQLAlchemyError

class Evaluation_Controller():
    
    def create_evaluation(self, evaluation_data:dict) -> str:
        try:
            with db.session.begin():    
                evaluation:object = Evaluation(**evaluation_data)
                db.session.add(evaluation)
                db.session.commit()
            return 'Evaluation created successfully.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def read_evaluation(self, id:int) -> str|dict:
        try:
            evaluation:object = db.session.query(Evaluation).get(ident=id)
            if evaluation:
                return evaluation.to_dict()
            else:
                return 'Evaluation not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()


    def read_evaluations(self) -> str | dict:
        try:
            with db.session.begin():
                evaluations:List[Evaluation] = db.session.query(Evaluation).all()
                if evaluations:
                    data:dict = {evaluation.id:evaluation.to_dict() for evaluation in evaluations}
                    return data
                else: 
                    return 'Evaluations not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'        
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def update_evaluation(self, id:int, new_data:dict) -> str:
        try:
            with db.session.begin():
                evaluation:object = db.session.query(Evaluation).get(ident=id)
                if evaluation:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(evaluation, attribute, data)
                    db.session.commit()
                    return "Evaluation updated successfully."
                else:
                     return 'Evaluation not found.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def delete_evaluation(self, id:int) -> str:
        try:
            with db.session.begin():
                evaluation:object = db.session.query(Evaluation).get(ident=id)
                if evaluation:
                        db.session.delete(evaluation)
                        db.session.commit()
                        return 'Evaluation deleted successfully.'
                else:
                    return "Evaluation not found."
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()