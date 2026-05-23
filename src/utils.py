import json
import os

def json_reader(path_to_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data/operations.json'))):
    try:
        with open(path_to_file, encoding='utf-8') as f:
            response = json.load(f)
        if type(response) != list:
            return []
        return response
    except FileNotFoundError:
        return []
