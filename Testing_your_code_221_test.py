import unittest


class Employee:
    """ """

    def __init__(self, first_name, last_name, annual_salary):
        """ """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def employee_name(self):
        """ """
        employee_info = f'Employee info:\n- {self.first_name} {self.last_name}'
        return employee_info

    def give_raise(self, salary_raise=5000):
        """ """
        self.annual_salary += salary_raise
        print(self.annual_salary)

# ------------------------------------------------------------------------------


class TestAnonymousSurvey(unittest.TestCase):

    def test_give_default_raise(self):
        first_name = "Tiago"
        last_name = "Reis"
        annual_salary = 20000
        employee = Employee(first_name, last_name, annual_salary)
        self.assertEqual(employee.give_raise(), 20000)

    if __name__ == '__main__':
        unittest.main()




    #def setUp(self):
    # first_name = "Tiago"
     #  last_name = "Reis"
     #   annual_salary = 20000
      #  self.employee = Employee(first_name, last_name, annual_salary)
       # self.salary_raise = 5000
        #self.correct = 25000
