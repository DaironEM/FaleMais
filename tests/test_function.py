import pytest
from function import fill_area_code

def test_if_one_digit_entry_is_acceptable():
    assert fill_area_code('1') == '001'

def test_if_two_digit_entry_is_acceptable():
    assert fill_area_code('11') == '011'

def test_if_three_digit_entry_is_acceptable():
    assert fill_area_code('011') == '011'

def test_if_a_highter_digit_entry_is_acceptable():
    assert fill_area_code('0000011') == '011'