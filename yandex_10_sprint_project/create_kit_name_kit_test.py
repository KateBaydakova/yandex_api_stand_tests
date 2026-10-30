import pytest
from sender_stand_request import post_new_client_kit
from configuration import API_TOKEN
def positive_assert(name_value, response):
    """
    Помощник для позитивных тестов.
    Проверяет статус 201 и совпадение имени.
    """
    assert response.status_code == 201, (
        f"Ожидался статус 201, но получен {response.status_code}. "
        f"Ответ сервера: {response.text}"
    )
    
    data = response.json()
    
    assert "name" in data, "В ответе сервера отсутствует поле 'name'"
    assert data["name"] == name_value, (
        f"Имя в ответе ({data['name']}) не совпадает с именем в запросе ({name_value})"
    )


def negative_assert(response, expected_status=400, error_keywords=None):
    """
    Помощник для негативных тестов.
    Проверяет статус и наличие ключевых слов в ошибке.
    """
    assert response.status_code == expected_status, (
        f"Ожидался статус {expected_status}, но получен {response.status_code}. "
        f"Ответ сервера: {response.text}"
    )

    if error_keywords:
        try:
            error_data = response.json()
            error_string = str(error_data)
        except ValueError:
            error_string = response.text
        
        found = any(keyword in error_string for keyword in error_keywords)
        assert found, (
            f"Сервер вернул статус {expected_status}, но в сообщении об ошибке "
            f"не найдено ни одного из ключевых слов: {error_keywords}. "
            f"Получено: {error_string}"
        )

# Тест 1 (позитивный): Допустимое количество символов (1)
def test_positive_assert_name_one_letter():
    """
    Позитивный тест: имя состоит из 1 символа ('a').
    """
    name_to_test = "a"
    kit_body = {"name": name_to_test}
    
    # Действие: вызываем функцию отправки запроса
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
    
    # ОДНА СТРОКА ПРОВЕРКИ! (используем наш помощник)
    positive_assert(name_to_test, response)


# Тест 2 (позитивный): Допустимое количество символов (511)
def test_positive_assert_name_511_letters():
    """
    Позитивный тест: имя состоит из 511 символов.
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    # ВСТАВЬ СЮДА СВОЮ СТРОКУ ИЗ 511 СИМВОЛОВ ВМЕСТО ЗАГЛУШКИ
    long_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    positive_assert(long_name, response)
    
# Тест 3 (негативный): Количество символов меньше допустимого (0):

def test_negative_assert_code_400_empty_name():
    """
    Негативный тест: имя пустое (0 символов).
    Ожидаемый результат: статус 400 + сообщение об ошибке, указывающее на проблему с именем.
    """
    # 1. Подготовка данных: ПУСТОЕ имя
    kit_body = {
        "name": ""
    }

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    # Мы передаем ключевые слова, которые должны быть в тексте ошибки.
    # Если сервер скажет "Name is required" или "Field name cannot be empty", тест пройдет.
    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["name", "empty", "required", "blank"]
    )
    

# Тест 4 (негативный): Количество символов больше допустимого (512):

def test_negative_assert_code_400_long_name():
    """
    Негативный тест: имя слишком длинное (512 символов).
    Ожидаемый результат: статус 400 + сообщение об ошибке, указывающее на превышение длины.
    """
    # 1. Подготовка данных: ДЛИННОЕ имя
    # ВСТАВЬ СЮДА СВОЮ СТРОКУ ИЗ 512 СИМВОЛОВ ВМЕСТО ЗАГЛУШКИ
    long_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

    
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}


    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    # Ключевые слова подобраны специально для ошибки "слишком длинное":
    # "length" (длина), "max" (максимум), "limit" (лимит), "too long", "exceeded"
    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["length", "max", "limit", "too long", "exceeded"]
    )


    

# Тест 5 (позитивный): Разрешены английские буквы:

def test_positive_assert_name_english_letters():
    """
    Позитивный тест: имя состоит из английских символов ('QWErty').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    name_to_test = "QWErty"
    kit_body = {"name": name_to_test}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    positive_assert(name_to_test, response)


    # Тест 6 (позитивный): Разрешены русские буквы:

def test_positive_assert_name_russian_letters():
    """
    Позитивный тест: имя состоит из русских символов ('Мария').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    name_to_test = "Мария"
    kit_body = {"name": name_to_test}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    positive_assert(name_to_test, response)
    

# Тест 7 (позитивный): Разрешены спецсимволы:

def test_positive_assert_name_special_symbols():
    """
    Позитивный тест: имя состоит из спецсимволов ('№%@,').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    name_to_test = "№%@,"
    kit_body = {"name": name_to_test}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    positive_assert(name_to_test, response)
            


# Тест 8 (позитивный): Разрешены пробелы:

def test_positive_assert_name_blank_spaces():
    """
    Позитивный тест: в имени есть пробелы (' Человек и КО ').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    # Обрати внимание: пробелы в начале и в конце строки сохранены специально,
    # так как тест проверяет, что сервер их принимает.
    name_to_test = " Человек и КО "
    kit_body = {"name": name_to_test}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    positive_assert(name_to_test, response)
                             


# Тест 9 (позитивный): Разрешены цифры:

def test_positive_assert_name_numbers():
    """
    Позитивный тест: имя состоит из цифр ('123').
    Ожидаемый результат: статус 201, name в ответе совпадает с name в запросе.
    """
    # 1. Подготовка данных
    # Важно: цифры передаем как строку "123", а не как число 123,
    # так как поле name в JSON должно быть строкой.
    name_to_test = "123"
    kit_body = {"name": name_to_test}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    positive_assert(name_to_test, response)
                             


# Тест 10 (негативный): Параметр не передан в запросе:

def test_negative_assert_code_400_empty_parameter():
    """
    Негативный тест: тело запроса пустое (параметр name отсутствует).
    Ожидаемый результат: статус 400 + сообщение об ошибке, указывающее на отсутствие поля.
    """
    # 1. Подготовка данных: ПУСТОЙ словарь (поле name вообще не передано)
    kit_body = {}

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    # Ключевые слова подобраны специально для случая "поле не передано":
    # "required" (обязательно), "missing" (отсутствует), "name" (имя поля)
    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["required", "missing", "name", "absent"]
    )
        

# Тест 11 (негативный): Передан другой тип параметра (число):

def test_negative_assert_code_400_another_parameter():
    """
    Негативный тест: в поле name передано число (123) вместо строки.
    Ожидаемый результат: статус 400 + сообщение об ошибке валидации типа данных.
    """
    # 1. Подготовка данных: передаем число вместо строки
    # Важно: именно 123 (без кавычек), чтобы спровоцировать ошибку типа
    kit_body = {
        "name": 123
    }

    # 2. Действие: вызываем функцию
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    # 3. Проверка: ОДНА СТРОКА через наш помощник!
    # Ключевые слова подобраны специально для ошибки "неверный тип":
    # "type" (тип), "invalid" (некорректно), "string" (должна быть строка), "format"
    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["type", "invalid", "string", "format", "must be"]
    )