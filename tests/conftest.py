import pytest
import random
import string
import requests
from data.data import Urls

@pytest.fixture()
def generate_random_email():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

@pytest.fixture()
def generate_random_password():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

@pytest.fixture()
def generate_random_name():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

@pytest.fixture()
def user_random_data(generate_random_email, generate_random_password, generate_random_name):
    random_data = [
        {"email": generate_random_email + "@mail.com", "password": generate_random_password},
        {"email": generate_random_email + "@mail.com", "name": generate_random_name},
        {"password": generate_random_password, "name": generate_random_name}]
    return random_data

@pytest.fixture()
def user_register_random_data(generate_random_email, generate_random_password, generate_random_name):
    random_data = {"email": generate_random_email + "@mail.com", "password": generate_random_password, "name": generate_random_name}
    requests.post(Urls.URL_USER_REGISTER, data=random_data)
    return random_data

@pytest.fixture()
def user_token(generate_random_email, generate_random_password, generate_random_name):
    random_data = {"email": generate_random_email + "@mail.com", "password": generate_random_password, "name": generate_random_name}
    repost = requests.post(Urls.URL_USER_REGISTER, data=random_data)
    return {**random_data, "accessToken": repost.json()["accessToken"], "refreshToken": repost.json()["refreshToken"],}