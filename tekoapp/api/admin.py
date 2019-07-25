from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from tekoapp import models, services

ns = Namespace('admin', description='function for Admin')

parser_getlistuser = ns.parser()
parser_getlistuser.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

@ns.route('/getlistuser/')
class Getlistuser(Resource):
    @ns.expect(parser_getlistuser)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.getlistuser.get_list_user(token)