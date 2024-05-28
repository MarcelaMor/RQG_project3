# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# This my "Random Quote Generator" project for the Python course
# I used the "Dice Roll Generator" -
# from https://hackr.io/blog/python-projects as guidance
# also https://www.javatpoint.com/create-a-quote-generator-in-python.

# Sketching out the program flow:
# 1. present user with a choice of quote style
# 2. User inputs choice by a number
# 3. Program proccess the number, there will be a function that matches
#    the number with the list that matches the user choice of quote style.
# 4. The lists are stored in the program and will be named according
#    to the style of the quotes, e.g inner_strength[a, b, c,]
#    or guidance_quotes[a, b, c,].
# 5. The program will randomly select a
#    quote from the list and print it to the user.
# 6. The program will not ask the user for
#    another quote and will end with a message.

"""
imported sys module to use sys.exit()
method to quit the app (google search).
"""
import sys
import random  # imported as per the "Dice Roll Generator" example.

# These lists contain the quotes that are randomly chosen from.
innerStrength = [
    "How long are you going to wait before "
    "you demand the best for yourself? - Epictetus",
    "It is not because things are difficult that we do not dare; it is "
    "because we do not dare that they are difficult. - Seneca",
    "It is not what happens to you, but"
    "how you react to it that matters. - Epictetus",
    "The happiness of your life depends upon the quality "
    "of your thoughts. - Marcus Aurelius",
    "First say to yourself what you would be, and then "
    "do what you have to do. - Epictetus",
]

selfControl = [
    "You have power over your mind - not outside events. "
    "Realize this, and you will find strength. - Marcus Aurelius",
    "Freedom is not procured by a full"
    "enjoyment of what is desired, but by controlling the desire. - Epictetus",
    "The best revenge is not to be like your enemy. - Marcus Aurelius",
    "We suffer more often in imagination than in reality. - Seneca",
    "No man is free who is not master of himself. - Epictetus",
]

# Welcome message and the user choice input.
print("Welcome to the Random Quote Generator! Please make a choice.")

while True:

    # This is the user choice input.
    choice = input("Choose a category: "
                   "'1' for Inner Strength, '2' for Self Control: ")

    # this is the function that will
    # match the user choice with the list of quotes.
    if choice == "1":
        print(random.choice(innerStrength))
    elif choice == "2":
        print(random.choice(selfControl))
    else:
        print("Invalid choice. Please enter 1 or 2.")
        # Added 'continue' to proceed with the
        # outer loop if the input is invalid.
        continue

    # Added 'while' to keep asking if a
    # new quote is desired until a valid input is entered.
    while True:
        # Following line gives choice for a new quote.
        newRun = input("Would you like another quote? Type 'yes' or 'no': ")
        if newRun.lower() in ["yes", "y"]:
            break
        if newRun.lower() in ["no", "n"]:
            sys.exit("Bye!")  # Added this to exit the app
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
