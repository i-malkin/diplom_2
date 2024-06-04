import pytest
import requests
import random
import string
from data import REGISTER_URL, LOGIN_URL, AUTH_TOKEN, BASE_URL

# Фикстура для получения базового URL
@pytest.fixture(scope="session")
def base_url():
    return "https://stellarburgers.nomoreparties.site/api"

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

# Фикстура для использования зарегистрированного пользователя
@pytest.fixture(scope="function")
def existing_user():
    user = {
        "email": "test_kogorta_7@ya.ru",
        "password": "123456",
        "name": "test_kogorta_7"
    }
    return user

# Фикстура для получения заголовков с токеном аутентификации
@pytest.fixture(scope="function")
def headers():
    return {
        "Authorization": AUTH_TOKEN
    }

# Фикстура для получения списка ингредиентов
@pytest.fixture(scope="function")
def ingredients():
    response = requests.get(f"{BASE_URL}/ingredients")
    assert response.status_code == 200
    return [ingredient['_id'] for ingredient in response.json()['data']]
