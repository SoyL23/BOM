import os
from flask import Flask
from config.config import ConfigDev
from dotenv import load_dotenv
from routes.user_routes import user_bp
from routes.course_routes import course_bp


class App():

    def __init__(self):
        
        load_dotenv()
        self.app = Flask(__name__)
        self.app.config.from_object(ConfigDev)
        self.app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        
        self.app.register_blueprint(user_bp)
        self.app.register_blueprint(course_bp)
        
    def app_context(self):
        return self.app.app_context()
    
app = App()

