class URLS:
    BASE = "https://qa-scooter.praktikum-services.ru/api/v1"
    COURIER = f"{BASE}/courier"
    LOGIN = f"{COURIER}/login"
    ORDER = f"{BASE}/orders"

class AuthorizationCourier:
    JSON_COURIER = {
        "firstName": "test",
        "login": "test235",
        "password": "test1234"
    }
    USER_ID = '586694'

class CreateOrderData:
    JSON_ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}
