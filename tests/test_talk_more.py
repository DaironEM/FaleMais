from talk_more import TalkMore
import pytest


@pytest.fixture()
def first_case():
    return TalkMore('011', '016', 20, 'FaleMais 30')

@pytest.fixture()
def second_case():
    return TalkMore('011', '017', 80, 'FaleMais 60')

@pytest.fixture()
def third_case():
    return TalkMore('018', '011', 200, 'FaleMais 120')

@pytest.fixture()
def fourth_case():
    return TalkMore('018', '017', 100, 'FaleMais 30')

def test_se_a_tarifa_esta_sendo_calculada_corretamente(first_case):
    first_case.cost_per_minute()
    assert first_case.tariff == 1.9

def test_se_tarifas_validas_estao_sendo_tratadas_corretamente(first_case):
    assert first_case.is_valid_call() == True

def test_se_tarifas_invalidas_estao_sendo_tratadas_corretamente(fourth_case):
    assert fourth_case.is_valid_call() == False

def test_se_o_calculo_custo_esta_sendo_feito_corretamente(first_case):
    assert first_case.cost_time_without_plan() == 38

def test_se_franquia_esta_sendo_calculada_corretamente(first_case):
    assert first_case.free_time_for_plan() == 30

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente(first_case):
    assert first_case.cost_of_call_with_plan() == '$ 0.00'

def test_se_valor_total_sem_plano_esta_sendo_calculado_corretamente(first_case):
    assert first_case.cost_of_call_without_plan() == '$ 38.00'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_segundo_caso(second_case):
    assert second_case.cost_of_call_with_plan() == '$ 37.40'

def test_se_valor_total_sem_plano_esta_sendo_calculado_corretamente_segundo_caso(second_case):
    assert second_case.cost_of_call_without_plan() == '$ 136.00'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_segundo_caso(third_case):
    assert third_case.cost_of_call_with_plan() == '$ 167.20'

def test_se_valor_total_sem_plano_esta_sendo_calculado_corretamente_segundo_caso(third_case):
    assert third_case.cost_of_call_without_plan() == '$ 380.00'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_caso_ligacao_ilegal_com_plano(fourth_case):
    assert fourth_case.cost_of_call_with_plan() == '-'

def test_se_valor_total_com_plano_esta_sendo_calculado_corretamente_caso_ligacao_ilegal_sem_plano(fourth_case):
    assert fourth_case.cost_of_call_without_plan() == '-'