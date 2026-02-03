from src.core.Model import Model


class User(Model):
    table_name = "users"
    columns = {
        "user_id": {
            "key": "user_id",
            "type": "int",
            "primary": True
        },
        "name": {
            "key": "name",
            "type": "varchar",
            "length": 45
        },
        "username": {
            "key": "username",
            "type": "varchar",
            "length": 100
        },
        "password": {
            "key": "password",
            "type": "varchar",
            "length": 150
        },
        "status": {
            "key": "status",
            "type": "int",
        },
        "email_address": {
            "key": "status",
            "type": "varchar",
            "length": 255
        },
        "is_email_verified": {
            "key": "status",
            "type": "int",
        },
        "otp": {
            "key": "status",
            "type": "int",
        },
        "created_at": {
            "key": "created_at",
            "type": "datetime"
        },
        "modified_at": {
            "key": "modified_at",
            "type": "datetime"
        }
    }
