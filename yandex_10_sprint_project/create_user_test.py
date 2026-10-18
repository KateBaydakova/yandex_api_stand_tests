# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

# ВАЖНО: Весь код, который делает запросы, должен быть ВНУТРИ этой функции
def test_create_user_and_kit():
    # Шаг 1: Создаем пользователя
    user_body = get_user_body("АннаТест123")
    user_response = sender_stand_request.post_new_user(user_body)
    
    assert user_response.status_code == 201
    user_json = user_response.json()
    assert "authToken" in user_json
    auth_token = user_json["authToken"]
    
    # Шаг 2: Создаем набор
    kit_body = get_kit_body("Тестовый набор")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    assert kit_response.status_code in [200, 201]
    print("Тест прошел успешно!")