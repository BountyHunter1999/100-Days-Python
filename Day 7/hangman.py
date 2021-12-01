import random
import re
import sys

# Step 1
word_list = ["misery", "greed", "life", "pokemon"]

# Randomly CHoose a word from the word_list and assign it to a variable called chosen_word
random_word = random.choice(word_list)
random_word_l = list(random_word)
# print(random_word)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


life = len(stages) # 7
our_word = ["_" for _ in random_word]

guess_letters = []

def check(locations, word, guess):
    # print("We are live and reporting from check function")
    # print(f"locations: {locations} \n word:{word} \n guess:{guess} \n\n")
    if locations:
        for i in locations:
            word[i] = guess
        return word
    else:
        return False

while life:
    print(f"Life is: {life}")
    guess = input("Guess a letter: ").lower()
    
    if guess not in guess_letters:
        guess_letters.append(guess)

        locations = [i.start() for i in re.finditer(guess, random_word)]
        check_output = check(locations, our_word, guess)
        if check_output:
            our_word == check_output
            print(f"{our_word}")
        else:
            print(f"{stages[life - 1]}")
            life -= 1
    else:
        print("try another letter it's already used")
    
    print()
    # if our_word == random_word_l:
    if "_" not in our_word:
        print("You won!!")
        sys.exit()


print("Game Over")
        