from models.user_data_model import User_Data
from db.db import db
from sqlalchemy.exc import SQLAlchemyError

class User_Data_Controller:
    
    def create_data(self, data:dict) -> str:
        try:
            user_data = User_Data(**data)
            with db.session.begin():
                db.session.add(user_data)
                db.session.commit()
                return 'User Data is Saved'    
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def read_data(self, id:int) -> str | dict:
        try:
            with db.session.begin():
                data = db.session.query(User_Data).get(ident=id)
                if data:
                    return data.to_dict()
                else:
                     return 'User data not found.'   
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()


    def update_data(self,id:int, new_data:dict) -> str:
        try:
            with db.session.begin():
                user_data = db.session.query(User_Data).get(ident=id)
                if user_data:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(user_data, attribute, data)
                    return 'User data updated succesfully.'
                else:
                     return 'User data not found.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def delete_data(self, id:int) -> str:
        try:
            with db.session.begin():
                user_data:User_Data = db.session.query(User_Data).get(ident=id)
                if user_data:
                    db.session.delete(user_data)
                    db.session.commit()
                    return 'Data deleted successfully.'
                else:
                    return 'Data Not found.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()