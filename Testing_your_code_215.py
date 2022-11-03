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


# 11_1/2 ---------------------------------------------------------------------------------
def get_formatted_capital(city, country, population=''):
    """This function returns the country and city name all formatted"""
    if population:
        full_address = f'{country.title()} as a city called {city.title()} - population {population}.'
    else:
        full_address = f'{country.title()} as a city called {city.title()}.'
    return full_address


class TestGetFormattedCapital(unittest.TestCase):
    """Test for function 'get_formatted_capital' """

    def test_city_country(self):
        """Do cities like Santiago and countries like Chile works?"""
        formatted_capital = get_formatted_capital("Santiago", "Chile")
        self.assertEqual(formatted_capital, "Chile as a city called Santiago.")

    def test_city_county_population(self):
        """Do cities like Santiago, countries like Chile works and population like 5000000 works? """
        formatted_capital = get_formatted_capital("Santiago", "Chile", "5000000")
        self.assertEqual(formatted_capital, "Chile as a city called Santiago - population 5000000.")

    if __name__ == '__main__':
        unittest.main()
