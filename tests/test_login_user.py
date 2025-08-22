import requests
import allure
import helpers.helpers
from urls.urls import *
from data.data import Messages

class TestUserLogin:

    @allure.title('Проверка логина существующего пользователя')
    def test_login_exist_user(self, user_register_random_data):
        user_random_data = {"email": user_register_random_data["email"], "password": user_register_random_data["password"]}
        with allure.step('Отправка запроса на логин пользователя'):
            response = requests.post(Urls.URL_USER_LOGIN, data=user_random_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка ошибки логина несуществующего пользователя')
    def test_login_not_exist_user(self):
        user_random_data = {"email": helpers.helpers.generate_random_email() + 'wrong', "password": helpers.helpers.generate_random_password() + 'wrong'}
        with allure.step('Отправка запроса на логин несуществующего пользователя'):
            response = requests.post(Urls.URL_USER_LOGIN, data=user_random_data)
        assert response.status_code == 401
        assert response.json()["message"] == Messages.MESSAGE_INCORRECT_CREDENTIALS