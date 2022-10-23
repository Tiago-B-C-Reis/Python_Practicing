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
class Lottery:

    def __init__(self):
        self.numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, )
        self.stars = ("A", "B", "C", "D", "E")
        self.win_keys = []
        self.my_ticket = []

    def lottery_keys(self):

        i = 0
        while i < 4:
            self.win_keys.append(random.choice(self.numbers + self.stars))
            i += 1
        print(f'If you have choose these key: {self.win_keys}, congratulations, you are the winner!')

    def win_probability(self):
        i = 0
        z = 0
        while True:
            while i < 4:
                self.my_ticket.append(random.choice(self.numbers + self.stars))
                i += 1
            i = 0
            print(self.my_ticket)

            if self.my_ticket != self.win_keys:
                z += 1
            elif self.my_ticket == self.win_keys:
                break
            self.my_ticket = []
        print(z)


lottery = Lottery()
lottery.lottery_keys()
lottery.win_probability()


# 9.15

