from src.core.Model import Model


class Url(Model):

    columns = {
        "id": {
            "key": "id",
            "type": "int",
            "primary": True
        },
        "url": {
            "key": "url",
            "type": "varchar",
            "length": 300
        },
        "short_url": {
            "key": "short_url",
            "type": "varchar",
            "length": 50
        },
        "clicks": {
            "key": "clicks",
            "type": "int",
        },
        "status": {
            "key": "status",
            "type": "enum",
            "options": ["Active", "Inactive"]
        },
    }
