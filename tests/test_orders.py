import pytest
import requests
from data import ORDER_URL

class TestOrders:

    def test_create_order_with_auth(self, headers, ingredients):
        order = {
            "ingredients": ingredients
        }
        response = requests.post(ORDER_URL, json=order, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") == True

    def test_create_order_without_auth(self, ingredients):
        order = {
            "ingredients": ingredients
        }
        response = requests.post(ORDER_URL, json=order)
        assert response.status_code == 401 # баг в требованиях, сказано что не авторизованный не может создать заказ
        assert response.json().get("message") == "You should be authorised"

    def test_create_order_empty(self, headers):
        order = {
            "ingredients": []
        }
        response = requests.post(ORDER_URL, json=order, headers=headers)
        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"

    def test_create_order_invalid_ingredient(self, headers):
        order = {
            "ingredients": ["invalid_ingredient"]
        }
        response = requests.post(ORDER_URL, json=order, headers=headers)
        assert response.status_code == 500

    def test_get_orders_with_auth(self, headers):
        response = requests.get(f"{ORDER_URL}/all", headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") == True

    def test_get_orders_without_auth(self):
        response = requests.get(f"{ORDER_URL}/all")
        # Ожидается успешный ответ, так как авторизация не требуется
        assert response.status_code == 200
        assert response.json().get("success") == True
