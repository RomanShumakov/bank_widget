import json
import os
from json import JSONDecodeError


def json_reader(
    path_to_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/operations.json"))
) -> list:
    """Функция чтения json-файлов"""
    try:
        with open(path_to_file, encoding="utf-8") as f:
            response = json.load(f)
        if not isinstance(response, list):
            return []
        return response
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
