import unittest

class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(0.2 + 0.1, 0.3)

    def test_case2(self):
        self.assertAlmostEqual(0.2 + 0.1, 0.3)

    def test_case3(self):
        self.assertAlmostEqual(0.1234567, 0.1234567)

    def test_case4(self):
        self.assertAlmostEqual(0.12345678, 0.12345679, 6)

    def test_case5(self):
        self.assertAlmostEqual(0.1234567, 0.12345679, 6)