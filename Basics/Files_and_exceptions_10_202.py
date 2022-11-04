import shutil

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("You cant enter a sting!")
    else:
        print(answer)

print("\n")

# One is the use of the variable f to represent
# the file object, which is a common convention. The second is the use of
# the encoding argument. This argument is needed when your system’s default
# encoding does not match the encoding of the file that’s being read.


def count_words(files_names):
    """Count the approximate number of words in a file."""
    try:
        with open(files_names, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {files_names} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {files_names} has about {num_words} words.")


files_names = ['../Python_Crash_Course_material/chapter_10alice.txt',
               '../Python_Crash_Course_material/chapter_10/siddhartha.txt',
               '../Python_Crash_Course_material/chapter_10/moby_dick.txt',
               '../Python_Crash_Course_material/chapter_10/little_women.txt']
for i in files_names:
    count_words(i)
print("\n")


# 10.6/7 ------------------------------------------------------------------------------------------
while True:
    try:
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
    except ValueError:
        print("Please enter an integer.")
    else:
        print(first_number, second_number)
        break
print("\n")


# 10.8
files_name = ["../Python_Crash_Course_material/chapter_10/Cats.txt",
              "../Python_Crash_Course_material/chapter_10/dogs.txt"]
for i_files_name in files_name:
    try:
        with open(i_files_name) as file_object:
            for line in file_object:
                print(line.rstrip())
    except FileNotFoundError:
        print(f'Sorry but the file ({i_files_name}) that you are locking is missing.')

# shutil.move("text_files/cats.txt", "text_files/10_8/cats.txt")
# print("The file 'cats.txt' was move to 'text_files/10_8/cats.txt'.")


# 10.9
for i_files_name in files_name:
    try:
        with open(i_files_name) as file_object:
            for line in file_object:
                print(line.rstrip())
    except FileNotFoundError:
        pass
print("\n")


# 10.10
file_names = "../Python_Crash_Course_material/chapter_10/10_10.txt"
with open(file_names) as file_object:
    content = file_object.read()
    words = content.split()
    occurrences = content.lower().count("the ")
    print(f'There is {len(words)} words in this file.')
    print('Number of occurrences of the word :', occurrences)

