# 4.3
def counting_to_twenty():

    for i in range(1, 21):
        print(i)


# counting_to_twenty()

# 4.4
def one_million():

    list1 = []

    for i in range(1, 1000001):
        list1.append(i)
        print(i)
    print(list1)


# one_million()


# 4.5
def summing_a_million():

    list1 = []

    for i in range(1, 1000001):
        list1.append(i)
    print(min(list1))
    print(max(list1))
    print(sum(list1))


# summing_a_million()


# 4.6
def odd_numbers():

    for i in range(1, 21, 2):
        print(i)


# odd_numbers()


# 4.7
def multiples_of_threes():

    list1 = []

    for i in range(1, 31):
        list1.append(i * 3)
    print(list1)


# multiples_of_threes()


# 4.8
def cubes():

    for i in range(1, 11):
        x = i**3
        print(x)


cubes()


# 4.9
def cubes_comprehension():

    list1 = [i ** 3 for i in range(1, 11)]
    print(list1)


cubes_comprehension()
