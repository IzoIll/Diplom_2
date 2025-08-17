import pytest
import requests
import allure
import helpers.helpers
from urls.urls import *
from data.data import *

class TestRegistrationUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_registration_new_user(self):
        user_random_data = {"email": helpers.helpers.generate_random_email() + "@mail.com", "password": helpers.helpers.generate_random_password(), "name": helpers.helpers.generate_random_name()}
        with allure.step('Отправка запроса на регистрацию пользователя'):
            response = requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка наличия ошибки при создании пользователя который уже зарегистрирован')
    def test_registration_same_user(self):
        user_random_data = {"email": helpers.helpers.generate_random_email() + "@mail.com", "password": helpers.helpers.generate_random_password(), "name": helpers.helpers.generate_random_name()}
        with allure.step('Отправка запроса на регистрацию пользователя'):
            requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        with allure.step('Отправка запроса на регистрацию пользователя с уже используемыми данными'):
            response = requests.post(Urls.URL_USER_REGISTER, data=user_random_data)
        assert response.status_code == 403
        assert response.json()["message"] == Messages.MESSAGE_USER_ALREADY_EXISTS

    @allure.title('Проверка наличия ошибки создания пользователя у которого не указаны все обязательные поля')
    @pytest.mark.parametrize('empty_field', UserData.data_with_empty_field)
    def test_registration_user_without_any_field(self, empty_field):
        with allure.step('Отправка запроса на регистрацию пользователя без заполнения обязательного поля'):
            response = requests.post(Urls.URL_USER_REGISTER, data=empty_field)
        assert response.status_code == 403
        assert response.json()["message"] == Messages.MESSAGE_REQUIRED_FIELDS