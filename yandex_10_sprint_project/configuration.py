URL_SERVICE = "https://40b52ede-0fae-4a79-a246-4fe0d435cbca.serverhub.praktikum-services.ru"

CREATE_USER_PATH = "/api/v1/users/"
#API_TOKEN = "authToken: 'jknnFApafP4awfAIFfafam2fma'"
PRODUCTS_KITS_PATH = "/api/v1/products/kits/"
CREATE_PRODUCT_KITS = "/api/v1/kits"
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")