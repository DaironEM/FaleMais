import pytest
from function import fill_area_code

def test_entrada_de_um_digito_é_corrigida():
    assert fill_area_code('1') == '001'

def test_entrada_de_dois_digitos_é_corrigida():
    assert fill_area_code('11') == '011'

def test_entrada_de_tres_digitos_é_corrigida():
    assert fill_area_code('011') == '011'

def test_entrada_de_mais_de_tres_digitos_é_corrigida():
    assert fill_area_code('0000011') == '011'