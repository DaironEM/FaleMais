from fale_mais import FaleMais
import pytest


@pytest.fixture()
def primeiro_caso():
    return FaleMais('011', '016', 20, 'FaleMais 30')

@pytest.fixture()
def segundo_caso():
    return FaleMais('011', '017', 80, 'FaleMais 60')

@pytest.fixture()
def terceiro_caso():
    return FaleMais('018', '011', 200, 'FaleMais 120')

@pytest.fixture()
def quarto_caso():
    return FaleMais('018', '017', 100, 'FaleMais 30')

def test_se_a_tarifa_esta_sendo_calculada_corretamente(primeiro_caso):
    primeiro_caso.custo_por_minuto()
    assert primeiro_caso.tarifa == 1.9

def test_se_tarifas_validas_estao_sendo_tratadas_corretamente(primeiro_caso):
    assert primeiro_caso.ligacao_valida() == True

def test_se_tarifas_invalidas_estao_sendo_tratadas_corretamente(quarto_caso):
    assert quarto_caso.ligacao_valida() == False

def test_se_o_calculo_custo_esta_sendo_feito_corretamente(primeiro_caso):
    assert primeiro_caso.custo_tempo_sem_plano() == 38

def test_se_franquia_esta_sendo_calculada_corretamente(primeiro_caso):
    assert primeiro_caso.franquia_plano() == 30

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente(primeiro_caso):
    assert primeiro_caso.valor_com_plano() == '$ 0.00'

def test_se_valor_total_sem_plano_esta_sendo_calculado_corretamente(primeiro_caso):
    assert primeiro_caso.valor_sem_plano() == '$ 38.00'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_segundo_caso(segundo_caso):
    assert segundo_caso.valor_com_plano() == '$ 37.40'

def test_se_valor_total_sem_plano_esta_sendo_calculado_corretamente_segundo_caso(segundo_caso):
    assert segundo_caso.valor_sem_plano() == '$ 136.00'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_segundo_caso(terceiro_caso):
    assert terceiro_caso.valor_com_plano() == '$ 167.20'

def test_se_valor_total_sem_plano_esta_sendo_calculado_corretamente_segundo_caso(terceiro_caso):
    assert terceiro_caso.valor_sem_plano() == '$ 380.00'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_caso_ligacao_ilegal_com_plano(quarto_caso):
    assert quarto_caso.valor_com_plano() == '-'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_caso_ligacao_ilegal_sem_plano(quarto_caso):
    assert quarto_caso.valor_sem_plano() == '-'