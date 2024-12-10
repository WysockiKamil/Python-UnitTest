import unittest
from parameterized import parameterized
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    @parameterized.expand([
        (-3, -2, -5),
        (-3, 2, -1),
        (3, -2, 1),
        (3, 2, 5)
    ])
    def test_add(self, addend1, addend2, sum):
        self.assertEqual(self.calc.add(addend1, addend2), sum)

    @parameterized.expand([
        (4, 2, 2),
        (4, 6, -2),
        (4, 4, 0),
        (4, -6, 10),
        (-6, -8, 2),
    ])
    def test_subtraction(self, subtrahend, minued, difference):
        self.assertEqual(self.calc.sub(subtrahend, minued), difference)

    @parameterized.expand([
        (7, 3, 21),
        (-7, -3, 21),
        (-7, 3, -21),
        (3.5, 2, 7),
        (3.25, 2, 6.5),
        (3.14, 3.14, 9.8596)
    ])
    def test_multiplication(self, factor1, factor2, product):
        self.assertEqual(self.calc.mul(factor1, factor2), product)