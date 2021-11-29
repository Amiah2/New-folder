# 8.1
# Write a function that accepts the name of your favorite radio station and prints a message saying something like "Let me tune in ."
# Then, ask the user for their favorite radio station and store the inputted value in a variable. Call the function you wrote above and pass the value that was inputted."""
def favorite_RadioStation(RadioStation):
    print("Let me tune in: " + str(RadioStation))

RadioStation = input("Enter the of Radio station: ")
favorite_RadioStation(RadioStation)
# 8.2
# Write a function called "print_business_cards" that accepts name,quantity, and tag line information as parameters. The function should print out a message stating how many business cards you are printing, who they are for, and the tag line that will appear on each card.
# Call the function three times passing different arguments to it.

def print_business_cards(name, quantity, tagline):
    print("business cards are printed for " +name)
    print("quantity of the cards " +str(quantity))
    print("tag line is " +tagline)
    print("\n")

print_business_cards("Anwar",20,"law firm")
print_business_cards("Munni",200,"Future hacker")
print_business_cards("Dula bhai",400,"Mr. land lord")

# 8.3 Re-write the function in problem 8-2 so that the default quantity of business cards ordered by default is 100. 
# Call the re-written function twice, once by passing a quantity of 150 and once by not passing quantity information.

def print_business_cards(name,tagline, quantity= 100):
    print("business cards are printed for " ,name)
    print("quantity of the cards " ,quantity)
    print("tag line is " ,tagline)
    print("\n")

print_business_cards("Anwar","law firm", 150)
print_business_cards("Munni","Future hacker")
print_business_cards("Dula bhai","Mr. land lord")

# 8.4
# Write a function that accepts song information, specifically song title and artist. 
# Make the default artist set to "Unknown" by default. This function should return a formatted string that looks like this: "<song> by <artist>."

# Call the function you just created three times. Make sure that at least one of the times,you don't pass artist information. Print out the result you get from each function.

def song_information(songtitle, artistname="Unknown"):
    information =songtitle+" by "+ artistname
    return information

firstTime = song_information("Aami ki tumay birokto korchi", " Bokul full sheuly full")
print(firstTime)

secondTime = song_information("Hello", " Oviman")
print(secondTime)

thirdTime = song_information("aakash chuya valobasha", )
print(thirdTime)


# 8.5 Modify the program you created in problem 8-4 so that it returns a dictionary item in the format we've studied instead of a string.

# Introduce a function that will loop through a list of dictionaries containing song information and print out each entry (note: you may not print dictionary items directly).

# Next, create an empty list called "playlist" and introduce a while loop where users are asked for items to add to the playlist. Be sure to ask for artist and song information, store them as a dictionary using your function, and add them to your playlist. Be sure to include a way to break the while loop.

# After a user has inputted all of the songs they wish to add to the playlist, pass the list to the function you wrote to print out all song entries.
def song_information(songtitle, artistname="Unknown"):
    return {"songtitle": songtitle, "artistname": artistname}

def print_songs(songs):
    print("Songs: ")
    for song in songs:
        information =song["songtitle"]+" by "+ song["artistname"]
        print(information)

playlist = []
more = "y"
while more == "y":
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    playlist.append(song_information(title,artist))
    more = input("Add more songs? y/n: ")

print_songs(playlist)
