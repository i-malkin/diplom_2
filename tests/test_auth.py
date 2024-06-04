import pytest
import requests
from data import REGISTER_URL, LOGIN_URL

class TestAuth:
    # Тест регистрации уникального пользователя
    def test_register_unique_user(self, unique_user):
        response = requests.post(REGISTER_URL, json=unique_user)
        assert response.status_code == 200
        assert response.json()["success"] == True

    # Тест регистрации уже существующего пользователя
    def test_register_existing_user(self, existing_user):
        response = requests.post(REGISTER_URL, json=existing_user)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    # Тест регистрации пользователя с пропущенным обязательным полем
    def test_register_missing_field(self):
        user = {
            "email": "missing_field@example.com",
            "password": "password"
        }
        response = requests.post(REGISTER_URL, json=user)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

    # Тест авторизации пользователя с правильными данными
    def test_login_valid_user(self, existing_user):
        response = requests.post(LOGIN_URL, json=existing_user)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.json()}"
        assert response.json()["success"] == True

    # Тест авторизации пользователя с неверными данными
    def test_login_invalid_credentials(self):
        user = {
            "email": "non_existing_user@example.com",
            "password": "wrong_password"
        }
        response = requests.post(LOGIN_URL, json=user)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
