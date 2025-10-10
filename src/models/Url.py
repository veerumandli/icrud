from src.core.Model import Model


class Url(Model):
    table_name = "urls"
    slug_column = "status"
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
        "count": {
            "key": "clicks",
            "type": "int",
        },
        "status": {
            "key": "status",
            "type": "enum",
            "options": ["Active", "Inactive"]
        },
    }
