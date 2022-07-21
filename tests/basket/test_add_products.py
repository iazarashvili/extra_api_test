import json

from pprint import pprint
from requests import Response

from src.helpers.basket_helpers import ExtraBasketApi
from src.helpers.mercury_helpers import MercuryApi
from src.utilities.checking_response import Checking


def test_add_product_to_cart(get_token):
    """Add Product in Basket And Check it"""

    result_post_empty: Response = ExtraBasketApi.empty_basket(get_token)
    Checking.check_status_code(result_post_empty, 200)
    Checking.check_json_required_field(result_post_empty, ['data', 'totalPrice', 'quantityFailed'])

    result_post_set: Response = MercuryApi.search_billie_jean_set_items(499)
    Checking.check_status_code(result_post_set, 200)
    Checking.check_json_required_field(result_post_set, ['data', 'totalCount'])

    product_id = result_post_set.json()['data'][0]

    post_result_update: Response = ExtraBasketApi.update_basket(product_id, 1, token=get_token)
    Checking.check_status_code(post_result_update, 200)
    Checking.check_json_required_field(post_result_update, ['data', 'totalPrice', 'quantityFailed'])
    Checking.check_json_value_not_equal(post_result_update, 'totalPrice', 0)
    Checking.check_json_value_equal(post_result_update, 'quantityFailed', False)

    pprint(post_result_update.json(), indent=1)

    check = post_result_update.json()


    print(check)
