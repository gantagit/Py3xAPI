# this file is for storing api constants


class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_token(self):
        return self.base_url() + "/auth"

    def url_create_booking(self):
        return self.base_url() + "/booking"

    def url_put_patch_delete(self, booking_id):
        return self.url_create_booking() + str(booking_id)
