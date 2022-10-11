# 6.4
def glossary1():
    fruit_price = {"Apple": 2, "Banana": 1.5, "Orange": 3, "Pear": 2.5, "Peach": 5, "Pineapple": 10,
                   "Strawberry": 20, "Mango": 17, "Lemons": 4.5, "Grapefruit": 21}

    for key, value in fruit_price.items():
        print(f'The price of the {key} is: \n {value} €')


# glossary1()

# 6.5
def rivers():
    rivers_names = {"Nile": "Egypt", "Amazon river": "South America", "Mississippi River": "U.S.A",
                    "Yangtze River": "China"}

    for key, values in rivers_names.items():
        print(f'The {key} runs trough {values}')
    for key, values in rivers_names.items():
        print(key)
    for key, values in rivers_names.items():
        print(values)


# rivers()

# 6.6
def polling():

    favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',
                          'John': 'Java', 'Alfred': 'C++', 'Matias': 'C#', 'Jaime': 'JAvaScript'}
    friends = ['phil', 'sarah']

    for name in favorite_languages.keys():
        print(name.title())

        if name in friends:
            language = favorite_languages[name].title()
            print(f"\t{name.title()}, I see you love {language}!")

    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}, thank you for taking the poll.")

    print("\nThe following languages have been mentioned:")

    for language in favorite_languages.values():
        print(language.title())


polling()
