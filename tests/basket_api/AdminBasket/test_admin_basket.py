import os

from requests import Response
from src.helpers.basket_helpers import ExtraBasketApi
from src.utilities.checking_response import Checking

user_id = os.getenv('USERID')


def test_admin_basket(get_admin_token):
    result_get: Response = ExtraBasketApi.admin_basket(get_admin_token, user_id)
    Checking.check_status_code(result_get, 200)

