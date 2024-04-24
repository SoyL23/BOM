from models.sell_model import Sell
from db.db import db
from sqlalchemy.exc import SQLAlchemyError
from typing import List

class Sell_Controller:
    
    def create_sell(self, data:dict) -> str:
        try:
            sell:object = Sell(**data)
            with db.session.begin():
                db.session.add(sell)
                db.session.commit()    
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def read_sell(self, id:int) -> str | dict:
        try:
            with db.session.begin():
                 sell = db.session.query(Sell).get(ident=id)
                 if sell:
                     return sell.to_dict()
                 else:
                     return 'Sell not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'           
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def read_sells(self) -> str | dict:
        try:
            with db.session.begin():
                 sells = db.session.query(Sell).all()
                 if sells:
                     data = {sell.id:sell.to_dict() for sell in sells} 
                     return data
                 else:
                     'Sells Not found'   
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def update_sell(self, id:int, new_data:dict) -> str:
        try:
            with db.session.begin():
                sell = db.session.query(Sell).get(ident=id)
                if sell:
                    for attribute, data in new_data.items():
                        setattr(sell, attribute, data)
                    db.session.commit()
                    return 'Sell updated successfully'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def delete_sell(self, id:int) -> str:
        try:
            with db.session.begin():
                sell = db.session.query(Sell).get(ident=id)
                if sell:
                    db.session.delete(sell)
                    db.session.commit()
                    return 'Sell deleted successfully.'
                else:
                    return 'Sell not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()