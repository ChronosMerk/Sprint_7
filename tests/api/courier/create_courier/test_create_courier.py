import allure
import helpers
import pytest
from api_methods.courier_methods import CourierMethods
from data.messages import MessagesOrder
from data.data import URLS

@allure.title('Тестирование создание курьера 201 Created и Message: ok')
class TestCreateCourier:
    @allure.title('Создание курьера с уникальными данными ')
    @allure.description('Генерация данных курьера, отправка на регистрацию и проверка кода и успешность создания')
    def test_create_couriers(self):
        data = helpers.register_new_courier()
        cm = CourierMethods(URLS.BASE)

        response = cm.create_courier(data)

        assert MessagesOrder.OK_RESPONSE == response.text and 201 == response.status_code

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('При обращение создании 2 курьера с одинаковыми данными выходит ошибка "Этот логин уже используется" и код ошибки 409')
    def test_create_two_identical_couriers_error(self):
        data_courier = helpers.register_new_courier()

        cm = CourierMethods(URLS.BASE)
        cm.create_courier(data_courier)
        response = cm.create_courier(data_courier)
        body = response.json()

        assert MessagesOrder.DUPLICATE_LOGIN == body['message'] and 409 == response.status_code

    @allure.description('Проверка 2 полей логин и пароль, без них будет ошибка 400 и сообщение Недостаточно данных')
    @pytest.mark.parametrize("input_value", ["login", "password"])
    def test_missing_required_field_returns_error(self, input_value):
        allure.dynamic.title(f"Проверка, что без поля '{input_value}' нельзя зарегистрировать курьера")
        data_courier = helpers.register_new_courier()
        data_courier[input_value] = ""

        cm = CourierMethods(URLS.BASE)
        response = cm.create_courier(data_courier)
        body = response.json()

        assert MessagesOrder.MISSING_INPUT == body['message'] and 400 == response.status_code