from requests import request

from .api_map import _API_MAP

from .exceptions import BadRequest, ResourceNotFound


class Api:
    def __init__(self):
        self.base_endpoint = _API_MAP['current']['api_root']

    def request(self, url, api_key, method, **kwargs):
        """
        Request structure
        """
        complete_url = '{}{}'.format(self.base_endpoint, url)
        header = {'TRN-Api-Key': api_key}
        response = request(method=method, url=complete_url, headers=header)
        return self.handle_response(response)

    def handle_response(self, response):
        """
        Evaluate response status code
        """
        status_code = response.status_code
        if 200 <= status_code <= 299:
            return response
        elif status_code == 400:
            raise BadRequest
        elif status_code == 404:
            raise ResourceNotFound
