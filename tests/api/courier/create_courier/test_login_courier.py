import allure
import pytest
from data.data import AuthorizationCourier, URLS
from data.messages import MessagesCourier
from api_methods.courier_methods import CourierMethods

@allure.title('Тестирование авторизации курьера')
class TestLoginCourier:
    @allure.title('Позитивный тест на авторизацию')
    @allure.description('При передачи данных зарегистрированного курьера запрос отправляет ответ виде ID и с кодом 200')
    def test_courier_authorization_success(self):
        cm = CourierMethods(URLS.COURIER)
        response = cm.login_courier(AuthorizationCourier.JSON_COURIER)

        assert response.status_code == 200 and str(AuthorizationCourier.USER_ID) in response.text

    @allure.description('Проверка, что без полей нельзя авторизовать курьера и код ошибки должен быть 400')
    @pytest.mark.parametrize('input_value', ["login", "password"])
    def test_transfer_of_basic_data_for_authorization(self,auth_payload, input_value):
        allure.dynamic.title(f"Проверка, что без поля '{input_value}' нельзя авторизовать курьера")
        auth_payload[input_value] = ""

        cm = CourierMethods(URLS.COURIER)
        response = cm.login_courier(auth_payload)
        body = response.json()

        assert MessagesCourier.MISSING_INPUT == body['message'] and 400 == response.status_code

    @allure.title('Некорректные данные в пароле и логине или не существующия запись')
    @allure.description('Проверка что при некорректном пароле и логине будет ошибка 404 и Учетная запись не найдена')
    @pytest.mark.parametrize('input_value_lp', ["login", "password"])
    def test_not_correct_login_or_password(self, input_value_lp):
        data_courier = AuthorizationCourier.JSON_COURIER
        data_courier[input_value_lp] = 'test777'

        cm = CourierMethods(URLS.COURIER)
        response = cm.login_courier(data_courier)
        body = response.json()

        assert MessagesCourier.NOT_FOUND == body['message'] and 404 == response.status_code

