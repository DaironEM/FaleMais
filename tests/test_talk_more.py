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

def test_if_tariff_is_being_computed_correctly(first_case):
    first_case.cost_per_minute()
    assert first_case.tariff == 1.9

def test_if_valid_tariff_are_beimg_rightly_precessed(first_case):
    assert first_case.is_valid_call() == True

def test_if_invalid_tariff_are_beimg_rightly_precessed(fourth_case):
    assert fourth_case.is_valid_call() == False

def test_if_cost_timeis_being_correctly_rsolved(first_case):
    assert first_case.cost_time_without_plan() == 38

def test_if_free_time_of_plan_is_correct(first_case):
    assert first_case.free_time_for_plan() == 30

def test_if_total_cost_with_plan_is_being_rightly_computed_first_case(first_case):
    assert first_case.cost_of_call_with_plan() == '$ 0.00'

def test_if_total_cost_without_plan_is_being_rightly_computed_first_case(first_case):
    assert first_case.cost_of_call_without_plan() == '$ 38.00'

def test_if_total_cost_with_plan_is_being_rightly_computed_second_case(second_case):
    assert second_case.cost_of_call_with_plan() == '$ 37.40'

def test_if_total_cost_without_plan_is_being_rightly_computed_second_case(second_case):
    assert second_case.cost_of_call_without_plan() == '$ 136.00'

def test_if_total_cost_with_plan_is_being_rightly_computed_third_case(third_case):
    assert third_case.cost_of_call_with_plan() == '$ 167.20'

def test_if_total_cost_without_plan_is_being_rightly_computed_third_case(third_case):
    assert third_case.cost_of_call_without_plan() == '$ 380.00'

def test_if_total_cost_with_plan_is_being_rightly_computed_with_inlegal_code(fourth_case):
    assert fourth_case.cost_of_call_with_plan() == '-'

def test_if_total_cost_without_plan_is_being_rightly_computed_with_inlegal_code(fourth_case):
    assert fourth_case.cost_of_call_without_plan() == '-'