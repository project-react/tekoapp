from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from tekoapp import models, services

ns = Namespace('logout', description='logout operator')

parser = ns.parser()
parser.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

@ns.route('/')
class Logout(Resource):   
    @ns.expect(parser)
    def get(self):
        token = request.headers.get('Authorization')
        return services.logout.check_token_from_logout_request(token)