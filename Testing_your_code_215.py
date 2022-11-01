import unittest

# These tests are done in a separate file and by importing the function we want to test,
# but here I'm doing it all in the same file since it is a simples exercise.


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

    if __name__ == '__main__':
        unittest.main()


# 11_2 ---------------------------------------------------------------------------------
def get_formatted_capital(city, country):
    """THis function returns the country and city name all formatted"""
    full_address = f'{country.title()} as a city called {city.title()}.'
    return full_address


class TestGetFormattedCapital(unittest.TestCase):
    """Test for function 'get_formatted_capital' """

    def test_city_country(self):
        """ """
        formatted_capital = get_formatted_capital("Santiago", "Chile")
        self.assertEqual(formatted_capital, "Chile as a city called Santiago.")

    if __name__ == '__main__':
        unittest.main()
