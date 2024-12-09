import unittest
from employee.emp import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('start setting up...')
        self.emp = Employee('Kamil', 'Wysocki', 80000)

    def tearDown(self):
        print('tearing down')
        del self.emp


    def test_email(self):
        self.assertEqual(self.emp.email, 'kamil.wysocki@mail.com')

    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Jan'
        self.assertEqual(self.emp.email, 'jan.wysocki@mail.com')

    def test_email_after_changing_last_name(self):
        self.emp.last_name = 'Marchewka'
        self.assertEqual(self.emp.email, 'kamil.marchewka@mail.com')

    def test_tax_couting(self):
        self.assertEqual(self.emp.tax, 13600)

    def test_apply_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 88000)