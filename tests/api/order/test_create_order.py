import allure
import pytest
from data import CreateOrderData
from api_methods.order_methods import OrderMethods

@allure.title('Тестирование создания заказа')
class TestLoginCourier:

    @allure.description('Создание заказа с цветом, с двумя цветами, без цвета. Получение статуса 201 и track поле')
    @pytest.mark.parametrize('input_value', [[],['BLACK', 'GREY'],['BLACK']])
    def test_create_order(self, base_url_order, input_value):
        allure.dynamic.title(f'Позитивный тест на создания заказа с {input_value}')
        data_order = CreateOrderData.JSON_ORDER["color"] = input_value

        om = OrderMethods(base_url_order)
        response = om.order_methods(data_order)

        assert response.status_code == 201 and "track" in response.text
