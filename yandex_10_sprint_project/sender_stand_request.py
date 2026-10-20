import requests

def post_new_user(user_body):
    """Создает пользователя."""
    base_url = "https://7a7b25c2-e735-4d80-8dc0-73f13216a708.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/users"
    url = f"{base_url}{endpoint}"
    
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=user_body, headers=headers)
    return response


def post_new_client_kit(kit_body, auth_token):
    """Создает набор для пользователя."""
    base_url = "https://7a7b25c2-e735-4d80-8dc0-73f13216a708.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/kits"
    url = f"{base_url}{endpoint}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    
    response = requests.post(url, json=kit_body, headers=headers)
    return response