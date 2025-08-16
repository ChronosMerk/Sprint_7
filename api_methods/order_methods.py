import allure
import requests


class OrderMethods:
    def __init__(self, url):
        self.url = url
    @allure.step('Отправка запроса на создание заказа (POST + JSON-data)')
    def order_methods(self, payload):
        response = requests.post(url=self.url, json=payload)
        return response