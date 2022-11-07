import pytest
import requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


def test_george_washington():
    pass


def test_john_adams():
    pass


def test_thomas_jefferson():
    pass


def test_james_madison():
    pass


def test_james_monroe():
    pass


def test_john_quincy_adams():
    pass


def test_andrew_jackson():
    pass


def test_martin_van_buren():
    pass


def test_william_henry_harrison():
    pass


def test_john_tyler():
    pass


def test_james_k_polk():
    pass


def test_zachary_taylor():
    pass


def test_millard_fillmore():
    pass


def test_franklin_pierce():
    pass


def test_james_buchanan():
    pass


def test_abraham_lincoln():
    pass


def test_andrew_johnson():
    pass


def test_ulysses_s_grant():
    pass


def test_rutherford_b_hayes():
    pass


def test_james_garfield():
    pass


def test_chester_a_arthur():
    pass


def test_grover_cleveland():
    pass


def test_benjamin_harrison():
    pass


def test_william_mckinley():
    pass


def test_theodore_roosevelt():
    pass


def test_william_howard_taft():
    pass


def test_woodrow_wilson():
    pass


def test_warren_g_harding():
    pass


def test_calvin_coolidge():
    pass


def test_herbert_hoover():
    pass


def test_franklin_d_roosevelt():
    pass


def test_harry_s_truman():
    pass


def test_dwight_d_eisenhower():
    pass


def test_john_f_kennedy():
    pass


def test_lyndon_b_johnson():
    pass


def test_richard_m_nixon():
    pass


def test_gerald_r_ford():
    pass


def test_james_carter():
    pass


def test_ronald_reagan():
    pass


def test_george_h_w_bush():
    pass


def test_william_j_clinton():
    pass


def test_george_w_bush():
    pass


def test_barack_obamma():
    pass


def test_donald_trump():
    pass


def test_joseph_r_biden_jr():
    pass
