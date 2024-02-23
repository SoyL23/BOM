from flask import jsonify
from config.db import db
class Config_Development:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:SmartCol24*@localhost/bom_entrenamiento"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    SECRET_KEY = "*b0m_3ntr3n4m13nt0_db*"
    SESSION_TYPE = 'sqlalchemy'
    SESSION_SQLALCHEMY = db

config_dev:object = Config_Development()