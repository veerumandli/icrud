from src.core.Model import Model
class User(Model):
    table_name = "users"
    columns = {
        "id": {
            "key": "id",
            "type": "int",
            "primary": True
        },
        "user_id": {
            "key": "user_id",
            "type": "int"
        },
        "product_name": {
            "key": "product_name",
            "type": "varchar",
            "length": 150
        },
        "quantity": {
            "key": "quantity",
            "type": "int"
        },
        "price": {
            "key": "price",
            "type": "decimal(10,2)"
        },
        "status": {
            "key": "status",
            "type": "enum",
            "options": ["Pending", "Completed", "Cancelled"]
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