import unittest


class Employee:
    """This class needs three inputs and returns two outputs, that are computed on in each function"""

    def __init__(self, first_name, last_name):
        """Definition of the three inputs needed in this class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = 20000

    def employee_name(self):
        """This function returns the info given related to the employee"""
        employee_info = f'Employee info:\n- {self.first_name} {self.last_name}' \
                        f'\n- Annual income: {self.annual_salary} euros.'
        return employee_info

    def give_raise(self, salary_raise=5000):
        """This function needs an input on how much the employee is going to be raised
        and returns the new annual income of that employee"""
        self.annual_salary += salary_raise
        raise_info = f'\n{self.first_name}, you have being raised!\nNow your annual income is: ' \
                     f'{self.annual_salary} euros.\n'
        return raise_info
# ------------------------------------------------------------------------------


class TestAnonymousSurvey(unittest.TestCase):

    def test_give_employee_name(self):
        first_name = "Tiago"
        last_name = "Reis"
        employee = Employee(first_name, last_name)
        test_name = employee.employee_name()
        test_name_result = f'Employee info:\n- {first_name} {last_name}' \
                           f'\n- Annual income: {employee.annual_salary} euros.'
        self.assertEqual(test_name, test_name_result)

    def test_give_default_raise(self):
        first_name = "Tiago"
        last_name = "Reis"
        employee = Employee(first_name, last_name)
        test_raise = employee.give_raise()
        test_raise_result = f'\n{first_name}, you have being raised!\nNow your annual income is: ' \
                            f'{employee.annual_salary} euros.\n'
        self.assertEqual(test_raise, test_raise_result)

    if __name__ == '__main__':
        unittest.main()
