import unittest

def setUpModule():
    print('Setting up module...')

class TestClass1(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])

class TestClass2(unittest.TestCase):

    def test_case2(self):
        self.assertEqual('3.9'.split('.'), ['3','9'])

class TestClass3(unittest.TestCase):

    def test_case3(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')

def tearDownModule():
    print('Tearing down module...')