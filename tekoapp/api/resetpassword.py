from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from tekoapp import models, services

ns = Namespace('resetpassword', description='resetpassword system')

_resetpass_req = ns.model(
    'resetpass_req', 
    {
        'username': fields.String(required=True, description='user username'),
        'email' : fields.String(required=True, description='user email')
    }
)

@ns.route('/')
class Resetpassword(Resource):
    @ns.expect(_resetpass_req, validate=True)
    def post(self):
        data = request.json or request.args
        user = services.resetpassword.check_info_form_resetpassword_and_res(**data)
        return user