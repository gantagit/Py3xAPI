import requests


def get_requests(url, headers):
    get_request = requests.get(url=url, headers=headers)
    return get_request


def post_requests(url, headers, payload):
    post_request = requests.post(url=url, headers=headers, json=payload)
    return post_request


def put_requests(url, auth, headers, payload):
    put_request = requests.put(url=url, auth=auth, headers=headers, json=payload)
    return put_request


def patch_requests(url, auth, headers, payload):
    patch_request = requests.patch(url=url, auth=auth, headers=headers, json=payload)
    return patch_request


def delete_requests(self, url, auth, headers):
    delete_request = requests.delete(url=url, auth=auth, headers=headers)
    return delete_request
