
import requests

from src.utilities.logger import Logger


class HttpMethods:
    cookie = ""

    @staticmethod
    def get(base_url, endpoint, body=None, headers=None):
        url = base_url + endpoint
        Logger.add_request(url, method="GET")
        response = requests.get(url=url, json=body, headers=headers, cookies=HttpMethods.cookie)
        Logger.add_response(response)
        return response

    @staticmethod
    def post(base_url, endpoint, payload=None, headers=None, body=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = base_url + endpoint
        Logger.add_request(url, method="POST")
        response = requests.post(url=url, json=body, data=payload, headers=headers)
        Logger.add_response(response)
        return response

    @staticmethod
    def put(url, body, headers=None):
        Logger.add_request(url, method="PUT")
        response = requests.put(url, json=body, headers=headers, cookies=HttpMethods.cookie)
        Logger.add_response(response)
        return response

    @staticmethod
    def delete(url, body, headers=None):
        Logger.add_request(url, method="delete")
        response = requests.delete(url, json=body, headers=headers, cookies=HttpMethods.cookie)
        Logger.add_response(response)
        return response
