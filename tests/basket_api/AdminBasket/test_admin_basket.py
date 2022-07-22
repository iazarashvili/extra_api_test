import json
import os

from jsonschema import validate
from src.schemas.basket_schema import ProductDetail

from src.utilities.response import Response

from requests import Response
from src.helpers.basket_helpers import ExtraBasketApi
from src.utilities.checking_response import Checking


user_id = os.getenv('USERID')


def test_admin_basket(get_admin_token):
    result_get: Response = ExtraBasketApi.admin_basket(get_admin_token, user_id)
    Checking.check_status_code(result_get, 200)
    print(result_get.json())
    name = ProductDetail.parse_obj(result_get.json())
    print(name.totalPrice)




