import json
from requests import Response
from src.enums.global_enums import GlobalErrorMessages, GlobalSuccessMessages


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"{GlobalSuccessMessages.SUCCESSFUL_STATUS_CODE.value} = " + str(response.status_code))
        else:
            print(f"{GlobalErrorMessages.WRONG_STATUS_CODE.value} = " + str(response.status_code))

    @staticmethod
    def check_json_required_field(response: Response, expected_value):
        field = json.loads(response.text)
        assert list(field) == expected_value, GlobalErrorMessages.REQUIRED_FIELD_ERROR.value

    @staticmethod
    def check_json_value_equal(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, GlobalErrorMessages.WRONG_JSON_VALUE_EQUAL.value

    @staticmethod
    def check_json_value_not_equal(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info != expected_value, GlobalErrorMessages.WRONG_JSON_VALUE_NOT_EQUAL.value

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
        assert check_info == check_second_info, GlobalErrorMessages.WRONG_JSON_VALUE_EQUAL.value
