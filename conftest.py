import logging

# import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils


@pytest.fixture(scope="session")
def create_token():
    # LOGGER = logging.getLogger(__name__)
    response = post_requests(
        url=APIConstants().url_create_token(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )
    token = response.json()["token"]
    # LOGGER.info(token)
    return token


@pytest.fixture(scope="session")
def get_booking_id():
    # LOGGER = logging.getLogger(__name__)
    response = post_requests(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    # LOGGER.info(booking_id)
    return booking_id
