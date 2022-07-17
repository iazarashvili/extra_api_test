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
    def billie_jean():
        payload = json.dumps({
            "categorySlug": "",
            "setIds": [
                "499"
            ],
            "pageNumber": 1,
            "pageSize": 20,
            "sortBy": 4,
            "sortType": 1
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
