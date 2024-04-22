import os
from flask import Flask
from config.config import ConfigDev
from dotenv import load_dotenv
from routes.user_routes import user_bp
from routes.user_data_route import user_data_bp
from routes.course_routes import course_bp
from routes.company_routes import company_bp
from routes.employee_route import employee_bp
from routes.evaluation_route import evaluation_bp
class App():

    def __init__(self):
        
        load_dotenv()

        self.app = Flask(__name__)
        self.app.config.from_object(ConfigDev)
        self.app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        
        self.app.register_blueprint(user_bp)
        self.app.register_blueprint(course_bp)
        self.app.register_blueprint(company_bp)
        self.app.register_blueprint(employee_bp)
        self.app.register_blueprint(evaluation_bp)
        self.app.register_blueprint(user_data_bp)

        @self.app.route('/')
        def home():
            return "HI MADAFAKAS, I'M ONLINE!"
        
    def app_context(self):
        return self.app.app_context()
    
app = App()