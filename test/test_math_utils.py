import unittest
from math_utils import is_float


class TestMathUtil(unittest.TestCase):

    def test_is_float_None_value(self):
        self.assertFalse(is_float(None))

    def test_is_float_empty_value(self):
        self.assertFalse(is_float(''))

    def test_is_float_alphabetic_value(self):
        self.assertFalse(is_float('abc'))

    def test_is_float_mix_value(self):
        self.assertFalse(is_float('12A'))

    def test_is_float_digit_value(self):
        self.assertTrue(is_float('12'))

    def test_is_float_float_value(self):
        self.assertTrue(is_float('12.234'))

    def test_is_float_invalid_value(self):
        self.assertFalse(is_float('12.234.45'))
