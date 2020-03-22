import pytest
from converter_utils import celsius_to_fahrenheit


def test_celsius_to_fahrenheit_100():
    assert celsius_to_fahrenheit(100) == 212


def test_celsius_to_fahrenheit_with_default_rounding():
    assert celsius_to_fahrenheit(1) == 33.8
