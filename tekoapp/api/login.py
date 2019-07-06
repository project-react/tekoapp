from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from tekoapp import models, services

ns = Namespace('login', description='login operator')

_login_req = ns.model(
    'login_req', models.UserSchema.user_create_req
)

@ns.route('/')
class Login(Resource):
    @ns.expect(_login_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.login.check_info_from_login_request(**data)