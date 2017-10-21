import pytest

from bf1.battlefield import Battlefield
from bf1.exceptions import PlatformError, ConfigError

from .utils import API_KEY

from vehicle import VEHICLES
from weapon import  WEAPONS

def _convert_to_list(data):
    if isinstance(data, (str)):
        res = [data]
    elif isinstance(data, (list)):
        res = data
    else:
        res = []
    return res

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


def test_weapon_call(weapon=None):
    bf = Battlefield('girbons', API_KEY, 'Pc')
    if weapon is None:
        weapon_list = WEAPONS
    else:
        weapon_list = _convert_to_list(weapon)

    for w in weapon_list:
        try:
            response = bf.progression_service.get_weapon(weapon=w)
            assert response.status_code == 200
        except AssertionError:
            # Do something
            raise


def test_vehicle_call(vehicle=None):
    bf = Battlefield('girbons', API_KEY, 'Pc')
    if vehicle is None:
        vehicle_list = VEHICLES
    else:
        vehicle_list = _convert_to_list(vehicle)

    for v in vehicle_list:
        try:
            response = bf.progression_service.get_vehicle(vehicle=v)
            assert response.status_code == 200
        except AssertionError:
            # Do something
            raise


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
