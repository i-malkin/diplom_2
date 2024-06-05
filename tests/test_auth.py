import pytest
import requests
from data import REGISTER_URL, LOGIN_URL

class TestAuth:

    def test_register_existing_user(self, existing_user):
        # Проверка, что пользователь уже существует
        login_response = requests.post(LOGIN_URL, json=existing_user)
        if login_response.status_code == 200:
            # Пользователь существует, можно продолжать тест
            response = requests.post(REGISTER_URL, json=existing_user)
            assert response.status_code == 403, f"Expected 403, got {response.status_code}. Response body: {response.text}"
        else:
            pytest.fail(f"User does not exist or login failed with status code: {login_response.status_code}")

    def test_login_existing_user(self, existing_user):
        response = requests.post(LOGIN_URL, json=existing_user)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response body: {response.text}"
        data = response.json()
        assert "accessToken" in data
        assert "refreshToken" in data
