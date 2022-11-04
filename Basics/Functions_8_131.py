# 8.1
def display_message():

    print("In this chapter you’ll learn to write functions, which are named blocks of code "
          "that are designed to do one specific job.\nWhen you want to perform a particular task"
          "that you’ve defined in a function, you call the function responsible for it.\n"
          "If you need to perform that task "
          "multiple times throughout your program, you don’t need to type all the "
          "code for the same task again and again you just call the function dedicated"
          "to handling that task, and the call tells Python to run the code inside the "
          "function.\nYou’ll find that using functions makes your programs easier to write, read, test, and fix.\n"
          "In this chapter you’ll also learn ways to pass information to functions.\n"
          "You’ll learn how to write certain functions whose primary job is to display "
          "information and other functions designed to process data and return a "
          "value or set of values. \nFinally, you’ll learn to store functions in separate files "
          "called modules to help organize your main program files.")


# display_message()


def favorite_book(title):

    print(f'One of my favorite books is {title}.')


favorite_book("Python Crash Course_A Hands-On")



