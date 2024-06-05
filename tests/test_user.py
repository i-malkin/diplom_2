import pytest
import requests
import allure
from data import USER_URL
from conftest import random_email, random_name

class TestUser:

    @allure.story('Обновление данных пользователя с авторизацией')
    @allure.title("Проверка обновления данных пользователя с авторизацией")
    @allure.description("тест проверяет успешное обновление данных пользователя при наличии авторизации")
    def test_update_user_with_auth(self, headers):
        updated_user = {
            "email": random_email(),
            "name": random_name()
        }
        response = requests.patch(USER_URL, json=updated_user, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.story('Обновление данных пользователя без авторизации')
    @allure.title("Проверка обновления данных пользователя без авторизации")
    @allure.description("тест проверяет, что обновление данных пользователя без авторизации возвращает ошибку 401")
    def test_update_user_without_auth(self):
        updated_user = {
            "email": random_email(),
            "name": random_name()
        }
        response = requests.patch(USER_URL, json=updated_user)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
