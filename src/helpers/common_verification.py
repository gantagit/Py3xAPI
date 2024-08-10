def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data


def verify_response_keys(key, expected_data):
    assert key == expected_data


def verify_response_json_key_not_null(key):
    # assert key is not None
    # assert key != 0 AND key is not None
    assert key is not None and (key != 0 or key > 0)
