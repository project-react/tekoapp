from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from tekoapp import models

ns = Namespace('login', description='login operator')

_login_req = ns.model(
    'login_req', models.UserSchema.user_create_req
)

_login_res = ns.model(
    'login_res', models.UserSchema.user_create_res 
)

@ns.route('/')
class Login(Resource):
    
    def post(self):
        data = request.json or request.args
        
        return ''