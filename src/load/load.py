import requests

API_URL = "http://localhost:8080/users"

def update_user(user):
    response = requests.put(
        f"{API_URL}/{user['id']}",
        json=user
    )
    return response.status_code == 200
