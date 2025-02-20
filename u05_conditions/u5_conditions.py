# using for loop 
# print the numbers from 0 to 57

# print the numbers from 4 to 18

# print the multiples of 7 from 7 to 84


###################################################
# Part 1: Learning Exercises

# Exercise 1: Simple If Condition
# Write a program to check if a number is positive.
# If the number is positive, print "The number is positive."
# number = 5
# if number < 0:
#     print("The number is negative.")


#------------------------------------------------------------
# Exercise 2: If-Else Condition
# Write a program to check if a number is positive or negative.
# Example: If the number is -3, print "The number is negative."
# number = 3
# if number >= 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")


# #------------------------------------------------------------
# # Exercise 3: Using Relational Operators
# # Write a program to compare two numbers and print which is 
# # larger. Example: Input = 5, 10. Output = "10 is larger."
# num1 = 10
# num2 = 10
# if num1 > num2:
#     print("{} is larger.".format(num1))
# else:
#     print("{} is larger.".format(num2))


# #------------------------------------------------------------
# # Exercise 4: Multi-Way Selection with If-Elif-Else
# # Write a program to check if a number is positive, zero, or 
# # negative. Example: Input = 0. Output = "The number is zero."
# number = 0
# if number > 0:
#     print("The number is positive.")
# elif number == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")


# # #------------------------------------------------------------
# # # Exercise 5: Using Logical Operators (and)
# # # Write a program to check if a number is divisible by both 3 
# # # and 5. Example: Input = 15. Output = "Divisible by both."
# number = 15
# if number % 3 == 0 and number % 5 == 0:
#     print("Divisible by both 3 and 5.")
# else:
#     print("Not divisible by both.")


# # #------------------------------------------------------------
# # # Exercise 6: Using Logical Operators (or)
# # # Write a program to check if a number is divisible by 3 or 5.
# # # Example: Input = 9. Output = "Divisible by 3 or 5."
# number = 9
# if number % 3 == 0 or number % 5 == 0:
#     print("Divisible by 3 or 5.")
# else:
#     print("Not divisible by 3 or 5.")


# # #------------------------------------------------------------
# # # Exercise 7: Using Logical Operators (not)
# # # Write a program to check if a number is not divisible by 2.
# # # Example: Input = 7. Output = "The number is not divisible by 2."
# number = 7
# if not (number % 2 == 0):
#     print("The number is not divisible by 2.")
# else:
#     print("The number is divisible by 2.")


# # #------------------------------------------------------------
# # # Exercise 8: Combining Logical Operators
# # # Write a program to check if a number is divisible by 2 and 
# # # not divisible by 3. Example: Input = 10.
# # # Output = "Divisible by 2 but not divisible by 3."
# number = 10
# if number % 2 == 0 and not (number % 3 == 0):
#     print("Divisible by 2 but not divisible by 3.")
# else:
#     print("Does not meet the condition.")

##### RANDOM NUMBER GUESSER GAME

# # Part 1: your computer needs to think of a random number between 1 - 100
# import random
# correct = random.randint(1, 100)
# print(correct)

# # 2: your computer will ask you to guess
# print("Let's play a guessing game. ")


# # 3: your computer will check if you answer 
 
# else:
#     # the code here will run on succesful completion of loop
    

# 3b too big
# 3c too small
# 3a correctly

# computer also needs to give 7 chances...
# i need to ask again for 7 times... until i get the answer.

import random
money = 100
jackpot_num = 0
continue1 = '1'
continue3 = 0
print("Welcome to the gambling game!")
while True:
    if continue1 == str(1):
        if continue3 == "1":
            print("awww, leaving so soon...? ")
            print("I'll see you soom :)")
            break

    playerchoice = input("Which game would you like to play? If it is slot machine, press 1 if it is roulette, press 2.  ")


    if playerchoice == "1":
        while True:
            if continue1 == str(1):
                if continue3 == "1":
                    continue1 = '1'
                    
                num_1 = random.randint(1,9)
                num_2 = random.randint(1,9)
                num_3 = random.randint(1,9)
                if money <= 0:
                    print("ur broke hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha")
                    break

                money-=7
                if num_1 == num_2 ==num_3:
                    money +=50
                    jackpot_num +=1
                else:
                    if num_1 == num_2 or num_2 == num_3  or num_3 == num_1:
                        money+=20

                
                print(f"{num_1} / {num_2} / {num_3}")
                print("your balance is ",money) 
                while True:
                    continue3= str(input("Do you want to continue?(press enter  is yes enter 1 if no)  "))
                    if continue3 == "":
                        continue1 = '1'
                        break
                    
                    elif continue3 == "1":
                            continue1 = 1
                            break
                    else:
                        print("come on. It's just 2 simple buttons that is so easy to press and yet you still can't follow simple instructions and for that you have lost all the money that you have accumilated so far and you have to restart the program(yes i broke the 4th wall)")        
                    
                    if money>1000:
                        print("You have won too much... GET OUTTTTTTT")
                        break

            else:
                break
    else:
        while True:
            playerchoice_roulette = str(input("Would you like to play number roulette (press 1 )or colour roulette?(press 2) or if you want to exit, (press 3) "))
            if playerchoice_roulette == '3':
                    continue1 = 0
                    break
            

            if playerchoice_roulette == "1":
                wager = int(input("How much are you willing to bet?  "))
                random_num_roulette = random.randint(1,10)
                player_num = int(input("Which number from 1 to 10 do you chose?  "))
                if player_num not in range(1,11):
                    print("Just pick a number from 1 to 10!!!! Is it really that hard???")
                else:
                    if player_num == random_num_roulette:
                        print(f"Yes the number{random_num_roulette} is correct!!!")
                        money = money*10
                        print(money)
                    else:
                        print(f"Nope, you lost.The number was {random_num_roulette} ")
                        money-=wager
                        print("you have, ",money, "left")
                
            else:
                if playerchoice_roulette == "2":
                    random_colour = random.randint(1,2)
                    if random_colour == '1':
                        random_colour = "red"
                    else:
                        random_colour = "black"
                    player_colour_choice = str(input("Which colour red or black do you choose? "))
                    wager_colour = int(input("How much do you bet? "))
                    money -= wager_colour
                    if player_colour_choice == random_colour:
                        money = money + wager_colour*2
                        print(f"Yes! you got it correct!! Your current balance is {money}")
                    else:
                        print(f"Nope, you are wrong. The colour was actually {random_colour}.")
                        print(f"You currently have {money}")









            













