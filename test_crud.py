import requests
import json
from definitions import BASE_URL
from json_validator import validate_json_against_schema

with open("test_data.json") as json_file:
    test_data = json.load(json_file)


def test_create_resource():
    response = requests.post(
        url=f"{BASE_URL}/post",
        headers={"Content-Type": "application/json"},
        data=test_data,
    )
    response_json = response.json()
    # Assert that response status is 200 OK
    assert response.status_code == 200
    # Assert that response data value is present
    assert len(response_json["data"]) > 0
    # Check if returned data format conforms to JSON Schema
    validate_json_against_schema(response_json, "create_resource_schema.json")


def test_read_resource():
    response = requests.get(
        url=f"{BASE_URL}/get",
        headers={"Accept": "application/json"},
        params=json.dumps(test_data),
    )
    response_json = response.json()
    # Assert that response status is 200 OK
    assert response.status_code == 200
    # Assert that response args value is present
    assert len(response_json["args"]) > 0
    # Check if returned data format conforms to JSON Schema
    validate_json_against_schema(response_json, "read_resource_schema.json")
