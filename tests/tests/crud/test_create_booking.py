import logging

import allure
import pytest
import openpyxl

from src.helpers.api_request_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.utils.utils import Utils
from src.helpers.common_verification import *


class TestApiRequest(object):

    @allure.title("TC#1 Create Booking")
    @allure.description("Test case to verify create booking")
    @pytest.mark.positive
    def test_create_booking(self):
        LOGGER = logging.getLogger(__name__)
        response = post_requests(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_keys(key=response.json()["booking"]["firstname"], expected_data="Sally")
        verify_response_json_key_not_null(booking_id)
        LOGGER.info(booking_id)
        # return booking_id

    @allure.title("TC#1 Create Booking with no payload")
    @allure.description("Test case to verify create booking with no payload")
    @pytest.mark.negative
    def test_create_booking_no_payload(self):
        LOGGER = logging.getLogger(__name__)
        response = post_requests(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)
        # return booking_id

