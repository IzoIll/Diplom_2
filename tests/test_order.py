import requests
import allure
from urls.urls import *
from data.data import *

class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией и с ингредиентами')
    def test_create_order_with_authorization(self, user_token):
        with allure.step('Отправка запроса на создание заказа'):
            response = requests.post(Urls.URL_ORDERS, data={"ingredients": Ingredients.correct_ingredients}, headers={"Authorization": user_token['accessToken']})
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_authorization(self, user_token):
        with allure.step('Отправка запроса на создание заказа без авторизации'):
            response = requests.post(Urls.URL_ORDERS, data={"ingredients": Ingredients.correct_ingredients}, headers={})
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания заказа с авторизацией без ингредиентов')
    def test_cant_create_order_without_ingredients(self, user_token):
        with allure.step('Отправка запроса на создание заказа'):
            response = requests.post(Urls.URL_ORDERS, data={"ingredients": Ingredients.null_ingredient}, headers={"Authorization": user_token['accessToken']})
        assert response.status_code == 400
        assert response.json()["message"] == Messages.MESSAGE_NO_INGREDIENTS

    @allure.title('Проверка создания заказа с неверными ингредиентами')
    def test_cant_create_order_without_ingredients(self, user_token):
        payload = {"ingredients": Ingredients.no_correct_ingredients}
        with allure.step('Отправка запроса на создание заказа с неверными ингредиентами'):
            response = requests.post(Urls.URL_ORDERS, data=payload, headers={"Authorization": user_token['accessToken']})
        assert response.status_code == 500