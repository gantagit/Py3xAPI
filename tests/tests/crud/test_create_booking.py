import allure
import pytest


class TestApiRequest(object):

    @allure.title("TC#1 Create Booking")
    @allure.description("Test case to verify create booking")
    @pytest.mark.crud
    def test_create_booking(self):
        pass
