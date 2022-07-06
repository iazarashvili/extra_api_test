
import pytest
from requests import Response
from src.helpers.basket_helpers import ExtraBasketApi
from src.helpers.mercury_helpers import MercuryApi
from src.utilities.checking_response import Checking
from src.helpers.identity_helper import ExtraIdentityApi


class TestExtraBasket:

    @pytest.fixture()
    def get_token(self):
        result_post: Response = ExtraIdentityApi.connect_token()
        Checking.check_status_code(result_post, 200)
        check_json = result_post.json()
        token = check_json.get('access_token')
        access_token = {'Authorization': 'Bearer ' + token}
        return access_token

    def test_check_basket_item(self, get_token):
        result_post_billie: Response = MercuryApi.billie_jean()
        Checking.check_status_code(result_post_billie, 200)
        result_get: Response = ExtraBasketApi.check_basket_item(get_token)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['data', 'totalPrice', 'quantityFailed'])

    def test_cms_access_tocken(self):
        print('CMS Api')
        result_post_cms: Response = ExtraIdentityApi.cms_connect_roken()
        Checking.check_status_code(result_post_cms, 200)
        check_json = result_post_cms.json()
        cms_token = check_json.get('access_token')
        print(cms_token)
