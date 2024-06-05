import pytest
import requests
import allure
from data import ORDER_URL

class TestOrders:

    @allure.story('Создание заказа с авторизацией')
    @allure.title("Проверка создания заказа с авторизацией")
    @allure.description("тест проверяет успешное создание заказа при наличии авторизации")
    def test_create_order_with_auth(self, headers, ingredients):
        order = {
            "ingredients": ingredients
        }
        response = requests.post(ORDER_URL, json=order, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") == True

    @allure.story('Создание заказа без авторизации')
    @allure.title("Проверка создания заказа без авторизации")
    @allure.description("тест проверяет, что создание заказа без авторизации возвращает ошибку 401")
    def test_create_order_without_auth(self, ingredients):
        order = {
            "ingredients": ingredients
        }
        response = requests.post(ORDER_URL, json=order)
        assert response.status_code == 401   # баг в документации - не авторизованный не может создать заказа, может.
        assert response.json().get("message") == "You should be authorised"

    @allure.story('Создание пустого заказа')
    @allure.title("Проверка создания пустого заказа")
    @allure.description("тест проверяет, что создание заказа без ингредиентов возвращает ошибку 400")
    def test_create_order_empty(self, headers):
        order = {
            "ingredients": []
        }
        response = requests.post(ORDER_URL, json=order, headers=headers)
        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"

    @allure.story('Создание заказа с невалидным ингредиентом')
    @allure.title("Проверка создания заказа с невалидным ингредиентом")
    @allure.description("тест проверяет, что создание заказа с невалидным ингредиентом возвращает ошибку 500")
    def test_create_order_invalid_ingredient(self, headers):
        order = {
            "ingredients": ["invalid_ingredient"]
        }
        response = requests.post(ORDER_URL, json=order, headers=headers)
        assert response.status_code == 500

    @allure.story('Получение всех заказов с авторизацией')
    @allure.title("Проверка получения всех заказов с авторизацией")
    @allure.description("тест проверяет успешное получение всех заказов при наличии авторизации")
    def test_get_orders_with_auth(self, headers):
        response = requests.get(f"{ORDER_URL}/all", headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") == True

    @allure.story('Получение всех заказов без авторизации')
    @allure.title("Проверка получения всех заказов без авторизации")
    @allure.description("тест проверяет успешное получение всех заказов без авторизации")
    def test_get_orders_without_auth(self):
        response = requests.get(f"{ORDER_URL}/all")
        assert response.status_code == 200
        assert response.json().get("success") == True
