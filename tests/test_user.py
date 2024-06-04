import pytest
import requests
from data import USER_URL
from conftest import random_email, random_name

class TestUser:
    # Тест обновления данных пользователя с авторизацией
    def test_update_user_with_auth(self, headers):
        updated_user = {
            "email": random_email(),
            "name": random_name()
        }
        response = requests.patch(USER_URL, json=updated_user, headers=headers)
        assert response.status_code == 403 # не верный код ошибки
        assert response.json()["success"] == False

    # Тест обновления данных пользователя без авторизации
    def test_update_user_without_auth(self):
        updated_user = {
            "email": random_email(),
            "name": random_name()
        }
        response = requests.patch(USER_URL, json=updated_user)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
