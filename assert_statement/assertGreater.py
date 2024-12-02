import unittest

class testClass(unittest.TestCase):

    def testCase1(self):
        self.assertGreater(0.2, 0.1)


    def testCase2(self):
        self.assertGreaterEqual(0.2, 0.2)


    def testCase3(self):
        self.assertLess(0.1, 0.2)


    def testCase4(self):
        self.assertLessEqual(0.1, 0.1)