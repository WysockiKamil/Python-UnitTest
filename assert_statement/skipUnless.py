import unittest
import sys
from unittest import skipUnless


class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('darwin'), 'Requires mac')
    def test_case2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def test_casee(self):
        self.assertEqual('aws'.upper(), 'AWS')