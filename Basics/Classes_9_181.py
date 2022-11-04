import random


# 9.13
class Die:
    """
    This class rolls a die that have 'x' sides and rolls 'y' times
    """
    def __init__(self, roll):
        self.roll = roll
        # how many times the user wants to roll the dice
        self.sides = 20
        # nº of sides the dice has

    def roll_die(self):
        i = 0
        while i < self.roll:
            print(random.randint(1, self.sides))
            i += 1


# die = Die(10)
# die.roll_die()


# 9.14 / 9.15
# 9.14 / 9.15
class Lottery:

    """
    This class contains functions that randomly creates a 4 items list from 2 lists.
    """

    def __init__(self, my_ticket):
        self.numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        self.stars = ("A", "B", "C", "D", "E")
        self.win_keys = []
        self.my_ticket = my_ticket

    def lottery_keys(self):
        """
        Generates a list of 4 random keys from numbers and stars list.
        :return: the winning 4 keys
        """
        i = 0
        while i < 4:
            self.win_keys.append(random.choice(self.numbers + self.stars))
            i += 1
        print(f'If you have choose these key: {self.win_keys}, congratulations, you are the winner!')

    def lottery_analysis(self):
        """
        This function generates an amount of keys randomly until match the winning keys.
        :return: the nº of iterations until match the winning keys with the bet keys.
        """
        i = 0
        z = 0
        while True:
            while i < 4:
                self.my_ticket.append(random.choice(self.numbers + self.stars))
                i += 1
            i = 0

            self.win_keys.sort()
            self.my_ticket.sort()

            if self.win_keys != self.my_ticket:
                z += 1
            elif self.win_keys == self.my_ticket:
                break
            self.my_ticket = []

        single_probability = (1 / (len(self.numbers) + len(self.stars)))
        win_probability = single_probability * single_probability * single_probability * single_probability
        print(f'The probability to win is {win_probability}.')
        print(f'It was necessary to bet {z} before matching the'
              f' winning keys.\n')


lottery = Lottery(['2', 'A', '6', 'E', '5'])
lottery.lottery_keys()
lottery.lottery_analysis()


# 9.16
# Python 3 Module of the Week
import webbrowser
import time

# This module can open a website:
webbrowser.open_new_tab('https://pymotw.com')

# This module can screen the present time
print('The time is      :', time.ctime())
later = time.time() + 15
print('15 secs from now :', time.ctime(later))


