from flask import Blueprint
from flask_restplus import Api
from .signup import ns as signup_ns
from .login import ns as login_ns

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_bp,
    version='1.0',
    title='API',
    validate=False,
    # doc='' # disable Swagger UI
)

def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    api.add_namespace(signup_ns)
    api.add_namespace(login_ns)
    app.register_blueprint(api_bp)