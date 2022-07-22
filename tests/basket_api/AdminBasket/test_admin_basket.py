import json
import os

from src.enums.global_enums import StatusCode
from src.schemas.basket_schema import ProductDetail
from src.utilities.response import Response
from requests import Response
from src.helpers.basket_helpers import ExtraBasketApi
from src.utilities.checking_response import Checking

user_id = os.getenv('USERID')


def test_empty_admin_basket(get_admin_token):
    """Check empty admin basket"""
    result_get: Response = ExtraBasketApi.admin_basket(get_admin_token, user_id)
    Checking.check_status_code(result_get, StatusCode.OK.value)
    Checking.check_json_required_field(result_get, ['data', 'totalPrice', 'quantityFailed'])
    ProductDetail.parse_obj((result_get.json()))


def test_admin_basket_one_item(get_admin_token):
    """Check admin basket one item"""
    result_get: Response = ExtraBasketApi.admin_basket(get_admin_token, user_id)
    Checking.check_status_code(result_get, StatusCode.OK.value)
    ProductDetail.parse_obj(result_get.json())
    Checking.check_json_required_field(result_get, ['data', 'totalPrice', 'quantityFailed'])


def test_admin_basket_remove_product(get_admin_token):
    """Remove item from admin basket"""
    result_get: Response = ExtraBasketApi.admin_basket(get_admin_token, user_id)
    product_id = result_get.json()['data'][0]['productId']
    result_post: Response = ExtraBasketApi.admin_basket_remove_product(get_admin_token, user_id, product_id)
    ProductDetail.parse_obj(result_post.json())
