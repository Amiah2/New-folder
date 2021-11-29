# eliminate redundant code / promote code re-use 
def print_message_if_invalid(is_valid, field_name):
    if not is_valid:
        print("You entered invalid "+ field_name)

def has_bad_character(string_to_test, bad_chars):
    for bad_char in bad_chars:
        if bad_char in string_to_test:
            return True
    return False
                    
def print_employees(employees):
    for employee in listOfEmployees:
        print()
        for employee_key, employee_value in employee.items():
            print(employee_key+": "+str(employee_value))

#As an employee input result
def get_employee_number():
    Employ_ID_is_valid = False
    while not Employ_ID_is_valid:
        # As an input result, enter the employee ID number
        Employ_ID = input("Enter employee ID:") 
        Employ_ID_is_integer = True
        try: 
            Employ_ID = int(Employ_ID)
        except:
            Employ_ID_is_integer = False
        # Employee ID (this is required, and must be a number that is 7 or less digits long).
        if( Employ_ID_is_integer and Employ_ID >= 0 and Employ_ID<= 9999999):
            Employ_ID_is_valid = True
        print_message_if_invalid(Employ_ID_is_valid, "Employee ID")
    return Employ_ID

def get_employee_name():
    Employ_name_is_valid = False
    while not Employ_name_is_valid:
        Employ_name_is_valid = True  
        #As an input result, enter the employee name.
        Employ_name = input("Enter Employee name:") 
        # In a string, all the characters that should be avoided are listed.
        if has_bad_character(Employ_name, "0123456789!\"@#$%^&*()_=+,<>/?;:[]{}\\" ):
            Employ_name_is_valid = False
        print_message_if_invalid(Employ_name_is_valid, "Employee Name")
    return Employ_name

def get_employee_email():
    Employ_email_is_valid = False
    while not Employ_email_is_valid:
        Employ_email_is_valid = True
        # As an input result, enter the employee email.
        Employ_email = input("Enter Employee email:") 
        # In a string, all the characters that should be avoided are listed.
        if has_bad_character(Employ_email, "!\"'#$%^&*()=+,<>/?;:[]{}\\)"):
            Employ_email_is_valid = False
        if(Employ_email.count("@")!=1):
            Employ_email_is_valid = False                          
        print_message_if_invalid(Employ_email_is_valid, "Employee email")
    return Employ_email

def get_employee_address():
    Employ_address_is_valid = False
    while not Employ_address_is_valid:
        Employ_address = input("Enter Employee address:") 
        if(len(Employ_address) == 0): 
            return Employ_address
        else:
            Employ_address_is_valid = True
            if has_bad_character(Employ_address, "!\"'@$%^&*_=+<>?;:[]{}"):
                Employ_address_is_valid = False
            if Employ_address_is_valid: 
                return Employ_address
        print_message_if_invalid(Employ_address_is_valid, "Employee address")

def get_again():
    again_is_valid=True
    again = input("Would you like to add another employee? (y/n): ")
    while again != "y" and again != "n":
        again_is_valid =False
        again = input("Would you like to add another employee? (y/n): ")
        if again == "y" and again == "n":
            again_is_valid = True
        print_message_if_invalid(again_is_valid, "Employee address")
    return again



# main Program
# For a total of five employees, a counter variable to keep track.
numEmployees = 1
# A list to keep track of all of the employees' information. 
listOfEmployees = [] 
another = "y"
# While loop that repeats for a total of five times
while numEmployees <= 5 and another == "y":
    # Employee information will be stored in a dictionary.
    employee = {} 
    print("Enter Employee # "+str(numEmployees) +" information")
    employee["id"] = get_employee_number()    
    employee["name"] = get_employee_name()
    employee["email"] = get_employee_email()
    temp_address = get_employee_address()
    if temp_address == "": 
        print( "Hello, "+employee["name"]+". Your Employee ID is "+str(employee["id"])+" and your email address is "+employee["email"]+". You did not provide an address.")
    else:
        employee["address"] = temp_address
        print("Hello, "+employee["name"]+". Your Employee ID is "+str(employee["id"])+" and your email address is "+employee["email"]+". Your address is "+employee["address"] +".")        
    listOfEmployees.append(employee)
    numEmployees = numEmployees + 1
    another = get_again()

print_employees(listOfEmployees)