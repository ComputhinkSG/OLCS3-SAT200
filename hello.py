'''
Mock Task 3 Question 1
A library program needs to keep track of books being borrowed and returned. 
Each book has a unique ID and a title. The program allows a user to 
input the book ID and whether the book is being borrowed or returned. 
The program updates the status of the book accordingly and displays a message. 
There are several syntax and logic errors in the program.
'''
### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this


print("before program run")
print(books)
if action.upper() == "B": # fixed missing equal sign and colon  ## fixed upper case for B
    if books[book_id] == "AVAILABLE": ## fixed value should be upper case
        books[book_id] = "BORROWED"   # books["B"] is wrong. change to upper case
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action =="r": # fixed missing equal
    if books[book_id] == "borrowed":
        books["R"] = "available"    # changed to []
        print("You have returned the book.")    # added missing quotation
    else:
        print("The book is already available.") # fixed indentation error
else:    # fixed indentation error.
    print("Invalid action.") # fixed missing quotation
print("after program run")
print(books)
'''
Open the file LIBRARY.py. Save the file as 
MYLIBRARY_<your name><center number><index number>.py.
Identify and correct the errors in the program so that it works according to 
the requirements given. Save your program.
[10 marks]
'''


# ### DO NOT CHANGE the first 3 lines of code.
# books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
# action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
# book_id = input("Enter the book ID: ")
# ### Make your code fixes after this

# if action = "b"
#     if books[book_id] == "Available":
#         books["B"] = "borrowed"
#         print("You have borrowed the book.")
#     else:
#         print("The book is already borrowed.")
# elif action = "r":
#     if books[book_id] == "borrowed":
#         books("R") = "available"
#         print(You have returned the book.")
#     else:
#     print("The book is already available.")
#     else:
#         print("Invalid action.)


# this is a back up of the original buggy code
# if action = "b"
#     if books[book_id] == "Available":
#         books["B"] = "borrowed"
#         print("You have borrowed the book.")
#     else:
#         print("The book is already borrowed.")
# elif action = "r":
#     if books[book_id] == "borrowed":
#         books("R") = "available"
#         print(You have returned the book.")
#     else:
#     print("The book is already available.")
#     else:
#         print("Invalid action.)