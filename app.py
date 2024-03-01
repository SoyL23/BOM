from flask import Flask, send_from_directory, render_template, jsonify
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager
from config.config import config_dev
from config.db import db
from routes.user import user
from routes.auth import auth
from routes.role import role
from routes.doc_type import doc_type
from services.generate_token import generate_token

app = Flask(__name__)
app.config.from_object(config_dev)

db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db_migrate = Migrate(app=app, db=db)
db.init_app(app)

csrf = CSRFProtect()
csrf.init_app(app)
JWTManager(app=app)

@app.route('/')
def home():
  with app.app_context():
    token = generate_token()
    return render_template('index.html', token=token)


@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(role)
app.register_blueprint(doc_type)