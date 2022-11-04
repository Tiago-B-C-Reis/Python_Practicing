# 9.1 / 9.2
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'This is restaurant "{self.restaurant_name}"')
        print(f'The cuisine type is: {self.cuisine_type}')

    def open_restaurant(self):
        print("The restaurant is open")


# my_restaurant = Restaurant("Tasco", "Portuguese")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# your_restaurant = Restaurant("Mademoiselle", "French")
# your_restaurant.describe_restaurant()

# his_restaurant = Restaurant("Cais 35 Sushi", "Japanese")
# his_restaurant.describe_restaurant()


# 9.3
class User:

    def __init__(self, first_name, last_name, age, e_mail, country, city, marital_status):
        self.fist_name = first_name
        self.last_name = last_name
        self.age = age
        self.e_mail = e_mail
        self.country = country
        self.city = city
        self.marital_status = marital_status

    def describe_user(self):
        print(f'This is your input information:\n'
              f'First name: {self.fist_name}\n'
              f'Last name: {self.last_name}\n'
              f'Age: {self.age}\n'
              f'E-mail: {self.e_mail}\n'
              f'Country: {self.country}\n'
              f'City: {self.city}\n'
              f'Marital status: {self.marital_status}\n')

    def greet_user(self):
        print(f'Thank for sign in {self.fist_name, self.last_name}!')


# users = User("Jon", "Snow", "30", "Jon.snow@gmail.com", "The real north", "none", "Complicated")
# users.describe_user()
# users.greet_user()
