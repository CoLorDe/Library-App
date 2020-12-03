from flask import Blueprint

bp = Blueprint('manage', __name__)

from app.admin import manage
