from flask_restplus import Namespace, Resource, fields 
from flask import request, jsonify
from tekoapp import models, services

ns = Namespace('auth', description='Sign in operators')
_signup_request_req = ns.model(
    'signup_request_req', models.SignupSchema.signup_request_req
    )

_signup_request_res = ns.model(
    'signup_request_res', models.SignupSchema.signup_request_res
    )

_verify_res = ns.model('', model={
    'message': fields.String(required=True, description='verify success or not'),
})

_login_req = ns.model(
    'login_req', models.UserSchema.user_create_req
)

_changepassword_req = ns.model(
    'changepassword_req', 
    {
        'token' : fields.String(required=True, description='user email'),
        'password' : fields.String(required=True, description='your password'),
        'newpassword' : fields.String(required=True, description='new password')
    }
)

_resetpass_req = ns.model(
    'resetpass_req', 
    {
        'username': fields.String(required=True, description='user username'),
        'email' : fields.String(required=True, description='user email')
    }
)

parser_logout = ns.parser()
parser_logout.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

parser_maintain = ns.parser()
parser_maintain.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

@ns.route('/register/')
class Register(Resource):
    @ns.expect(_signup_request_req, validate=True)
    # @ns.marshal_with(_signup_request_res)
    def post(self):
        data = request.json or request.args
        # user = services.signup.create_user_to_signup_request(**data)
        return services.signup.create_user_to_signup_request(**data)

@ns.route('/register/verify/<string:token>')
class Verify(Resource):
    @ns.marshal_with(_verify_res)
    def get(self, token):
        message = services.signup.verify(token)
        return message

@ns.route('/login/')
class Login(Resource):
    @ns.expect(_login_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.login.check_info_from_login_request(**data)

@ns.route('/logout/')
class Logout(Resource):   
    @ns.expect(parser_logout)
    def get(self):
        token = request.headers.get('Authorization')
        return services.logout.check_token_from_logout_request(token)

@ns.route('/changePassword/')
class Changepassword(Resource):
    @ns.expect(_changepassword_req, validate=True)
    def post(self):
        data = request.json or request.args
        print("changePassword valid!!!!")
        return services.changepassword.check_info_and_res(**data)

@ns.route('/resetPassword/')
class Resetpassword(Resource):
    @ns.expect(_resetpass_req, validate=True)
    def post(self):
        data = request.json or request.args
        user = services.resetpassword.check_info_form_resetpassword_and_res(**data)
        return user

@ns.route('/maintainLogin/')
class MaintainLogin(Resource):   
    @ns.expect(parser_maintain)
    def get(self):
        token = request.headers.get('Authorization')
        return services.login.check_maintain_login(token)
