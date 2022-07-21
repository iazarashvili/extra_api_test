
import json
from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully!!! Status code = " + str(response.status_code))
        else:
            print("Failure!!! Status code = " + str(response.status_code))


    @staticmethod
    def check_json_required_field(response: Response, expected_value):
        field = json.loads(response.text)
        assert list(field) == expected_value
        print("All fields are present")


    @staticmethod
    def check_json_value_equal(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " true !!!")

    @staticmethod
    def check_json_value_not_equal(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info != expected_value
        print(field_name + " true !!!")


    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " present !!!")
        else:
            print("Word " + search_word + " missing !!!")

    @staticmethod
    def check_json_value_equal_result(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        check_second_info = check.get(expected_value)
        assert check_info == check_second_info
        print(field_name + " true !!!")