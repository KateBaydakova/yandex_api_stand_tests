import requests
from data import HEADERS_TEMPLATE

def post_new_client_kit(kit_body, auth_token):
    """Создает набор для пользователя (требует авторизации)."""
    base_url = "https://500b63cb-770c-4a6c-af8c-48522a8d0914.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/kits"
    url = f"{base_url}{endpoint}"
    
    # Берем шаблон и подставляем токен
    headers = HEADERS_TEMPLATE.copy()
    headers["Authorization"] = headers["Authorization"].format(token=auth_token)
    
    response = requests.post(url, json=kit_body, headers=headers)
    return response


def post_new_user(user_body):
    """Создает нового пользователя (регистрация, токен НЕ нужен)."""
    base_url = "https://500b63cb-770c-4a6c-af8c-48522a8d0914.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/users"
    url = f"{base_url}{endpoint}"
    
    headers = {
        "Content-Type": "application/json"
    }
        
    response = requests.post(url, json=user_body, headers=headers)
    return response