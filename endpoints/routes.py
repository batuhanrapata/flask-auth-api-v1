from endpoints.list_users_endpoint import ListUsersApi
from endpoints.login_endpoint import LoginApi 
from endpoints.register_endpoint import RegisterApi
from endpoints.forgot_password_endpoint import ForgotPasswordApi
from endpoints.reset_password_endpoint import ResetPasswordApi
from endpoints.health_check_endpoint import HealthCheckApi


def initialize_routes(api): 
    api.add_resource(LoginApi, '/api/v1/login')
    api.add_resource(RegisterApi, '/api/v1/register')
    api.add_resource(ListUsersApi, '/api/v1/list_users')
    api.add_resource(ForgotPasswordApi, '/api/v1/forgot_password')
    api.add_resource(ResetPasswordApi, '/api/v1/reset_password')
    api.add_resource(HealthCheckApi, '/api/v1/health_check')