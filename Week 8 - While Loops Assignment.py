#For a total of five employees, a counter variable to keep track.

number_of_Employees = 1

#A list to keep track of all of the employees information.

Employees_List = [] 

# While loop that repeats for a total of five times.

while number_of_Employees <= 5:
    print("Enter Employee # "+str(number_of_Employees) +" information")

# Employee information will be stored in a dictionary.

    employee = {} 

    employee_ID_is_valid = False
    while not employee_ID_is_valid:
        employee_ID_is_valid = True

# As an input result, enter the employee ID number.

        employee_ID = input("Enter employee ID:") 
        employee_ID_is_integer = True
        try: 
            employee_ID = int(employee_ID)
        except:
            employee_ID_is_integer = False

# Employee ID is number and less than or equal to 7 digits.

        if( employee_ID_is_integer and employee_ID >= 0 and employee_ID<= 9999999):
            employee_ID_is_valid = True
        if not employee_ID_is_valid:
            print("You entered invalid employee ID")
    employee["ID"] = employee_ID       
             
    employee_name_is_valid = False
    while not employee_name_is_valid:
        employee_name_is_valid = True  
# As an input result, enter the employee name.

        employee_name = input("Enter Employee name:") 

# In a string, all the characters that should be avoided are listed.

        name_characters = "0123456789!\"@#$%^&*()_=+,<>/?;:[]{}\\" 
        for bad_characters in name_characters:
            if bad_characters in employee_name:
                employee_name_is_valid = False
        if not employee_name_is_valid:
            print("You entered invalid employee name")
    employee["name"] = employee_name

    employee_email_is_valid = False
    while not employee_email_is_valid:
        employee_email_is_valid = True

# As an input result, enter the employee email.

        employee_email = input("Enter Employee email:") 

# In a string, all the characters that should be avoided are listed.

        bad_email_characters = "!\"'#$%^&*()=+,<>/?;:[]{}\\)" 
        for bad_characters in bad_email_characters:
            if bad_characters in employee_email:
                employee_email_is_valid = False
        if(employee_email.count("@")!=1):
            employee_email_is_valid = False                          
        if not employee_email_is_valid:
            print("You entered invalid employee_Email")
    employee["email"] = employee_email

    employee_address_is_valid = False
    while not employee_address_is_valid:

#As an input result, enter the employee address.

        employee_address = input("Enter Employee address:") 
        if(len(employee_address) == 0): 
            employee_address_is_valid = True
            print( "Hello, "+employee_name+". Your Employee ID is "+str(employee_ID)+" and your email address is "+employee_email+". You did not provide an address.")
        else:
            employee_address_is_valid = True

# In a string, all the characters that should be avoided are listed.

            bad_address_characters = "!\"'@$%^&*_=+<>?;:[]{}" 
            for bad_characters in bad_address_characters:
                if bad_characters in employee_address:
                    employee_address_is_valid = False
            if employee_address_is_valid:
                employee["address"] = employee_address
                print("Hello, "+employee_name+". Your Employee ID is "+str(employee_ID)+" and your email address is "+employee_email+". Your address is "+employee_address+".")        
        if not employee_address_is_valid:
            print("You entered invalid Employee address")
        else:
            Employees_List.append(employee)
    number_of_Employees = number_of_Employees + 1
for employee in Employees_List:
    print()
    for employee_key, employee_value in employee.items():
        print(employee_key+": "+str(employee_value))


