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
    replay = False
    # loop until user finds the correct number
    while guess != random_number or replay == True:
        try:
            guess = int(input("Please choose a number between 1 and 10  "))
            # increment the number of attempts
            attempts += 1
            if guess > 10 or guess < 1:
                print("The number is between 1 and 10. Please choose again")
                continue
            # conditional to check if the guess is greater than the number
            elif guess > random_number:
                print("It's lower")
            # otherwise the guess is lower - show a message to say it's higher
            elif guess < random_number:
                print("It's higher")
        except ValueError: 
            print("Sorry, it seems you have not entered a number. Please enter a number between 1 and 10")
    # Show a winning message. Let user know how many attempts they have made.
    print("Got it. You have made {} attempts".format(attempts))
    # Show goodbye message
    print("*** Game Over ***")
    play_again = input("Would you like to play again? (yes/no)  ")
    if play_again.lower() == "yes":
        replay = True
    else:
        replay = False

  


#Call the function to start the game
start_game()