from db.db import db
from models.user_model import User
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from typing import List
from werkzeug.security import generate_password_hash

class User_Controller():

#---CREATE USER CONTROLLER---#

    def create_user(self, user_data:dict) -> str:
        try:
            user_data['password'] = generate_password_hash(password=user_data['password'])
            user:object = User(**user_data)
            with db.session.begin():
                db.session.add(user)
                db.session.commit()
            return 'User created successfully.'
        except IntegrityError as ie:
            db.session.rollback()
            return 'Username has been used'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
        
#---END CREATE USER CONTROLLER---#



#---READ USER CONTROLLER---#

    #---Read User by id---#
    def read_user(self, id:int) -> str | dict:
        try:
            with db.session.begin():
                user:object = db.session.query(User).get(ident=id)
                if user:
                    return user.to_dict()
                else:
                    return 'User not found.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    #---END Read User by id---#

    #---Read All Users---#
    def read_users(self) -> str | dict:
        try:
            with db.session.begin():
                users:List[User] = db.session.query(User).all()
                if users:
                    data:dict = {user.id: user.to_dict() for user in users}
                    return data
                else:
                    return 'Users not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    #---END Read All Users---#

#---END READ USER CONTROLLER---#



#---UPDATE USER CONTROLLER---#
    def update_user(self, id:int, new_data:dict) -> str:
        try:
            with db.session.begin():    
                user:object = db.session.query(User).get(ident=id)
                if user:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(user, attribute, data)
                    db.session.commit()
                    return "User updated successfully."
                else:
                    return "User not found."
        except IntegrityError as ie:
            db.session.rollback()
            return 'Username has been used'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---UPDATE USER CONTROLLER---#

#---DELETE USER CONTROLLER---#
    def delete_user(self, id:int) -> str:
        try:
            with db.session.begin():    
                user:object = db.session.query(User).get(ident=id)
                if user:
                    db.session.delete(user)
                    db.session.commit()
                    return "User deleted successfully."
                else:
                    return "User not found."
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END DELETE USER CONTROLLER---#