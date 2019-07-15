import json
import logging
import jwt
import config
import re

from datetime import datetime, timedelta
from tekoapp import models as m
from tekoapp.tests.api import APITestCase
from tekoapp import repositories as r, helpers

_logger = logging.getLogger(__name__)


class UserApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/register/'

    def method(self):
        return 'POST'

    def test_create_user_when_success_then_insert_user_into_db(self):
        valid_data = {
            'username': 'nguyenduychien',
            'email': 'duychien226@gmail.com',
            'password': 'Nguyenduychien1.',
        }
        self.send_request(data=valid_data)
        saved_signup = r.signup.find_one_by_email_or_username_in_signup_request(valid_data['email'], valid_data['username'])
        assert saved_signup
        self.assertEqual(saved_signup.username, valid_data['username'])
        self.assertEqual(saved_signup.email, valid_data['email'])

class LoginApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/login/'

    def method(self):
        return 'POST'

    def test_login(self):
        # create mock user data
        mock_data = {
            'username' : 'nguyenduychien',
            'email' : 'duychien226@gmail.com',
            'password' : 'Nguyenduychien1.',
        }
        signup_req = r.signup.save_user_to_signup_request(
            **mock_data
        )
        print(signup_req.password_hash)
        user = r.signup.save_user_to_user(
            username=signup_req.username,
            email=signup_req.email,
            password=signup_req.password_hash
        )
        user_test = r.user.find_user_by_username_and_email(user.username, user.email)
        print(user_test.id)
        # create req login
        valid_data = {
            'username': 'nguyenduychien',
            'password': 'Nguyenduychien1.',
        }
        self.send_request(data=valid_data)
        check_exist_user_token = m.User_Token.query.filter(
            m.User_Token.user_id == user_test.id
        ).first()
        self.assertEqual(check_exist_user_token.id, user_test.id)