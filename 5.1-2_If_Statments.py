# 5.1
def age_prediction():

    my_age = 27
    age_guess = int(input("Guess my age: "))

    while age_guess != my_age:
        print("wrong, please try again: ")
        age_guess = int(input("Guess my age: "))
    else:
        print("Your guess is correct!")


# age_prediction()

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

my_country = "Portugal"
print("Is my country == 'Portugal'? I predict to be True")
print(my_country == "Portugal")


def lobby_key():

    allowed_persons = ["Ana", "Tiago", "Joana", "Helena", "Amilcar"]
    enter_key = str(input("What's your name?"))

    if enter_key == "Tony":
        print("Fuck you Tony!")
    elif enter_key in allowed_persons:
        print(f'Welcome home {enter_key}')
    else:
        print("Sorry, but you are not allowed!")


# lobby_key()


# 5.2

car_list = ["Bmw", "Mazda", "Renault", "Audi", "Volkswagen", "Mercedes"]

print('Bmw' in car_list)
print('Ferrari' in car_list)

car = "Mazda"
print(car.lower() == "mazda")
print(car.lower() == "BMW")

if "Bmw" and "Ferrari" in car_list:
    print("Great choice")
elif "Bmw" or "Ferrari" in car_list:
    print("Good choice")

if "Bmw" in car_list:
    print("Great!")

if "Ferrari" not in car_list:
    print("Not good!")







