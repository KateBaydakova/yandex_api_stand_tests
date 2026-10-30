HEADERS_TEMPLATE = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {token}"
} 
user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}
products_ids = {
    "ids": [1, 2, 3]
}

kit_body = {
       "name": "Мой набор",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": None,
       "id": 7,
       "productsCount": 0
   }

