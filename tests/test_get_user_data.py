from core.contracts import LIST_RESOURSE_SCHEME, USER_DATA_SCHEME
import httpx
import allure
from jsonschema import validate

BASE_URL = "https://reqres.in"

LIST_USERS_ENDPOINT = "/api/users?page=2"

SINGLE_USER_ENDPOINT = "/api/users/2"

SINGLE_USER_NOT_FOUND_ENDPOINT = "/api/users/23"

EMAIL_ENDS = "@reqres.in"

LIST_RESOURCE_ENDPOINT = "/api/unknown"

SINGLE_SOURCE_NOT_FOUND_ENDPOINT = "/api/unknown/23"


@allure.suite('проверка запросов данных пользователей')
@allure.title('лист пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_USERS_ENDPOINT}'):
        response = httpx.get(BASE_URL + LIST_USERS_ENDPOINT)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()["data"]
    for item in data:
        with allure.step('Проверем элемент из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание Email адреса'):
                assert item['email'].endswith(EMAIL_ENDS)


def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER_ENDPOINT)
    assert response.status_code == 200
    user = response.json()["data"]
    validate(user, USER_DATA_SCHEME)
    email = user["email"]
    assert email.endswith('@reqres.in')


def test_single_user_not_found():
    response = httpx.get(BASE_URL + SINGLE_USER_NOT_FOUND_ENDPOINT)
    assert response.status_code == 404


def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE_ENDPOINT)
    assert response.status_code == 200
    data = response.json()["data"]
    for item in data:
        validate(item, LIST_RESOURSE_SCHEME)
        assert item["id"] >= 0


def test_single_source_not_found():
    response = httpx.get(BASE_URL + SINGLE_SOURCE_NOT_FOUND_ENDPOINT)
    assert response.status_code == 404
