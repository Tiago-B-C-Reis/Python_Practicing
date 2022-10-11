# 7.8
def deli():
    sandwich_orders = ["Chicken Sandwich", "Egg Sandwich", "Seafood Sandwich", "Roast Beef Sandwich",
                       "Grilled Cheese", "Ham Sandwich", "Nutella Sandwich", "Grilled Chicken Sandwich"]

    finished_sandwiches = []

    i = 0
    for sandwich in sandwich_orders:
        print(f'I made your {sandwich_orders[i]}')
        i += 1
        finished_sandwiches.append(sandwich)
    print(f'All the finish sandwiches:\n{finished_sandwiches}')


# deli()

# 7.9
def no_pastrami():
    sandwich_orders = ["Chicken Sandwich", "Egg Sandwich", "Pastrami Sandwich",
                       "Seafood Sandwich", "Roast Beef Sandwich", "Grilled Cheese",
                       "Ham Sandwich", "Pastrami Sandwich", "Nutella Sandwich",
                       "Grilled Chicken Sandwich", "Pastrami Sandwich"]
    finished_sandwiches = []
    print(sandwich_orders)
    print("Deli has run out of pastrami")

    while "Pastrami Sandwich" in sandwich_orders:
        sandwich_orders.remove("Pastrami Sandwich")

    print(sandwich_orders)

    i = 0
    for sandwich in sandwich_orders:
        print(f'I made your {sandwich_orders[i]}')
        i += 1
        finished_sandwiches.append(sandwich)
    print(f'All the finish sandwiches:\n{finished_sandwiches}')


# no_pastrami()

def dream_vacation():

    d_vacation = {}

    while True:
        name = input("What's you name? ")
        response = input("What is your dream destination for vacation? ")
        d_vacation[name] = response
        repeat = str(input("Would you like to add another response? ('yes' or 'no')"))
        if repeat == 'no':
            break

    print(d_vacation)

    for value, key in d_vacation.items():
        print(f'{value} dream destination for vacation is {key}')


dream_vacation()
