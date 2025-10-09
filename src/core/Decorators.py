from functools import wraps
import importlib
import inflect
import re
p = inflect.engine()


def to_camel_case(name: str) -> str:
    # Remove special characters except underscores
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)

    # Split into words
    parts = name.split('_')

    # Convert plural → singular using inflect
    singular_parts = [
        p.singular_noun(word) if p.singular_noun(word) else word
        for word in parts
    ]
    # Join as PascalCase (CamelCase)
    class_name = ''.join(word.capitalize() for word in singular_parts)

    return class_name


def model_from_path(func):
    @wraps(func)
    def wrapper(table_name: str, *args, **kwargs):
        try:
            # Convert table_name to PascalCase singular class
            class_name = to_camel_case(table_name)

            # Import module dynamically
            module = importlib.import_module(f"src.models.{class_name}")

            # Get the class from module
            model_class = getattr(module, class_name)

        except ModuleNotFoundError:
            return {"error": f"Model file for '{table_name}' not found"}, 404
        except AttributeError:
            return {"error": f"Class '{class_name}' not found in model file"}, 404

        return func(model_class, *args, **kwargs)

    return wrapper
