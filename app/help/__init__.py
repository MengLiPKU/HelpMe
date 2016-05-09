from flask import Blueprint

help = Blueprint('help', __name__, url_prefix='/help/')

from . import views
