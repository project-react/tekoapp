from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from tekoapp import services, helpers

ns = Namespace('admin', description='function for Admin')

parser_getlistuser = ns.parser()
parser_getlistuser.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

_edituser_req = ns.model(
    'edituser_req',
    {
        'old_username': fields.String(required=True, description='old username'),
        'new_username': fields.String(required=True, description='username'),
        'new_email': fields.String(required=True, description='email'),
        'is_admin': fields.Boolean(required=True, description='is admin', default=False)
    }
)

@ns.route('/getlistuser/')
class Getlistuser(Resource):
    @ns.expect(parser_getlistuser)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.getlistuser.get_list_user(token)

@ns.route('/isAdmin/')
class VerifyAdmin(Resource):
    @ns.expect(parser_getlistuser)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.verifyadmin.verify_is_admin_by_token(token)

@ns.route('/edituser/')
class EditUser(Resource):
    @ns.expect(parser_getlistuser, _edituser_req)
    def put(token):
        token = request.headers.get('Authorization')
        services.admin.verifyadmin.verify_is_admin_by_token(token)
        data = request.json or request.args
        return services.admin.edituser.edit_user(**data)
