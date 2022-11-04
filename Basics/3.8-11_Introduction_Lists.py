# 3.9
def sorted_sort_reverse():

    places_to_visit = ["Italy", "Spain", "England", "Scotland", "Netherlands",
                       "Greece", "France", "switzerland", "Croatia"]

    print(f'Here is the original list: \n {places_to_visit}')
    print(f'Here is the sorted list: \n {sorted(places_to_visit)}')
    print(f'Here is the original list: \n {places_to_visit}')
    print(f'Here is the reversed sorted list: \n {sorted(places_to_visit, reverse=True)}')
    print(f'Here is the original list: \n {places_to_visit}')

    places_to_visit.reverse()
    print(f'Here is the reversed list: \n {places_to_visit}')
    print(f'Here is the updated list: \n {places_to_visit}')
    places_to_visit.reverse()
    print(f'Here is the re-reversed list: \n {places_to_visit}')
    print(f'Here is the original list: \n {places_to_visit}')

    places_to_visit.sort()
    print(f'Here is the sort list: \n {places_to_visit}')
    print(f'Here is the updated list: \n {places_to_visit}')
    places_to_visit.sort(reverse=True)
    print(f'Here is the reversed sort list: \n {places_to_visit}')
    print(f'Here is the updated list: \n {places_to_visit}')


# 3.10
def dinner_guests():
    person_names = ["Scarlett Johansson", "Jennifer Aniston", "Penelope Cruz",
                    "Angelina Jolie", "Marilyn Monroe", "Jennifer Lawrence",
                    "Emma Watson", "Sara Matos", "Emma Stone", "Natalie Portman",
                    "Julia Roberts", "Anne Hathaway", "Reese Witherspoon", "Cameron Diaz",
                    "Gwyneth Paltrow", "Jessica Chastain", "Margot Robbie", "Selena Gomez",
                    "Emilia Clarke", "Emily Blunt", "Megan Fox", "Chloe Grace Moretz",
                    "Eva Green", "Daisy Ridley", "Sophie Turner"]

    print(f'\nThis list has {len(person_names)} persons names.\n')


def every_function():

    rivers_list = []

    i = 0

    print("Please right the name of 10 rivers, one at a time!")

    while i < 10:
        x = input(f'River nº {i+1} of {10} :')
        rivers_list.append(x)
        i += 1

    print(f'The original list: \n{rivers_list}')
    print(f'\nThis list has {len(rivers_list)} rivers names.\n')

    print(f'Here is the sorted list: \n {sorted(rivers_list)}')
    print(f'Here is the reversed sorted list: \n {sorted(rivers_list, reverse=True)}')
    rivers_list.reverse()
    print(f'Here is the reversed list: \n {rivers_list}')
    rivers_list.sort()
    print(f'Here is the sort list: \n {rivers_list}')
    print(f'Here is the updated list: \n {rivers_list}')
    rivers_list.sort(reverse=True)
    print(f'Here is the reversed sort list: \n {rivers_list}')
    print(f'Here is the updated list: \n {rivers_list}')

    rivers_list.insert(5, "Rio Uima")
    rivers_list.append("Rio Caima")
    rivers_list.pop(2)
    print(f'The final list: \n{rivers_list}')


# every_function()


# 3.11
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles[3])

# IndexError: list index out of range, because the index 3 does not exist on that list
