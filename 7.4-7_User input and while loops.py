# 7.4
def pizza_toppings():

    available_topping_types = ["Cheese", "Pepperoni", "Meat", "Hawaiian",
                               "Veggie", "Margherita", "BBQ Chicken", "Supreme",
                               "Buffalo", "The Works"]
    available_topping_types1 = [i.lower() for i in available_topping_types]

    toppings_to_add = []

    i = 0
    while True:
        if i == 0:
            topping = str(input("\nIf you want to see the options, please write 'help'\n"
                                "What is the topping you want to add to your pizza? "))
        else:
            topping = str(input("\nIf you want to see the options, please write 'help'\n"
                                "If you don't want to add more toppings, please write 'stop'\n"
                                "What is the topping you want to add to your pizza? "))
        if topping == 'help':
            print(f'\nToppings available:\n{available_topping_types}')
        elif topping.lower() in available_topping_types1:
            print("Thank you, we will add that topping to the pizza.")
            toppings_to_add.append(topping.title())
        elif topping.lower() == 'stop':
            print("These are the pizza you order:")
            for i in toppings_to_add:
                print(f'- {i} pizza')
            break
        else:
            print("\nSorry but we don't have it. Please enter help to see our options.")

        i += 1


# pizza_toppings()


# 7.5
def movie_tickets():

    people_number = 1
    cost = 0
    tickets_sold = {}

    while True:
        try:
            numb_of_people = int(input("How many are you? "))
        except ValueError:
            print("Please insert a number!")
        else:
            while people_number <= numb_of_people:
                try:
                    age = int(input(f'Person nº{people_number}, how old are you? '))
                except ValueError:
                    print("Please insert a number!")
                else:
                    if age < 3:
                        print("- Your ticket is free!")
                        a = f'Person nº{people_number}'
                        tickets_sold[a] = "Free!"
                    elif 3 <= age < 12:
                        print("- Your ticket is 10 euros.")
                        b = f'Person nº{people_number}'
                        tickets_sold[b] = "10 euros"
                        cost += 10
                    elif 12 <= age < 120:
                        print("- Your ticket is 15 euros.")
                        c = f'Person nº{people_number}'
                        tickets_sold[c] = "15 euros"
                        cost += 15
                    else:
                        print("**Are you sure that you are still alive?\n**Sorry but we are not selling you a ticket.")
                        d = f'Person nº{people_number}'
                        tickets_sold[d] = "Not sold"

                    people_number += 1

            for value, keys in tickets_sold.items():
                print(f'{value} = {keys}.')
            print(f'    - Total bill is = {cost}')
            break


# movie_tickets()


# 7.6
def three_exits():

    people_number = 1
    cost = 0
    tickets_sold = {}

    while True:
        try:
            numb_of_people = int(input("How many are you? "))
        except ValueError:
            print("Please insert a number!")
        else:
            # *** Requisite nº2, was already done ***
            while people_number <= numb_of_people:
                try:

                    # *** Requisite nº3, done ***
                    stop_button = str(input("If you wish to cancel you order, please enter 'quit': ")).lower()
                    if stop_button == "quit":
                        print("Thank you very much!")
                        break

                    age = int(input(f'Person nº{people_number}, how old are you? '))

                except ValueError:
                    print("Please insert a number!")
                else:
                    if age < 3:
                        print("- Your ticket is free!")
                        a = f'Person nº{people_number}'
                        tickets_sold[a] = "Free!"
                    elif 3 <= age < 12:
                        print("- Your ticket is 10 euros.")
                        b = f'Person nº{people_number}'
                        tickets_sold[b] = "10 euros"
                        cost += 10
                    elif 12 <= age < 135:
                        print("- Your ticket is 15 euros.")
                        c = f'Person nº{people_number}'
                        tickets_sold[c] = "15 euros"
                        cost += 15
                    else:
                        # *** Requisite nº1, done ***
                        print("**Sorry but that is disrespectful, we are trying to work!"
                              "\nNext customer please!")
                        break

                    people_number += 1

            for value, keys in tickets_sold.items():
                print(f'{value} = {keys}.')
            print(f'    - Total bill is = {cost}')
            break


# three_exits()

# 7.7

while 5 < 6:
    print("This loop will never end!")

