from werkzeug.exceptions import UnsupportedMediaType
from flask import request

def require_content_type(content_type:str):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if request.mimetype != content_type:
                print(request.mimetype)
                raise UnsupportedMediaType(description=f"Tipo de contenido no admitido. Se esperaba {content_type}")
            return f(*args, **kwargs)
        return wrapper
    return decorator