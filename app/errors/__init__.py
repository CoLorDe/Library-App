from flask import Blueprint
from app import create_app

bp = Blueprint('errors', __name__)

from app.errors import handlers
