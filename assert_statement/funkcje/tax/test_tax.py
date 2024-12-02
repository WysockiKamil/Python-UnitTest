import unittest

from tax import calc_tax

class TestCalcTax(unittest.TestCase):

    def test_should_calc_tax_with_ten_percent(self):
        self.assertEqual(10, calc_tax(100, 0.1))

    def test_should_calc_tax_with_fourteen_percent(self):
        self.assertAlmostEqual(14, calc_tax(100, 0.14))

    def test_calc_tax_with_incorrect_cmmount_type(self):
        self.assertRaises(TypeError, calc_tax, 'ten', 0.23)

    def test_calc_tax_with_incorrect_tax_rate_type(self):
        self.assertRaises(TypeError, calc_tax, 100, '0.23')

    def test_calc_tax_with_incorrect_tax_rate_and_amount_type(self):
        self.assertRaises(TypeError, calc_tax, '100', '0.23')

    def test_calc_tax_with_incorrect_tax_rate_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 100, 1.0)
        self.assertRaises(ValueError, calc_tax, 100, 0.0)

    def test_calc_negative_ammount_incorrect_tax_rate_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, -100, 0.23)