import random

person_names = ["Scarlett Johansson", "Jennifer Aniston", "Penelope Cruz",
                "Angelina Jolie", "Marilyn Monroe", "Jennifer Lawrence",
                "Emma Watson", "Sara Matos", "Emma Stone", "Natalie Portman",
                "Julia Roberts", "Anne Hathaway", "Reese Witherspoon", "Cameron Diaz",
                "Gwyneth Paltrow", "Jessica Chastain", "Margot Robbie", "Selena Gomez",
                "Emilia Clarke", "Emily Blunt", "Megan Fox", "Chloe Grace Moretz",
                "Eva Green", "Daisy Ridley", "Sophie Turner"]

print(f'\nThis list have {len(person_names)} persons names.\n')


# 3.4
def gest_list():

    for i in range(0, len(person_names)):
        print(f'Hello {person_names[i]}, would you like to go dinner with me?')
    print("\n")


# gest_list()


# 3.5
def changing_gest_list():

    x = random.randint(0, 25)
    print(f"Unfortunately '{person_names[x]}' can't come to dinner this evening.")
    person_names.pop(x)
    # del person_names[x] -> this code line does the same as the one above

    for i in range(0, len(person_names)):
        print(f'Hello {person_names[i]}, would you like to go dinner with me?')
    print("\n")


# changing_gest_list()


# 3.6
def more_guests():

    print(f"Hurray! there is 3 more seats at the table, now we can have 3 more guests.")
    a = input("Who is the first person to invite?")
    b = input("Who is the second person to invite?")
    c = input("Who is the third person to invite?")
    person_names.insert(0, a)
    person_names.insert(12, b)
    person_names.insert(len(person_names), c)

    for i in range(0, len(person_names)):
        print(f'Hello {person_names[i]}, would you like to go dinner with me?')
    print("\n")


# more_guests()


# 3.7
def shrinking_guests_list():

    print(f"I'm deeply sorry to announce that due to technical problems we are only being able to invite two persons\n")

    while len(person_names) > 2:
        x = random.randint(0, len(person_names)-1)
        print(f"I'm deeply sorry to announce that '{person_names[x]}' is no longer invited.")
        person_names.pop(x)

    print(f'\nThis list have {len(person_names)} persons names.\n')
    print(person_names, "\n")


shrinking_guests_list()

