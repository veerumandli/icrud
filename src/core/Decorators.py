from functools import wraps
import importlib


def model_from_path(func):
    """Decorator to load model dynamically based on <table_name> in route."""

    @wraps(func)
    def wrapper(table_name, *args, **kwargs):
        try:
            module = importlib.import_module(
                f"src.models.{table_name.capitalize()}")
            model_class = getattr(module, table_name.capitalize())
        except (ModuleNotFoundError, AttributeError):
            return {"error": f"Model '{table_name}' not found"}, 404

        return func(model_class, *args, **kwargs)
    return wrapper
