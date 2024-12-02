import unittest

def setUpModule():
   print('dla modułu: POCZĄTEK')

def tearDownModule():
    print('dla modułu: KONIEC')

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'dla klasy testowej: POCZATEK{cls.__name__}')

    @classmethod
    def tearDownClass(cls):
        print(f'dla klasy testowe: KONIEC{cls.__name__}')

    def test_case1(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])

    def test_case2(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])


class TestClass2(unittest.TestCase):

    def setUp(self):
        print('dla przypadku: POCZATEK')

    def tearDown(self):
        print("dla przypadku: KONIEC")

    def test_case1(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])
    def test_case2(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])
    def test_case3(self):
        self.assertEqual('Jan Kowalski'.split(), ['Jan', 'Kowalski'])

class TestClass3(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')

