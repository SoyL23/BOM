from db.db import db
from model.user_model import User
from flask import request

class User_Controller():
    def __init__(self):
        # print('HI MADAFAKAS!')
        pass

#---CREATE USER CONTROLLER---#

    def create_user(self, user_data:dict) -> str:
        try:
            user = User(**user_data)
            with db.session.begin():
                db.session.add(user)
                db.session.commit()
            return 'User created successfully.'
        except Exception as e:
            return str(e)
        
#---END CREATE USER CONTROLLER---#



#---READ USER CONTROLLER---#

    #---Read User by id---#
    def read_user(self, id:int):
        try:
            user = db.session.query(User).filter(User.id == id).first()
            if user:
                return user.to_dict()
            else:
                return 'User not found.'
        except Exception as e:
            return str(e)
    #---END Read User by id---#

    #---Read All Users---#
    def read_users(self):
        try:
            data = {}
            users = db.session.query(User).all()
            if users:
                for user in users:
                    data[user.id] = user.to_dict()
                return data
            else:
                return 'Users not found'
        except Exception as e:
            return str(e)
    #---END Read All Users---#

#---END READ USER CONTROLLER---#



#---UPDATE USER CONTROLLER---#

    def update_user(self, id:int, new_data:dict) -> str:
        try:
            user = db.session.query(User).filter(User.id == id).first()
            if user:
                for attribute, data in new_data.items():
                    if attribute != 'id':
                        setattr(user, attribute, data)
                db.session.commit()
                return "User updated successfully."
            else:
                return "User not found."
        except Exception as e:
            return str(e)

#---UPDATE USER CONTROLLER---#



#---DELETE USER CONTROLLER---#

    def delete_user(self, id:int):
        try:
            user = db.session.query(User).filter(User.id == id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return "User deleted successfully."
            else:
                return "User not found."
        except Exception as e:
            return str(e)

#---END DELETE USER CONTROLLER---#