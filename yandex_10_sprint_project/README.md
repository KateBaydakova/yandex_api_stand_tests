# Проект: разработка автотестов 10 спринт

Автотесты для поля name в запросе на создание набора - приложение Яндекс. Прилавок

# Как запустить проект

1.  **Склонируй репозиторий:**
    ```
    git clone https://github.com/KateBaydakova/yandex_10_sprint_project.git
    ```
2.  **Перейди в папку:**
    ```
    cd yandex_10_sprint_project
    ```
3.  **Создай виртуальное окружение:**
    ```
    python -m venv venv
    # Активация (Windows):
    venv\Scripts\activate
    # Активация (Mac/Linux):
    source venv/bin/activate
    ```

# Как запустить тесты

Для запуска тестов используй pytest:

```
pytest

# Структура проекта

- configuration.py - настройки и URL
- data.py - тестовые данные
- create_kit_name_kit_test.py - тесты для создания наборов
- create_user_test.py - тест для создания пользователя
- .gitignore - игнорируемые файлы
- .env - реальный токен проекта
- sender_stand_request.py - запросы на создание набора и формирование заголовков
- README.md - о проекте

# Автор

Екатерина Байдакова - 49 когорта