from flask import jsonify
from flask_restful import Resource


class HealthCheckApi(Resource):
    def get(self):
        """Health Check API"""
        return jsonify({'message': 'OK', 'status': 200})