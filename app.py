from flask import Flask
from flask import send_from_directory
from sqlalchemy import create_engine
from config.config import config_dev
from config.db import db

app:object = Flask(__name__)
app.config.from_object(config_dev)
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

db.init_app(app)