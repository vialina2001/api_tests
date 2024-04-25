from core.contracts import CREATED_USER_SCHEME, USER_UPDATE_SCHEME
import httpx
import allure
from jsonschema import validate

BASE_URL = "https://reqres.in/api/users/2"


def test_create_user():
    body = {"name": "morpheus",
            "job": "leader"}
    response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    assert response.status_code == 201
    validate(response.json(), CREATED_USER_SCHEME)
    assert body["name"] == response_json["name"]


def test_create_user1():
    body = {"name": "morpheus",
            "job": "leader"}
    response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    assert response.status_code == 201
    validate(response.json(), CREATED_USER_SCHEME)
    assert body["job"] == response_json["job"]


def test_update_user():
    body = {"name": "morpheus",
            "job": "zion resident"}
    response = httpx.put(BASE_URL, json=body)
    response_json = response.json()
    assert response.status_code == 200
    validate(response.json(), USER_UPDATE_SCHEME)
    assert body["job"] == response_json["job"]
    print(response_json)


def test_update_user1():
    body = {"name": "morpheus",
            "job": "zion resident"}
    response = httpx.patch(BASE_URL, json=body)
    response_json = response.json()
    assert response.status_code == 200
    validate(response.json(), USER_UPDATE_SCHEME)
    assert body["job"] == response_json["job"]
    print(response_json)

def test_delete_user():
    response = httpx.delete(BASE_URL)
    assert response.status_code == 204