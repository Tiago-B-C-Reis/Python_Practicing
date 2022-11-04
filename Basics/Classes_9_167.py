# 9.4
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'This is restaurant "{self.restaurant_name}".')
        print(f'The cuisine type is: {self.cuisine_type}.')

    def set_number_served(self):
        print(f'Today the restaurant has served {self.number_served} costumers.')

    def increment_number_served(self, add):
        """ a """
        try:
            if add < 0:
                print("You can't add a negative number of persons!")
            else:
                self.number_served += add
                print(f'Until now, a total of {self.number_served} were served.')
        except TypeError:
            print("Please enter am integer")


# restaurant = Restaurant("Tasco", "Portuguese")
# restaurant.describe_restaurant()
# print(restaurant.number_served)
# restaurant.number_served = 10
# print(restaurant.number_served)
# restaurant.set_number_served()
# restaurant.number_served = 15
# restaurant.set_number_served()
# restaurant.increment_number_served(6)


# 9.5
class Userlog:

    def __init__(self, first_name, last_name, age, e_mail, country, city, marital_status):
        self.fist_name = first_name
        self.last_name = last_name
        self.age = age
        self.e_mail = e_mail
        self.country = country
        self.city = city
        self.marital_status = marital_status
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'You have tried to log in {self.login_attempts} times.')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'You have reset the log in attempts, now is {self.login_attempts}.')


# users = Userlog("Jon", "Snow", "30", "Jon.snow@gmail.com", "The real north", "none", "Complicated")
# users.increment_login_attempts()
# users.increment_login_attempts()
# users.increment_login_attempts()
# users.reset_login_attempts()





