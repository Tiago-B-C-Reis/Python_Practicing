# 6.1
def person():
    person_info = {'first_name': 'John', 'last_name': 'Smith', 'Age': 35, 'City': 'London'}

    print(person_info)
    print(person_info['first_name'], person_info['last_name'], person_info['Age'], person_info['City'])

    print("\n")


# 6.2
def favorite_numbers():

    each_favorite_numbers = {"Tiago": 7, "Ana": 9, "Joana": 2, "Diana": 10, "Margarida": 21, "Joao": 8, "Isaac": 4}

    for key, value in each_favorite_numbers.items():
        print(f' {key}__{value}')


# 6.3 - I'm doing the requested but with different theme:
def glossary():
    fruit_price = {"Apple": 2, "Banana": 1.5, "Orange": 3, "Pear": 2.5, "Peach": 5, "Pineapple": 10, "Strawberry": 20}

    for key, value in fruit_price.items():
        print(f'The price of the {key} is: \n {value} €')


glossary()


