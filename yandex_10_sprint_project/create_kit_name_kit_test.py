import pytest
# Импортируем нашу функцию и токен
from sender_stand_request import post_new_client_kit
from configuration import API_TOKEN  # Убедись, что в .env лежит реальный токен, если хочешь тест "вживую"

def test_create_kit_success():
    """Тест: создаем набор и проверяем, что сервер вернул 201 Created"""
    
    # 1. Подготовка данных (тело запроса)
    # Эти данные должны соответствовать требованиям API из задания
    test_kit_body = {
        "name": "Test Kit for Automation",
        "description": "Created by pytest",
        "user_id": 12345  # Пример ID пользователя
    }

    # 2. Вызов функции
    # Передаем тело запроса и токен
    response = post_new_client_kit(kit_body=test_kit_body, auth_token=API_TOKEN)

    # 3. Проверка результатов (Assert)
    # Тестировщик проверяет:
    # - Статус код 201 (ресурс создан) или 200 (успех)
    # - Что в ответе есть ID созданного набора
    
    assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ: {response.text}"
    
    response_data = response.json()
    assert "id" in response_data, "В ответе сервера не найден ID созданного набора"
    
    print(f"✅ Набор успешно создан! ID: {response_data['id']}")

   # Тест 1 (позитивный): Допустимое количество символов (1)

def test_positive_assert_name_one_letter():
    """
    Позитивный тест: имя состоит из 1 символа ('a').
    Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
    """
    # 1. Подготовка данных (то, что ты просила)
    kit_body = {
        "name": "a"
    }

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка 1: Статус код должен быть 201
    assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
    response_data = response.json()
    
    # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
    # Проверь документацию API, какое именно поле возвращает сервер.
    # Допустим, сервер возвращает {"id": 123, "name": "a"}
    
    assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
    assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"

    print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

    # Тест 2 (позитивный): Допустимое количество символов (511)

    def test_positive_assert_name_511_letters():
    """
    Позитивный тест: имя состоит из 511 символов ('Ab').
    Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
    """
    # 1. Подготовка данных (то, что ты просила)
    kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка 1: Статус код должен быть 201
    assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
    response_data = response.json()
    
    # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
    # Проверь документацию API, какое именно поле возвращает сервер.
    # Допустим, сервер возвращает {"id": 123, "name": "a"}
    
    assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
    assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"

    print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

    # Тест 3 (негативный): Количество символов меньше допустимого (0):

def test_negative_assert_code_400_empty_name():
    """
    Негативный тест: имя пустое (0 символов).
    Ожидаемый результат: статус 400, сервер отвергает запрос.
    """
    # 1. Подготовка данных: ПУСТОЕ имя
    kit_body = {
        "name": ""
    }

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: статус код должен быть 400
    assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. (Опционально, но очень полезно) Проверка сообщения об ошибке
    # Хороший API всегда возвращает понятное сообщение в теле ошибки.
    # Попробуем его достать и проверить, что там есть слово "name" или "empty".
    try:
        error_data = response.json()
        # Проверяем, что сервер явно говорит про имя (зависит от реализации API)
        # Например: {"error": "Name cannot be empty"} или {"name": ["This field is required"]}
        # Если сервер возвращает просто текст, а не JSON, этот блок упадет в except.
        
        # Раскомментируй строки ниже, если знаешь точную структуру ошибки твоего API:
        # assert "name" in error_data or "empty" in str(error_data), "Ошибка не содержит информации про поле name"
        
        print(f"✅ Сервер корректно отверг пустой запрос. Ответ: {error_data}")
    except ValueError:
        # Если сервер вернул не JSON (например, HTML страницу ошибки), 
        # мы всё равно считаем тест успешным, если статус 400.
        print("✅ Сервер вернул статус 400. Тело ответа не является JSON (возможно, HTML).")

    print("Тест негативного сценария пройден.")

    # Тест 4 (негативный): Количество символов больше допустимого (512):

