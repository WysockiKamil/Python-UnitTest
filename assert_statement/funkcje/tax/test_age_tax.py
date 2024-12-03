import unittest
from tax import *

class testClass_age(unittest.TestCase):
    def test_age_incorrect_value_minus(self):
        with self.assertRaises(ValueError):
            calc_tax(1000, 0.2, -5)

    def test_age_incorrect_value_zero(self):
        with self.assertRaises(ValueError):
            calc_tax(1000, 0.2, 0)

    def test_age_incorrect_value_string(self):
        with self.assertRaises(TypeError):
            calc_tax(1000, 0.2, '0')

    def test_age_incorrect_value_float(self):
        with self.assertRaises(TypeError):
            calc_tax(1000, 0.2, 1.2)

class testClass_tax(unittest.TestCase):
    def test_young_age_below_limit(self):
        self.assertEqual(calc_tax(20000, 0.2, 18), 4000)

    def test_young_age_at_limit(self):
        self.assertEqual(calc_tax(30000, 0.2, 18), 5000)

    def test_young_age_exceeding_limit(self):
        self.assertEqual(calc_tax(80000, 0.2, 18), 5000)

    def test_working_age_edge_case_no_limit(self):
        self.assertEqual(calc_tax(60000, 0.2, 19), 12000)

    def test_working_age_edge_case_low_income(self):
        self.assertEqual(calc_tax(6000, 0.2, 19), 1200)

    def test_working_age_edge_case(self):
        self.assertEqual(calc_tax(60000, 0.5, 65), 30000)

    def test_senior_age_edge_case(self):
        self.assertEqual(calc_tax(60000, 0.2, 66), 7000)

    def test_senior_age_edge_case_exceedes_lmits(self):
        self.assertEqual(calc_tax(60000, 0.5, 66), 7000)