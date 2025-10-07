from functools import wraps
import importlib

def to_camel_case(name: str) -> str:
    return ''.join(word.capitalize() for word in name.split('_'))

def model_from_path(func):
    @wraps(func)
    def wrapper(table_name, *args, **kwargs):
        try:
            class_name = to_camel_case(table_name)
            print(f"[DEBUG] URL table_name: {table_name} -> Converted class: {class_name}")

            module = importlib.import_module(f"src.models.{class_name}")
            print(f"[DEBUG] Imported module: src.models.{class_name}")

            model_class = getattr(module, class_name)
            print(f"[DEBUG] Loaded class: {model_class}")

        except ModuleNotFoundError:
            print(f"[ERROR] Model file src/models/{class_name}.py not found")
            return {"error": f"Model file for '{table_name}' not found"}, 404
        except AttributeError:
            print(f"[ERROR] Class {class_name} not found in module")
            return {"error": f"Class '{class_name}' not found in model file"}, 404

        return func(model_class, *args, **kwargs)

    return wrapper
