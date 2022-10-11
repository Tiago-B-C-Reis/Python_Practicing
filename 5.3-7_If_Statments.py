# 5.3

alien_color = "Green"

if alien_color == "Red":
    print("You shall not receive points!")
elif alien_color == "Yellow":
    print("You shall not receive points!")
elif alien_color == "Green":
    print("You shall receive 5 points!")

if alien_color == "Red":
    pass
elif alien_color == "Yellow":
    print("You shall not receive points!")
else:
    print("Failed")

# 5.4
alien_color = "Red"

if alien_color == "Green":
    print("You shall receive 5 points!")
elif alien_color == "Yellow":
    print("You shall receive 10 points!")
elif alien_color == "Red":
    print("You shall receive 10 points!")

if alien_color == "Green":
    print("You shall receive 5 points!")
else:
    print("You shall receive 10 points!")

# 5.5
alien_color = "Green"

if alien_color == "Green":
    print("You shall receive 5 points!")
elif alien_color == "Yellow":
    print("You shall receive 10 points!")
else:
    print("You shall receive 15 points!")

alien_color = "Yellow"

if alien_color == "Green":
    print("You shall receive 5 points!")
elif alien_color == "Yellow":
    print("You shall receive 10 points!")
else:
    print("You shall receive 15 points!")

alien_color = "Red"

if alien_color == "Green":
    print("You shall receive 5 points!")
elif alien_color == "Yellow":
    print("You shall receive 10 points!")
else:
    print("You shall receive 15 points!")

# 5.6
def person_age():

    age = int(input("What's your age? "))

    if age == 2:
        print("You are a baby")
    elif 2 < age < 4:
        print("You are a toddler")
    elif 4 <= age < 13:
        print("You are a kid")
    elif 13 <= age < 20:
        print("You are a teenager")
    elif 20 <= age < 65:
        print("You are a adult")
    elif age >= 65:
        print("You are a elder")


person_age()

# 5.7
favorite_fruits = ["Mango", "Banana", "Orange"]

if "Mango" in favorite_fruits:
    print("You really like Mango!")

if "Banana" in favorite_fruits:
    print("You really like Banana!")

if "Orange" in favorite_fruits:
    print("You really like Orange!")

if "Apple" in favorite_fruits:
    print("You really like Apple!")

if "Strawberry" in favorite_fruits:
    print("You really like Strawberry!")


