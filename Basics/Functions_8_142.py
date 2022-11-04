# 8.6
def describe_city(city_input, country_input="Portugal"):

    return_city_country = f'"{city_input}, {country_input}"'
    return return_city_country


return_func = describe_city("Braga")
# print(return_func)


# 8.7
def make_album(artist_name, album_title, n_of_songs=None):

    music_album = {artist_name: album_title, "Album nº of songs: ": n_of_songs}

    return music_album


x = make_album("The Dark Side of the Moon", " Pink Floyd", 10)
# print(x)


# 8.8
def make_album(artist_name=None, album_title=None, n_of_songs=None):

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


x1 = make_album("The Dark Side of the Moon", " Pink Floyd", 10)
print(x1)
