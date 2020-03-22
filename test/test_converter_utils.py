import unittest
from converter_utils import celsius_to_fahrenheit


class TestUnitConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit_100(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_with_default_rounding(self):
        self.assertEqual(celsius_to_fahrenheit(1), 33.8)
