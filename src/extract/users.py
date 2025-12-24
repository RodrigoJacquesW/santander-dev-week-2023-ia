import requests

URL = "http://localhost:8080/users"

def get_users():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def get_user(user_id):
    response = requests.get(f"{URL}/{user_id}")
    response.raise_for_status()
    return response.json()
