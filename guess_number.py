#"Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code here
secret_number = random.randint(0,100)
left_guesses = 0

def new_game():
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global left_guesses
    secret_number = random.randint(0,100)
    left_guesses = 7
    print "New Game! Enter a number from 0 to 100."
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global left_guesses
    secret_number = random.randint(0,1000)
    left_guesses = 10
    print "New Game! Enter a number from 0 to 1000."    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global left_guesses
    left_guesses -= 1
    guessed_number = int(guess)
    if guessed_number == secret_number:
        print "Correct!", guessed_number, "is secret number."
        print "You had", left_guesses, "guesses left."
        range100()
    elif left_guesses > 0:
        if guessed_number > secret_number:
            print "You guessed", guessed_number, "try LOWER."
        elif guessed_number < secret_number:
            print "You guessed", guessed_number, "try HIGHER"
    else:
        print "You are out of guesses. Game over. Try again."
        range100()
    
# create frame
frame = simplegui.create_frame("Guess: ", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("0-100", range100, 200)
frame.add_button("0-1000", range1000, 200) 
frame.add_input("Enter a guess:", input_guess, 200)
frame.start()
new_game()

