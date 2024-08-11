import requests


def get_requests(url, headers):
    get_request = requests.get(url=url, headers=headers)
    return get_request


def post_requests(url, auth, headers, payload, in_json):
    post_request = requests.post(url=url, auth=auth, headers=headers, json=payload)
    if in_json is True:
        return post_request.json()
    return post_request


def put_requests(url, auth, headers, payload, in_json):
    put_request = requests.put(url=url, auth=auth, headers=headers, json=payload)
    if in_json is True:
        return put_request.json()
    return put_request


def patch_requests(url, auth, headers, payload, in_json):
    patch_request = requests.patch(url=url, auth=auth, headers=headers, json=payload)
    if in_json is True:
        return patch_request.json()
    return patch_request


def delete_requests(url, auth, headers, payload, in_json):
    delete_request = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return delete_request.json()
    return delete_request
