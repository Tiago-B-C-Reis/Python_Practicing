import unittest


class Employee:
    """This class needs three inputs and returns two outputs, that are computed on in each function"""

    def __init__(self, first_name, last_name, annual_salary):
        """Definition of the three inputs needed in this class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def employee_name(self):
        """This function returns the info given related to the employee"""
        employee_info = f'Employee info:\n- {self.first_name} {self.last_name};' \
                        f'\n- Annual income: {self.annual_salary} euros.'
        print(employee_info)

    def give_raise(self, salary_raise=5000):
        """This function needs an input on how much the employee is going to be raised
        and returns the new annual income of that employee"""
        self.annual_salary += salary_raise
        print(f'\n{self.first_name}, you have being raised!\nNow your annual income is: {self.annual_salary} euros.\n')
# ------------------------------------------------------------------------------


class TestAnonymousSurvey(unittest.TestCase):

    def test_give_default_raise(self):
        first_name = "Tiago"
        last_name = "Reis"
        annual_salary = 80000
        employee = Employee(first_name, last_name, annual_salary)
        result = f'Employee info:\n- {first_name} {last_name};\n- Annual income: {annual_salary} euros.'
        self.assertEqual(employee.employee_name(), result)

    if __name__ == '__main__':
        unittest.main()
