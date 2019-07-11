from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from tekoapp import services

ns = Namespace('maintainLogin', description='verify maintain login')

parser = ns.parser()
parser.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

@ns.route('/')
class MaintainLogin(Resource):   
    @ns.expect(parser)
    def get(self):
        token = request.headers.get('Authorization')
        return services.login.check_maintain_login(token)