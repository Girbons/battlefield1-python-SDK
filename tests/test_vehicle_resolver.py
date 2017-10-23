import pytest

from bf1.battlefield import Battlefield
from bf1.resolvers import resolve_vehicle

from .utils import API_KEY


def vehicle_call(vehicle):
    bf = Battlefield('girbons', API_KEY, 'Pc')
    response = bf.progression_service.get_vehicle(vehicle=resolve_vehicle(vehicle))
    return response


def test_dr1_fighter():
    response = vehicle_call('dr.1 fighter')
    assert response.status_code == 200


def test_airship_l30():
    response = vehicle_call('airship l30')
    assert response.status_code == 200


def test_rumpler_ci_attack_plane():
    response = vehicle_call('rumpler c.i attack plane')
    assert response.status_code == 200


def test_mc_35hp_sidecar():
    response = vehicle_call('mc 3.5hp sidecar')
    assert response.status_code == 200


def test_st_chamond():
    response = vehicle_call('st chamond')
    assert response.status_code == 200


def test_artillery_truck():
    response = vehicle_call('artillery truck')
    assert response.status_code == 200


def test_horse():
    response = vehicle_call('horse')
    assert response.status_code == 200


def test_mc_18j_sidecar():
    response = vehicle_call('mc 18j sidecar')
    assert response.status_code == 200


def test_kft_scout():
    response = vehicle_call('kft scout')
    assert response.status_code == 200


def test_mark_v_landship():
    response = vehicle_call('mark v landship')
    assert response.status_code == 200


def test_fortress_gun():
    response = vehicle_call('fortress gun')
    assert response.status_code == 200


def test_halberstadt_cl_ii_attack_plane():
    response = vehicle_call('halberstadt cl. ii attack plane')
    assert response.status_code == 200


def test_char_2c():
    response = vehicle_call('char 2c')
    assert response.status_code == 200


def test_sopwith_camel_fighter():
    response = vehicle_call('sopwith camel fighter')
    assert response.status_code == 200


def test_fk_96_field_gun():
    response = vehicle_call('fk 96 field gun')
    assert response.status_code == 200


def test_albatros_diii_fighter():
    response = vehicle_call('albatros diii  fighter')
    assert response.status_code == 200


def test_3795_scout():
    response = vehicle_call('37/95 scout')
    assert response.status_code == 200


def test_romfell_armored_car():
    response = vehicle_call('romfell armored car')
    assert response.status_code == 200


def test_ft_armored_car():
    response = vehicle_call('f.t. armored car')
    assert response.status_code == 200


def test_aef_2a2_attack_plane():
    response = vehicle_call('a.e.f 2-a2 attack plane')
    assert response.status_code == 200


def test_spad_s_xiii_fighter():
    response = vehicle_call('spad s xiii fighter')
    assert response.status_code == 200


def test_rnas_armored_car():
    response = vehicle_call('rnas armored car')
    assert response.status_code == 200


def test_heavy_machine_gun():
    response = vehicle_call('heavy machine gun')
    assert response.status_code == 200


def test_dreadnought():
    response = vehicle_call('dreadnought')
    assert response.status_code == 200


def test_gotha_giv_bomber():
    response = vehicle_call('gotha g.iv bomber')
    assert response.status_code == 200


def test_m30_scout():
    response = vehicle_call('m30 scout')
    assert response.status_code == 200


def test_qf_1_aa():
    response = vehicle_call('qf 1 aa')
    assert response.status_code == 200


def test_a7v_heavy_tank():
    response = vehicle_call('a7v heavy tank')
    assert response.status_code == 200


def test_ev4_armored_car():
    response = vehicle_call('ev4 armored car')
    assert response.status_code == 200


def test_mas_torpedo_boat():
    response = vehicle_call('m.a.s. torpedo boat')
    assert response.status_code == 200


def test_ft17_light_tank():
    response = vehicle_call('ft-17 light tank')
    assert response.status_code == 200


def test_bl_92_siege_gun():
    response = vehicle_call('bl 9.2 siege gun')
    assert response.status_code == 200


def test_caproni_ca5_bomber():
    response = vehicle_call('caproni ca.5 bomber')
    assert response.status_code == 200


def test_bristol_f2b_attack_plane():
    response = vehicle_call('bristol f2.b attack plane')
    assert response.status_code == 200


def test_armored_train():
    response = vehicle_call('armored train')
    assert response.status_code == 200


def test_he_autocannon():
    response = vehicle_call('he auto-cannon')
    assert response.status_code == 200