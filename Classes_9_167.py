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


restaurant = Restaurant("Tasco", "Portuguese")
restaurant.describe_restaurant()
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served()
restaurant.number_served = 15
restaurant.set_number_served()
restaurant.increment_number_served(6)


# 9.5






