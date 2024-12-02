import unittest

class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(isinstance('aws', str))

    def test_case2(self):
        self.assertTrue(isinstance('aws', int))

    def test_case3(self):
        self.assertFalse(isinstance('aws', str))

    def test_case4(self):
        self.assertFalse(isinstance('aws', int))