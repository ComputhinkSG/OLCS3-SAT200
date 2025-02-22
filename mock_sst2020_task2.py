# The following program simulates a scenario that a 
# user sets a password for the first time. 
# After that, the system allows the user to have three attempts 
# in logging into the system with the correct password

#User sets password and tries to log into a system
password = input("Please set password: ")
print("Your password is : ", password)
count = 3
hit = False
while count > 0 and hit == False:
    print("Please log into the system.")
    print("You have {} attempt(s) left.".format(count))
    user_input = input("Please enter the password: ")
    if user_input == password:
        print("You have successfully logged into the system.")
        hit = True
    else:
        print("You did not enter the correct password.")
        count -= 1
if count == 0:
    print("You are locked out of the system.")


# Edit the program so that it:
# 7. Allows up to 4 password attempts when logging into the system. [1]

# 8. Prints out the reversed form of the password 
#  (e.g. “ABCD” is printed as “DCBA”) right after 
#  a valid password has been set. [2] 

# 9. Ensures that the password consists of at least 8 characters. 
#  Otherwise, the program should inform the user about the 
#  input requirements and ask for re-entry of the input. [3] 

# 10. Ensures that the set password consists of at 
#  least 1 upper case alphabet (‘A’ to ‘Z’). 
#  Otherwise, the program should inform the 
#  user about the input requirements and ask for 
#  re-entry of the input. [4] 
