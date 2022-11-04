# 6.7
def people():

    person_info = {'first_name': 'Jon', 'last_name': 'Snow', 'Age': 30, 'City': 'Winterfell'}
    person_info1 = {'first_name': 'Robert', 'last_name': 'Baratheon', 'Age': 50, 'City': 'kings landing'}
    person_info2 = {'first_name': 'Tyrion', 'last_name': 'Lannister', 'Age': 33, 'City': 'Casterly rock'}
    person_info3 = {'first_name': 'Jaime', 'last_name': 'Lannister', 'Age': 37, 'City': 'Casterly rock'}

    people_info = [person_info, person_info1, person_info2, person_info3]

    for info in people_info:
        print(info)


# people()


# 6.8
def pets():

    pets_info1 = {'first_name': 'Gost', 'Breed': 'Direwolves', 'Power': 25}
    pets_info2 = {'first_name': 'Drogon', 'Breed': 'Dragon', 'Power': 100}
    pets_info3 = {'first_name': 'Nymeria', 'Breed': 'Direwolves', 'Power': 20}
    pets_info4 = {'first_name': 'Viserion', 'Breed': 'Ice dragon', 'Power': 95}

    pets_info = [pets_info1, pets_info2, pets_info3, pets_info4]

    for info in pets_info:
        print(info)


# pets()


# 6.9
def favorite_places():

    favorite_destinations = {"Jon": ['Norway', 'Greenland', 'Denmark', 'Sweden'],
                             "Sansa": ['France', 'England', 'Italy', 'U.S.A'],
                             "Daenerys": ['Brazil', 'Argentina', 'Saudi Arabia', 'South Africa']}

    for names, places in favorite_destinations.items():
        print(f'{names} favorite places are:')
        for place in places:
            print(f'- {place}')
        print('\n')


# favorite_places()


# 6.10
def favorite_multiple_numbers():

    each_favorite_numbers = {"Tiago": [7, 21, 46, 1, 12], "Ana": [9, 11, 98, 15, 24],
                             "Joana": [2, 4, 32, 43, 57], "Diana": [10, 46, 87, 57, 16],
                             "Margarida": [21, 23, 45, 21, 28], "Joao": [8, 32, 46, 65, 92],
                             "Isaac": [4, 82, 17, 71, 14]}

    for names, numbers in each_favorite_numbers.items():
        print(f'\n {names} favorite numbers are:')
        for number in numbers:
            print(f'- {number}')


# favorite_multiple_numbers()


# 6.11
def cities():

    cities_info = {'Lisbon': {'Population': '504.718 people', 'Area': '100,00 km²', 'Ratio': '5047,18 persons/km²'},
                   'Madrid': {'Population': '3.223.000 people', 'Area': '604,30 km²', 'Ratio': '5333,44 persons/km²'},
                   'London': {'Population': '8.982.000 people', 'Area': '1.572,00 km²', 'Ratio': '5713,74 persons/km²'}}

    for name, information in cities_info.items():
        print(f'\n{name} population density info:')
        for info, numbers in information.items():
            print(f'- {info} = {numbers}')


# cities()


# 6.12
def extensions():
    import random

    alien_easy = {'color': 'green', 'power': 20, 'speed': 5}
    alien_medium = {'color': 'yellow', 'power': 60, 'speed': 25}
    alien_hard = {'color': 'red', 'power': 100, 'speed': 65}
    existing_aliens = [alien_easy, alien_medium, alien_hard]

    chosen_aliens = []

    for i in range(20):
        random_index = random.randrange(len(existing_aliens))
        random_alien = existing_aliens[random_index]
        chosen_aliens.append(random_alien)

    for i in chosen_aliens:
        if 20 in i.values():
            print('You have to fight a EASY level alien!')
        elif 60 in i.values():
            print('You have to fight a MEDIUM level alien!')
        elif 100 in i.values():
            print('You have to fight a HARD level alien!')


extensions()
