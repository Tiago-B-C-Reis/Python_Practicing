peson_names = ["Tiago", "João", "André", "Daniel", "André", "Martim", "Raul", "Xavier", "Francisco", "Fernando"]
car_names = ["Ferrari", "Lamborghini", "Mercedes", "Audi", "BMW", "Jaguar", "Lexus", "Toyota"]

# 3.1
def names():

    for i in range(0, len(peson_names)):
        print(peson_names[i])

names()

# 3.2
def greetings():

    for i in range(0, len(peson_names)):
        print(f'Greetings {peson_names[i]}, welcome te party!')

greetings()

# 3.3
def your_own_list():

    for i in range(0, len(car_names)):
        print(f'I would like to own a {car_names[i]}!')

your_own_list()


