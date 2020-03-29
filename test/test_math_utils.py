import pytest
from math_utils import is_float

def test_is_float_none_value():
    assert not is_float(None)


def test_is_float_empty_value():
    assert not is_float('')


def test_is_float_alphabetic_value():
    assert not is_float('abc')


def test_is_float_mix_value():
    assert not is_float('12A')


def test_is_float_digit_value():
    assert is_float('12')


def test_is_float_float_value():
    assert is_float('12.234')


def test_is_float_invalid_value():
    assert not is_float('12.234.45')
