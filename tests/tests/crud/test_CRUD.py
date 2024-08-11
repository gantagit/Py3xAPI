import logging

import allure
import pytest
import openpyxl

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils


class TestCRUD(object):

    @allure.title("TC#1 Update Booking")
    @allure.description("Test case to Update booking")
    @pytest.mark.crud
    def test_update_booking(self, create_token, get_booking_id):
        LOGGER = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        put_patch_delete_url = APIConstants().url_put_patch_delete(booking_id)
        response = put_requests(
            url=put_patch_delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token),
            payload=payload_update_booking(),
            in_json=False
        )
        response_data = response.json()
        first_name = response.json()["firstname"]
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_keys(key=first_name, expected_data="Vijay")
        LOGGER.info(response_data)
        # return booking_id

    @allure.title("TC#2 Partial Update Booking")
    @allure.description("Test case to Partial Update booking")
    @pytest.mark.crud
    def test_patch_booking(self, create_token, get_booking_id):
        LOGGER = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        put_patch_delete_url = APIConstants().url_put_patch_delete(booking_id)
        response = patch_requests(
            url=put_patch_delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token),
            payload=payload_patch_booking(),
            in_json=False
        )
        response_data = response.json()
        first_name = response.json()["firstname"]
        verify_http_status_code(response_data=response, expected_data=200)
        # verify_response_keys(key=first_name, expected_data="Vijay")
        verify_response_keys(key=first_name, expected_data="VJ")
        LOGGER.info(response_data)


    @allure.title("TC#3 Delete Update Booking")
    @allure.description("Test case to delete booking")
    @pytest.mark.crud
    def test_delete_booking(self, create_token, get_booking_id):
        LOGGER = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        put_patch_delete_url = APIConstants().url_put_patch_delete(booking_id)
        response = patch_requests(
            url = put_patch_delete_url,
            auth = None,
            headers=Utils().common_headers_put_patch_delete_cookie(token),
            payload=None,
            in_json=False
        )
        response_text = response.text
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_json_key_not_null(response_text)
        LOGGER.info(response_text)
