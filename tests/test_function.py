import pytest
from function import fill_area_code, correct_lenght

#tests for fill_area_code

def test_if_one_digit_entry_is_acceptable():
    assert fill_area_code('1') == '001'

def test_if_two_digit_entry_is_acceptable():
    assert fill_area_code('11') == '011'

def test_if_three_digit_entry_is_acceptable():
    assert fill_area_code('011') == '011'

def test_if_a_highter_digit_entry_is_acceptable():
    assert fill_area_code('0000011') == '011'
    
#tests for correct_lenght

def test_if_empty_lenght_is_acceptable():
    assert correct_lenght('') == 0

def test_if_negative_minutes_is_acceptable():
    assert correct_lenght('-21') == 0

def test_if_string_is_being_correctly_converted():
    assert correct_lenght('23.4') == 23.4