
import os
from dotenv import load_dotenv
from src.config.host_config import API_HOSTS_STAGING
from src.utilities.requests_methods import HttpMethods


load_dotenv()
env = os.environ.get('ENV', 'identity_url')
base_url = API_HOSTS_STAGING[env]
endpoint = "/connect/token"
password = os.getenv("EXTRAPASSWORD")
email = os.getenv('EXTRAMAIL')
email_cms = os.getenv('CMSEMAIL')
password_cms = os.getenv('CMSPASSWORD')

class ExtraIdentityApi:

    @staticmethod
    def connect_token():
        payload = 'grant_type=password&scope=identity%20offline_access%20openid%20email%20profile' \
                  '%20phone%20address&username=' + email + '&password=' + password + '&client_id=dev&client_secret=secret'

        headers = {
            'authority': 'identity.staging.extra.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8,ka;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://staging.extra.ge',
            'referer': 'https://staging.extra.ge/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }


        requests_method = HttpMethods.post(base_url, endpoint, payload, headers)
        return requests_method


    @staticmethod
    def cms_connect_roken():
        payload = 'grant_type=password&scope=identity%20offline_access%20openid%20email%20profile%20p' \
                  'hone%20address&username=' + email_cms + '&' \
                                                       'password=' + password_cms + '&client_id=dev&client_secret=secret'

        headers = {
            'Origin': 'https://admin.staging.extra.ge',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        request_method = HttpMethods.post(base_url, endpoint, payload, headers)
        return request_method
