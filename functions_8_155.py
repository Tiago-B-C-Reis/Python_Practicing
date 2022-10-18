# 8.15
import functions_8_150

functions_8_150.car_build('subaru', 'impreza', color='blue', tow_package=True, rali_prepare='Yes')

# 8.16
# import functions_8_131
# from functions_8_150 import build_profile
# from functions_8_142 import make_album as ma
# import functions_8_146 as f8
# from functions_8_137 import *


# 8.17
def make_album(artist_name=None, album_title=None, n_of_songs=None):

    """
    This function has the purpose to build a dictionary that can contain
    the number of albums as much as the user wants and in order to fulfill
    it, these parameters must be added by album:

    :param: artist_name: the name of the artist that composed the album;
    :param: album_title: the title of the album;
    :param: n_of_songs: the nº of songs that the album contains;
    :return: a complete dictionary with the amount of albums and it's
             information as the user wants.

    """

    music_album = {artist_name: [album_title, n_of_songs]}

    while True:
        loop_break = input("\nDo you wish to add more albums? (yes or no) ")
        if loop_break.lower() == "no":
            break
        elif loop_break.lower() == "yes":
            try:
                artist_name = str(input("What is the artist name of the album? "))
                album_title = str(input("What is the music album name? "))
                n_of_songs = int(input("How many songs does the album have? "))
                music_album[artist_name] = [album_title, n_of_songs]

            except ValueError:
                print("Please enter a valid number.")
                n_of_songs = int(input("How many songs does the album have? "))
                music_album[artist_name] = [album_title, n_of_songs]
        else:
            print("That is not a valid answer!")

    return music_album
# ------------------------------------------------------------------------------------------------


def make_shirt(size):

    """
    The purpose of these function is to give the user a shirt of the size he wants among the ones
    available and allow the user to input a print message on the shirt with a number of characters
    that is limit per size of shirt.


    :param: size: needs to give an input with the chosen size of user shirt
    :return: the information about the ordered shirt, the size, letter quantity and message printed.
    """

    # key = letter size / value = nº of characters accepted
    shirt_limit = {12: 20, 14: 16, 16: 14, 18: 12, 20: 10, 22: 8, 24: 6}

    while size not in shirt_limit.keys():
        try:
            size = int(input("What is the size of the letter that you want on your shirt? "))
            print(f'\n - You have chosen the letter size: "{size}"\n '
                  f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')
        except KeyError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        except ValueError:
            print(f'There are only these options available: {shirt_limit.keys()}')
        else:
            break

    if size in shirt_limit.keys():
        print(f'\n - You have chosen the letter size: "{size}"\n '
              f'- So the letter quantity limit for your shirt is: "{shirt_limit[size]}"\n')

    shirt_printing = input("What is the message you want to print in your shirt? ")

    if len(shirt_printing) > size:
        print(f'This shirt size allow you that have {shirt_limit}')
    else:
        print(f'\n - You have choose a shirt with letter size: "{size}"\n '
              f'- And with the following message: "{shirt_printing}"\n')
# ------------------------------------------------------------------------------------------------


def build_profile(first, last, **user_info):

    """
    Build a dictionary containing everything we know about a user.

    :param: first: the user first name;
    :param: last: the user last name;
    :param: user_info: all the extra info that he user wants to give;
    :return: all the user info that has been given to the function.
    """

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
