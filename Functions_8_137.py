def make_shirt_input(size, letter_quantity):

    # key = letter size / value = nº of characters accepted
    shirt_limit = {12: 20, 14: 16, 16: 14, 18: 12, 20: 10, 22: 8, 24: 6}

    while True:
        try:
            size_limit_input = int(input("What is the size of the letter that you want on your shirt? "))
            print(f'\nYou have chosen the letter size {size_limit_input}, '
                  f'so the letter quantity limit for your shirt is: {shirt_limit[size_limit_input]}\n')
        except KeyError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        except ValueError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        else:
            break

    print(f'\nYour shirt has no limits, and you chose to have the letter size {size}, '
          f'and this quantity of letter {letter_quantity}.\n')


# 8.3
def make_shirt(size):

    # key = letter size / value = nº of characters accepted
    shirt_limit = {12: 20, 14: 16, 16: 14, 18: 12, 20: 10, 22: 8, 24: 6}

    while size not in shirt_limit.keys():
        try:
            size = int(input("What is the size of the letter that you want on your shirt? "))
            print(f'\n - You have chosen the letter size: "{size}"\n '
                  f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')
        except KeyError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        except ValueError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        else:
            break

    if size in shirt_limit.keys():
        print(f'\n - You have chosen the letter size: "{size}"\n '
              f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')

    shirt_printing = input("What is the message you want to print in your shirt? ")

    if len(shirt_printing) > size:
        print(f'This shirt size allow you that have {shirt_limit}')
    else:
        print(f'\n - You have choose a shirt with letter size: "{size}"\n '
              f'- And with the following message: "{shirt_printing}"\n')


# make_shirt(size="asg")


# 8.4
def large_shirt(size=24):

    # key = letter size / value = nº of characters accepted
    shirt_limit = {12: 20, 14: 16, 16: 14, 18: 12, 20: 10, 22: 8, 24: 6}

    while size not in shirt_limit.keys():
        try:
            size = int(input("What is the size of the letter that you want on your shirt? "))
            if size == 24:
                print(f'\n - You have chose the large size shirt with letter size with letter '
                      f'size: "{size}"\n '
                      f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')
            elif size == 18:
                print(f'\n - You have chose the medium size shirt with letter size: "{size}"\n '
                      f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')
            else:
                print(f'\n - You have chosen the letter size: "{size}"\n '
                      f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')
        except KeyError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        except ValueError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        else:
            break

    if size in shirt_limit.keys():
        if size == 24:
            print(f'\n - You have choose a shirt with letter size: "{size}"\n '
                  f'- That has the following standard message: I love Python"\n')
        elif size == 18:
            print(f'\n - You have choose a shirt with letter size: "{size}"\n '
                  f'- That has the following standard message: I love Python"\n')
        else:
            shirt_printing = input("What is the message you want to print in your shirt? ")
            if len(shirt_printing) > size:
                print(f'This shirt size allow you that have {shirt_limit}')
            else:
                print(f'\n - You have shirt with letter size: "{size}"\n '
                      f'- And with the following message: "{shirt_printing}"\n')


# large_shirt()


# 8.5
def describe_city(city_input, country_input="Portugal"):

    print(f'{city_input} is in {country_input}')


describe_city("Porto")

