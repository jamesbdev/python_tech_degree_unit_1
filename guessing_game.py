"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
#import random module
import random

#main function to start the game
# contains play_game function with the game logic
def start_game():
    # get the user name
    name = input("What is your name?  ")
    # show a welcome message
    print("***Welcome to the game, {} ***".format(name))

    # contains the logic to loop until the user finds the correct answer
    def play_game():
        # create a random number between 1 and 10
        random_number = random.randint(1, 10)
        # set a default guess number before starting
        guess = 0
        # set number of attempts
        attempts = 0
        # loop until user finds the correct number
        while guess != random_number:
            try:
                guess = int(input("Please choose a number between 1 and 10  "))
                # increment the number of attempts
                attempts += 1
                # check if the number is out of range
                if guess > 10 or guess < 1:
                    print("Sorry, the number you chose is out of range.")
                    continue
                # conditional to check if the guess is greater than the number
                elif guess > random_number:
                    print("It's lower")
                # otherwise the guess is lower - show a message to say it's higher
                elif guess < random_number:
                    print("It's higher")
            #handle exception
            except ValueError: 
                print("Sorry, it seems you have not entered a number")
        # Show a winning message. Let user know how many attempts they have made.
        print("Got it. You have made {} attempts".format(attempts))
        # Show goodbye message
        print("*** Game Over ***")
    
        # function to ask the user if they want to play again, then repeats the game       
        def play_again():
            # ask user if they wish to play again
            play_again = input("Would you like to play again? (yes/no)  ")
            if play_again.lower() == "yes":
                #repeat the game logic
                play_game()
                
            else:
                # Show goodbye message
                print("Thank you for playing. Bye for now.")
        play_again()
    play_game()


#Call the function to start the game
start_game()