# productos/__init__.py
from flask import Blueprint


productos_bp = Blueprint('productos', __name__)

# import routes
from . import routes