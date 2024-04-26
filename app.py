from flask import Flask
from config.config import ConfigDev
from routes.user_routes import user_bp
from routes.user_data_route import user_data_bp
from routes.course_routes import course_bp
from routes.company_routes import company_bp
from routes.employee_route import employee_bp
from routes.evaluation_route import evaluation_bp
from routes.certificate_routes import certificate_bp
from routes.shopping_route import shopping_bp
from routes.sell_route import sell_bp
from routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
class App():

    def __init__(self):
        
        

        self.app = Flask(__name__)
        self.app.config.from_object(ConfigDev)
        self.jwt = JWTManager(self.app)
        
        
        self.app.register_blueprint(user_bp)
        self.app.register_blueprint(course_bp)
        self.app.register_blueprint(company_bp)
        self.app.register_blueprint(employee_bp)
        self.app.register_blueprint(evaluation_bp)
        self.app.register_blueprint(user_data_bp)
        self.app.register_blueprint(certificate_bp)
        self.app.register_blueprint(shopping_bp)
        self.app.register_blueprint(sell_bp)
        self.app.register_blueprint(auth_bp)

        @self.app.route('/')
        def home():
            return "HI MADAFAKAS, I'M ONLINE!"
        
    def app_context(self):
        return self.app.app_context()
    
app = App()