# The data list
employee_numbers = [1121, 1122, 1127, 1132, 1137, 1138, 1152, 1157]
employee_name = ['Jackie Grainger','Jignesh Thrakkar','Dion Green','Jacob Gerber','Sarah Sanderson','Brandon Heck','David Toma','Charles King']
wage = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]
rate = [28.886, 29.445, 30.485, 30.875, 31.616000000000003, 32.825, 33.592, 37.375 ]
rises = [29.46372, 30.0339, 31.0947, 31.4925, 32.24832000000001, 33.481500000000004, 34.26384, 38.1225]

# Above data are stored 
dictionary_items =[]

# For retriving the form one of the list, using this variable. 
count_index = 0

for name in employee_name: 
    dictionary_items.append ({'employee numbers': employee_numbers[count_index],
    'employee numbers': name, 'employee salary': wage[count_index],
    'total hourly rate': rate[count_index], 'company rise': rises[count_index]})
    
# for loop increment our current index variable
    count_index = count_index + 1
    
    
print(dictionary_items)    