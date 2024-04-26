from db.db import db
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError


class Auth_Controller():
    def __init__(self):
        pass

    def login(self, data: dict)-> str|dict:
        try:
            username = data.get('username')
            password = data.get('password')
            if not username or not password:
                return 'Username and password are required'
            with db.session.begin():
                user = db.session.query(User).filter_by(username=username).first()
                if user:
                    if user.check_password(password=password):
                        data = user.to_dict()
                        data['role'] = data['data'][0]['role'] if 'data' in data and data['data'] else None
                        data['email'] = data['data'][0]['email'] if 'data' in data and data['data'] else None
                        return data
                    else:
                        return 'Invalid Password'
                else:
                    return 'User does not exist'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            return str(e)
        finally:
            db.session.close()

        

    def logout(self):
        pass