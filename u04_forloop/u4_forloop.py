# for###################################################
# Part 1: Learning Exercises
# Exercise 1: Simple Loop with range(stop)
# Write a program to print "Welcome to Python!" 5 times.
# Use range(stop) to repeat the message.
# for i in range(5):
#     print("hi")


# #------------------------------------------------------------
# # Exercise 2: Printing Numbers with range(stop)
# # Write a program to print numbers from 0 to 4 using range(stop).
# # Example: Output = 0, 1, 2, 3, 4.

# # option 1 : range(stop)
# for i in range(5):  # Loop from 0 to 4
#     print("Number: {}".format(i))

# option 2: range(start, stop)
# scenario is i want to count from 5 to 21
# for i in range(5,22):    #5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
#     print(i)

# option 3: range(start, stop, step)
# scenario is i want multiples of 6 from 6 to 72
# for i in range(6,73,6): #6,12,18,
#     print(i)

# new year countdown 10 - 1
# for ksdhfskjdhfksjdfhjksdhfkjsdhfkjsdjk in range(10, 0, -1): # 10,9,8,7,6,5,4,3,2,1
#     print(ksdhfskjdhfksjdfhjksdhfkjsdhfkjsdjk)






# #------------------------------------------------------------
# # Exercise 3: Counting with range(start, stop)
# # Write a program to print numbers from 10 to 15.
# # Use range(start, stop) to set the range.
# # Example: Output = 10, 11, 12, 13, 14, 15.
# for i in range(10, 16):  # Loop from 10 to 15
#     print("Counting: {}".format(i))


# #------------------------------------------------------------
# # Exercise 4: Using range(start, stop, step)
# # Write a program to print even numbers from 2 to 10.
# # Use range with a step value.
# # Example: Output = 2, 4, 6, 8, 10.
# for i in range(2, 11, 2):  # Step value is 2
#     print("Even number: {}".format(i))


# #------------------------------------------------------------
# # Exercise 5: Printing Numbers in Reverse
# # Write a program to print numbers from 10 to 1.
# # Use range(start, stop, step) with a negative step value.
# # Example: Output = 10, 9, 8, ..., 1.
# for i in range(10, 0, -1):  # Loop backwards
#     print("Countdown: {}".format(i))


# #------------------------------------------------------------
# # Exercise 6: Summing Numbers in a Range
# # Write a program to calculate the sum of numbers from 1 to 10.
# # Use range(start, stop) and a loop to add the numbers.
# # Example: Output = 55.
# total = 0
# for i in range(1, 11):  # Loop from 1 to 10
#     total += i
# print("The total sum is: {}".format(total))


# #------------------------------------------------------------
# # Exercise 7: Printing a Simple Pattern
# # Write a program to print the following pattern:
# # *
# # **
# # ***
# # ****
# # *****
# for i in range(1, 6):  # Loop for rows
#     print("*" * i)


###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Printing Odd Numbers
# Write a program to print all odd numbers from 1 to 15.
# Use range(start, stop, step) to skip even numbers.
# Example: Output = 1, 3, 5, ..., 15.



#------------------------------------------------------------
# Exercise 9: Multiplying Numbers
# Write a program to print the first 5 multiples of 7.
# Use range(start, stop, step).
# Example: Output = 7, 14, 21, 28, 35.


#------------------------------------------------------------
# Exercise 10: Repeating a Phrase
# Write a program to print "I love Python!" 3 times.
# Use range(stop) to repeat the phrase.



#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 5
# 44
# 333
# 2222
# 11111


print("*"*1)
print("*"*3)
print("*"*5)
print("*"*7)
print("*"*9)


#------------------------------------------------------------
# Exercise 12: Generating a Multiplication Table
# Write a program to print the multiplication table of 6.
# Example: 6 x 1 = 6, ..., 6 x 10 = 60.




#------------------------------------------------------------
# Exercise 13: Printing a Custom Star Pattern
# Write a program to print the following pattern:
# *
# ***
# *****
# *******
# *********


# for loop

# straightforward repeat
# >>> range(start,stop,step)

# loop through all the characters in a string...

for c in "jared":
    print(f"Give me a {c}!")

print("Who is the best?? ")
print("JARED!!! ")


# count the number of A in the WORDA
counter_a = 0
word = input("Type a word: ")

for c in word:
    if c == "A":
        counter_a = counter_a + 1

print(f"THere are {counter_a} A in the word {word}")
