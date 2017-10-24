import pytest

from bf1.api import Api
from bf1.exceptions import BadRequest, ResourceNotFound

from .utils import API_KEY, METHOD


def test_api_request():
    api = Api()
    api_url = 'Stats/CareerForOwnedGames?platform=3&displayName=Girbons'
    response = api.request(api_url, API_KEY, METHOD)
    assert len(response.json()) == 4


def test_api_request_forbidden():
    api = Api()
    api_url = 'Stats/CareerForOwnedGames?platform=3&displayName=Girbons'
    with pytest.raises(BadRequest) as ex:
        api.request(api_url, '123456', METHOD)
    assert ex.typename == 'BadRequest'


def test_api_request_resource_not_found():
    api = Api()
    api_url = 'Stats/CareerForOwnedGames?'
    with pytest.raises(ResourceNotFound) as ex:
        api.request(api_url, API_KEY, METHOD)
    assert ex.typename == 'ResourceNotFound'
