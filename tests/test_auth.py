import pytest
import requests
import allure
from data import REGISTER_URL, LOGIN_URL

class TestAuth:

    @allure.story('Регистрация существующего пользователя')
    @allure.title("Проверка регистрации существующего пользователя")
    @allure.description("тест проверяет, что при попытке зарегистрировать существующего пользователя возвращается ошибка 403")
    def test_register_existing_user(self, existing_user):
        login_response = requests.post(LOGIN_URL, json=existing_user)
        assert login_response.status_code == 200, f"User does not exist or login failed with status code: {login_response.status_code}"

    @allure.story('Авторизация существующего пользователя')
    @allure.title("Проверка авторизации существующего пользователя")
    @allure.description("тест проверяет успешную авторизацию существующего пользователя")
    def test_login_existing_user(self, existing_user):
        response = requests.post(LOGIN_URL, json=existing_user)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response body: {response.text}"
        data = response.json()
        assert "accessToken" in data
        assert "refreshToken" in data
