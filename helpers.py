import random
import string
import requests
from auth import get_tokens
from data import REGISTER_URL


# Функция для генерации случайного email
def random_email():
    return f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}@example.com"

# Функция для генерации случайного имени пользователя
def random_name():
    return ''.join(random.choices(string.ascii_letters, k=10))

def ensure_user_exists(user):
    try:
        get_tokens(user["email"], user["password"])
    except requests.exceptions.HTTPError:
        response = requests.post(REGISTER_URL, json=user)
        assert response.status_code == 200, f"Failed to register user: {response.status_code} {response.text}"

