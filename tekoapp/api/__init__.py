import logging

from flask import Blueprint
from flask_restplus import Api

# from boilerplate.extensions.exceptions import global_error_handler
from .user import ns as user_ns

_logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app = api_bp, 
    version = '1.0', 
    title = 'tekoapp API', 
    validate = False, 
)

def init_app(app, **kwargs): 
    api.add_namespace(user_ns)