class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    URL_USER_REGISTER = MAIN_URL + 'api/auth/register'
    URL_USER_LOGIN = MAIN_URL + 'api/auth/login'
    URL_USER_LOGOUT = MAIN_URL + 'api/auth/logout'
    URL_USER_GET_DATA = MAIN_URL + 'api/auth/user'
    URL_USER_DELETE = MAIN_URL + 'api/auth/user'
    URL_ORDERS = MAIN_URL + 'api/orders'

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