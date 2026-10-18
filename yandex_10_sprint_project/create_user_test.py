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

def test_create_user_and_kit():
    # Шаг 1: Создаем пользователя
    user_body = get_user_body("АннаТест")
    user_response = sender_stand_request.post_new_user(user_body)
    
    # Проверка статуса
    assert user_response.status_code == 201, f"Ожидался статус 201, но получен {user_response.status_code}"
    
    # Получаем токен
    user_json = user_response.json()
    assert "authToken" in user_json, "В ответе нет поля authToken"
    auth_token = user_json["authToken"]
    assert auth_token, "authToken пустой"

    # Шаг 2: Создаем набор для этого пользователя
    kit_body = get_kit_body("Тестовый набор")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    # Проверка статуса создания набора
    assert kit_response.status_code in [200, 201], f"Ожидался 200 или 201, но получен {kit_response.status_code}"
    
    # Можно добавить проверку, что набор действительно создался, если стенд это подтверждает
    kit_json = kit_response.json()
    assert kit_json.get("name") == "Тестовый набор", "Название набора не совпадает"