import allure
import pytest

from src.helpers.api_request_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.utils.utils import Utils
from src.helpers.common_verification import *


class TestApiRequest(object):

    @allure.title("TC#1 Create Booking")
    @allure.description("Test case to verify create booking")
    @pytest.mark.crud
    def test_create_booking(self):
        response = post_requests(
            url=APIConstants().url_create_booking(),
            headers=Utils().common_headers_json(),
            payload=payload_create_booking()
        )
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_keys(key=response.json()["booking"]["firstname"], expected_data="Sally")
        verify_response_json_key_not_null(booking_id)
        return booking_id

    @allure.title("TC#1 Create Token")
    @allure.description("Test case to verify create token")
    @pytest.mark.crud
    def test_create_token(self):
        response = post_requests(
            url=APIConstants().url_create_token(),
            headers=Utils().common_headers_json(),
            payload=payload_create_token()
        )
        token = response.json()["token"]
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_json_key_not_null(token)
        return token
