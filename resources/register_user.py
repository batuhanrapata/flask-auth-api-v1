import datetime
import json
import re
from flask import request,jsonify
from flask_restful import Resource
from db.db import get_db
from utils.hash_password import hash_password 
from utils.exceptions import RegisterError, InternalServerError


col = get_db("user")


class RegisterApi(Resource):
    def post(self):
        try: 
            """Register API"""
            req = json.loads(request.data)
            username = req['username']
            password = req['password']
            dummy = password
            email = req['email']
            password = hash_password(password)
            uname = col.find_one({'username': username})
            mail_exist=col.find_one({'email':email})
            if uname:
                return jsonify({'message':'Username already exists'})
            elif mail_exist:
                return jsonify({'message':'Email already exists'})
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return jsonify({'message':'Invalid email'})
            elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', dummy):
                return jsonify({'message':'Password must contain atleast 8 characters, one uppercase, one lowercase, one number and one special character'})
            elif not re.match(r'[A-Za-z0-9]+', username):
                return jsonify({'message':'Username must contain only characters and numbers'}) 
            else:
                user_dict = {'username': username, 'email': email, 'password': password,
                            'date': datetime.datetime.now()}
                status = col.insert_one(user_dict)
                return jsonify({'message':'User registered successfully','id': str(status.inserted_id)})
        except RegisterError:
            raise RegisterError
        except Exception as e:
            raise InternalServerError

