import json
import os

from jsonschema import validate


def __load_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


def validate_json_against_schema(json_data, json_schema):
    validate(json_data, __load_json(os.path.join("json_schemas", json_schema)))
