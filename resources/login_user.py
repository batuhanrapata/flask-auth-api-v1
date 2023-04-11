import json
import jwt
import os
from flask import request, jsonify
from flask_restful import Resource
from db.db import get_db
from utils.hash_password import decode_hash
from utils.exceptions import LoginError, InternalServerError


SECRET_KEY = os.getenv('SECRET_KEY')
col = get_db("user")

    
class LoginApi(Resource):
    def post(self):
        try:
            """Login a user"""
            req = json.loads(request.data)
            uname = col.find_one({'username': req['username']})
            if decode_hash(uname['password'],req['password']):
                token = jwt.encode({'_id': str(uname['_id'])}, SECRET_KEY, algorithm='HS256')
                return jsonify({'token': token})
            else:
               raise LoginError
        except LoginError:
            raise LoginError
        except Exception as e:
            raise InternalServerError
        
        


    
        
