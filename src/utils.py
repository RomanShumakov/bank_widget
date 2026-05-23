import json
import os

script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data/operations.json'))

def json_reader(path_to_file=script_path):
    try:
        with open(path_to_file) as f:
            response = json.load(f)
        if type(response) != list:
            return []
        return response
    except FileNotFoundError:
        return []
