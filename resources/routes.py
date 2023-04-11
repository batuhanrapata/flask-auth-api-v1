from resources.list_user import ListUsersApi
from resources.login_user import LoginApi 
from resources.register_user import RegisterApi
from resources.forgot_password import ForgotPasswordApi
from resources.reset_password import ResetPasswordApi
from resources.healt_check import HealthCheckApi


def initialize_routes(api): 
    api.add_resource(LoginApi, '/api/v1/login')
    api.add_resource(RegisterApi, '/api/v1/register')
    api.add_resource(ListUsersApi, '/api/v1/list_users')
    api.add_resource(ForgotPasswordApi, '/api/v1/forgot_password')
    api.add_resource(ResetPasswordApi, '/api/v1/reset_password')
    api.add_resource(HealthCheckApi, '/api/v1/health_check')