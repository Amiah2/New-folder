# 6.1 Use a dictionary to store information about a favorite movie. Include movie title, rating, director, and the year it was released. 
# Include two other pieces of information about the movie of your choosing.

movie={'title':'Black Panther','Rating':7.3,'director':'Ryan Coogler',
        'year':2018,'Distributed by':'Walt Disney Studios Motion Pictures','Running time': '135 Minutes'
        }

# 6.2 Create a dictionary that stores item number, product name, and pricing information for a product of your choosing. 
# Write code that will take the current price, increase it by 30% and store the updated price back into the dictionary.
# Then print a message that the price of the item has been increased by 30%. Include the name of the product in your message.

store_item =  {'item_number':120965, 'product_name':'shoes', 'price_info': 15.54}

for store_key, store_value  in store_item.items():
    print(store_key +": "+str(store_value))

store_item['price_info']*=1.3
print("The price of "+ store_item["product_name"]+ ", has been increased by 30% to " + str(store_item["price_info"]))

# 6.3 Using the dictionary you created in problem 6-1, print out all of the keys and values in your dictionary using a loop.

for movie_key, movie_value  in movie.items(): 
    print(movie_key +": "+str(movie_value))

# 6.4 Create a list of 3 or more dictionary items. Each dictionary item should contain a word and its definition. 
# Make sure each dictionary item is stored in the format discussed in the lecture.
# Once you have created your list, loop through each item in it and neatly print out each word/definition pair (do not just print the dictionary item directly).

dictionary  = {
    'Electricity': 'Electricity is the set of physical phenomena associated with the presence and motion of matter that has a property of electric charge.',
    'Python': 'Python is an interpreted high-level general-purpose programming language.',
    'Search': 'try to find something by looking or otherwise seeking carefully and thoroughly.',
    'Look': 'direct ones gaze toward someone or something or in a specified direction.',
    }

for word, definition in dictionary.items():
    print("\n" + word.title() + ": " + definition)

# 6.5 Start with the dictionary you created for problem 6-1.
# Add a key to it that stores a list of actors/actresses who appear in the movie. Add 4 names to this list.
# Then, loop through the list of names and print them out, each on its own line.

movie["actors"]  = ['jason statham', 'christian bale', 'keira knightley', 'margot robbie']

print("\nActors: ")
for actor in movie["actors"]:
    print(actor.title())