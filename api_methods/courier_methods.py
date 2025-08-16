import requests
import allure

class CourierMethods:
    def __init__(self, url):
        self.url = url

    @allure.step('Запрос создания курьера (POST + JSON-data)')
    def create_courier(self, payload):
        response = requests.post(url=self.url, json=payload)
        return response

    @allure.step('Авторизация курьера (POST + JSON-data)')
    def login_courier(self, payload):
        response = requests.post(url=self.url, json=payload)
        return response