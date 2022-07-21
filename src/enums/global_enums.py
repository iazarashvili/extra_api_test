from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    REQUIRED_FIELD_ERROR = "Not all fields are represented"
    WRONG_JSON_VALUE_EQUAL = "The value is not equal to expected value"
    WRONG_JSON_VALUE_NOT_EQUAL = "The value equal to expected value"

class GlobalSuccessMessages(Enum):
    SUCCESSFUL_STATUS_CODE = "The received status code is valid"
