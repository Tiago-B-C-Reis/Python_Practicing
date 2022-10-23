# 9.6
from Classes_9_167 import Restaurant


class IceCreamStand(Restaurant):
    """
    This class inherits the Restaurant methods and allow to describe
    a specific restaurant type and the ice cream flavors.
    """
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        flavors = [self.flavors]
        print(f'These are the flavors you choose {flavors}')


# my_icecream = IceCreamStand("Olá", "Ice_cream", "strawberry", "mango")
# my_icecream.describe_restaurant()
# my_icecream.display_flavors()


# 9.7 / 9.8
from Classes_9_162 import User


class Admin(User):
    """
    Simples class that inherits the user class methods and has one method itself
    to welcome the admin.
    """
    def __init__(self, first_name, last_name, age, e_mail, country, city, marital_status):
        super().__init__(first_name, last_name, age, e_mail, country, city, marital_status)
        self.privileges = Privileges()

    def congrat_admin(self):
        if self.fist_name == "Tiago":
            print("Hello admin")


class Privileges:
    """
    This class as a method to show the admin privileges.
    """
    def __init__(self):
        self.privileges = "can add post", "can delete post", "can ban user"

    def show_privileges(self):
        privileges = [self.privileges]
        print(privileges)


# admin = Admin("Jon", "Snow", "30", "Jon.snow@gmail.com", "The real north", "none", "Complicated")
# admin.congrat_admin()
# admin.privileges.show_privileges()


# 9.9
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            car_range = 260
            print(f"This car can go about {car_range} miles on a full charge.")
        elif self.battery_size == 100:
            car_range = 315
            print(f"This car can go about {car_range} miles on a full charge.")

    def upgrade_battery(self):
        """If the battery size is standard, this function upgrade it to 100"""
        if self.battery_size == 75:
            self.battery_size = 100
        print(f'You battery size has been updated to {self.battery_size}')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
        # The super() function at x is a special function that allows you to call
        # a method from the parent class. This line tells Python to call the __init__()
        # method from Car, which gives an ElectricCar instance all the attributes


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
