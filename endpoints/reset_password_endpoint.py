import json
import os
import jwt
from bson import ObjectId
from flask import jsonify
from flask import request
from flask_restful import Resource
from resources.db import get_db
from utils.exceptions import ResetPasswordError, InternalServerError
from utils.hash_password import hash_password
from utils.mailgun_service import verify_reset_otp


SECRET_KEY=os.getenv('SECRET_KEY')
col=get_db("user")


class ResetPasswordApi(Resource):
    def post(self):
        try:
            """Reset Password API"""
            req = json.loads(request.data)
            token = req['token']
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = col.find_one({'_id': ObjectId(data['_id'])})
            if current_user:
                if verify_reset_otp(req['otp'], current_user['_id']):
                    col.update_one({'_id': ObjectId(data['_id'])}, {'$set': {'password': hash_password(req['password'])}})
                    return jsonify({'message': 'Password reset successful'})
                else:
                    raise ResetPasswordError
            else:
                raise ResetPasswordError
        except ResetPasswordError:
            raise ResetPasswordError
        except Exception as e:
            raise InternalServerError