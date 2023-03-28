import json
import jwt
import os
from flask import request
from flask import jsonify
from flask_restful import Resource
from resources.db import get_db
from utils.exceptions import ForgotPasswordError, InternalServerError
from utils.mailgun_service import send_reset_mail


SECRET_KEY = os.getenv('SECRET_KEY')
col = get_db("user")


class ForgotPasswordApi(Resource):
    def post(self):
        try:
            """Forgot Password API"""
            req = json.loads(request.data)
            uname = col.find_one({'username': req['username']})
            if uname:
                send_reset_mail(uname['email'], uname['_id'])
                reset_token=jwt.encode({'_id': str(uname['_id'])}, SECRET_KEY, algorithm='HS256')
                return jsonify({'token': reset_token})
            else:
                raise ForgotPasswordError
            
        except ForgotPasswordError:
            raise ForgotPasswordError
        except Exception as e:
            raise InternalServerError
        
