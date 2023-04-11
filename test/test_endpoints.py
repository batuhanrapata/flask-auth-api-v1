#tests endpoints

from flask import Flask
from endpoints.routes import initialize_routes
from flask_restful import Api
from utils.exceptions import errors

app=Flask(__name__)
api=Api(app, errors=errors)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)

#tests test_endpoints.py

import unittest
from app import app

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/api/v1/health_check')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.post('/api/v1/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.post('/api/v1/register')
        self.assertEqual(response.status_code, 200)

    def test_list_users(self):
        response = self.app.get('/api/v1/list_users')
        self.assertEqual(response.status_code, 200)

    def test_forgot_password(self):
        response = self.app.post('/api/v1/forgot_password')
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        response = self.app.post('/api/v1/reset_password')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

#tests test_endpoints.py

