from flask import request, jsonify
from src.models.User import User
import hashlib
import jwt


class AuthController:

    def login():
        data = request.json
        password = data['password'].encode('utf-8')
        conditions = {"username": str(data['username']),
                      "password": hashlib.md5(password).hexdigest()}
        exist_user = User.filter(conditions)
        if (exist_user):
            token = jwt.encode({"uid": exist_user['user_id']},
                               "aeajthehjtlekj", algorithm="c")
            return jsonify({'success': True, 'token': token})
        else:
            return jsonify({'success': False, "error_message": "Username or Password is incorrect"}), 401

    def signup():
        data = request.json
        return False

    def email_verify():
        data = request.json
        return False

    def email_otp_send():
        data = request.json
        return False

    def reset_password():
        data = request.json
        return False
