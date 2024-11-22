"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
#import random module
import random

#main function to start the game
# creates a random number
# takes input from the user to guess the random number
# tells the user how many attempts they have made 
def start_game():
    # get the user name
    name = input("What is your name?  ")
    # show a welcome message
    print("***Welcome to the game, {} ***".format(name))
    # create a random number between 1 and 10
    random_number = random.randint(1, 10)
    # set a default guess number before starting
    guess = 0
    # set number of attempts
    attempts = 0
    # loop until user finds the correct number
    while guess != random_number:
        guess = int(input("Please choose a number between 1 and 10  "))
        # increment the number of attempts
        attempts += 1
        # conditional to check if the guess is greater than the number
        if guess > random_number:
            print("It's lower")
        # otherwise the guess is lower - show a message to say it's higher
        else:
            print("It's higher")
    # Show a winning message. Let user know how many attempts they have made.
    print("Got it. You have made {} attempts".format(attempts))
    # Show goodbye message
    print("*** Game Over ***")

#Call the function to start the game
start_game()