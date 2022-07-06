from requests import Response
from src.utilities.checking_response import Checking
from src.helpers.identity_helper import ExtraIdentityApi

class Token:


    @staticmethod
    def get_token():
        result_post: Response = ExtraIdentityApi.connect_token()
        Checking.check_status_code(result_post, 200)
        check_json = result_post.json()
        token = check_json.get('access_token')
        access_token = {'Authorization': 'Bearer ' + token}
        return access_token