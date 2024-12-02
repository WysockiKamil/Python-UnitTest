import unittest

class testClass(unittest.TestCase):

    def test_case1(self):
        self.assertIn('@', 'sample@mail.com')

    def test_case2(self):
        self.assertIn('a', 'kamil')

    def test_case3(self):
        self.assertIn('apple', ['apple', 'orange', 'sample@mail.com'])

    def test_case4(self):
        tech_stack= ['java', 'js', 'python', 'aws']
        self.assertIn('python', tech_stack)

    def test_case4(self):
        tech_stack= ['java', 'js', 'python', 'aws']
        self.assertIn('c++', tech_stack)

    def test_case5(self): #tylko po kluczu, nie wartosci;
        tech_stack= {'java': 'mid', 'js': 'junior', 'python': 'junior', 'aws': 'mid'}
        self.assertIn('junior', tech_stack)

    def test_case6(self):
        tech_stack= {'java': 'mid', 'js': 'junior', 'python': 'junior', 'aws': 'mid'}
        self.assertNotIn('junior', tech_stack)