import pytest

from bf1.battlefield import Battlefield
from bf1.resolvers import resolve_weapon

from .utils import API_KEY


def weapon_call(weapon):
    bf = Battlefield('girbons', API_KEY, 'Pc')
    response = bf.progression_service.get_weapon(weapon=resolve_weapon(weapon))
    return response


def test_p08_pistol():
    response = weapon_call('p08 pistol')
    assert response.status_code == 200


def test_huot_automatic_low_weight():
    response = weapon_call('huot automatic low weight')
    assert response.status_code == 200


def test_mg_0815():
    response = weapon_call('mg 08/15')
    assert response.status_code == 200


def test_m1907_sl_trench():
    response = weapon_call('m1907 sl trench')
    assert response.status_code == 200


def test_antitank_mine():
    response = weapon_call('anti-tank mine')
    assert response.status_code == 200


def test_cavalry_sword():
    response = weapon_call('cavalry sword')
    assert response.status_code == 200


def test_smle_mkiii_infantry():
    response = weapon_call('smle mkiii infantry')
    assert response.status_code == 200


def test_lebel_model_1886_infantry():
    response = weapon_call('lebel model 1886 infantry')
    assert response.status_code == 200


def test_lewis_gun_low_weight():
    response = weapon_call('lewis gun low weight')
    assert response.status_code == 200


def test_gewehr_98_marksman():
    response = weapon_call('gewehr 98 marksman')
    assert response.status_code == 200


def test_antitank_grenade():
    response = weapon_call('anti-tank grenade')
    assert response.status_code == 200


def test_1903_hammerless():
    response = weapon_call('1903 hammerless')
    assert response.status_code == 200


def test_hellfighter_m1911():
    response = weapon_call('hellfighter m1911')
    assert response.status_code == 200


def test_bartek_bludgeon():
    response = weapon_call('bartek bludgeon')
    assert response.status_code == 200


def test_trench_fleur():
    response = weapon_call('trench fleur')
    assert response.status_code == 200


def test_c93():
    response = weapon_call('c93')
    assert response.status_code == 200


def test_doughboy_m1911():
    response = weapon_call('doughboy m1911')
    assert response.status_code == 200


def test_kukri():
    response = weapon_call('kukri')
    assert response.status_code == 200


def test_bar_m1918_trench():
    response = weapon_call('bar m1918 trench')
    assert response.status_code == 200


def test_m1911_extended():
    response = weapon_call('m1911 extended')
    assert response.status_code == 200


def test_trench_periscope():
    response = weapon_call('trench periscope')
    assert response.status_code == 200


def test_rsc_1917_factory():
    response = weapon_call('rsc 1917 factory')
    assert response.status_code == 200


def test_sniper_decoy():
    response = weapon_call('sniper decoy')
    assert response.status_code == 200


def test_m1909_benet_mercie_optical():
    response = weapon_call('m1909 benet mercie Optical')
    assert response.status_code == 200


def test_autoloading_8_35_marksman():
    response = weapon_call('autoloading 8 .35 marksman')
    assert response.status_code == 200


def test_survival_knife():
    response = weapon_call('survival knife')
    assert response.status_code == 200


def test_modello_1915():
    response = weapon_call('modello 1915')
    assert response.status_code == 200


def test_m97_trench_gun_hunter():
    response = weapon_call('m97 trench gun hunter')
    assert response.status_code == 200


def test_frommer_stop():
    response = weapon_call('frommer stop')
    assert response.status_code == 200


def test_madsen_mg_trench():
    response = weapon_call('madsen mg trench')
    assert response.status_code == 200


def test_bayonet_charge():
    response = weapon_call('bayonet charge')
    assert response.status_code == 200


def test_kolibri():
    response = weapon_call('kolibri')
    assert response.status_code == 200


def test_repair_tool():
    response = weapon_call('repair tool')
    assert response.status_code == 200


