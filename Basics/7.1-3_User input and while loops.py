# 7.1
def rental_car():

    available_cars = ["Audi", "BMW", "Mercedes", "Renault", "Tesla", "Peugeot", "Volkswagen", "Mazda", "Ford",
                      "Toyota", "Volvo", "Nissan", "Rivian", "Porsche", "Kia", "Honda", "Jaguar", "Alfa Romeo",
                      "Fiat", "Land Rover", "Lexus", "Mini", "Polestar", "Jeep", "Seat", "Skoda", "Dacia",
                      "Opel", "Hyundai", "Chevrolet", "Suzuki", "DS", "Cupra"]

    costumer_name = input("Hello Sr/Madam, what is your name? ")
    costumer_request = input("What is the car brand you wish to rent? ")

    if costumer_request in available_cars:
        print(f'Thank you very much Sr/Madam {costumer_name}, we have the {costumer_request} at your disposal.')
    else:
        print("Sorry, but we dont have that for rental!")


# rental_car()


# 7.2
def restaurant_seating():

    while True:
        try:
            group_size = int(input("Good evening, how many people are you? "))
        except ValueError:
            print("That input is not acceptable!")
        else:
            if group_size > 8:
                print("Sorry, but you will need to wait for a table.")
                break
            else:
                print("The table is ready, come with me.")
                break


# restaurant_seating()


# 7.3
def multiples_of_ten():

    while True:
        try:
            user_input = int(input("Please give a number: "))
        except ValueError:
            print("That input is not acceptable!")
        else:
            if user_input % 10 != 0:
                print(f'{user_input} is NOT a multiple of 10!')
            elif user_input % 10 == 0:
                print(f'\nCongratulations!! \n- {user_input} is a multiples fo 10.')
                break


multiples_of_ten()

