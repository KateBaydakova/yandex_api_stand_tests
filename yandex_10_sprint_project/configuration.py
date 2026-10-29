URL_SERVICE = "https://500b63cb-770c-4a6c-af8c-48522a8d0914.serverhub.praktikum-services.ru"

# DOC_PATH содержит путь к документации веб-сервиса.
# Этот путь используется для формирования полного URL пути к документации, добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://api.example.com/docs/"

# CREATE_USER_PATH хранит путь к API-методу для создания нового пользователя.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание пользователя.
CREATE_USER_PATH = "/api/v1/users/"
#API_TOKEN = "authToken: 'jknnFApafP4awfAIFfafam2fma'"
PRODUCTS_KITS_PATH = "/api/v1/products/kits/"
CREATE_PRODUCT_KITS = "/api/v1/kits"
import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Берем токен из переменной окружения
API_TOKEN = os.getenv("API_TOKEN")