import pytest
from funcoes import completa_codigo_de_area

def test_entrada_de_um_digito_é_corrigida():
    assert completa_codigo_de_area('1') == '001'

def test_entrada_de_dois_digitos_é_corrigida():
    assert completa_codigo_de_area('11') == '011'

def test_entrada_de_tres_digitos_é_corrigida():
    assert completa_codigo_de_area('011') == '011'

def test_entrada_de_mais_de_tres_digitos_é_corrigida():
    assert completa_codigo_de_area('0000011') == '011'