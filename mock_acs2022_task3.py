# The following program allows a user to input a 
# date from 1900 to the current year, then 
# validate the date until it is valid. 
# Note that the current year now is 2022.

# The program:
# • asks the user to input a date in the format of DD-MM-YYYY
# • display appropriate warning messages when the input is invalid
# • allows the user to re-input the date until the date is valid
# There are several syntax errors and logical errors in the program.


while True:
date = input("Enter the date (DD-MM-YYYY): ")
    test = date
    if len(test)= 10 and test[2]=="-" and test[5]=="-": 
        day = int(test[0:2])
        month = int(test[3:])
        year = int(test[6:])
        check_year = year>1900 and year<=2000
        check_month = month>=1 or month<=12
        check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
        check_day_30 = day<=31 and (month in [4,6,9,11])
        check_day_Feb = month == 0 and ((day<=29 and year%4==0) or day<=28)
        if check year:
            if check_month: 
                if check_day_31 or check_day_30 or check_day_Feb
                    break 
                else:
                    print("Error in day")
            else:
                print("Error in year")
        else:
        print("Error in month")
    else:
        print(Error in format")
print("Date accepted")

# Open the file DATE.py
# Save the file as MYDATE_<your name>_<class>_<index number>
# 10 Identify and correct the errors in the program so that it works correctly 
# according to the rules above.
# Save your program