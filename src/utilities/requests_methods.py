
import requests


class HttpMethods:
    cookie = ""

    @staticmethod
    def get(base_url, endpoint, body=None, headers=None):
        url = base_url + endpoint
        response = requests.get(url=url, json=body, headers=headers, cookies=HttpMethods.cookie)
        return response

    @staticmethod
    def post(base_url, endpoint, payload=None, headers=None, body=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = base_url + endpoint
        response = requests.post(url=url, json=body, data=payload, headers=headers)
        return response

    @staticmethod
    def put(url, body, headers=None):
        response = requests.put(url, json=body, headers=headers, cookies=HttpMethods.cookie)
        return response

    @staticmethod
    def delete(url, body, headers=None):
        response = requests.delete(url, json=body, headers=headers, cookies=HttpMethods.cookie)
        return response
