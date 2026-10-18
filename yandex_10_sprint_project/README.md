# Проект: Разработка автотестов 10 спринт

Автотесты для поля name в запросе на создание набора - приложение Яндекс. Прилавок

## 🚀 Как запустить проект

1.  **Склонируй репозиторий:**
    ```bash
    git clone https://github.com/KateBaydakova/yandex_10_sprint_project.git
    ```
2.  **Перейди в папку:**
    ```bash
    cd yandex_10_sprint_project
    ```
3.  **Создай виртуальное окружение (рекомендуется):**
    ```bash
    python -m venv venv
    # Активация (Windows):
    venv\Scripts\activate
    # Активация (Mac/Linux):
    source venv/bin/activate
    ```
4.  **Установи зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
    Файла requirements.txt нет. Зависимости устанавливаются согласно заданию спринта

## 🧪 Как запустить тесты

Для запуска тестов используй pytest:

```bash
pytest

## **Структура проекта**

- configuration.py - настройки и URL
- data.py - тестовые данные
- create_kit_name_kit_test.py - тесты для создания наборов
- create_user_test.py - тест для создания пользователя
- .gitignore - игнорируемые файлы
- .env - реальный токен проекта
- sender_stand_request.py - запросы на создание набора и формирование заголовков
- README.md - о проекте

## **Автор**

Екатерина Байдакова - 49 когорта