def test_negative_assert_code_400_long_name():
    """
    Негативный тест: имя слишком длинное (512 символов).
    Ожидаемый результат: статус 400, сервер отвергает запрос.
    """
    # 1. Подготовка данных: ДЛИННОЕ имя
    kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: статус код должен быть 400
    assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. (Опционально, но очень полезно) Проверка сообщения об ошибке
    # Хороший API всегда возвращает понятное сообщение в теле ошибки.
    # Попробуем его достать и проверить, что там есть слово "name" или "empty".
    try:
        error_data = response.json()
        # Проверяем, что сервер явно говорит про имя (зависит от реализации API)
        # Например: {"error": "Name cannot be empty"} или {"name": ["This field is required"]}
        # Если сервер возвращает просто текст, а не JSON, этот блок упадет в except.
        
        # Раскомментируй строки ниже, если знаешь точную структуру ошибки твоего API:
        # assert "name" in error_data or "empty" in str(error_data), "Ошибка не содержит информации про поле name"
        
        print(f"✅ Сервер корректно отверг пустой запрос. Ответ: {error_data}")
    except ValueError:
        # Если сервер вернул не JSON (например, HTML страницу ошибки), 
        # мы всё равно считаем тест успешным, если статус 400.
        print("✅ Сервер вернул статус 400. Тело ответа не является JSON (возможно, HTML).")

    print("Тест негативного сценария пройден.")

    # Тест 5 (позитивный): Разрешены английские буквы:

    def test_positive_assert_name_english_letters():
    """
    Позитивный тест: имя состоит из английских символов ('QWErty').
    Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
    """
    # 1. Подготовка данных (то, что ты просила)
    kit_body = {
"name": "QWErty"
}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка 1: Статус код должен быть 201
    assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
    response_data = response.json()
    
    # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
    # Проверь документацию API, какое именно поле возвращает сервер.
    # Допустим, сервер возвращает {"id": 123, "name": "QWErty"}
    
    assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
    assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"

    print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

    # Тест 6 (позитивный): Разрешены русские буквы:

    def test_positive_assert_name_russian_letters():
        """
        Позитивный тест: имя состоит из русских символов ('Мария').
        Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
        """
        # 1. Подготовка данных (то, что ты просила)
        kit_body = {
"name": "Мария"
}
    
        # 2. Действие: вызываем функцию
        response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
    
        # 3. Проверка 1: Статус код должен быть 201
        assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"
    
        # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
        response_data = response.json()
        
        # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
        # Проверь документацию API, какое именно поле возвращает сервер.
        # Допустим, сервер возвращает {"id": 123, "name": "Мaрия"}
        
        assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
        assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"
    
        print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

        # Тест 7 (позитивный): Разрешены спецсимволы:

        def test_positive_assert_name_special_symbols():
                """
                Позитивный тест: имя состоит из спецсимволов ('"№%@",').
                Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
                """
                # 1. Подготовка данных (то, что ты просила)
                kit_body = {
"name": ""№%@","
}
            
                # 2. Действие: вызываем функцию
                response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
            
                # 3. Проверка 1: Статус код должен быть 201
                assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"
            
                # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
                response_data = response.json()
                
                # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
                # Проверь документацию API, какое именно поле возвращает сервер.
                # Допустим, сервер возвращает {"id": 123, "name": ""№%@","}
                
                assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
                assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"
            
                print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

                 # Тест 8 (позитивный): Разрешены пробелы:

                 def test_positive_assert_name_blank_spaces():
                  """
                                 Позитивный тест: имя состоит из спецсимволов ('Человек и КО').
                                 Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
                                 """
                                 # 1. Подготовка данных (то, что ты просила)
                                 kit_body = {
"name": " Человек и КО "
}
                             
                                 # 2. Действие: вызываем функцию
                                 response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
                             
                                 # 3. Проверка 1: Статус код должен быть 201
                                 assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"
                             
                                 # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
                                 response_data = response.json()
                                 
                                 # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
                                 # Проверь документацию API, какое именно поле возвращает сервер.
                                 # Допустим, сервер возвращает {"id": 123, "name": ""№%@","}
                                 
                                 assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
                                 assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"
                             
                                 print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

                  # Тест 9 (позитивный): Разрешены цифры:

def test_positive_assert_name_numbers():
                  """
                                 Позитивный тест: имя состоит из спецсимволов ('123').
                                 Ожидаемый результат: статус 201, имя в ответе совпадает с именем в запросе.
                                 """
                                 # 1. Подготовка данных (то, что ты просила)
                                 kit_body = {
"name": "123"
}
}
                             
                                 # 2. Действие: вызываем функцию
                                 response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
                             
                                 # 3. Проверка 1: Статус код должен быть 201
                                 assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"
                             
                                 # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
                                 response_data = response.json()
                                 
                                 # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
                                 # Проверь документацию API, какое именно поле возвращает сервер.
                                 # Допустим, сервер возвращает {"id": 123, "name": "123"}
                                 
                                 assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
                                 assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"
                             
                                 print(f"✅ Тест пройден! Создан набор с именем: {response_data['name']}")

# Тест 10 (негативный): Параметр не передан в запросе:

def test_negative_assert_code_400_empty_parameter():
    """
    Негативный тест: имя пустое (_ символов).
    Ожидаемый результат: статус 400, сервер отвергает запрос.
    """
    # 1. Подготовка данных: ПУСТОЕ имя
    kit_body = {
}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: статус код должен быть 400
    assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. (Опционально, но очень полезно) Проверка сообщения об ошибке
    # Хороший API всегда возвращает понятное сообщение в теле ошибки.
    # Попробуем его достать и проверить, что там есть слово "name" или "empty".
    try:
        error_data = response.json()
        # Проверяем, что сервер явно говорит про имя (зависит от реализации API)
        # Например: {"error": "Name cannot be empty"} или {"name": ["This field is required"]}
        # Если сервер возвращает просто текст, а не JSON, этот блок упадет в except.
        
        # Раскомментируй строки ниже, если знаешь точную структуру ошибки твоего API:
        # assert "name" in error_data or "empty" in str(error_data), "Ошибка не содержит информации про поле name"
        
        print(f"✅ Сервер корректно отверг пустой запрос. Ответ: {error_data}")
    except ValueError:
        # Если сервер вернул не JSON (например, HTML страницу ошибки), 
        # мы всё равно считаем тест успешным, если статус 400.
        print("✅ Сервер вернул статус 400. Тело ответа не является JSON (возможно, HTML).")

    print("Тест негативного сценария пройден.")

    # Тест 11 (негативный): Передан другой тип параметра (число):

def test_negative_assert_code_400_another_parameter():
    """
    Негативный тест: имя пустое (число "123").
    Ожидаемый результат: статус 400, сервер отвергает запрос.
    """
    # 1. Подготовка данных: ПУСТОЕ имя
    kit_body = {
"name": 123
}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: статус код должен быть 400
    assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}. Ответ сервера: {response.text}"

    # 4. (Опционально, но очень полезно) Проверка сообщения об ошибке
    # Хороший API всегда возвращает понятное сообщение в теле ошибки.
    # Попробуем его достать и проверить, что там есть слово "name" или "empty".
    try:
        error_data = response.json()
        # Проверяем, что сервер явно говорит про имя (зависит от реализации API)
        # Например: {"error": "Name cannot be empty"} или {"name": ["This field is required"]}
        # Если сервер возвращает просто текст, а не JSON, этот блок упадет в except.
        
        # Раскомментируй строки ниже, если знаешь точную структуру ошибки твоего API:
        # assert "name" in error_data or "empty" in str(error_data), "Ошибка не содержит информации про поле name"
        
        print(f"✅ Сервер корректно отверг пустой запрос. Ответ: {error_data}")
    except ValueError:
        # Если сервер вернул не JSON (например, HTML страницу ошибки), 
        # мы всё равно считаем тест успешным, если статус 400.
        print("✅ Сервер вернул статус 400. Тело ответа не является JSON (возможно, HTML).")

    print("Тест негативного сценария пройден.")