def test_light_antitank_grenade():
    response = weapon_call('light anti-tank grenade')
    assert response.status_code == 200


def test_lebel_model_1886_sniper():
    response = weapon_call('lebel model 1886 sniper')
    assert response.status_code == 200


def test_chauchat_low_weight():
    response = weapon_call('chauchat low weight')
    assert response.status_code == 200


def test_mini_grenade():
    response = weapon_call('mini grenade')
    assert response.status_code == 200


def test_m1907_sl_factory():
    response = weapon_call('m1907 sl factory')
    assert response.status_code == 200


def test_bedouin_dagger():
    response = weapon_call('bedouin dagger')
    assert response.status_code == 200


def test_mp_18_experimental():
    response = weapon_call('mp 18 experimental')
    assert response.status_code == 200


def test_selbstlader_1906_factory():
    response = weapon_call('selbstlader 1906 factory')
    assert response.status_code == 200


def test_12g_automatic_backbored():
    response = weapon_call('12g automatic backbored')
    assert response.status_code == 200


def test_lawrence_of_arabia's_smle():
    response = weapon_call('lawrence of arabia's SMLE')
    assert response.status_code == 200


def test_gewehr_98():
    response = weapon_call('gewehr 98')
    assert response.status_code == 200


def test_mars_automatic():
    response = weapon_call('mars automatic')
    assert response.status_code == 200


def test_howdah_pistol_sweeper():
    response = weapon_call('howdah pistol sweeper')
    assert response.status_code == 200


def test_billhook():
    response = weapon_call('billhook')
    assert response.status_code == 200


def test_sawed_off_shotgun():
    response = weapon_call('sawed off shotgun')
    assert response.status_code == 200


def test_bodeo_1889():
    response = weapon_call('bodeo 1889')
    assert response.status_code == 200


def test_ceirigotti_trench():
    response = weapon_call('cei-rigotti trench')
    assert response.status_code == 200


def test_mp_18_optical():
    response = weapon_call('mp 18 optical')
    assert response.status_code == 200


def test_automatico_m1918_storm():
    response = weapon_call('automatico m1918 storm')
    assert response.status_code == 200


def test_mortar_he():
    response = weapon_call('mortar he')
    assert response.status_code == 200


def test_bull_dog_revolver():
    response = weapon_call('bull dog revolver')
    assert response.status_code == 200


def test_medical_crate():
    response = weapon_call('medical crate')
    assert response.status_code == 200


def test_hatchet():
    response = weapon_call('hatchet')
    assert response.status_code == 200


def test_mortar_air():
    response = weapon_call('mortar air')
    assert response.status_code == 200


def test_ammo_pouch():
    response = weapon_call('ammo pouch')
    assert response.status_code == 200


def test_automatico_m1918_trench():
    response = weapon_call('automatico m1918 trench')
    assert response.status_code == 200


def test_gas_grenade():
    response = weapon_call('gas grenade')
    assert response.status_code == 200


def test_model_10a_factory():
    response = weapon_call('model 10-a factory')
    assert response.status_code == 200


def test_russian_1895_trench():
    response = weapon_call('russian 1895 trench')
    assert response.status_code == 200


def test_m1903():
    response = weapon_call('m1903')
    assert response.status_code == 200


def test_tripwire_bomb_inc():
    response = weapon_call('tripwire bomb INC')
    assert response.status_code == 200


def test_ceirigotti_optical():
    response = weapon_call('cei-rigotti optical')
    assert response.status_code == 200


def test_gewehr_m95_marksman():
    response = weapon_call('gewehr m.95 marksman')
    assert response.status_code == 200


def test_us_trench_knife():
    response = weapon_call('us trench knife')
    assert response.status_code == 200


def test_selbstlader_m1916_factory():
    response = weapon_call('selbstlader m1916 factory')
    assert response.status_code == 200


def test_m1903_marksman():
    response = weapon_call('m1903 marksman')
    assert response.status_code == 200


def test_gasser_m1870():
    response = weapon_call('gasser m1870')
    assert response.status_code == 200


def test_lebel_model_1886():
    response = weapon_call('lebel model 1886')
    assert response.status_code == 200


def test_chauchat_telescopic():
    response = weapon_call('chauchat telescopic')
    assert response.status_code == 200


def test_lewis_gun_suppressive():
    response = weapon_call('lewis gun suppressive')
    assert response.status_code == 200


def test_lewis_gun_optical():
    response = weapon_call('lewis gun optical')
    assert response.status_code == 200


def test_m97_trench_gun_sweeper():
    response = weapon_call('m97 trench gun sweeper')
    assert response.status_code == 200


def test_mondragon_storm():
    response = weapon_call('mondragon storm')
    assert response.status_code == 200


def test_incendiary_grenade():
    response = weapon_call('incendiary grenade')
    assert response.status_code == 200


def test_rifle_grenade_—_he():
    response = weapon_call('rifle grenade — HE')
    assert response.status_code == 200


def test_c96():
    response = weapon_call('c96')
    assert response.status_code == 200


def test_bandage_pouch():
    response = weapon_call('bandage pouch')
    assert response.status_code == 200


def test_12g_automatic_hunter():
    response = weapon_call('12g automatic hunter')
    assert response.status_code == 200


def test_k_bullets():
    response = weapon_call('k bullets')
    assert response.status_code == 200


def test_tripwire_bomb_—_gas():
    response = weapon_call('tripwire bomb — GAS')
    assert response.status_code == 200


def test_mp_18_trench():
    response = weapon_call('mp 18 trench')
    assert response.status_code == 200


def test_ribeyrolles_1918_factory():
    response = weapon_call('ribeyrolles 1918 factory')
    assert response.status_code == 200


def test_m1909_benet_mercie_storm():
    response = weapon_call('m1909 benet mercie Storm')
    assert response.status_code == 200


def test_gewehr_98_sniper():
    response = weapon_call('gewehr 98 sniper')
    assert response.status_code == 200


def test_nail_knife():
    response = weapon_call('nail knife')
    assert response.status_code == 200


def test_smle_mkiii():
    response = weapon_call('smle mkiii')
    assert response.status_code == 200


def test_crossbow_launcher_frg():
    response = weapon_call('crossbow launcher FRG')
    assert response.status_code == 200


def test_combat_knife():
    response = weapon_call('combat knife')
    assert response.status_code == 200


def test_mondragon_optical():
    response = weapon_call('mondragon optical')
    assert response.status_code == 200


def test_dynamite():
    response = weapon_call('dynamite')
    assert response.status_code == 200


def test_compact_trench_knife():
    response = weapon_call('compact trench knife')
    assert response.status_code == 200


def test_shovel():
    response = weapon_call('shovel')
    assert response.status_code == 200


def test_tripwire_bomb_—_he():
    response = weapon_call('tripwire bomb — HE')
    assert response.status_code == 200


def test_club():
    response = weapon_call('club')
    assert response.status_code == 200


def test_madsen_mg_low_weight():
    response = weapon_call('madsen mg low weight')
    assert response.status_code == 200


def test_no_3_revolver():
    response = weapon_call('no. 3 revolver')
    assert response.status_code == 200


def test_crossbow_launcher_he():
    response = weapon_call('crossbow launcher HE')
    assert response.status_code == 200


def test_raider_club():
    response = weapon_call('raider club')
    assert response.status_code == 200


def test_martinihenry():
    response = weapon_call('martini-henry')
    assert response.status_code == 200


def test_limpet_charge():
    response = weapon_call('limpet charge')
    assert response.status_code == 200


def test_impact_grenade():
    response = weapon_call('impact grenade')
    assert response.status_code == 200


def test_jambiya_knife():
    response = weapon_call('jambiya knife')
    assert response.status_code == 200


def test_flare_gun_spot():
    response = weapon_call('flare gun spot')
    assert response.status_code == 200


def test_ceirigotti_factory():
    response = weapon_call('cei-rigotti factory')
    assert response.status_code == 200


def test_rsc_1917_optical():
    response = weapon_call('rsc 1917 optical')
    assert response.status_code == 200


def test_trench_mace():
    response = weapon_call('trench mace')
    assert response.status_code == 200


def test_mondragonn_sniper():
    response = weapon_call('mondragonn sniper')
    assert response.status_code == 200


def test_red_baron's_p08():
    response = weapon_call('red baron's p08')
    assert response.status_code == 200


def test_repetierpistole_m1912():
    response = weapon_call('repetierpistole m1912')
    assert response.status_code == 200


def test_villar_perosa():
    response = weapon_call('villar perosa')
    assert response.status_code == 200


def test_model_10a_slug():
    response = weapon_call('model 10-a slug')
    assert response.status_code == 200


def test_hellfighter_trench_shotgun():
    response = weapon_call('hellfighter trench shotgun')
    assert response.status_code == 200


def test_m97_trench_gun_backbored():
    response = weapon_call('m97 trench gun backbored')
    assert response.status_code == 200


def test_russian_1895_infantry():
    response = weapon_call('russian 1895 infantry')
    assert response.status_code == 200


def test_gewehr_m95_carbine():
    response = weapon_call('gewehr m.95 carbine')
    assert response.status_code == 200


def test_mle_1903():
    response = weapon_call('mle 1903')
    assert response.status_code == 200


def test_spiked_club():
    response = weapon_call('spiked club')
    assert response.status_code == 200


def test_12g_automatic_extended():
    response = weapon_call('12g automatic extended')
    assert response.status_code == 200


def test_smoke_grenade():
    response = weapon_call('smoke grenade')
    assert response.status_code == 200


def test_automatico_m1918_factory():
    response = weapon_call('automatico m1918 factory')
    assert response.status_code == 200


def test_sniper_shield():
    response = weapon_call('sniper shield')
    assert response.status_code == 200


def test_madsen_mg_storm():
    response = weapon_call('madsen mg storm')
    assert response.status_code == 200


def test_smle_mkiii_marksman():
    response = weapon_call('smle mkiii marksman')
    assert response.status_code == 200


def test_gewehr_98_infantry():
    response = weapon_call('gewehr 98 infantry')
    assert response.status_code == 200


def test_pieper_m1893():
    response = weapon_call('pieper m1893')
    assert response.status_code == 200


def test_selbstlader_m1916_marksman():
    response = weapon_call('selbstlader m1916 marksman')
    assert response.status_code == 200


def test_hellfighter_bolo_knife():
    response = weapon_call('hellfighter bolo knife')
    assert response.status_code == 200


def test_howdah_pistol():
    response = weapon_call('howdah pistol')
    assert response.status_code == 200


def test_saber():
    response = weapon_call('saber')
    assert response.status_code == 200


def test_mg15_na_storm():
    response = weapon_call('mg15 n.a. storm')
    assert response.status_code == 200


def test_trench_knife():
    response = weapon_call('trench knife')
    assert response.status_code == 200


def test_mg15_na_suppressive():
    response = weapon_call('mg15 n.a. suppressive')
    assert response.status_code == 200


def test_c96_carbine():
    response = weapon_call('c96 carbine')
    assert response.status_code == 200


def test_m1907_sl_sweeper():
    response = weapon_call('m1907 sl sweeper')
    assert response.status_code == 200


def test_m1903_sniper():
    response = weapon_call('m1903 sniper')
    assert response.status_code == 200


def test_bar_m1918_telescopic():
    response = weapon_call('bar m1918 telescopic')
    assert response.status_code == 200


def test_gewehr_m95():
    response = weapon_call('gewehr m.95')
    assert response.status_code == 200


def test_pickaxe():
    response = weapon_call('pickaxe')
    assert response.status_code == 200


def test_smle_mkiii_carbine():
    response = weapon_call('smle mkiii carbine')
    assert response.status_code == 200


def test_m1911():
    response = weapon_call('m1911')
    assert response.status_code == 200


def test_at_rocket_gun():
    response = weapon_call('at rocket gun')
    assert response.status_code == 200


def test_selbstlader_m1916_optical():
    response = weapon_call('selbstlader m1916 optical')
    assert response.status_code == 200


def test_sawtooth_knife():
    response = weapon_call('sawtooth knife')
    assert response.status_code == 200


def test_m1909_benet_mercie_telescopic():
    response = weapon_call('m1909 benet mercie Telescopic')
    assert response.status_code == 200


def test_ammo_crate():
    response = weapon_call('ammo crate')
    assert response.status_code == 200


def test_autoloading_8_35_factory():
    response = weapon_call('autoloading 8 .35 factory')
    assert response.status_code == 200


def test_sjogren_inertial_factory():
    response = weapon_call('sjogren inertial factory')
    assert response.status_code == 200


def test_hellriegel_1915_factory():
    response = weapon_call('hellriegel 1915 factory')
    assert response.status_code == 200


def test_mg15_na_low_weight():
    response = weapon_call('mg15 n.a. low weight')
    assert response.status_code == 200


def test_rifle_grenade_frg():
    response = weapon_call('rifle grenade FRG')
    assert response.status_code == 200


def test_bar_m1918_storm():
    response = weapon_call('bar m1918 storm')
    assert response.status_code == 200


def test_cogwheel_club():
    response = weapon_call('cogwheel club')
    assert response.status_code == 200


def test_mle_1903_extended():
    response = weapon_call('mle 1903 extended')
    assert response.status_code == 200


def test_model_10a_hunter():
    response = weapon_call('model 10-a hunter')
    assert response.status_code == 200


def test_russian_1895():
    response = weapon_call('russian 1895')
    assert response.status_code == 200


def test_frommer_stop_auto():
    response = weapon_call('frommer stop auto')
    assert response.status_code == 200


def test_wex():
    response = weapon_call('wex')
    assert response.status_code == 200


def test_rifle_grenade_smk():
    response = weapon_call('rifle grenade SMK')
    assert response.status_code == 200


def test_frag_grenade():
    response = weapon_call('frag grenade')
    assert response.status_code == 200


def test_taschenpistole_m1914():
    response = weapon_call('taschenpistole m1914')
    assert response.status_code == 200


def test_barbed_wire_bat():
    response = weapon_call('barbed wire bat')
    assert response.status_code == 200


def test_tankgewehr_m1918():
    response = weapon_call('tankgewehr m1918')
    assert response.status_code == 200


def test_medical_syringe():
    response = weapon_call('medical syringe')
    assert response.status_code == 200


def test_autoloading_8_25_extended():
    response = weapon_call('autoloading 8 .25 extended')
    assert response.status_code == 200


def test_martinihenry_infantry():
    response = weapon_call('martini-henry infantry')
    assert response.status_code == 200


def test_flare_gun_flash():
    response = weapon_call('flare gun flash')
    assert response.status_code == 200


def test_p08_artillerie():
    response = weapon_call('p08 artillerie')
    assert response.status_code == 200


def test_m1903_experimental():
    response = weapon_call('m1903 experimental')
    assert response.status_code == 200


def test_auto_revolver():
    response = weapon_call('auto revolver')
    assert response.status_code == 200


def test_gewehr_m95_infantry():
    response = weapon_call('gewehr m.95 infantry')
    assert response.status_code == 200


def test_russian_1895_sniper():
    response = weapon_call('russian 1895 sniper')
    assert response.status_code == 200