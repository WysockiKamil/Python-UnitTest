import unittest

def setUpModule():
    print('Setting up module...')

def tearDownModule():
    print('Tearing down module...')

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'Setting up class...{cls.__name__}')

    @classmethod
    def tearDownClass(cls):
        print(f'Teating down class...{cls.__name__}')

    def test_case1(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])

    def test_case2(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])


class TestClass2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up class...')
    def test_case1(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])
    @classmethod
    def tearDownClass(cls):
        print('Teating down class...')

class TestClass3(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')

