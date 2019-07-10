from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from tekoapp import models, services

ns = Namespace('changepassword', description='changepassword operator')

_changepassword_req = ns.model(
    'changepassword_req', 
    {
        'token' : fields.String(required=True, description='user email'),
        'password' : fields.String(required=True, description='your password'),
        'newpassword' : fields.String(required=True, description='new password')
    }
)

@ns.route('/')
class Changepassword(Resource):
    @ns.expect(_changepassword_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.changepassword.check_info_and_res(**data)