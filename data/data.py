import random
import string

class Messages:
    MESSAGE_USER_UNAUTHORIZED = "You should be authorised"
    MESSAGE_USER_ALREADY_EXISTS = "User already exists"
    MESSAGE_INCORRECT_CREDENTIALS = "email or password are incorrect"
    MESSAGE_REQUIRED_FIELDS = "Email, password and name are required fields"
    MESSAGE_NO_INGREDIENTS = "Ingredient ids must be provided"

class Ingredients:
    correct_ingredients = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]
    no_correct_ingredients = ["61c0c5a71d1f82001vkvkyu4", "w4875gbwoi8whgwe7gw7os7e"]
    null_ingredient = []

class UserData:
    data_with_empty_field = [
        {'email': '',
         'password': ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
         'name': ''.join(random.choice(string.ascii_lowercase) for i in range(10))},

        {'email': ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
         'password': '',
         'name': ''.join(random.choice(string.ascii_lowercase) for i in range(10))},

        {'email': ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
         'password': ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
         'name': ''}]