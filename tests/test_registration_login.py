import json

import pytest

from core.contracts import REGISTRATION_SCHEME
import httpx
import allure
from jsonschema import validate

BASE_URL = "https://reqres.in/api"
REGISTRATION_ENPOINT = "/register"
json_file = open("/Users/vialinafarmanova/PycharmProjects/API_Tests/core/users_data.json")
users_data = json.load(json_file)

@pytest.mark.parametrize("users_data", users_data)
def test_registration_user(users_data):
    headers = {'Content-Type': 'application/json'}
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + REGISTRATION_ENPOINT}'):
        response = httpx.post(BASE_URL + REGISTRATION_ENPOINT, json=users_data, headers=headers)