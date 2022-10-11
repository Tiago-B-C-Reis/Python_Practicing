# 8.3
def make_shirt(size, letter_quantity):

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


make_shirt(1234, 124)
