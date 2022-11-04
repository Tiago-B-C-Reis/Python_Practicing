# The second argument, 'w',
# tells Python that we want to open the file in write mode. You can open a file
# in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
# you to read and write to the file ('r+'). If you omit the mode argument,
# Python opens the file in read-only mode by default.
# The open() function automatically creates the file you’re writing to if
# it does not already exist. However, be careful opening a file in write mode
# ('w') because if the file does exist, Python will erase the contents of the file
# before returning the file object.

filename = '../Python_Crash_Course_material/chapter_10/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    file_object.write("I love Python!\n")


# 10.3 ----------------------------------
gest_name = input("Hello, what is your name? ")

file_name = '../Python_Crash_Course_material/chapter_10/Guest.txt'
with open(file_name, "w") as fileobject:
    fileobject.write(gest_name)

# 10.4
file_book = '../Python_Crash_Course_material/chapter_10/Guest_book.txt'
with open(file_book, "w") as file_book_object:
    while True:
        gest_names = input("Hello, what is your name? ")
        print(f'Welcome, enjoy the party!')
        file_book_object.write(f'{gest_names}, paid his visit.\n')
        end_loop = input("Are you finished? (yes/no)")
        if end_loop.lower() == "yes":
            break

# 10.5
with open(file_book) as file_book_object:
    for line in file_book_object:
        name_i = ""
        for i in line:
            if i == ",":
                break
            elif i != ",":
                name_i += i
        name = name_i
        question = input(f'Hello {name}, what is the reason for you to program? ')
        with open('../text_files/Programing_poll.txt', "a") as file_poll_object:
            file_poll_object.write(f'{name} answer:\n{question}\n')










