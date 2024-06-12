# Base URL for the API
BASE_URL = "https://stellarburgers.nomoreparties.site/api"

# Endpoint URLs
REGISTER_URL = f"{BASE_URL}/auth/register"
LOGIN_URL = f"{BASE_URL}/auth/login"
USER_URL = f"{BASE_URL}/auth/user"
ORDER_URL = f"{BASE_URL}/orders"

#error responses
ANSWERS_1 = "You should be authorised"
ANSWERS_2 = "Ingredient ids must be provided"