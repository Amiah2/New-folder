# As an input result, enter the employee ID number.
employee_ID = input("Enter employee ID:") 
employee_ID_is_integer = True

try: 
    employee_ID = int(employee_ID)
except:
    employee_ID_is_integer = False
# Employee ID (this is required, and must be a number that is 7 or less digits long)
if( employee_ID_is_integer and employee_ID >= 0 and employee_ID<= 9999999):
    
    employee_name_is_valid = True
# As an input result, enter the employee name.
    employee_name = input("Enter Employee name:") 
# In a string, all the characters that should be avoided are listed.
    name_character = " 0123456789!\"@#$%^&*()_=+,<>/?;:[]{}\\" 
    for bad_character in name_character:
        if bad_character in employee_name:
            employee_name_is_valid = False
    if employee_name_is_valid:

        employee_email_is_valid = True
# As an input result, enter the employee email.
        employee_email = input("Enter Employee email:")
# In a string, all the characters that should be avoided are listed. 
        bad_email_character = "!\"'#$%^&*()=+,<>/?;:[]{}\\)" 
        for bad_character in bad_email_character:
            if bad_character in employee_email:
                employee_email_is_valid = False
                         

        if(employee_email_is_valid):
# As an input result, enter the employee address.
            employee_address = input("Enter Employee address:") 
            if(len(employee_address) == 0): 
                print( "Hello, "+employee_name+". Your Employee ID is "+str(employee_ID)+" and your email address is "+employee_email+". You did not provide an address.")
            else:
                employee_address_is_valid = True
# In a string, all the characters that should be avoided are listed. 
                bad_address_character = "!\"'@$%^&*_=+<>?;:[]{}" 
                for bad_character in bad_address_character:
                    if bad_character in employee_address:
                        employee_address_is_valid = False
                if employee_address_is_valid:
                    print("Hello, "+employee_name+". Your Employee ID is "+str(employee_ID)+" and your email address is "+employee_email+". Your address is "+employee_address+".")
                    
                else:
                    print("You entered invalid employee_Address")
        else:
            print("You entered invalid employee_Email")
    else:
        print("You entered invalid employee_Name")
else:
    print("You entered invalid employee_ID")