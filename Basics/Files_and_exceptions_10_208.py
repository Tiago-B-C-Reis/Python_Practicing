# The JSON (JavaScript Object Notation) format was originally developed for JavaScript.
# The json module allows you to dump simple Python data structures into a
# file and load the data from that file the next time the program runs.
# You can also use json to share data between different Python programs.
# Even better, the JSON data format is not specific to Python, so you can share data you
# store in the JSON format with people who work in many other programming languages.
# It’s a useful and portable format, and it’s easy to learn.
import json


# 10.11 & 12 -----------------------------------------------------------------------------

def get_stored_number():
    """Get stored username if available."""
    filename = '../Python_Crash_Course_material/numbers.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_number():
    """Prompt for a new username."""
    list_numbers = []
    while True:
        try:
            user_numbers = int(input("What is your favorite number(s)? "))
            list_numbers.append(user_numbers)
        except ValueError:
            print("PLease enter a number! ")
        else:
            end_loop = input("Do you have any more favorite number(s) to add? (yes/no) ")
            if end_loop.lower() == "no":
                break
    filename = '../Python_Crash_Course_material/numbers.json'
    with open(filename, 'w') as f:
        json.dump(list_numbers, f)
    return list_numbers


def greet_the_user():
    """Greet the user by name."""
    user_number = get_stored_number()
    if user_number:
        if len(user_number) > 1:
            print(f"I know your favorite numbers! They are, {user_number}!")
        else:
            print(f"I know your favorite number! It’s, {user_number}!")
    else:
        user_number = get_new_number()
        if len(user_number) > 1:
            print(f"I know your favorite numbers! They are, {user_number}!")
        else:
            print(f"I know your favorite number! It’s, {user_number}!")


greet_the_user()

# 10.13 -----------------------------------------------------------------------------


def get_stored_username():
    """Get stored username if available."""
    filename = '../Python_Crash_Course_material/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = '../text_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        confirm_username = input(f'Are you {username}? (yes/no) ')
        if confirm_username.lower() == "no":
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
        else:
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()



