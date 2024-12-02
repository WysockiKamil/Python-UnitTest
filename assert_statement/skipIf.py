import unittest
from datetime import date


class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2  != 0, 'Skipping odd days')
    def test_case2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2  == 0, 'Skipping even days')
    def test_case3(self):
        self.assertEqual('aws'.upper(), 'AWS')