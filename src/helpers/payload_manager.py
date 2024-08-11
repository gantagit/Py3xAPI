def payload_create_booking():
    create_booking_payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return create_booking_payload


def payload_update_booking():
    update_booking_payload = {
        "firstname": "Vijay",
        "lastname": "Choc",
        "totalprice": 100,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-02-01",
            "checkout": "2019-02-01"
        },
        "additionalneeds": ["Breakfast", "Dinner"]
    }
    return update_booking_payload


def payload_patch_booking():
    partial_update_booking_payload = {
        "firstname": "VJ"
    }
    return partial_update_booking_payload


def payload_create_token():
    create_token_payload = {
        "username": "admin",
        "password": "password123"
    }
    return create_token_payload
