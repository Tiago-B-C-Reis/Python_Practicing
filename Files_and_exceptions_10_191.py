# ---------- Reading an Entire File ---------------------------
# with open('text_files/pi_digits.txt') as file_object:
#    contents = file_object.read()
# print(contents.rstrip())


# ---------- Reading Line by Line ---------------------------
# filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())


# ---------- Making a List of Lines from a File ---------------------------
# filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
#    lines = file_object.readlines()
#    for line in lines:
#        print(line.rstrip())


# ---------- Working with a File’s Contents ---------------------------
# filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
#    lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#    pi_string += line.rstrip()
    # or -> pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))


# ---------- Large Files: One Million Digits ---------------------------
# filename = 'text_files/pi_million_digits.txt'

# with open(filename) as file_object:
#    lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#    pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#    print("Your birthday appears in the first million digits of pi!")
# else:
#    print("Your birthday does not appear in the first million digits of pi.")


# ---------- 10.1 ---------------------------
filename1 = 'text_files/code_everyday.txt'
with open(filename1) as file_object:
    for line0 in file_object:
        print(line0.rstrip())

with open(filename1) as file_object1:
    content = file_object1.read()
print(content.rstrip())

pi_string1 = ''
for line in content:
    pi_string1 += line.rstrip()
print(pi_string1)
print(len(pi_string1))


# ---------- 10.2 ---------------------------
filename2 = 'text_files/code_everyday.txt'
with open(filename2) as file_object2:
    for line1 in file_object2:
        print(line1.rstrip())

with open(filename2) as file_object3:
    content1 = file_object3.read()
print(content1.rstrip())

pi_string1 = ''
for line in content1:
    pi_string1 += line.rstrip()
print(pi_string1)
print(len(pi_string1))

message = content1
message.replace('python', 'Python')
print(message.replace('Python', 'Java'))





