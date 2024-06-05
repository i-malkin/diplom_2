import requests
from data import LOGIN_URL

def get_tokens(email, password):
    response = requests.post(LOGIN_URL, json={"email": email, "password": password})
    if response.status_code != 200:
        print(f"Failed to get tokens: {response.status_code} {response.text}")
    response.raise_for_status()
    data = response.json()
    return data["accessToken"], data["refreshToken"]

def get_auth_headers(email, password):
    access_token, _ = get_tokens(email, password)
    return {
        "Authorization": access_token
    }
