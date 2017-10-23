import pytest

from bf1.battlefield import Battlefield
from bf1.exceptions import PlatformError, ConfigError

from .utils import API_KEY


def test_platform_play():
    bf = Battlefield('test', '123456', 'playstation')
    assert bf.get_platform() == 2


def test_platform_with_number_lower_than_1():
    bf = Battlefield('test', '123456', 0)
    with pytest.raises(PlatformError) as ex_info:
        bf.get_platform()
    assert 'Platform unavailable' in str(ex_info)


def test_platform_with_number_greater_than_3():
    bf = Battlefield('test', '123456', 4)
    with pytest.raises(PlatformError) as ex_info:
        bf.get_platform()
    assert 'Platform unavailable' in str(ex_info)


def test_platform_is_integer():
    bf = Battlefield('test', '12345', 3)
    assert bf.get_platform() == 3


def test_platform_xbox():
    bf = Battlefield('test', '123456', 'Xbox')
    assert bf.get_platform() == 1


def test_platform_pc():
    bf = Battlefield('test', '123456', 'PC')
    assert bf.get_platform() == 3


def test_platform_error():
    bf = Battlefield('test', '123456', 'nintendo')
    with pytest.raises(PlatformError) as ex_info:
        bf.get_platform()
    assert 'Platform unavailable' in str(ex_info.value)


def test_api_call_not_configured():
    bf = Battlefield('user', API_KEY, 'Pc')
    with pytest.raises(ConfigError) as ex_info:
        bf.test_call()
    assert 'Configuration not available in api_map for this call' in str(ex_info.value)


def test_api_call():
    bf = Battlefield('girbons', API_KEY, 'Pc')
    response = bf.stats_service.basic_stats()
    assert len(response) == 4


def test_custom_api_map():
    custom_api_map = {
        'api': {
            'stats_service': {
                'career_for_owned_games': {
                    'url': 'Stats/CareerForOwnedGames?{platform}&{username}',
                    'method': 'get'
                },
            }
        }
    }
    bf = Battlefield('girbons', API_KEY, 'Pc', custom_api_map['api'])
    response = bf.stats_service.career_for_owned_games()
    assert bf.api_map == custom_api_map['api']
    assert len(response) == 4
