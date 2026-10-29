import pytest
# Импортируем нашу функцию и токен
from sender_stand_request import post_new_client_kit
from configuration import API_TOKEN


# Тест 1 (позитивный): Допустимое количество символов (1)

def test_positive_assert_name_one_letter():
    """
    Позитивный тест: имя состоит из 1 символа ('a').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
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


    # Тест 2 (позитивный): Допустимое количество символов (511)

def test_positive_assert_name_511_letters():
    """
    Позитивный тест: имя состоит из 511 символов ('Ab').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
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
        assert error_data is not None
       
    except ValueError:
        
        pass

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
        assert error_data.get("error") and "length" in error_data["error"]
    except ValueError:
        

        pass

    # Тест 5 (позитивный): Разрешены английские буквы:

def test_positive_assert_name_english_letters():
    """
    Позитивный тест: имя состоит из английских символов ('QWErty').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
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


    # Тест 6 (позитивный): Разрешены русские буквы:

def test_positive_assert_name_russian_letters():
    """
    Позитивный тест: имя состоит из русских символов ('Мария').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
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
    

        # Тест 7 (позитивный): Разрешены спецсимволы:

def test_positive_assert_name_special_symbols():
    """
    Позитивный тест: имя состоит из спецсимволов ('"№%@",').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    kit_body = {
        "name": "№%@,"
}
    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
    # 3. Проверка 1: Статус код должен быть 201
    assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Ответ сервера: {response.text}"
    # 4. Проверка 2: Парсим JSON из ответа и сверяем имя
    response_data = response.json()
                
    # Если сервер возвращает имя в поле 'name' (часто бывает 'name' или 'kit_name')
    # Проверь документацию API, какое именно поле возвращает сервер.
    # Допустим, сервер возвращает {"id": 123, "name": "№%@,"}
                
    assert "name" in response_data, "В ответе сервера отсутствует поле 'name'"
    assert response_data["name"] == kit_body["name"], f"Имя в ответе ({response_data['name']}) не совпадает с именем в запросе ({kit_body['name']})"
            


                 # Тест 8 (позитивный): Разрешены пробелы:

def test_positive_assert_name_blank_spaces():
    """
    Позитивный тест: в имени есть пробелы ('Человек и КО').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
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
                             


                  # Тест 9 (позитивный): Разрешены цифры:

def test_positive_assert_name_numbers():
    """
    Позитивный тест: имя состоит из цифр ('123').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    kit_body = {
        "name": "123"
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
                             


# Тест 10 (негативный): Параметр не передан в запросе:

def test_negative_assert_code_400_empty_parameter():
    """
    Негативный тест: параметр не передан в запросе (_ символов).
    Ожидаемый результат: статус 400, сервер отвергает запрос.
    """
    # 1. Подготовка данных: параметр не передан в запросе
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
        assert "name" in str(error_data) or "required" in str(error_data) or "missing" in str(error_data), \
            f"Сервер вернул статус 400, но в ответе нет понятного сообщения об ошибке. Получено: {error_data}"
        
    except ValueError:
        assert len(response.text) > 10
        

    # Тест 11 (негативный): Передан другой тип параметра (число):

def test_negative_assert_code_400_another_parameter():
    """
    Негативный тест: другой тип параметра (число "123").
    Ожидаемый результат: статус 400, сервер отвергает запрос.
    """
    # 1. Подготовка данных: другой тип параметра - число
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
        assert "name" in str(error_data) and ("type" in str(error_data) or "invalid" in str(error_data) or "string" in str(error_data)), \
            f"Сервер вернул статус 400, но в сообщении об ошибке нет понятных указаний на проблему с полем name. Получено: {error_data}
        
    except ValueError:
        assert len(response.text) > 10
