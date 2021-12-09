import random
from logo import logo
import os
import sys

os_clear = "cls" if os.name == "nt" else "clear"

difficulty = {
    "easy": 10,
    "medium": 8,
    "hard": 5
}

def game():
    print(logo)
    guess = random.randint(1,100)
    print("Let's Play A Game Of Guess: \n first select a difficulty")

    choose_difficulty = input("Choose the difficulty: easy, medium or hard? ").lower()
    turns = difficulty[choose_difficulty]

    while turns:
        number = int(input("\nGuess the number: "))
        turns -= 1

        if number == guess:
            print("That's right! It is the correct guess.")
            break
        elif number > guess:
            print("You aimed higher try going lower.")
        else:
            print("You aimed lower try going higher.")
        
        print(f"\t You got {turns} remaining")

    print(f"The number was {number}")

    play_again = input("Type 'y' to start a new game. 'n' if u want to quit: ")
    if play_again == 'y':
        os.system(os_clear)
        game()
    else:
        sys.exit()

game()
