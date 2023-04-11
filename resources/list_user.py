import jwt
import os 
from bson import ObjectId
from functools import wraps
from flask import jsonify, request
from flask_restful import Resource
from db.db import get_db
from utils.exceptions import ListUsersError, InternalServerError


SECRET_KEY = os.getenv('SECRET_KEY')
col = get_db("user")


def token_required(f):
    """Decorator to check if token is valid"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'})
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = col.find_one({'_id': ObjectId(data['_id'])})
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'payload': str(e)})
        return f(current_user, *args, **kwargs)

    return decorated


@token_required
def get_all_users(current_user):
    """Get all users"""
    try:
        if not current_user:
            return jsonify({'message': 'Invalid token'})
        users = col.find()
        output = []
        for user in users:
            user_data = {}
            user_data['username'] = user['username']
            output.append(user_data)
        return jsonify({'users': output})
    except ListUsersError:
        raise ListUsersError
    except Exception as e:
        raise InternalServerError



class ListUsersApi(Resource):
    def get(self):
        return get_all_users()