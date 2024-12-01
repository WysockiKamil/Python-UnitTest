import unittest
from asercja import *


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4,5), 20)

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 5, '4')
        self.assertRaises(TypeError, area, '4', '5')

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -5, 2)
        self.assertRaises(ValueError, area, 5, -4)
        self.assertRaises(ValueError, area, -5, -4)


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])

    def test_case_2(self):
        self.assertEqual('3.2'.split('.'), ['3', '2'])

    def test_case_3(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')

    def test_case_4(self):
        self.assertTrue('apple'.islower())


if __name__ == '__main__':
    unittest.main(verbosity=2)