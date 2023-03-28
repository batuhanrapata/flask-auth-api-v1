class InternalServerError(Exception):
    pass
class LoginError(Exception):
    pass
class RegisterError(Exception):
    pass
class ForgotPasswordError(Exception):
    pass
class ResetPasswordError(Exception):
    pass
class ListUsersError(Exception):
    pass


errors={
    "InternalServerError":{"message":"Internal Server Error","status":500},
    "LoginError":{"message":"Login failed","status":400},
    "RegisterError":{"message":"Register failed","status":400},
    "ForgotPasswordError":{"message":"Forgot password failed","status":400},
    "ResetPasswordError":{"message":"Reset password failed","status":400},
    "ListUsersError":{"message":"List users failed","status":400},
}
