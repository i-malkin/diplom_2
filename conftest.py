import pytest
import requests
import random
import string
from data import BASE_URL, REGISTER_URL, LOGIN_URL
from auth import get_auth_headers, get_tokens #добавил


# Фикстура для получения базового URL
@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# Функция для генерации случайного email
def random_email():
    return f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}@example.com"

# Функция для генерации случайного имени пользователя
def random_name():
    return ''.join(random.choices(string.ascii_letters, k=10))

# Фикстура для создания уникального пользователя
@pytest.fixture(scope="function")
def unique_user():
    user = {
        "email": random_email(),
        "password": "password",
        "name": random_name()
    }
    return user

def ensure_user_exists(user):
    try:
        get_tokens(user["email"], user["password"])
    except requests.exceptions.HTTPError:
        response = requests.post(REGISTER_URL, json=user)
        assert response.status_code == 200, f"Failed to register user: {response.status_code} {response.text}"

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
    try:
        return get_auth_headers(existing_user["email"], existing_user["password"])
    except requests.exceptions.HTTPError as e:
        print(f"Error obtaining auth headers: {e}")
        raise

# Фикстура для получения списка ингредиентов
@pytest.fixture(scope="function")
def ingredients():
    response = requests.get(f"{BASE_URL}/ingredients")
    assert response.status_code == 200
    return [ingredient['_id'] for ingredient in response.json()['data']]
