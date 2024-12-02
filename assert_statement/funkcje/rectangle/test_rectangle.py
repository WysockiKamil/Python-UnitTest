import unittest
from rectangle import area, perimeter

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

class TestPerimeter(unittest.TestCase):

    def test(self):
        self.assertEqual(perimeter(4,5), 18)

    def test_perimeter_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, perimeter, '4', 5)
        self.assertRaises(TypeError, perimeter, 5, '4')
        self.assertRaises(TypeError, perimeter, '4', '5')

    def test_perimeter_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, perimeter, -5, 2)
        self.assertRaises(ValueError, perimeter, 5, -4)
        self.assertRaises(ValueError, perimeter, -5, -4)