from flask import current_app
from flask_wtf.csrf import generate_csrf

def generate_token():
    with current_app.app_context():
        return generate_csrf()
