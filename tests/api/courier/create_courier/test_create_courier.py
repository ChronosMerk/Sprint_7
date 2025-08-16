import allure
import helpers
import pytest
from api_methods.courier_methods import CourierMethods

@allure.title('Тестирование создание курьера 201 Created и Message: ok')
class TestCreateCourier:
    @allure.title('Создание курьера с уникальными данными ')
    @allure.description('Генерация данных курьера, отправка на регистрацию и проверка кода и успешность создания')
    def test_create_couriers(self, base_url_courier):
        final_result = '{"ok":true}'

        data = helpers.register_new_courier()
        cm = CourierMethods(base_url_courier)

        response = cm.create_courier(data)

        assert final_result == response.text and 201 == response.status_code

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('При обращение создании 2 курьера с одинаковыми данными выходит ошибка "Этот логин уже используется" и код ошибки 409')
    def test_create_two_identical_couriers_error(self, base_url_courier):
        final_result = 'Этот логин уже используется. Попробуйте другой.'
        data_courier = helpers.register_new_courier()

        cm = CourierMethods(base_url_courier)
        cm.create_courier(data_courier)
        response = cm.create_courier(data_courier)
        body = response.json()

        assert final_result == body['message'] and 409 == response.status_code

    @allure.description('Проверка 2 полей логин и пароль, без них будет ошибка 400 и сообщение Недостаточно данных')
    @pytest.mark.parametrize("input_value", ["login", "password"])
    def test_missing_required_field_returns_error(self, base_url_courier, input_value):
        allure.dynamic.title(f"Проверка, что без поля '{input_value}' нельзя зарегистрировать курьера")

        final_result = 'Недостаточно данных для создания учетной записи'

        data_courier = helpers.register_new_courier()
        data_courier[input_value] = ""

        cm = CourierMethods(base_url_courier)
        response = cm.create_courier(data_courier)
        body = response.json()

        assert final_result == body['message'] and 400 == response.status_code