import allure
import requests


class OrderMethods:
    def __init__(self, url):
        self.url = url
    @allure.step('Отправка запроса на создание заказа (POST + JSON-data)')
    def order_methods(self, payload):
        response = requests.post(url=self.url, json=payload)
        return response

    @allure.step('Отправка запроса на получение списка заказов')
    def list_order(self):
        response = requests.get(url=self.url)
        return response