# 4.10
def slices():

    peson_names = ["Scarlett Johansson", "Jennifer Aniston", "Penelope Cruz",
                   "Angelina Jolie", "Marilyn Monroe", "Jennifer Lawrence",
                   "Emma Watson", "Sara Matos", "Emma Stone", "Natalie Portman",
                   "Julia Roberts", "Anne Hathaway", "Reese Witherspoon", "Cameron Diaz",
                   "Gwyneth Paltrow", "Jessica Chastain", "Margot Robbie", "Selena Gomez",
                   "Emilia Clarke", "Emily Blunt", "Megan Fox", "Chloe Grace Moretz",
                   "Eva Green", "Daisy Ridley", "Sophie Turner", "Manel"]
    x = len(peson_names)
    print(f'The first three names of the list are: {peson_names[0:3]}!\n')

    x = int(len(peson_names))
    if x % 2 != 0:
        x = int((x / 2) - 0.5)
        print(f"The names from the middle of the list is '{peson_names[x]}'!")
        print(f"Three names from the middle of the list is '{peson_names[(x-1):(x+2)]}'!")
    else:
        x = int(x / 2)
        print(f"The names from the middle of the list are '{peson_names[x:(x+2)]}'!")
        print(f"Three names from the 'middle' of the list is '{peson_names[(x-1):(x+2)]}'!")

    print(f'The three last names of the list are: {peson_names[-3:]}!\n')


# slices()

# 4.11

def my_pizzas_your_pizza():

    pizza_types = ["Cheese Pizza", "Pepperoni Pizza", "Meat Pizza", "Hawaiian Pizza"]
    friend_pizzas = ["Cheese Pizza", "Pepperoni Pizza", "Meat Pizza", "Hawaiian Pizza"]

    pizza_types.append("Veggie pizza")
    friend_pizzas.append("Margherita Pizza")

    for i in pizza_types:
        print(i)

    print("\n")

    for i in friend_pizzas:
        print(i)


my_pizzas_your_pizza()

# 4.12
# more of the same
