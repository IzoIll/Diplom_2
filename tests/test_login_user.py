import requests
import allure
from data.data import *

class TestUserLogin:

    @allure.title('Проверка логина существующего пользователя')
    def test_login_exist_user(self, user_register_random_data):
        user_random_data = {"email": user_register_random_data["email"], "password": user_register_random_data["password"]}
        response = requests.post(Urls.URL_USER_LOGIN, data=user_random_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка ошибки логина несуществующего пользователя')
    def test_login_not_exist_user(self, generate_random_email, generate_random_password):
        user_random_data = {"email": generate_random_email + 'wrong', "password": generate_random_password}
        response = requests.post(Urls.URL_USER_LOGIN, data=user_random_data)
        assert response.status_code == 401
        assert response.json()["message"] == Messages.MESSAGE_INCORRECT_CREDENTIALS