import unittest

class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('python'.upper(), 'PYTHON')

    def test_case2(self):
        self.assertEqual('python'.upper(), 'PYTHON')

    def test_case3(self):
        self.assertEqual('3.9.1'.split('.'), ['3', '9', '1'])

    def test_case4(self):
        self.assertEqual(tuple('3.2.1'.split('.'), ('3', '2', '1')))

if __name__ == '__main__':
    unittest.main(verbosity=2)