import requests

def post_new_client_kit(kit_body, auth_token):
    
    base_url = "https://084b5ea6-f033-4027-a83f-121c16983fdb.serverhub.praktikum-services.ru"
    endpoint = "/api/v1/kits"             
    url = f"{base_url}{endpoint}"

    # 2. Формируем заголовки (обязательно с Authorization)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }

    # 3. Отправляем запрос
    # json=kit_body автоматически превратит словарь в JSON и поставит правильный заголовок
    response = requests.post(url, json=kit_body, headers=headers)

    # 4. Возвращаем ответ, чтобы тест мог его проверить
    return response