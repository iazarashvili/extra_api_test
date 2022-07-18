import os
import json

from src.config.host_config import API_HOSTS_STAGING
from src.utilities.requests_methods import HttpMethods

env = os.environ.get('ENV', 'mercury_url')
base_url = API_HOSTS_STAGING[env]


class MercuryApi:

    @staticmethod
    def categories():
        endpoint = "/categories"
        request_method = HttpMethods.get(base_url, endpoint)
        return request_method

    @staticmethod
    def categories_id(category_id):
        endpoint = "/categories/" + str(category_id)
        request_method = HttpMethods.get(base_url, endpoint)
        return request_method

    @staticmethod
    def categories_id_cheri_cher(category_id):
        endpoint = f"/categories/{category_id}/cheri-cheri"
        request_method = HttpMethods.get(base_url, endpoint)
        return request_method

    @staticmethod
    def filters_beat_it(category_id, page_number, page_size, brand_ids=None, model_id=None,
                        sort_type=1, sort_by=1, ):
        endpoint = "/filters/beat-it"
        payload = json.dumps({
            "categoryId": category_id,  # int
            "pageNumber": page_number,  # int
            "pageSize": page_size,  # int
            "brandIds": brand_ids,  # list []
            "modelIds": model_id,  # list []
            "sortType": sort_type,  # int
            "sortBy": sort_by,  # int
            "features": {},
            "merchantSlugs": []
        })

        request_method = HttpMethods.post(base_url, endpoint, payload)
        return request_method

    @staticmethod
    # use products_gimme(first_id, second_id)
    def products_gimme(*args):
        endpoint = "/products/gimme"
        payload = json.dumps(
            args
        )
        request_method = HttpMethods.post(base_url, endpoint, payload)
        return request_method

    @staticmethod
    def products_id(product_id):
        endpoint = f"/products/{product_id}"
        request_method = HttpMethods.get(base_url, endpoint)
        return request_method

    @staticmethod
    def search_go_go(search_text):
        endpoint = "/search/go-go"

        payload = json.dumps({
            "searchText": search_text
        })
        request_method = HttpMethods.post(base_url, endpoint, payload)
        return request_method

    @staticmethod
    def billie_jean(category_id):
        payload = json.dumps({
            "brandIds": [],
            "categoryId": category_id,
            "modelIds": [],
            "features": {},
            "merchantSlugs": [],
            "sortType": 1,
            "sortBy": 1,
            "pageNumber": 1,
            "pageSize": 48,
            "filterByDiscount": False,
            "filterByGift": False,
            "filterByVisaDiscount": False,
            "filterByMastercard": False
        })

        headers = {
            'authority': 'mercury.staging.extra.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8,ka;q=0.7',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://staging.extra.ge',
            'referer': 'https://staging.extra.ge/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                          ' like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        endpoint = '/search/billie-jean'
        request_method = HttpMethods.post(base_url, endpoint, payload, headers)
        return request_method

    @staticmethod
    def search_coll_cat(search_text=None, user_slug=None, merchant_id=None):
        endpoint = "/search/cool-cat"

        payload = json.dumps({
            "searchText": search_text,  # string
            "userSlug": user_slug,  # string
            "merchantId": merchant_id   # int
        })

        request_method = HttpMethods.post(base_url, endpoint, payload)
        return request_method
