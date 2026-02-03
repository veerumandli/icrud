from flask import Blueprint
from src.controllers.AuthController import AuthController


auth_route = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_route.route("/login", methods=['POST'])
def login():
    return AuthController.login()


@auth_route.route("/signup", methods=['POST'])
def signup():
    return AuthController.signup()


@auth_route.route("/email_otp_send", methods=['POST'])
def email_otp_send():
    return AuthController.email_otp_send()


@auth_route.route("/reset_password", methods=['POST'])
def reset_password():
    return AuthController.reset_password()
