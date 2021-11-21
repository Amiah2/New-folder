#7.1
#Write a program that asks a user what their favorite restaurant is. 
#Then, print a message saying something like, "Let me help you find the closest <restaurant name>."

restaurant_name = input("What is your favorite restaurant?")
print("Let me help you find the closest"+ restaurant_name)

#7.2 
# Write a program that asks a user for two numbers, multiplies them together, and then prints out the result of the multiplication operation.
print( "Enter two numbers")

number_one = int(input())
number_two = int(input())
output = int(number_one*number_two)
print( "The result of the multiplication operation"+ str(output))

#7.3
#Write a while loop that asks a user what they are having for dinner. 
# As they add items, add them to a list. Make sure you include a way for a user to break the loop.
#Once the loop has finished executing, print out the items in the list.
dinner_items = []  # Here we define an empty list.
menu = ""

while menu != "stop":
    menu = input('Please enter dinner item or write stop to make stop')
    if menu != "stop":
        dinner_items.append(menu)
print("Dinner items: ")
for dinner_item in dinner_items:
    print(dinner_item)

#7.4
#A carnival has three rides. 
# In a while loop, ask the user which ride they would like to go on. 
# If it's the Ferris Wheel, print a message asking the user for $2. If it's the tilt-a-whirl, print a message asking the user for $3. If it's the pirate ship, printing a message asking the user for $3.50. If the ride wasn't found, print a message that the ride wasn't found.
#Be sure to include a way for a user to break the loop.

while True:
    print("Below is the datails about rides :")
    print("Enter 1 for Ferris Wheel.")
    print("Enter 2 for Tilt-a -Whirl.")
    print("Enter 3 for Pirate ship")
    print("Enter 4 for to Exit")
    ride=input("Enter your choice : ")
    if ride=="1":
        print("please give $2")
    elif ride=="2":
        print("please give $3")
    elif ride=="3":
        print("please give $3.50")
    elif ride == "4":
        break
    else:
        print("Ride wasn't found.")
  



#7.5
#Create a list of items you think you will need the next time you go to the grocery store. 
# Have one item appear multiple times.
#Pretend that you decided not to purchase the item that appears multiple times. 
# Loop through each item in your original list using a while loop and remove all instances of this item.
list_of_item=['beans','mango','pear','beans','orange','Chillies','apple','garlic','potato','banana','beans']

while "beans" in list_of_item:
    list_of_item.remove('beans')

print("Items: ")
for item in list_of_item:
    print(item)