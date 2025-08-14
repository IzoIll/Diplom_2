import requests
import allure
from data.data import *

class TestRegistrationUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_registration_new_user(self, generate_random_email, generate_random_password, generate_random_name):
        user_random_data = {"email": generate_random_email + "@mail.com", "password": generate_random_password, "name": generate_random_name}
        response = requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка наличия ошибки при создании пользователя который уже зарегистрирован')
    def test_registration_same_user(self, generate_random_email, generate_random_password, generate_random_name):
        user_random_data = {"email": generate_random_email + "@mail.com", "password": generate_random_password, "name": generate_random_name}
        requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        response = requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        assert response.status_code == 403
        assert response.json()["message"] == Messages.MESSAGE_USER_ALREADY_EXISTS

    @allure.title('Проверка наличия ошибки создания пользователя у которого не указаны все обязательные поля')
    def test_registration_user_without_any_field(self, user_random_data):
        response = requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        assert response.status_code == 403
        assert response.json()["message"] == Messages.MESSAGE_REQUIRED_FIELDS