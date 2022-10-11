# 5.8
def log_in():

    user_names = ["Tiago", "Ana", "Joana", "Diana", "Margarida"]

    user_input = str(input("Enter Username: "))

    if user_input in user_names:
        if user_input == "Tiago":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f' Hello {user_input}, thank you for logging in again.')
    else:
        print("Sorry, but this Username is not registered")


# log_in()


def hello_admin():

    user_names = ["Tiago", "Ana", "Joana", "Diana", "Margarida"]

    for i in user_names:
        if i == "Tiago":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f'Hello {i}, thank you for logging in again.')


# hello_admin()


def order_pizza():

    available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
            print("\nFinished making your pizza!")


# 5.9
def no_users():

    user_names = []

    if user_names:
        for i in user_names:
            if i == "Tiago":
                print("Hello admin, would you like to see a status report?")
            else:
                print(f'Hello {i}, thank you for logging in again.')
    else:
        print("There is no Usernames registered")


# no_users()


# 5.10
def checking_usernames():

    current_usernames = ["Tiago", "Ana", "Joana", "Diana", "Margarida", "Joao", "Isaac", "NoobMaster69"]
    current_usernames = [i.lower() for i in current_usernames]
    print(current_usernames)

    new_users = []

    user_input = str(input("Please enter your user_name: ").lower())
    new_users.append(user_input)

    for user in new_users:
        if user in current_usernames:
            print("That user name has already been taken, please enter a new one: ")
            user_input = str(input("Please enter your user_name: ").lower())

            while user_input in current_usernames:
                print("That user name has already been taken, please enter a new one: ")
                user_input = str(input("Please enter your user_name: ").lower())
            else:
                print("That user name is available")
                current_usernames.append(user_input)
        else:
            print("That user name is available")
            current_usernames.append(user_input)


# checking_usernames()


# 5.11
def ordinal_number():

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for number in number_list:
        if number == 1:
            print("1 th")
        elif number == 2:
            print("2 nd")
        elif number == 3:
            print("3 rd")
        else:
            print(f'{number} th')


ordinal_number()


