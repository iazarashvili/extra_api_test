import json
import os

from dotenv import load_dotenv
from src.config.host_config import API_HOSTS_STAGING
from src.utilities.requests_methods import HttpMethods

load_dotenv()
env = os.environ.get('ENV', 'basket_url')
base_url = API_HOSTS_STAGING[env]


class ExtraBasketApi:

    @staticmethod
    def admin_basket(token, user_id):
        endpoint = "/v1/adminbasket?userId=" + user_id
        requests_method = HttpMethods.get(base_url, endpoint, headers=token)
        return requests_method

    @staticmethod
    def admin_basket_update_basket(token, user_id, product_id, product_count):
        payload = {
            "userId": user_id,
            "productId": product_id,
            "productCount": product_count
        }

        endpoint = "/v1/adminbasket/updatebasket?userId=" + user_id
        requests_method = HttpMethods.post(base_url, endpoint, body=payload, headers=token)
        return requests_method

    @staticmethod
    def admin_basket_remove_product(token, user_id, product_id):
        payload = {
            "userId": user_id,
            "productId": product_id
        }

        endpoint = "/v1/adminbasket/removeProduct?userId=" + user_id
        requests_method = HttpMethods.post(base_url, endpoint, body=payload, headers=token)
        return requests_method

    @staticmethod
    def admin_basket_empty_basket(token, user_id):
        endpoint = "/v1/adminbasket/emptybasket?userId=" + user_id
        requests_method = HttpMethods.post(base_url, endpoint, headers=token)
        return requests_method

    @staticmethod
    def check_basket_item(token):
        endpoint = "/v1/basket"
        requests_method = HttpMethods.get(base_url, endpoint, headers=token)
        return requests_method

    @staticmethod
    def update_basket(product_id, product_count, token):
        endpoint = "/v1/basket/updatebasket"
        payload = json.dumps({
            "productId": product_id,
            "discountType": 0,
            "productCount": product_count,
            "details": [],
            "type": "[BASKET] UpdateBasket"
        })
        requests_method = HttpMethods.post(base_url, endpoint, body=payload, headers=token)
        return requests_method

    @staticmethod
    def update_basket_multiple(token, item_id_1, item_id_2, first_count, second_count):
        endpoint = '/v1/basket/updatebasketmultiple'
        json_body = {
            "basketItems": [
                {
                    "productId": item_id_1,
                    "productCount": first_count,
                    "details": []
                },
                {
                    "productId": item_id_2,
                    "productCount": second_count,
                    "details": []
                }
            ]
        }
        requests_method = HttpMethods.post(base_url, endpoint, json_body, headers=token)
        return requests_method

    @staticmethod
    def empty_basket(token):
        endpoint = '/v1/basket/emptybasket'
        requests_method = HttpMethods.post(base_url, endpoint, headers=token)
        return requests_method

    @staticmethod
    def remove_product(product_id, token):
        endpoint = '/v1/basket/removeproduct'
        json_body = {
            "productId": product_id
        }
        requests_method = HttpMethods.post(base_url, endpoint, body=json_body, headers=token)
        return requests_method
