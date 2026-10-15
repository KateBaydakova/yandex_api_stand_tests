import requests

def post_new_client_kit(kit_body, auth_token):
    """
    Отправляет POST-запрос на создание нового набора.
    
    :param kit_body: Словарь с данными для создания набора (тело запроса).
    :param auth_token: Строка с токеном авторизации (без префикса 'Bearer').
    :return: Объект ответа от сервера (response).
    """
    # 1. Формируем URL (забери его из configuration.py или пропиши здесь для теста)
    # Лучше вынести URL в configuration.py, но для примера оставим так:
    base_url = "https://your-api-url.com"  # <-- Вставь сюда реальный URL из задания
    endpoint = "/api/kits"               # <-- Путь к эндпоинту создания набора (узнай в документации)
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