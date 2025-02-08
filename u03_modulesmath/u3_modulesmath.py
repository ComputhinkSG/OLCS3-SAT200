# # different types of variables

# # string, int, float, boolean, list, dictionary

# #string variable
# var1 = 'TOM'
# var2 = "CAT"
# var3 = var1 + var2 # do a plus on 2 strings, it joins them up, string concatenation
# # print(var3)

# var4 = 5 # integer variable
# var5 = 3.1419 # float variable
# var6 = 6
# var7 = var4 + var5 # the plus operator will add them
# # print(var7)

# # var8 = int(var1) + var4
# # print(var8)

# # data type conversion, change variables from one type to another type
# # str() - convert to a string

# ### using input to do an addition calculator
# num1 = int(input("What is the first number? "))
# num2 = int(input("What is the second number? "))
# answer = num1 + num2
# print(answer)

####################################################

# Part 1: Learning Exercises

# Exercise 1: Importing Modules
# Write a program to use the math module for calculations.
# Example: Calculate the square root of 16 and the power of 2^3.
# import math  # Importing the math module
# sqrt_value = math.sqrt(16)
# power_value = math.pow(2, 3)
# power_value2 = 3**3
# print("Square root of 16 is:", sqrt_value)
# print("2 to the power of 3 is:", power_value)
# print("3 to the power of 3 is:", power_value2)


# #------------------------------------------------------------
# # Exercise 2: Modulus and Floor Division
# # Write a program to calculate the modulus and floor division
# # of two numbers. Example: 17 divided by 5.
# num1 = 17
# num2 = 5
# modulus = num1 % num2
# floor_div = num1 // num2
# div = num1 / num2
# print("17 % 5 is:", modulus)
# print(div)
# print("17 // 5 is:", floor_div)


# to check if a number is odd or even
# num = int(input("ENter a number "))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")


# #------------------------------------------------------------
# # Exercise 3: Using Rounding Methods
# # Write a program to round a number using round(), math.ceil(),
# # and math.floor(). Example: number = 5.67.
# import math
# number = 5.17234567865689778
# rounded = round(number, 3)
# print(rounded)
# ceiled = math.ceil(number)
# floored = math.floor(number)
# print("Rounded:", rounded, "Ceiled:", ceiled, "Floored:", floored)


# #------------------------------------------------------------
# # Exercise 4: Floor Division for Time Conversion
# # Write a program to convert total seconds into minutes and 
# # seconds using floor division and modulus. Example: 125 seconds
# # = 2 minutes and 5 seconds.
# total_seconds = 254
# minutes = total_seconds // 60
# seconds = total_seconds % 60
# print("Minutes:", minutes, "Seconds:", seconds)


# #------------------------------------------------------------
# # Exercise 5: Rounding for Pricing
# # Write a program to calculate the total price of an item after 
# # rounding up to the nearest dollar. Example: If the price is 
# # 19.75, the total is 20.
# price = 19.75
# rounded_price = math.ceil(price)
# print("Rounded total price is:", rounded_price)



# #------------------------------------------------------------
# # Exercise 6: Generating Random Integers
# # Write a program to generate a random number between 1 and 10.
# # Example: The output could be any number from 1 to 10.
# import random
# random_number = random.randint(1, 10)
# print("Random number between 1 and 10:", random_number)
# import random

# dice1 = random.randint(1, 6) # return you a random number
# print(dice1)



#############################################################
# practice exercise
###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Simulating Two Dice Rolls
# Write a program to simulate the roll of a 6-sided die two times
# and display the results. Example: Output = 4, 6.
import random
random.randint(1, 6)


#------------------------------------------------------------
# Exercise 8: Floor Division for Groups
# Write a program to calculate how many full groups can be formed 
# and how many items are leftover. Example: 25 students divided 
# into groups of 4 = 6 groups and 1 leftover.




#------------------------------------------------------------
# Exercise 9: Rounding for Fuel Costs
# Write a program to calculate the total cost of fuel rounded up 
# to the nearest dollar. Example: If the fuel cost is 47.89, the 
# total is 48.




#------------------------------------------------------------
# Exercise 10: Floor Division for Age Conversion
# Write a program to calculate someone's age in decades and 
# remaining years. Example: Age = 29 -> Decades = 2, Years = 9.




#------------------------------------------------------------
# Exercise 11: Calculating Items in Boxes
# Write a program to calculate how many full boxes are needed to 
# pack items and how many items are leftover. Example: If there 
# are 53 items and each box holds 12, the output is:
# Full boxes = 4, Leftover = 5.