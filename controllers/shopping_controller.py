from models.shopping_model import Shopping
from db.db import db
from sqlalchemy.exc import SQLAlchemyError
from typing import List

class Shopping_Controller():

    def create_shopping(self, data:dict):
        try:
            new_data = Shopping(**data)
            with db.session.begin():
                db.session.add(new_data)
                db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {e}'
        finally:
            db.session.close()

    def read_shopping(self, id:int):
        try:
            with db.session.begin():
                shopping:Shopping = db.session.query(Shopping).get(ident=id)
                if shopping:
                    return shopping.to_dict()
                else:
                    return 'Shopping not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {e}'
        finally:
            db.session.close()

    def read_shoppings(self):
        try:
            with db.session.begin():
                shoppings:List[Shopping] = db.session.query(Shopping).all()
                if shoppings:
                    data = {shopping.id:shopping.to_dict() for shopping in shoppings}
                    return data
                else:
                    return 'Shoppings Not Found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {e}'
        finally:
            db.session.close()

    def update_shopping(self, id:int, new_data:dict):
        try:
            with db.session.begin():
                shopping:Shopping = db.session.query(Shopping).get(ident=id)
                if shopping:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(shopping, attribute, data)
                    db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f'Error: {e}'
        finally:
            db.session.close()

    def delete_shopping(self, id:int):
        try:
            with db.session.begin():
                db.session.delete()
                db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {e}'
        finally:
            db.session.close()
