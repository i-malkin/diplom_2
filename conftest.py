import pytest
import requests
from data import BASE_URL, REGISTER_URL, LOGIN_URL
from auth import get_auth_headers, get_tokens
from helpers import random_email, random_name, ensure_user_exists

# Фикстура для создания уникального пользователя
@pytest.fixture(scope="function")
def unique_user():
    user = {
        "email": random_email(),
        "password": "password",
        "name": random_name()
    }
    return user


# Фикстура для использования зарегистрированного пользователя
@pytest.fixture(scope="function")
def existing_user():
    user = {
        "email": "malkin_kogorta_7@ya.ru",
        "password": "123456",
        "name": "malkin_kogorta_7"
    }
    ensure_user_exists(user)
    return user

# Фикстура для получения заголовков с токеном аутентификации
@pytest.fixture(scope="function")
def headers(existing_user):
    return get_auth_headers(existing_user["email"], existing_user["password"])


# Фикстура для получения списка ингредиентов
@pytest.fixture(scope="function")
def ingredients():
    response = requests.get(f"{BASE_URL}/ingredients")
    assert response.status_code == 200
    return [ingredient['_id'] for ingredient in response.json()['data']]
