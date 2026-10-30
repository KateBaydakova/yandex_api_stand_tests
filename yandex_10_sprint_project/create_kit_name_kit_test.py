import pytest
from sender_stand_request import post_new_client_kit
from configuration import API_TOKEN
def positive_assert(name_value, response):
    
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
    
    name_to_test = "a"
    kit_body = {"name": name_to_test}
    
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)
    
    positive_assert(name_to_test, response)


# Тест 2 (позитивный): Допустимое количество символов (511)
def test_positive_assert_name_511_letters():
    
    long_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    positive_assert(long_name, response)
    
# Тест 3 (негативный): Количество символов меньше допустимого (0):

def test_negative_assert_code_400_empty_name():
    
    
    kit_body = {
        "name": ""
    }

    
    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["name", "empty", "required", "blank"]
    )
    

# Тест 4 (негативный): Количество символов больше допустимого (512):

def test_negative_assert_code_400_long_name():
    
    long_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

    
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}


    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["length", "max", "limit", "too long", "exceeded"]
    )


    

# Тест 5 (позитивный): Разрешены английские буквы:

def test_positive_assert_name_english_letters():
    

    name_to_test = "QWErty"
    kit_body = {"name": name_to_test}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    positive_assert(name_to_test, response)


    # Тест 6 (позитивный): Разрешены русские буквы:

def test_positive_assert_name_russian_letters():
    
    name_to_test = "Мария"
    kit_body = {"name": name_to_test}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    positive_assert(name_to_test, response)
    

# Тест 7 (позитивный): Разрешены спецсимволы:

def test_positive_assert_name_special_symbols():
    
    name_to_test = "№%@,"
    kit_body = {"name": name_to_test}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    positive_assert(name_to_test, response)
            


# Тест 8 (позитивный): Разрешены пробелы:

def test_positive_assert_name_blank_spaces():
    
    name_to_test = " Человек и КО "
    kit_body = {"name": name_to_test}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    positive_assert(name_to_test, response)
                             


# Тест 9 (позитивный): Разрешены цифры:

def test_positive_assert_name_numbers():
    
    name_to_test = "123"
    kit_body = {"name": name_to_test}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    positive_assert(name_to_test, response)
                             


# Тест 10 (негативный): Параметр не передан в запросе:

def test_negative_assert_code_400_empty_parameter():
    
    kit_body = {}

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["required", "missing", "name", "absent"]
    )
        

# Тест 11 (негативный): Передан другой тип параметра (число):

def test_negative_assert_code_400_another_parameter():
    
    kit_body = {
        "name": 123
    }

    response = post_new_client_kit(kit_body=kit_body, auth_token=API_TOKEN)

    negative_assert(
        response, 
        expected_status=400, 
        error_keywords=["type", "invalid", "string", "format", "must be"]
    )