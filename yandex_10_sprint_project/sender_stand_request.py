import requests
from data import HEADERS_TEMPLATE

def post_new_client_kit(kit_body, auth_token):
    
    base_url = "https://40b52ede-0fae-4a79-a246-4fe0d435cbca.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/kits"
    url = f"{base_url}{endpoint}"
    
    
    headers = HEADERS_TEMPLATE.copy()
    headers["Authorization"] = headers["Authorization"].format(token=auth_token)
    
    response = requests.post(url, json=kit_body, headers=headers)
    return response


def post_new_user(user_body):
    
    base_url = "https://40b52ede-0fae-4a79-a246-4fe0d435cbca.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/users"
    url = f"{base_url}{endpoint}"
    
    headers = {
        "Content-Type": "application/json"
    }
        
    response = requests.post(url, json=user_body, headers=headers)
    return response