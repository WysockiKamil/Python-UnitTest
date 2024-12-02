import unittest

def get_value(index, container):
    return container[index]

class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertRaises(IndexError, get_value, 3, 'AWS')

    def test_case2(self):
        self.assertRaises(Exception, get_value, 3, 'AWS')

    def test_casee(self):
        with self.assertRaises(IndexError):
            get_value(3, "AWS")