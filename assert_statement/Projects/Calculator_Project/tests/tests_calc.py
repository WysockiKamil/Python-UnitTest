import unittest

from calculator.calc_math import SimpleMathCalculator

# def setUpModule():
#     print('setting up...')
#     global calc
#     calc = SimpleMathCalculator()
#
# def tearDownModule():
#     print('tearing down....')
#     global calc
#     del calc


class TestSimpleMathCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'Setting up class...')
        global calc
        calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print(f'Teating down class...')
        global calc
        del calc
#addition
    def test_add_positive_numbers(self):
        self.assertEqual(calc.add(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(calc.add(-3, -4), -7)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(calc.add(-3, 4), 1)
#subtraction
    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)

    def test_sub_negative_result(self):
        self.assertEqual(calc.sub(4, 6), -2)

    def test_sub_zero_result(self):
        self.assertEqual(calc.sub(4, 4), 0)

    def test_sub_minus_minus_case(self):
        self.assertEqual(calc.sub(4, -6), 10)

    def test_sub_minus_numbers_case(self):
        self.assertEqual(calc.sub(-4, -6), 2)
#multiplication
    def test_mul(self):
        self.assertEqual(calc.mul(7, 3), 21)

    def test_mul_two_negative_numbers(self):
        self.assertEqual(calc.mul(-7, -3), 21)

    def test_mul_positive_and_negative(self):
        self.assertEqual(calc.mul(-7, 3), -21)

    def test_mul_float_and_int_result(self):
        self.assertEqual(calc.mul(3.5, 2), 7)

    def test_mul_float_float(self):
        self.assertEqual(calc.mul(3.25, 2), 6.5)

    def test_mul_float_float_result_float(self):
        self.assertEqual(calc.mul(3.14, 3.14), 9.8596)
